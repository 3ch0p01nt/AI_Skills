# AI Skills

Custom AI skills for GitHub Copilot CLI. These skills provide specialized capabilities for Microsoft professional development workflows.

## Installed Skills

### Connect
**Draft a complete Microsoft Connect self-reflection and Impact Card.**

Covers the full Connect lifecycle — all 5 form sections plus the companion Impact Card (baseball card) for manager calibration:
- **Goals** — Status + evidence for each organizational goal
- **Summarize Your Impact** — Top 3 impact areas with Challenge→Solution→Impact arc
- **Reflect on a Challenge** — Honest setback with Growth Mindset learning
- **Review Your Goals** — Sourced status table
- **How Will You Reach Your Goals?** — Forward-looking priorities

Features:
- Evidence mining via WorkIQ/M365 when available
- Source verification framework (every metric needs a named source + date)
- Calibration-optimized: both-sides-of-coin, acceleration framing, level-appropriate lens
- Impact Card companion with cliff-notes formatting for the calibration room
- Consulting-specific metrics (utilization, ACR, billable hours, IP created)
- Common pitfalls checklist and quality verification
- Level-appropriate framing guide (L63→L67)

### Perspectives
**Draft Microsoft Perspectives feedback through guided conversation.**

Produces polished, positive, impact-focused feedback in the official Microsoft Perspectives format:
- **Keep doing** — Specific, evidence-based narrative with STAR method
- **Re-think** — Constructive growth opportunities (positive framing)
- **Additional thoughts** — Personal, authentic closing

Features:
- Guided intake conversation to gather context and evidence
- Automatic evidence mining via WorkIQ/M365 when available
- Enterprise framing and Microsoft culture alignment
- Calibrated length (400-800 words total)
- Copy-paste ready output matching the exact Perspectives form fields

### Authoring Toolbox Prompts
**Author and upgrade .ttp / .ttt threat-hunting prompts for the Toolbox_EXE library.**

Produces high-signal detection prompts with structured JSON findings, MITRE mapping, and anti-false-positive guardrails:
- **7-block SystemPrompt anatomy** — Objective, Be vigilant for, Safe patterns, Detection Checklist, Instruction Details, Rewards, Response Schema
- **Tiered impact levers** — Tier 1 baseline correctness through Tier 4 production discipline
- **Severity + confidence rubrics** — stable criteria for critical/high/medium/low/informational plus 0-100 confidence gating
- **Hardening clauses** — copy-paste no-speculation, attribution-verbatim, prompt-injection defense, coherence check
- **3-example few-shot recipe** — positive / ambiguous-graded / negative for confidence calibration

Features:
- Ready-to-adapt `.ttp` and `.ttt` scaffolds
- Concrete before/after upgrade example on a real library prompt
- `validate.py` format + discipline checker for CI use
- Format reference for `.ttp` (single prompt) and `.ttt` (tape chain)

## Installation

```bash
# Clone to your Copilot CLI plugins directory
git clone https://github.com/3ch0p01nt/AI_Skills.git ~/.copilot/installed-plugins/ai-skills
```

## Plugin Structure

```
AI_Skills/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Skill registry
├── skills/
│   ├── connect/
│   │   └── SKILL.md         # Connect skill definition
│   ├── perspectives/
│   │   └── SKILL.md         # Perspectives skill definition
│   └── authoring-toolbox-prompts/
│       ├── SKILL.md                # Skill definition
│       ├── template-prompt.ttp     # Tier-2 scaffold for single prompts
│       ├── template-tape.ttt       # Scaffold for tape chains
│       ├── example-upgrade.md      # Before/after library prompt upgrade
│       └── validate.py             # Format + discipline validator
└── README.md
```

## License

MIT
