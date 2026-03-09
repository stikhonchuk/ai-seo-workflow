# Claude AI Project Guide — SEO & Content Strategy

## Architecture

```
.claude/
├── claude.md                    ← Project overview (thin orchestrator)
├── client/
│   └── client.md                ← CLIENT DATA: company, domains, services, CTAs, brand
├── workflows/
│   ├── SEO_WORKFLOW.md          ← MASTER WORKFLOW: 8 phases + monthly cycle
│   ├── SMM_WORKFLOW.md          ← Social media repurposing (Phase 7)
│   ├── CONTENT_WRITING_GUIDE.md ← Writing reference (loaded by /writing-guide)
│   ├── KEYWORD_RESEARCH_TEMPLATE.md ← Keyword research methodology (Phase 2)
│   ├── CONTENT_CALENDAR_TEMPLATE.md ← Calendar template (Phase 4)
│   ├── MONTHLY_REPORT_TEMPLATE.md   ← Report template (Monthly Close)
│   └── monthly-content-audit.md     ← Content audit instructions (Phase 1/Monthly)
├── skills/
│   ├── SKILL.md                 ← Skills index (all skills by phase)
│   ├── start-session/           ← /start-session — load context, show phase
│   ├── end-session/             ← /end-session — save, compliance check, commit
│   ├── brainstorm/              ← /brainstorm — ideation (Opus)
│   ├── writing-guide/           ← /writing-guide — writing standards (Sonnet)
│   ├── review-article/          ← /review-article — 8-critic review (Multi)
│   ├── create-social-posts/     ← /create-social-posts — SMM (Sonnet)
│   ├── monthly-report/          ← /monthly-report — performance report (Sonnet)
│   ├── analyze-gsc/             ← /analyze-gsc — Google Search Console (Sonnet)
│   └── analyze-webmaster/       ← /analyze-webmaster — Yandex Webmaster (Sonnet)
├── critics/                     ← 8 content review critics (used by /review-article)
├── prompts/
│   └── content-generation.md    ← Article type prompt templates
├── context/
│   ├── active-context.md        ← Current phase, sprint, priorities
│   └── progress.md              ← Phase completion, milestones
├── memory/
│   └── memory-bank.md           ← Strategic insights, learnings
└── retrospectives/              ← Session retrospectives (from /end-session)
```

## Quick Start

### Start a Session
```
/start-session
```
Shows current phase, priorities, and next actions.

### End a Session
```
/end-session
```
Saves progress, checks workflow compliance, commits changes.

## Workflow Phases

→ See [SEO_WORKFLOW.md](workflows/SEO_WORKFLOW.md) for full details.

| Phase | Action | Skill/Script | Model |
|-------|--------|-------------|-------|
| 1. Audit | Run content audit | `content_audit/main.py` | — |
| 2. Keywords | Research & process | `process_keywords.py` | — |
| 3. Competitors | Analyze gaps | Manual research | — |
| 4. Strategy | Create calendar | `/brainstorm` | Opus |
| 5. Write | Draft articles | `/writing-guide` | Sonnet |
| 6. Review | Quality gate | `/review-article` | Multi |
| 7. Amplify | Social media | `/create-social-posts` | Sonnet |
| 8. Links | Build authority | Manual outreach | — |
| Monthly | Audit → Report → Plan | `/monthly-report` | Sonnet |

## Client Data vs Process

**To switch clients:** Update only `.claude/client/client.md`. All workflows, skills, and critics reference it via `→ See client.md#section` markers.

**Client data includes:** company info, domains, services, pricing, team, audiences, content pillars, CTAs, brand colors, social channels, UTM conventions, site structure, competitors, keywords.

**Process stays generic:** SEO workflow phases, writing standards, critic criteria, skill logic, scripts.

## Key Principles

1. **Follow the workflow** — phases are sequential, don't skip
2. **Use recommended models** — Opus for creative/nuanced, Sonnet for structured, Haiku for checklists
3. **Reference client.md** — never hardcode client data in workflows or skills
4. **Quality gate** — every article through `/review-article` (score ≥7) before publishing
5. **Session discipline** — `/start-session` at start, `/end-session` at end (with compliance check)

---

**Last Updated:** 2026-03-09
