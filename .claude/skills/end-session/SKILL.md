---
name: end-session
description: Save progress, update tracking files, and commit changes at session end
---

# End Session

When this skill is invoked:

1. Update .claude/context/progress.md:
   - Add entry to weekly log with completed items, in-progress items, blockers, and next week priorities
   - Update phase completion checkboxes if tasks were completed
   - Update milestone tracker if milestones were reached

2. Update .claude/context/active-context.md:
   - Move completed tasks from "Current Priorities" to "Recent Completions" with date
   - Update "Working Notes (This Session)" with today's focus, key insights, and next session priorities
   - Update blockers section

3. Commit all changes to git:
   - Use format: "Session [date]: [summary]"
   - Include detailed description, key changes, next steps
   - Add Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
   - Push to origin main

4. Provide session summary to user:
   - What was accomplished
   - Files created/modified
   - Key decisions made
   - Next steps
   - Any blockers/questions
   - Confirm: "All changes committed and pushed to GitHub."

IMPORTANT: Only mark tasks as completed if they were actually finished during this session.
