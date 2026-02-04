# 🚀 Claude AI Project Guide for [YOUR-DOMAIN]

**Quick Navigation:**
- [Start New Session](#-start-new-session) - How to begin working
- [End Session](#-end-session) - How to close your work
- [Project Structure](#-project-structure) - What's where
- [Common Workflows](#-common-workflows) - Task guides
- [Files Reference](#-files-reference) - Purpose of each file

---

## 🎯 Start New Session

**Use the slash command:**

### Quick Start

Simply run:
```
/start-session
```

This is a **Claude Code skill** that automatically loads all context files and provides a status summary.

**Implementation:** See `skills/start-session/SKILL.md`

### Manual Protocol (if needed)

#### Step 1: Load Core Context (REQUIRED)
Read these 3 files in this order:

```
1. .claude/context/active-context.md    → What's happening NOW
2. .claude/context/progress.md          → What's been DONE
3. .claude/memory/memory-bank.md        → What we LEARNED
```

#### Step 2: Verify Understanding
Before starting work, confirm you understand:
- ✓ Current sprint priorities
- ✓ Any active blockers
- ✓ What was completed recently
- ✓ What needs to be done next

#### Step 3: Provide Status Summary
Report back to user:
- Current phase
- This week's priorities
- Recent completions
- Active blockers
- Ask: "What would you like to work on?"

#### Step 4: Start Working
- Use TodoWrite tool to track tasks during session
- Check relevant workflows as needed
- Update context as you go

---

## 💾 End Session

**Use the slash command:**

### Quick End

Simply run:
```
/end-session
```

This **Claude Code skill** will automatically update tracking files, commit changes, and provide a summary.

**Implementation:** See `skills/end-session/SKILL.md`

### Manual Protocol (if needed)

#### Step 1: Update Progress (REQUIRED)
Update [.claude/context/progress.md](.claude/context/progress.md):

```markdown
### Week of [Date]

**Completed:**
- ✅ [What was done]
- ✅ [What was done]

**In Progress:**
- 🔄 [What's ongoing]

**Blockers:**
- ⚠️ [Any issues]

**Next Week Priorities:**
1. [Priority 1]
2. [Priority 2]
```

### Step 2: Update Active Context (REQUIRED)
Update [.claude/context/active-context.md](.claude/context/active-context.md):
- Move completed tasks to "Recent Completions"
- Update current priorities status
- Update blockers section
- Update "Working Notes (This Session)"

### Step 3: Commit to Git (REQUIRED)
```bash
git add [changed files]
git commit -m "Session [date]: [summary]

[Detailed description]

Key changes:
- [Change 1]
- [Change 2]

Next steps:
- [Action 1]
- [Action 2]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main
```

### Step 4: Provide Summary
Tell the user:
- What was accomplished
- Files created/modified
- Key decisions made
- Next steps
- Any blockers/questions

---

## 📁 Project Structure

### Core Files (Read These Often)

| File | Purpose | When to Read | When to Update |
|------|---------|--------------|----------------|
| **[active-context.md](context/active-context.md)** | Current priorities, next actions | Every session start | Every session end |
| **[progress.md](context/progress.md)** | Phase status, milestones, weekly log | Every session start | When tasks complete |
| **[memory-bank.md](memory/memory-bank.md)** | Long-term insights, learnings | Every session start | When learning new things |
| **[decisions.md](memory/decisions.md)** | Strategic decisions with rationale | When making decisions | When decisions made |

### Workflow Guides (Read When Doing Tasks)

| File | Purpose | When to Use |
|------|---------|-------------|
| **[SEO_WORKFLOW.md](workflows/SEO_WORKFLOW.md)** | 8-phase overall strategy | Initial project setup |
| **[KEYWORD_RESEARCH_TEMPLATE.md](workflows/KEYWORD_RESEARCH_TEMPLATE.md)** | How to research keywords | During keyword research |
| **[CONTENT_CALENDAR_TEMPLATE.md](workflows/CONTENT_CALENDAR_TEMPLATE.md)** | Content planning guide | Planning content schedule |
| **[CONTENT_WRITING_GUIDE.md](workflows/CONTENT_WRITING_GUIDE.md)** | Writing templates & standards | Writing articles |
| **[SEO_FILTERS_IMPLEMENTATION.md](workflows/SEO_FILTERS_IMPLEMENTATION.md)** | InSales filters guide | Implementing SEO filters |

### Project Info (Read Once/Rarely)

| File | Purpose | When to Use |
|------|---------|-------------|
| **[claude.md](claude.md)** | Complete project overview | Onboarding, major changes |
| **[content-generation.md](prompts/content-generation.md)** | Reusable prompts | When writing content |

---

## ⚡ Available Slash Commands

These are **Claude Code skills** that automate common tasks:

| Command | What It Does | Usage Example |
|---------|--------------|---------------|
| `/start-session` | Load context files and provide status summary | `/start-session` |
| `/end-session` | Update tracking files, commit changes, provide summary | `/end-session` |
| `/monthly-report` | Generate monthly SEO performance report structure | `/monthly-report` or `/monthly-report 2026-02` |
| `/analyze-webmaster` | Analyze Yandex Webmaster reports and generate insights | `/analyze-webmaster` or `/analyze-webmaster 2026-01-27` |
| `/analyze-gsc` | Analyze Google Search Console query trend reports | `/analyze-gsc` or `/analyze-gsc 2026-01-27` |

**Implementation:** All skills are defined in `.claude/skills/[skill-name]/SKILL.md`

---

## 🔄 Common Workflows

### Workflow 1: Start Keyword Research
1. Read [workflows/KEYWORD_RESEARCH_TEMPLATE.md](workflows/KEYWORD_RESEARCH_TEMPLATE.md)
2. Use Yandex Wordstat for research
3. Save results in `/research/keywords/`
4. Update [active-context.md](context/active-context.md) with status
5. Update [progress.md](context/progress.md) when complete

### Workflow 2: Write New Article
1. Check [active-context.md](context/active-context.md) for content priorities
2. Review keyword research in `/research/keywords/`
3. Use template from [workflows/CONTENT_WRITING_GUIDE.md](workflows/CONTENT_WRITING_GUIDE.md)
4. Save draft in `/content/drafts/`
5. After publishing, move to `/content/published/`
6. Update [progress.md](context/progress.md)

### Workflow 3: Implement SEO Filters
1. Read [workflows/SEO_FILTERS_IMPLEMENTATION.md](workflows/SEO_FILTERS_IMPLEMENTATION.md)
2. Complete keyword research first
3. Follow 4-phase implementation plan
4. Track progress in [active-context.md](context/active-context.md)
5. Log decisions in [decisions.md](memory/decisions.md)

### Workflow 4: Fix Technical Issues
1. Check audit report: `/research/website-audit-2026-01.md`
2. Prioritize critical issues from [active-context.md](context/active-context.md) Priority 0
3. Implement fixes (requires backend access)
4. Document what was done in [progress.md](context/progress.md)
5. Update [memory-bank.md](memory/memory-bank.md) with learnings

### Workflow 5: Monthly Performance Review
1. Use slash command: `/monthly-report` or `/monthly-report 2026-02`
2. Collect data from Yandex.Metrica, Google Analytics
3. Fill in template: `/research/analytics/monthly-reports/report-[YYYY-MM].md`
4. Update metrics in [progress.md](context/progress.md)
5. Add insights to [memory-bank.md](memory/memory-bank.md)
6. Adjust priorities in [active-context.md](context/active-context.md)

### Workflow 6: Analyze Search Performance Data
**Yandex Webmaster (comprehensive data):**
1. Download .zip export from Yandex Webmaster to `/research/webmasters/`
2. Use slash command: `/analyze-webmaster` or `/analyze-webmaster 2026-01-27`
3. Review generated analysis report with clicks, CTR, positions

**Google Search Console (supplementary trends):**
1. Export query trend CSV from GSC to `/research/webmasters/`
2. Use slash command: `/analyze-gsc` or `/analyze-gsc 2026-01-27`
3. Review 7-day impression trends and patterns

**Next steps:**
4. Cross-reference findings between platforms
5. Identify platform-specific opportunities
6. Update content priorities in [active-context.md](context/active-context.md)

---

## 📂 Directory Layout

```
.claude/
├── README.md                    ← YOU ARE HERE (start here!)
├── claude.md                    → Project overview (read once)
│
├── context/                     → Current state (read EVERY session)
│   ├── active-context.md        → Current priorities & next actions
│   └── progress.md              → What's completed, milestones
│
├── memory/                      → Long-term knowledge
│   ├── memory-bank.md           → Strategic insights & learnings
│   └── decisions.md             → Decision log with rationale
│
├── workflows/                   → HOW-TO guides
│   ├── SEO_WORKFLOW.md
│   ├── KEYWORD_RESEARCH_TEMPLATE.md
│   ├── CONTENT_CALENDAR_TEMPLATE.md
│   ├── CONTENT_WRITING_GUIDE.md
│   └── SEO_FILTERS_IMPLEMENTATION.md
│
└── prompts/                     → Reusable prompts
    └── content-generation.md
```

---

## 🎯 Single Source of Truth for TODOs

**ALL active tasks are tracked in:**
- **[.claude/context/active-context.md](context/active-context.md)** - Current sprint priorities (this week)

**Long-term milestones are tracked in:**
- **[.claude/context/progress.md](context/progress.md)** - Phase completion, milestone tracker

**DO NOT** create TODO lists in other files (workflows, memory, etc.).

---

## ✅ Session Checklist

### At START of Every Session:
- [ ] Read `active-context.md`
- [ ] Read `progress.md`
- [ ] Read `memory-bank.md`
- [ ] Understand current priorities
- [ ] Check for active blockers

### DURING Session:
- [ ] Use TodoWrite tool to track tasks
- [ ] Log important decisions to `decisions.md`
- [ ] Add new insights to `memory-bank.md`
- [ ] Keep user informed of progress

### At END of Every Session:
- [ ] Update `progress.md` weekly log
- [ ] Update `active-context.md` priorities
- [ ] Mark completed tasks/milestones
- [ ] Commit all changes to git
- [ ] Push to GitHub
- [ ] Provide session summary to user

---

## 🆘 Troubleshooting

**"I don't know what to do next"**
→ Read [active-context.md](context/active-context.md) - it has your immediate priorities

**"Why did we make this decision?"**
→ Check [decisions.md](memory/decisions.md) for rationale

**"What's our current progress?"**
→ Check [progress.md](context/progress.md) for metrics and milestones

**"How do I implement X?"**
→ Check [workflows/](workflows/) for relevant guide

**"What have we learned about Y?"**
→ Check [memory-bank.md](memory/memory-bank.md) for insights

---

## 🔗 Quick Links

### Essential Reading
- [Current Priorities](context/active-context.md) ← START HERE
- [Progress Tracking](context/progress.md)
- [Strategic Insights](memory/memory-bank.md)
- [Decisions Log](memory/decisions.md)

### Implementation Guides
- [Overall SEO Strategy](workflows/SEO_WORKFLOW.md)
- [Keyword Research](workflows/KEYWORD_RESEARCH_TEMPLATE.md)
- [Content Writing](workflows/CONTENT_WRITING_GUIDE.md)
- [SEO Filters Guide](workflows/SEO_FILTERS_IMPLEMENTATION.md)

### Project Info
- [Complete Overview](claude.md)
- [Website Audit Report](../research/website-audit-2026-01.md)

---

## 💡 Key Principles

1. **Always load context first** - Never skip reading the 3 core files at session start
2. **Single source of truth** - TODOs go in active-context.md only
3. **Update as you go** - Don't batch updates at the end
4. **Document decisions** - Future you will thank you
5. **Commit often** - Git is your safety net
6. **Be explicit** - Tell user what you're doing and why

---

**Last Updated:** January 27, 2026
**Status:** Active - Planning Phase
**Next Review:** As project structure evolves
