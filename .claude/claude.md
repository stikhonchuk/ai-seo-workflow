# Claude Project Context: SEO & Content Strategy

## Architecture

This project separates **client data** from **process/workflow**:

| Layer | Location | Purpose |
|-------|----------|---------|
| **Client Data** | `.claude/client/client.md` | Company, domains, services, audiences, CTAs, brand — change per client |
| **Master Workflow** | `.claude/workflows/SEO_WORKFLOW.md` | 8-phase SEO strategy — reusable across clients |
| **Skills** | `.claude/skills/*/SKILL.md` | Slash commands with model recommendations |
| **Critics** | `.claude/critics/*.md` | Content review criteria with model assignments |
| **Prompts** | `.claude/prompts/*.md` | Reusable content generation templates |
| **Context** | `.claude/context/*.md` | Current phase, progress, priorities |
| **Memory** | `.claude/memory/memory-bank.md` | Strategic insights and learnings |
| **Scripts** | `scripts/` | Automation (content audit, keyword processing) |

**To onboard a new client:** Update only `client/client.md`. All workflows, skills, and critics reference it.

## Current Client

→ See [client.md](client/client.md) for full details.
→ Copy `client/client.example.md` to `client/client.md` and fill in your data to get started.

## Workflow Overview

→ See [SEO_WORKFLOW.md](workflows/SEO_WORKFLOW.md) for the master workflow with all phase details.

### Phases
1. **Audit** — Content audit script + technical SEO analysis
2. **Keywords** — Research + `process_keywords.py` script
3. **Competitors** — Content gap analysis
4. **Strategy** — Content calendar creation
5. **Write** — `/writing-guide` (Sonnet) + content-generation prompts
6. **Review & Publish** — `/review-article` (multi-model critics)
7. **Amplify** — `/create-social-posts` (Sonnet) + SMM workflow
8. **Link Building** — Internal clusters + external outreach
- **Monthly Close** — Audit script → `/analyze-gsc` + `/analyze-webmaster` → `/monthly-report` → plan next month

### Skills & Models

| Skill | Model | Phase | Purpose |
|-------|-------|-------|---------|
| `/start-session` | — | Start | Load context, show phase & next actions |
| `/brainstorm` | Opus | 1, 4 | Content ideation |
| `/writing-guide` | Sonnet | 5 | Load writing standards |
| `/review-article` | Multi | 6 | 8-critic content review |
| `/create-social-posts` | Sonnet | 7 | Social media repurposing |
| `/monthly-report` | Sonnet | Monthly | Performance report |
| `/analyze-gsc` | Sonnet | Monthly | Google Search Console analysis |
| `/analyze-webmaster` | Sonnet | Monthly | Yandex Webmaster analysis |
| `/end-session` | — | End | Progress save, workflow compliance, commit |

### Critic Models (used by /review-article)

| Critic | Model | Focus |
|--------|-------|-------|
| SEO | Sonnet | Keywords, meta, structure, links |
| Russian Language | Opus | Grammar, phrasing, native quality |
| English Language | Opus | Tone, clarity, professional writing |
| E-E-A-T | Sonnet | Authority signals, trust |
| User Intent | Sonnet | Intent satisfaction, completeness |
| Readability | Haiku | Scannability, sentence structure |
| Commercial | Haiku | CTAs, conversion path |
| Image Prompts | Haiku | Visual validation, brand consistency |

## Current Phase

→ See [active-context.md](context/active-context.md) for current sprint and priorities.
→ See [progress.md](context/progress.md) for phase completion status.

## Working Principles

- Follow the master workflow phase by phase — don't skip phases
- Use the recommended model for each skill (see table above)
- Reference `client.md` for all client-specific data — never hardcode
- Every article must pass `/review-article` (score ≥7) before publishing
- Every session: `/start-session` at start, `/end-session` at end
- `/end-session` checks workflow compliance and generates retrospective

## Communication Style

- Professional and authoritative tone
- Data-driven decisions based on keyword research and analytics
- Bilingual awareness — consider both markets → See `client.md#market-separation-rules`
- Lead-generation focused — drive consultation requests through valuable content

---

**Last Updated:** 2026-03-09
**Status:** Template — Ready for client configuration
