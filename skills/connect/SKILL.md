---
name: connect
description: Draft a complete Microsoft Connect self-reflection through guided conversation. Covers all 5 Connect form sections (Goals, Impact, Challenge, Plan, Key Metrics) plus the companion Impact Card. Mines M365 data for evidence, applies calibration guidance, and produces copy-paste ready output. Use when the user wants to write their Connect, prepare for a Connect conversation, build their Impact Card, or draft their self-assessment for performance review.
---

# Microsoft Connect Skill

Draft a complete, high-quality Microsoft Connect self-reflection and companion Impact Card through guided, evidence-based conversation. Produces copy-paste ready output calibrated to what managers need for advocacy during calibration.

## When to Activate

Activate when the user:
- Wants to write or update their Connect self-reflection
- Needs help preparing for a Connect conversation with their manager
- Asks to build or update their Impact Card (baseball card)
- Wants to draft their self-assessment for performance review
- Mentions Connect, self-reflection, performance review, calibration, or Impact Card
- Asks to capture accomplishments for their end-of-year or mid-year review

## Understanding the Connect Ecosystem

### What Is a Connect?

Microsoft Connects replaced the old stack-ranking performance review system. Key principles:
- **No forced rankings** — managers advocate for employees through narrative, not numbers
- **WHAT + HOW equally weighted** — results AND behaviors/culture both matter for rewards
- **Ongoing conversations** — not a once-a-year event, though Spring (end-of-year) is the primary rewards cycle
- **Growth-oriented** — setbacks and learning are valued, not punished

### The Two Documents

| Document | Purpose | Audience | Format |
|----------|---------|----------|--------|
| **Connect Self-Reflection** | Your narrative — tells the full story of your impact, challenges, growth | Manager (for 1:1 conversation and calibration advocacy) | Long-form paragraphs, pasted into Connect form |
| **Impact Card (Baseball Card)** | Manager's cheat sheet — cliff notes for calibration room | Manager → M2/M3 → calibration panel of peer managers | 1-slide PowerPoint, bullet points, both-sides-of-coin framing |

**Critical relationship**: The Connect feeds the Impact Card. Your Connect should be rich enough that your manager can distill cliff notes from it. The Impact Card is NOT a copy-paste of the Connect — it's a compressed, advocacy-optimized summary.

### How Calibration Works

1. Your M1 (direct manager) presents your Impact Card to peer M1s and M2 (skip-level)
2. Other managers challenge, compare, and calibrate across the team
3. The Impact Card IS your manager's ammunition — make it easy to advocate for you
4. **Reward multiplier** is determined through this discussion (affects bonus/stock)
5. Managers who come with specific, quantified, both-sides-of-coin narratives win the room

### The Connect Form Sections

The actual Microsoft Connect form has these sections:

1. **Goals** — Review your goals and rate progress
2. **Summarize Your Impact** — Your biggest accomplishments and their business outcomes
3. **Reflect on a Challenge or Setback** — What went wrong and what you learned
4. **Review Your Goals** — Status table showing progress against each goal
5. **How Will You Reach Your Goals?** — Forward-looking plan for remainder of period

## Relationship to Connects-Intake Skill

This skill and the `connects-intake` skill are complementary:
- **connects-intake** = capture individual wins as they happen throughout the year → stored as `Win - *.md` notes in Obsidian with structured frontmatter
- **connect** (this skill) = assemble accumulated wins into the complete Connect self-reflection + Impact Card at review time

**Workflow**: Use `connects-intake` throughout the year to log wins → Use this `connect` skill at mid-year and end-of-year to synthesize everything into your Connect submission.

When this skill activates, check `04 - Wins/` in the Obsidian vault for existing Win notes. Also check these vault files for framework context:
- `07 - Professional Development/Performance Reviews/Connects Framework.md` — WHAT/HOW structure
- `07 - Professional Development/Performance Reviews/Connects Goals.md` — the 4 organizational goals
- `07 - Professional Development/Performance Reviews/FY26 H1 Connect.md` — mid-year submission examples
- `07 - Professional Development/Performance Reviews/FY26 Manager Feedback.md` — manager coaching themes

## Intake Workflow

### Step 0: Parse What's Already Available

Before asking questions, silently inventory what's already present:

| Source | What to Look For |
|--------|-----------------|
| **Obsidian Win notes** (`04 - Wins/`) | Structured accomplishments with frontmatter (client, project, category, goals, behaviors, impact) |
| **Prior Connect submissions** | Mid-year draft, previous year's Connect for style/tone reference |
| **Impact Card / Talent Card** | Existing metrics, goal framing, manager-approved language |
| **Manager 1:1 notes** | Coaching themes, specific guidance on framing |
| **Perspectives received** | Peer feedback that validates claims |

Identify which of these fields are already covered across available sources:

| Field | Description | Example Signal |
|-------|-------------|----------------|
| **Action** | What specifically they did (verb + object) | "built", "deployed", "resolved", "led" |
| **Client** | Which customer | Customer name or project context |
| **Project** | Named initiative | Project name reference |
| **Category** | Win type: delivery, technical, leadership, relationship, efficiency, recognition | Nature of the accomplishment |
| **Quantified Impact** | Numbers: dollars, percentages, time saved, TB, hours, people impacted | Any numeric value |
| **Business Outcome** | What it enabled: ACR, adoption, risk reduction, time-to-value, compliance | Business language |
| **Goal Alignment** | Which of the 4 Connects goals this maps to | Goal keywords (see below) |
| **Behaviors** | Microsoft behaviors demonstrated | Collaboration, learning, mentoring signals |
| **AI Lens** | Whether AI/Copilot was involved or enabled | AI, Copilot, AOAI, automation |
| **Security Lens** | Security implications or improvements | Threat, detection, compliance, posture |
| **Timeline** | When this happened | Date references |
| **Evidence** | Artifacts, feedback, metrics, deliverables | Tangible outputs |

Only ask about fields that are NOT already covered by existing data.

### Step 1: Understand Context

Ask the user:
- What review period? (e.g., FY26 Spring, FY26 Mid-Year)
- What level are they? (IC levels matter for framing — L63 vs L65 vs L67 have different expectations)
- What are their organizational goals? (Usually 3-5, set at beginning of fiscal year)
- Do they have an existing Connect draft or mid-year submission to build from?
- Do they have manager guidance or feedback from their M1? (This is critical calibration input)

### Step 2: Gather Evidence

**If WorkIQ or Microsoft 365 MCP tools are available**, proactively search for:
- All emails, Teams chats, and meetings for the review period
- Customer feedback, recognition emails, thank-you notes
- Manager 1:1 meeting notes and transcripts
- Win notes in Obsidian vault (if available)
- Prior Connect submissions and Impact Cards
- Billing/utilization data, revenue metrics
- Peer feedback and Perspectives received

**If data tools are not available**, ask the user in priority order:

#### Priority 1 — Required (always ask if missing)
1. "What are your top 3 accomplishments this period? For each: what did you do, what was the measurable result?"
2. "What are your organizational goals, and how did you perform against each?"
3. "What revenue/business metrics can you claim? (ACR, NNR, pipeline, utilization, hours billed)"

#### Priority 2 — High Value (ask if not inferrable)
4. "Did you receive any formal recognition, customer praise, or leadership call-outs?"
5. "Who did you mentor, enable, or help grow? What was the measurable outcome?"
6. "What reusable IP, tools, or assets did you create that others use?"
7. "Was AI/Copilot involved in how you did this or what you delivered?" *(AI Lens)*
8. "Were there security implications or improvements?" *(Security Lens)*

#### Priority 3 — Critical for Completeness (ask if conversation is flowing)
9. "What was your biggest challenge or setback? What did you learn?"
10. "What's your plan for the remainder of the review period?"
11. "Has your manager given you any specific feedback or guidance on how to frame things?"
12. "Any artifacts — deliverables, dashboards, feedback, emails, metrics you can point to?" *(Evidence)*

#### When to Stop Asking

Stop gathering and start drafting when you have:
- At least 3 specific accomplishments with quantified impact or clear business outcomes
- Goal status for all organizational goals
- At least one revenue/business metric
- A challenge/setback identified
- Enough context to write the Challenge → Solution → Impact pattern for each impact area

### Step 3: Verify and Source

**Every claim must have a source.** Apply this verification framework:

| Claim Type | Acceptable Sources | Red Flags |
|-----------|-------------------|-----------|
| Revenue/ACR | Talent Card, billing reports, Win Wire, manager confirmation | Round numbers without source, "approximately" without basis |
| Customer praise | Email with date and sender, Teams message, trip report | Paraphrased without attribution |
| Metrics (TB, licenses, hours) | Specific email/Teams message with date | Aggregated estimates without individual sources |
| Collaboration claims | Calendar invites, email threads, meeting transcripts | Vague "worked with" without specifics |
| Impact statements | Documented before/after with dates | Claimed outcomes without causal link |

**If a claim cannot be sourced, flag it clearly** rather than including it as fact.

### Step 4: Apply Manager Guidance

If the user has received manager coaching, integrate it as calibration lens. Common manager guidance patterns:

#### Typical M1 Guidance Themes
- **"Cliff notes not chapters"** — Impact Card should be scannable; Connect can be longer
- **"Both sides of the coin"** — Every accomplishment should show customer value AND Microsoft value
- **"Acceleration framing"** — Show before→after, not just current state
- **"Numbers tell the story"** — Quantify everything; revenue, time saved, scope, scale
- **"Level-appropriate framing"** — L63: depth of execution. L65: cross-practice improvement. L67: org-level strategy
- **"Top 3 + there's more"** — Lead with biggest hits, signal breadth without overwhelming
- **"Quality over quantity"** — 2-4 key impacts, not a laundry list
- **"Spring = impact, Fall = planning"** — Spring Connects skew toward retrospective impact (tied to rewards/calibration). Fall skews toward future goals/development
- **"Bottom half of the Impact Card"** — Focus updates on key wins section, not the goals/compliance rows
- **"2 business days before"** — Written submission due before the Connect meeting; manager annotates and returns morning-of for discussion

### Step 5: Draft the Connect

Draft all 5 sections following the frameworks below.

## Section-by-Section Writing Framework

### Section 1: Goals

Format as a numbered list with brief status and key evidence:

```
1. **Compliance** — 100% compliant. [One line.]
2. **[Goal Name]** — [Status]. [Key metrics]. [One-line evidence.]
3. **[Goal Name]** — [Status]. [Key metrics]. [One-line evidence.]
4. **[Goal Name]** — [Status]. [Key metrics]. [One-line evidence.]
5. **Career Growth** — [One line max.]
```

**Calibration notes:**
- Compliance is always one line — "met" is sufficient
- Career Growth is one line max — it's table stakes, not a differentiator
- ACR/revenue goals should lead with numbers and the word "acceleration" (before→after)
- AI goals: if redundant with Impact section, write "See impact summary below"
- Service Delivery: frame at level-appropriate lens (L65 = how you made delivery better across the practice, not just your accounts)

### Section 2: Summarize Your Impact

This is the heart of the Connect. Structure as **Top 3 Impact Areas** with the pattern:

```
### [Impact Area Title] — [Customer Value + Microsoft Value]

[Problem statement: What was the customer/org challenge? 2-3 sentences.]

[What you did: Specific actions with strong verbs, named technologies, named people. Dense paragraph.]

[Additional wins under this theme: "There are additional wins beyond these top hits..." — signals breadth]

[Both-sides summary: "For the customer, this means... For Microsoft, this means..."]
```

**Writing rules:**
- Lead with the biggest impact area first
- Each area follows: Challenge → Solution → Impact (CSI) arc
- Use first person ("I architected", "I drove", "I coordinated")
- Name specific people, technologies, customers, and projects
- Quantify everything: dollars, percentages, time saved, endpoints, TB, hours, people
- Show "both sides of the coin" — customer value AND Microsoft value
- After top 3, include a "there's more" signal: brief mentions of additional wins grouped thematically
- Include direct quotes from stakeholders with attribution and date
- Avoid: vague praise, passive voice, hedging language, unquantified claims

**Length guidance:** Per typical manager guidance, "go a little more long form" than the Impact Card — "don't write a chapter, write a paragraph." Each impact area should be 1-3 substantive paragraphs plus a brief "additional wins" paragraph.

**Action → Impact → Value pattern:**
- **Do**: "Displaced Splunk as the Navy's Tier-1 SIEM by architecting the Sentinel Data Lake, resulting in unified security visibility and $2.6M ACR protected."
- **Don't**: "Worked on Sentinel for the Navy customer."

### Section 3: Reflect on a Challenge or Setback

This section demonstrates Growth Mindset — the HOW of performance. Structure:

```
[Specific situation: What happened? Name the project/context. 2-3 sentences.]

[What you did to mitigate: Concrete actions taken. 2-3 sentences.]

[What you learned: One clear, honest takeaway. 1-2 sentences.]
```

**Calibration notes:**
- Pick a REAL challenge, not a humble-brag ("my biggest challenge was being too excellent")
- Show responsible trade-off management, not failure
- The learning should be forward-looking and actionable
- This section should be SHORT — 1 paragraph for situation/action, 1 sentence for learning
- Good challenges: competing priorities forcing trade-offs, structural constraints, delegation decisions
- Bad challenges: things that were actually wins in disguise

### Section 4: Review Your Goals (Table)

Format as a status table:

```
| Goal | Status | Evidence |
|------|--------|----------|
| **Compliance** | ✅ Met | 100% on-time |
| **[Goal]** | ✅ Exceeded / ✅ Met / ⚠️ In Progress | [Key metric + source] |
```

**Rules:**
- Use ✅ for met/exceeded, ⚠️ for in progress, ❌ for not met
- Evidence column should reference specific metrics and sources
- Keep each row to one line — this is a summary, not a narrative

### Section 5: How Will You Reach Your Goals?

Forward-looking priorities for the remainder of the review period:

```
For the remainder of FY[XX], my top priorities are:

1. **[Priority]** — [specific action + expected outcome]
2. **[Priority]** — [specific action + expected outcome]
3. **[Priority]** — [specific action + expected outcome]

There are additional items in motion — [brief list] — that will continue progressing alongside these priorities.
```

**Rules:**
- 3-6 numbered priorities, ordered by impact
- Each should have a clear action AND expected outcome
- Include a "there's more" line to signal breadth
- Be realistic — these become commitments you'll be measured against
- Tie back to organizational goals where possible

## Companion: Impact Card (Baseball Card)

After drafting the Connect, offer to create the Impact Card. The Impact Card is a **1-slide PowerPoint** optimized for the calibration room.

### Impact Card Structure

Typical rows (varies by org):

| Row | Content | Guidance |
|-----|---------|----------|
| **Compliance** | One line | "100% compliant" — done |
| **ACR / Revenue** | Numbers only | Use "acceleration" framing: before→after |
| **AI Adoption** | If redundant with bottom rows | "See below" is acceptable |
| **Service Delivery** | Level-appropriate lens | L65: how you improved delivery across the practice |
| **Career Growth** | One line max | Table stakes, not differentiator |
| **[Bottom Rows: Key Wins]** | Cliff notes, priority order | Biggest impact first. Challenge→Solution→Impact. Both sides of coin. |

### Impact Card Writing Rules
- **Cliff notes, not chapters** — scannable in 30 seconds
- **Both sides of the coin** — customer value + Microsoft value on every row
- **Acceleration framing** — show the before→after transformation
- **Priority order** — biggest impact first
- **No jargon without context** — the M2 and peer M1s may not know your acronyms
- **Numbers tell the story** — revenue, percentages, scale, scope

## Key Metrics Table

Every Connect should include a sourced metrics table:

```
| Metric | Value | Source |
|--------|-------|--------|
| [Metric name] | [Value] | [Specific source with date] |
```

**Rules:**
- Every number must have a named source (email, Teams message, report) with date
- Flag stale or estimated metrics clearly
- Include utilization if available (it's a baseline expectation for consulting)

## Key Quotes Table

Include direct stakeholder quotes with attribution:

```
| Quote | Who | Source |
|-------|-----|--------|
| *"exact quote"* | Name (Role) | Source, Date |
```

**Rules:**
- Use exact quotes, not paraphrases
- Include role/title for context
- Date the source for verifiability
- Prioritize customer quotes, then leadership, then peers

## Quality Checklist

### Calibration Lenses

> [!important] Year-End Differentiators
> Apply these calibration lenses when writing (from common manager feedback patterns):
> - **Quantify everything** — dollars, percentages, time saved, people impacted
> - **Show AI impact, not just readiness** — adoption metrics, overhead reduction, not just "I built it"
> - **Mentorship needs measurable outcomes** — someone got promoted, recognized, or unblocked
> - **Connect learning to business metrics** — translate skill growth into delivery speed, risk reduction, CSAT
> - **Show influence scaling** — not just doing, but enabling others to do
> - **Internal + external values** — don't only show customer-facing behaviors

### Final Verification

Before finalizing, verify:

- [ ] Every revenue/metric claim has a named source with date
- [ ] Each impact area shows both customer AND Microsoft value
- [ ] Challenge section is honest, not a humble-brag
- [ ] Forward plan is realistic and ties to org goals
- [ ] No nation-state names in any document (use "nation-state actor" instead)
- [ ] Attribution is accurate (don't claim credit for others' work)
- [ ] Level-appropriate framing applied
- [ ] Manager guidance incorporated (if provided)
- [ ] Utilization/billing data included (for consulting roles)
- [ ] Direct quotes are exact and attributed

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Claiming credit for what you contributed to vs. what you built | "Assisted in design of X" vs "Designed X" — be precise |
| Unquantified impact | Every "resulting in" needs a number or named outcome |
| Revenue claimed as closed when it's anticipated | Use "anticipated $XM" not "$XM" for pipeline |
| Protecting ACR treated as less than generating ACR | Protecting existing revenue IS a valid achievement — frame it as defense |
| Too much detail on one area, nothing on others | Top 3 + "there's more" structure prevents this |
| Challenge section reads as a win | Pick a real trade-off with a real learning |
| Goals table says "exceeded" without evidence | Back every status with a specific metric |
| Forward plan is aspirational without actionable steps | Each priority needs a concrete action + expected outcome |
| Using passive voice | "I architected" not "the architecture was designed" |
| Mentorship without measurable outcomes | "Mentored X → they achieved Y" not "mentored X" |

## Behavioral Mapping

Connect feedback evaluates WHAT (impact/results) and HOW (behaviors). Map accomplishments to both:

### Microsoft Core Behaviors
| Behavior | Signals in Your Work |
|----------|---------------------|
| **Growth Mindset** | Iterated, learned from failure, experimented, shared knowledge, upskilled |
| **Customer Obsession** | Addressed customer gap, resolved blocker, preemptive action, exceeded expectations |
| **One Microsoft** | Cross-team collab, partner coordination, ecosystem orchestration |
| **Diversity & Inclusion** | Mentored, created inclusive environments, championed underrepresented voices |
| **Integrity** | Compliance, ethical decisions, transparent communication, recommended no-bid |
| **Accountability** | Owned outcomes, followed through, escalated risks, met commitments |

### Goal Mapping (ISD Federal Consulting)
| Goal | Keywords/Signals |
|------|-----------------|
| **Goal 1 — Transformational Deals & Consumption** | ACR, NNR, ECIF, partner orchestration, multi-solution-area, consumption, adoption, time-to-value, customer transformation |
| **Goal 2 — AI, Cloud & Security Solutions Depth** | AI integration, Copilot, Sentinel, Defender, XDR, identity, Zero Trust, certifications, solution area expertise, thought leadership |
| **Goal 3 — AI-First Delivery & Operational Excellence** | Utilization, delivery quality, trusted advisor, IP creation, AI-first methods, cost efficiency, customer strategy, operational hygiene |
| **Goal 4 — Trust, Culture & Compliance** | Compliance, training, values, ethics, culture, diversity, inclusion, mentorship culture |

## Level-Appropriate Framing

| Level | What Calibration Looks For |
|-------|---------------------------|
| **L63 (Consultant)** | Depth of execution, learning velocity, reliable delivery, growing independence |
| **L64 (Sr Consultant)** | Independent delivery, client relationship ownership, starting to enable others |
| **L65 (Principal Consultant)** | Cross-practice improvement, reusable IP, mentoring to measurable outcomes, strategic judgment, force multiplication |
| **L66-67 (Principal+)** | Org-level strategy, practice-wide capability building, business development, executive influence |

**Key L65 differentiators:**
- "How I made delivery better across the practice" — not just your own accounts
- Reusable IP that others actually use
- Mentees who achieved measurable outcomes (promotion, independent delivery, recognition)
- Strategic judgment calls (no-bids, architecture decisions) that saved/generated revenue
- Force multiplication — enabling the org to do more without proportional headcount

## Consulting-Specific Metrics

For Microsoft Federal ISD consulting roles, always include:

| Metric | Why It Matters |
|--------|---------------|
| **Utilization** | Baseline expectation — % billable and % total |
| **Hours billed** | Total hours across contracts |
| **Number of contracts** | Breadth of delivery |
| **ACR protected** | Defending existing revenue from competitor displacement |
| **ACR generated** | New revenue driven by your work |
| **Pipeline created** | Future revenue opportunities you influenced |
| **Customer recognition** | Formal recognition requests, CTO/CDR feedback |
| **IP created** | Tools, templates, frameworks reused by others |
| **Mentees** | Number + outcomes (independent delivery, promotion, recognition) |

## Output Format

Present the draft in sections matching the Connect form, using markdown for readability:

```markdown
## Goals
[Numbered list]

## Summarize Your Impact
### 1. [Title] — [Customer + Microsoft Value]
[Narrative]
### 2. [Title]
[Narrative]
### 3. [Title]
[Narrative]

## Reflect on a Challenge or Setback
[Narrative + learning]

## Review Your Goals
[Status table]

## How Will You Reach Your Goals?
[Numbered priorities]

## Key Metrics (All Sourced)
[Metrics table]

## Key Quotes (All Sourced)
[Quotes table]
```

### Step 6: Review and Iterate

After presenting the draft:
1. Ask if any sections need adjustment
2. Verify all metrics and claims with the user
3. Offer to create the companion Impact Card
4. Confirm it's ready for the Connect form

## References

- Microsoft Connect form: aka.ms/connect
- Impact Card template: Varies by org — check with M1
- Perspectives feedback: aka.ms/perspectives
- Microsoft Culture & Values: Growth Mindset, Customer Obsession, One Microsoft, D&I, Accountability
- Obsidian connects-intake skill: For capturing individual Win notes (this skill assembles wins into the complete Connect narrative)
