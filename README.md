# AI Skills

Custom AI skills for GitHub Copilot CLI. These skills provide specialized capabilities for Microsoft professional development workflows.

## Installed Skills

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
│   └── perspectives/
│       └── SKILL.md         # Perspectives skill definition
└── README.md
```

## License

MIT
