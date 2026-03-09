---
name: end-session
description: Save progress, update tracking files, run session retrospective, and commit changes at session end
---

# End Session

When this skill is invoked:

## Step 1: Workflow Compliance Check

Before anything else, check whether the session followed the SEO Master Workflow.

### 1a. Load Current Phase

Read `.claude/context/active-context.md` and `.claude/context/progress.md` to determine:
- Which phase the session was supposed to work on
- What tasks were on the priority list

### 1b. Analyze Session Against Workflow

Review the session transcript for:

**Workflow alignment:**
- Did the session work on the correct phase? (Phase from progress.md)
- Were the right skills/scripts used for this phase? → See SEO_WORKFLOW.md#skills--scripts-map
- Was the right model used? (Opus for brainstorming, Sonnet for writing, etc.)
- Were phase gate requirements addressed?

**Phase-specific checks:**

| Phase | Expected Actions | Check |
|-------|-----------------|-------|
| 1 | Content audit script run, audit analyzed | Script executed? Results reviewed? |
| 2 | Keywords researched, process_keywords.py used | Keywords documented in research/? |
| 3 | Competitors analyzed | competitor-analysis.md updated? |
| 4 | Content calendar created | Calendar file created in content/calendars/? |
| 5 | Article drafted, /writing-guide used | Draft saved to content/drafts/? |
| 6 | /review-article run, score ≥7 | Review report saved? Issues fixed? |
| 7 | /create-social-posts run | Social posts saved to content/social/? |
| Monthly | Audit → /analyze-gsc → /monthly-report → next month plan | All 4 steps done? |

**Compliance issues to flag:**
- Skipped skills that should have been used
- Wrong model for the task (e.g., Haiku for nuanced writing)
- Phase gate not met (e.g., article published without /review-article)
- Client data hardcoded instead of referencing client.md
- Workflow steps done out of order

### 1c. Generate Compliance Summary

```markdown
### Workflow Compliance: [PASS / PARTIAL / NEEDS ATTENTION]

**Current Phase:** [Phase N]
**Skills used:** [list]
**Skills that should have been used:** [list if any missing]
**Phase gate status:** [Met / Not yet met / In progress]

**Issues found:**
- [Issue 1] → [Recommendation]
```

---

## Step 2: Session Retrospective Analysis

### 2a. Identify Pitfalls & Mistakes

Review the session for:

- **Wasted effort** — work that had to be redone, wrong approaches tried first
- **Context loss** — information available but not used, forcing re-research
- **Tool misuse** — using Bash when a dedicated tool existed, sequential calls that could have been parallel
- **Incorrect assumptions** — assumptions about file structure, data format, or requirements that turned out wrong
- **Blocked moments** — times when progress stalled and what caused it
- **Overcomplicated solutions** — cases where a simpler approach existed
- **Repeated patterns** — the same type of issue appearing multiple times

### 2b. Evaluate Workflows, Skills & Scripts

For each workflow, skill, or script used during the session:

**Workflows (`.claude/workflows/*.md`):**
- Did the workflow provide clear enough instructions?
- Were there missing steps that caused confusion?
- Are there steps that should be added, removed, or reordered?
- Does the workflow correctly reference client.md sections?

**Skills (`.claude/skills/*/SKILL.md`):**
- Did the skill produce expected output quality?
- Were there edge cases the skill didn't handle?
- Should model assignments be changed?
- Are client.md references working correctly?

**Scripts (`scripts/*.py`):**
- Did scripts fail or produce unexpected output?
- Performance issues?

**Critics (`.claude/critics/*.md`):**
- Did any critic produce inaccurate scores?
- Were criteria too strict, too lenient, or unclear?

### 2c. Generate Improvement Recommendations

| Priority | Description |
|----------|-------------|
| **Fix Now** | Issues that will cause problems in the next session |
| **Fix Soon** | Improvements that would save significant time |
| **Backlog** | Nice-to-have improvements, low urgency |

### 2d. Save Retrospective

Write findings to: `.claude/retrospectives/retro-[YYYY-MM-DD].md`

```markdown
# Session Retrospective: [YYYY-MM-DD]

## Session Summary
[1-2 sentences on what was done]

## Workflow Compliance
[Compliance summary from Step 1]

## Pitfalls Encountered
1. **[Pitfall name]** — [What happened] → [How to avoid next time]

## Workflow/Skill/Script Issues
1. **[File]** — [Issue] → [Recommended fix]

## What Went Well
- [Things that worked efficiently — preserve these patterns]

## Improvement Actions
| Priority | Action | File to Update |
|----------|--------|----------------|
| Fix Now | [action] | [file path] |
| Fix Soon | [action] | [file path] |
| Backlog | [action] | [file path] |
```

### 2e. Apply "Fix Now" Items

If there are "Fix Now" improvements:
- Apply changes immediately before committing
- Note them in the commit message
- If too large for end-session, add as top priority in active-context.md

### 2f. Update Auto-Memory

If the retrospective revealed stable patterns or recurring issues:
- Update `the project auto-memory file (MEMORY.md)`
- Create or update topic-specific memory files if needed
- Remove any memory entries that turned out to be wrong

---

## Step 3: Update Progress Tracking

1. **Update `.claude/context/progress.md`:**
   - Update phase completion checkboxes
   - Update milestone tracker
   - Add entry to weekly log

2. **Update `.claude/context/active-context.md`:**
   - Move completed tasks to "Recent Completions" with date
   - Update "Working Notes (This Session)"
   - Update current phase if phase gate was met
   - Add any "Fix Now" items from retrospective to priorities

---

## Step 4: Commit and Push

Commit all changes to git:
- Use format: "Session [date]: [summary]"
- Include: key changes, workflow compliance status, next steps
- Add Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- Push to origin main

---

## Step 5: Session Summary to User

Provide:

1. **What was accomplished** — completed tasks and outputs
2. **Workflow compliance** — pass/partial/needs attention + details
3. **Files created/modified** — grouped by type
4. **Key decisions made** — and their rationale
5. **Retrospective highlights:**
   - Top pitfalls and how to avoid them
   - Workflow/skill improvements applied or recommended
   - What went well (patterns to keep)
6. **Next steps** — prioritized, with recommended skills and models
7. **Blockers/questions** — anything unresolved
8. Confirm: "All changes committed and pushed to GitHub."

---

IMPORTANT: Only mark tasks as completed if they were actually finished during this session.
IMPORTANT: The retrospective should be honest and specific — vague observations are useless. Cite specific moments.
IMPORTANT: Workflow compliance check is mandatory — it's what keeps the process improving.
