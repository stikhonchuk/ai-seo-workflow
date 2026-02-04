---
name: start-session
description: Load project context at the beginning of a session
---

# Start Session

When this skill is invoked:

1. Read these 3 files in order:
   - .claude/context/active-context.md
   - .claude/context/progress.md
   - .claude/memory/memory-bank.md

2. Provide a status summary including:
   - Current phase
   - This week's priorities (list all priority sections)
   - Recent completions
   - Active blockers
   - Key project info

3. End with: "Ready to proceed! What would you like to work on?"

4. Format the summary clearly with headers and bullet points.
