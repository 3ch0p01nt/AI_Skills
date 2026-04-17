#!/usr/bin/env python3
"""
Toolbox .ttp / .ttt validator.

Checks a prompt file against the authoring-toolbox-prompts quality checklist.
Reports Tier 1 (baseline correctness) failures as errors and Tier 2 (max-impact)
gaps as warnings. Exit code 1 on any Tier 1 failure, 0 otherwise.

Usage:
    python validate.py <path>             # validate one file
    python validate.py <path> [<path>...] # validate many
    python validate.py --dir <directory>  # validate every .ttp and .ttt in a dir
"""

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_TTP_KEYS = {
    "Name", "Type", "SystemPrompt", "FewShotExamples",
    "ChatParameters", "Model", "Version", "DescriptionMetadata",
}
REQUIRED_TTT_KEYS = {
    "Type", "Name", "Description", "Version", "Entry",
    "InitialDataID", "MaxDepth", "Steps", "Parameters", "DescriptionMetadata",
}
REQUIRED_CHAT_PARAMS = {
    "DeploymentName", "MaxResponseLength", "Temperature",
    "TopProbablities", "StopSequences", "FrequencyPenalty",
    "PresencePenalty", "OutputAsJSON",
}
REQUIRED_SECTIONS = [
    "**Objective**",
    "Be vigilant for:",
    "Safe patterns",
    "**Detection Checklist**",
    "**Instruction Details**",
    "**Rewards**",
    "**Response Schema**",
]
REQUIRED_FINDING_FIELDS = {
    "severity", "indicator_type", "evidence",
    "description", "mitre_technique", "attribution",
}
TIER2_FINDING_FIELDS = {"confidence"}
REQUIRED_ATTRIBUTION_FIELDS = {"source", "evidence_items"}
SEVERITY_VOCAB = {"critical", "high", "medium", "low", "informational"}
MITRE_PATTERN = re.compile(r"^T\d{4}(\.\d{3})?\s*-\s*.+")
VERSION_PATTERN = re.compile(r"^\d{14}$")


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.passed = []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def ok(self, msg):
        self.passed.append(msg)

    def print(self):
        print(f"\n=== {self.path} ===")
        for m in self.passed:
            print(f"  OK:   {m}")
        for m in self.warnings:
            print(f"  WARN: {m}")
        for m in self.errors:
            print(f"  FAIL: {m}")
        print(f"  Summary: {len(self.passed)} passed, "
              f"{len(self.warnings)} warnings, {len(self.errors)} failures")


def _check_few_shot(ex, idx, rep):
    user_input = ex.get("UserInput", "")
    resp_str = ex.get("ChatbotResponse", "")
    if not user_input:
        rep.err(f"FewShot[{idx}] missing UserInput")
        return
    if not resp_str:
        rep.err(f"FewShot[{idx}] missing ChatbotResponse")
        return
    if "```" in resp_str:
        rep.err(f"FewShot[{idx}] ChatbotResponse contains markdown fences")
    try:
        resp = json.loads(resp_str)
    except json.JSONDecodeError as e:
        rep.err(f"FewShot[{idx}] ChatbotResponse is not valid JSON: {e}")
        return
    if "findings" not in resp:
        rep.err(f"FewShot[{idx}] response missing 'findings' array")
        return
    if "summary" not in resp:
        rep.err(f"FewShot[{idx}] response missing 'summary' object")
        return
    findings = resp["findings"]
    summary = resp["summary"]
    if summary.get("total_findings") != len(findings):
        rep.err(f"FewShot[{idx}] summary.total_findings "
                f"({summary.get('total_findings')}) != findings.length "
                f"({len(findings)})")
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0,
              "informational": 0}
    for j, f in enumerate(findings):
        missing = REQUIRED_FINDING_FIELDS - set(f.keys())
        if missing:
            rep.err(f"FewShot[{idx}].findings[{j}] missing required fields: "
                    f"{sorted(missing)}")
        sev = f.get("severity")
        if sev not in SEVERITY_VOCAB:
            rep.err(f"FewShot[{idx}].findings[{j}] invalid severity: {sev}")
        else:
            counts[sev] += 1
        mitre = f.get("mitre_technique", "")
        if not MITRE_PATTERN.match(mitre):
            rep.err(f"FewShot[{idx}].findings[{j}] bad mitre_technique format: "
                    f"{mitre!r} (expected 'TXXXX - Name' or 'TXXXX.### - Name')")
        attr = f.get("attribution", {})
        attr_missing = REQUIRED_ATTRIBUTION_FIELDS - set(attr.keys())
        if attr_missing:
            rep.err(f"FewShot[{idx}].findings[{j}] attribution missing: "
                    f"{sorted(attr_missing)}")
        for k, item in enumerate(attr.get("evidence_items", [])):
            if item not in user_input:
                rep.err(f"FewShot[{idx}].findings[{j}].attribution."
                        f"evidence_items[{k}] is NOT a verbatim substring of "
                        f"UserInput: {item!r}")
        if "confidence" not in f:
            rep.warn(f"FewShot[{idx}].findings[{j}] missing 'confidence' "
                     f"(Tier 2 upgrade)")
        else:
            c = f["confidence"]
            if not (isinstance(c, (int, float)) and 0 <= c <= 100):
                rep.err(f"FewShot[{idx}].findings[{j}].confidence out of "
                        f"range 0-100: {c}")
            elif c < 50:
                rep.warn(f"FewShot[{idx}].findings[{j}].confidence={c} - "
                         f"findings below 50 should be omitted")
    for sev, n in counts.items():
        if summary.get(sev, 0) != n:
            rep.err(f"FewShot[{idx}] summary.{sev} ({summary.get(sev, 0)}) "
                    f"disagrees with actual count ({n})")


def validate_ttp(path, data):
    rep = Report(path)

    missing = REQUIRED_TTP_KEYS - set(data.keys())
    if missing:
        rep.err(f"Missing top-level keys: {sorted(missing)}")
    else:
        rep.ok("Top-level keys present")

    if data.get("Type") != "prompt":
        rep.err(f"Type must be 'prompt', got {data.get('Type')!r}")
    else:
        rep.ok("Type == 'prompt'")

    name = data.get("Name", "")
    if Path(path).stem != name:
        rep.err(f"Filename stem ({Path(path).stem!r}) does not match "
                f"Name field ({name!r})")
    else:
        rep.ok("Filename matches Name")

    ver = data.get("Version", "")
    if not VERSION_PATTERN.match(ver):
        rep.err(f"Version not in YYYYMMDDhhmmss format: {ver!r}")
    else:
        rep.ok("Version is 14-digit YYYYMMDDhhmmss")

    if data.get("DescriptionMetadata") is not None:
        rep.warn(f"DescriptionMetadata should be null, got "
                 f"{data.get('DescriptionMetadata')!r}")
    else:
        rep.ok("DescriptionMetadata is null")

    sp = data.get("SystemPrompt", "")
    missing_sections = [s for s in REQUIRED_SECTIONS if s not in sp]
    if missing_sections:
        rep.err(f"SystemPrompt missing sections: {missing_sections}")
    else:
        rep.ok("SystemPrompt has all 7 required section markers")

    if not sp.rstrip().endswith("**DATA**"):
        rep.err("SystemPrompt does not end with literal '**DATA**' marker")
    else:
        rep.ok("SystemPrompt ends with **DATA**")

    if "pizza party" not in sp or "$100" not in sp:
        rep.err("SystemPrompt missing Rewards block (pizza party / $100)")
    else:
        rep.ok("Rewards block present")

    if "evidence_items must be verbatim" not in sp:
        rep.warn("Missing attribution-verbatim hardening clause (Tier 2)")
    if "untrusted input" not in sp and "untrusted" not in sp:
        rep.warn("Missing prompt-injection hardening clause (Tier 2)")
    if "speculation" not in sp:
        rep.warn("Missing no-speculation clause (Tier 2)")
    if "summary.total_findings" not in sp:
        rep.warn("Missing coherence check clause (Tier 2)")

    cp = data.get("ChatParameters", {})
    cp_missing = REQUIRED_CHAT_PARAMS - set(cp.keys())
    if cp_missing:
        rep.err(f"ChatParameters missing fields: {sorted(cp_missing)}")
    else:
        rep.ok("ChatParameters has all required fields")
    if cp.get("OutputAsJSON") is not True:
        rep.err("ChatParameters.OutputAsJSON must be true")
    if "TopProbablities" not in cp:
        rep.err("ChatParameters.TopProbablities missing (note misspelling — "
                "it is the library's field name)")
    if cp.get("DeploymentName") != data.get("Model"):
        rep.warn(f"Model ({data.get('Model')!r}) does not mirror "
                 f"DeploymentName ({cp.get('DeploymentName')!r})")

    fs = data.get("FewShotExamples", [])
    if len(fs) < 2:
        rep.err(f"FewShotExamples must have >=2 entries, got {len(fs)}")
    else:
        rep.ok(f"FewShotExamples has {len(fs)} entries")
        if len(fs) < 3:
            rep.warn("Only 2 few-shots — Tier 2+ recommends a third "
                     "ambiguous/graded example")

    has_positive = False
    has_negative = False
    for i, ex in enumerate(fs):
        _check_few_shot(ex, i, rep)
        try:
            resp = json.loads(ex.get("ChatbotResponse", "{}"))
            if resp.get("findings"):
                has_positive = True
            elif resp.get("findings") == []:
                has_negative = True
        except json.JSONDecodeError:
            pass
    if not has_positive:
        rep.err("No positive FewShot example (one with findings)")
    if not has_negative:
        rep.err("No negative FewShot example (one with findings: [])")
    if has_positive and has_negative:
        rep.ok("At least one positive + one negative FewShot present")

    return rep


def validate_ttt(path, data):
    rep = Report(path)

    missing = REQUIRED_TTT_KEYS - set(data.keys())
    if missing:
        rep.err(f"Missing top-level keys: {sorted(missing)}")
    else:
        rep.ok("Top-level keys present")

    if data.get("Type") != "Tape":
        rep.err(f"Type must be 'Tape', got {data.get('Type')!r}")

    if data.get("InitialDataID") != "--data--":
        rep.warn(f"InitialDataID is usually '--data--', got "
                 f"{data.get('InitialDataID')!r}")

    if not VERSION_PATTERN.match(data.get("Version", "")):
        rep.err(f"Version not in YYYYMMDDhhmmss format: "
                f"{data.get('Version')!r}")
    else:
        rep.ok("Version valid")

    steps = data.get("Steps", [])
    if not steps:
        rep.err("No Steps")
        return rep

    entry = data.get("Entry")
    step_names = [s.get("Name") for s in steps]
    if entry not in step_names:
        rep.err(f"Entry {entry!r} does not match any Steps[].Name")
    else:
        rep.ok(f"Entry points to a defined step")

    for i, s in enumerate(steps):
        if s.get("Action") != "information":
            rep.warn(f"Steps[{i}] Action is {s.get('Action')!r} "
                     f"(usually 'information')")
        if s.get("Data") != "--data--":
            rep.warn(f"Steps[{i}] Data is {s.get('Data')!r} "
                     f"(usually '--data--')")
        next_step = s.get("NextStep")
        if i == len(steps) - 1:
            if next_step is not None:
                rep.err(f"Terminal step NextStep must be null, got "
                        f"{next_step!r}")
            else:
                rep.ok("Terminal step NextStep is null")
        else:
            if next_step is None:
                rep.err(f"Steps[{i}] NextStep is null but step is "
                        f"not terminal")
            elif next_step not in step_names:
                rep.err(f"Steps[{i}] NextStep {next_step!r} does not "
                        f"match any step Name")

    return rep


def validate_file(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep = Report(path)
        rep.err(f"Not valid JSON: {e}")
        return rep
    except OSError as e:
        rep = Report(path)
        rep.err(f"Could not read file: {e}")
        return rep

    t = data.get("Type")
    if t == "prompt":
        return validate_ttp(path, data)
    elif t == "Tape":
        return validate_ttt(path, data)
    else:
        rep = Report(path)
        rep.err(f"Unknown Type: {t!r} (expected 'prompt' or 'Tape')")
        return rep


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help=".ttp / .ttt file paths")
    parser.add_argument("--dir", help="Validate every .ttp/.ttt in directory")
    args = parser.parse_args()

    targets = []
    if args.dir:
        d = Path(args.dir)
        targets.extend(sorted(d.glob("*.ttp")))
        targets.extend(sorted(d.glob("*.ttt")))
    targets.extend(Path(p) for p in args.paths)

    if not targets:
        parser.print_help()
        sys.exit(1)

    any_failures = False
    total_warnings = 0
    total_ok = 0
    for p in targets:
        rep = validate_file(str(p))
        rep.print()
        if rep.errors:
            any_failures = True
        total_warnings += len(rep.warnings)
        total_ok += len(rep.passed)

    print(f"\n=== Grand total ===")
    print(f"  {len(targets)} files checked, "
          f"{total_ok} passes, {total_warnings} warnings, "
          f"{'FAILURES' if any_failures else 'no failures'}")
    sys.exit(1 if any_failures else 0)


if __name__ == "__main__":
    main()
