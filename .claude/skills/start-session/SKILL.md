---
name: start-session
description: Load project context at the beginning of a session
---

# Start Session

When this skill is invoked:

## Step 1: Load Context Files

Read these files in order:
1. `.claude/client/client.md` — Client profile and project data
2. `.claude/context/active-context.md` — Current sprint and priorities
3. `.claude/context/progress.md` — Phase completion status
4. `.claude/memory/memory-bank.md` — Strategic insights and learnings

## Step 2: Determine Current Phase

From `progress.md`, identify the current phase in the SEO Master Workflow:
- Phase 1: Website Analysis & Audit
- Phase 2: Keyword Research
- Phase 3: Competitor Analysis
- Phase 4: Content Strategy & Publication Plan
- Phase 5: Content Creation (monthly cycle)
- Phase 6: Review & Publish
- Phase 7: Social Media Amplification
- Phase 8: Link Building

Also check if **Monthly Close** is due (last working day of month).

## Step 3: Provide Status Summary

Present clearly with headers and bullet points:

### Status Summary Format
```
## Current Phase: [Phase N: Name]
**Workflow:** SEO Master Workflow → See SEO_WORKFLOW.md

### This Session's Priorities
1. [Priority from active-context.md]
2. ...

### Phase Progress
- [x] Completed task
- [ ] Pending task
- [ ] Next task

### Next Actions (from workflow)
- [Specific action from SEO_WORKFLOW.md for current phase]
- [Skill/script to use]: `/skill-name` (Model)

### Recent Completions
- [date]: [what was done]

### Blockers
- [any blockers from active-context.md]

### Quick Reference
- Client: [name] → See client.md
- Sites: [domains from client.md]
- Publishing schedule: [from client.md#publishing-schedule]
```

## Step 4: Suggest Next Action

Based on the current phase, suggest the specific next action from SEO_WORKFLOW.md:

| Phase | Suggested Next Action |
|-------|----------------------|
| 1 | "Run content audit: `venv/bin/python scripts/content_audit/main.py --full --all`" |
| 2 | "Start keyword research → See KEYWORD_RESEARCH_TEMPLATE.md" |
| 3 | "Begin competitor analysis → research/competitors/" |
| 4 | "Create content calendar → `/brainstorm` (Opus) or use CONTENT_CALENDAR_TEMPLATE.md" |
| 5 | "Write next article from calendar → `/writing-guide` (Sonnet)" |
| 6 | "Review draft → `/review-article` (Multi-model)" |
| 7 | "Generate social posts → `/create-social-posts` (Sonnet)" |
| 8 | "Work on link building strategy" |
| Monthly | "Run monthly close cycle → See SEO_WORKFLOW.md#monthly-close-cycle" |

End with: "Ready to proceed! What would you like to work on?"
