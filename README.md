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
│   └── perspectives/
│       └── SKILL.md         # Perspectives skill definition
└── README.md
```

## License

MIT
