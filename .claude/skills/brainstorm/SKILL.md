---
name: brainstorm
description: Structured product ideation session with concept evolution, use cases, and functional requirements
---

# Brainstorm Skill

**Recommended Model: Opus** — requires deep creative thinking, nuanced judgment, and iterative refinement.

When this skill is invoked, run a structured product ideation session that takes a rough idea through progressive refinement into a documented concept with use cases and functional requirements.

## Usage
- `/brainstorm` — Interactive: asks for the idea
- `/brainstorm "public goal paths with viral sharing"` — Start with a seed idea
- `/brainstorm --resume` — Continue from last brainstorm session (reads latest file from `research/`)
- `/brainstorm --spec-only` — Skip ideation, generate use cases + functional requirements from an existing concept doc

## Philosophy

Brainstorming is messy by nature. This skill provides just enough structure to capture ideas without killing creativity. The key principle: **refine iteratively with the user, don't over-plan in isolation.**

Each brainstorm session produces artifacts at three levels of formality:
1. **Concept doc** — the idea, architecture, and open questions (brainstorming artifact)
2. **Use cases** — concrete user journeys that test whether the concept works (validation artifact)
3. **Functional requirements** — what to build, mapped against existing system (implementation artifact)

## Execution Steps

### 1. Capture the Seed Idea

If not provided as parameter:
- Ask the user: "What's the idea? A sentence or two is enough — we'll refine from there."
- Don't ask for details yet. Just get the core concept.

If provided:
- Acknowledge the idea in one sentence
- Move to step 2

### 2. Load Context

Read these files to understand what exists:
- `research/` — existing research and strategy docs
- `the project auto-memory file (MEMORY.md)` — project memory

**Why:** Every idea must be grounded in what the client can already do. The best features build on existing mechanics rather than requiring greenfield development.

### 3. First Expansion — Explore the Idea Space

Present the user with:

**a. Concept framing** — Restate the idea in 2-3 sentences showing you understand it. Include how it connects to existing Client features.

**b. Three variations** — Present 3 different angles or scopes for the idea:
- **Minimal version** — What's the simplest form that delivers value?
- **Full version** — The idea as the user probably imagines it
- **Ambitious version** — What if we went further? (stretch thinking)

**c. Key questions** — Ask 2-3 clarifying questions using AskUserQuestion tool:
- Focus on scope decisions and user-facing behavior
- Don't ask implementation questions yet
- Frame as choices, not open-ended questions

**Important:** Don't write files yet. This is conversational.

### 4. Iterative Refinement (1-3 rounds)

Based on user answers:
- Refine the concept
- Present updated version
- Ask follow-up questions if needed
- Each round should narrow scope and increase clarity

**Signs you're ready to move on:**
- User says "yes, that's it" or similar
- Core mechanics are defined
- User-facing behavior is clear
- You've identified what's new vs what exists

**Signs you need another round:**
- User keeps adding "also..." or "but what about..."
- Core mechanic is still ambiguous
- You're not sure how it maps to existing features

### 5. Architecture Sketch

Once the concept stabilizes, present a text-based architecture diagram:

```
[Category/Container]
  └── [Component 1] — [brief description]
        ├── [Sub-component A]
        └── [Sub-component B]
```

Show:
- How the new concept fits into The client's existing hierarchy
- What data flows between components
- Which existing features it reuses vs what's new

Ask user to confirm before proceeding to documentation.

### 6. Generate Concept Document

Save to: `research/[concept-name].md`

**File structure:**
```markdown
# [Concept Name]

**Created:** [YYYY-MM-DD]
**Status:** Concept stage — brainstorming. Not yet formalized as product spec.

---

## 1. Concept
[2-3 paragraphs: what is it, why does it matter, how does it fit the client]

## 2. Architecture
[Text diagram showing hierarchy and relationships]

## 3. Core Mechanics
[How it works — the key behaviors and rules]

### What's defined at system level:
- [Shared structures]

### What's personal (per user):
- [Personal data and settings]

## 4. Key Insight
[The "aha" moment — the non-obvious principle that makes this work]

## 5. What This Enables
- [Capability 1]
- [Capability 2]
- ...

## 6. Open Questions
- [Question 1]
- [Question 2]
- ...
```

### 7. Ask: Go Deeper?

Ask the user using AskUserQuestion:

"Concept doc saved. What next?"
- **Use cases + functional requirements** — Full spec with user journeys and implementation details
- **Just use cases** — Validate the concept with concrete scenarios
- **Done for now** — Save and revisit later
- **Iterate more** — The concept needs more refinement

### 8. Generate Use Cases (if requested)

Save to: `research/[concept-name]-use-cases.md`

**Generate 5-10 use cases covering:**
- Solo user journey (discovery → adoption → ongoing use)
- Multi-user scenario (family, team, or friend invite)
- Viral/social scenario (share → new user acquisition)
- Edge case (re-use, cancellation, data privacy)
- Cross-feature interaction (how it connects to existing Client features)

**Use case format:**
```markdown
## UC-N: [Name] ([Category])

**Actor:** [Who, with context]
**Goal:** [What they want to achieve]

**Flow:**
1. [Step with specific UI/system behavior]
2. [Step]
...

**Key system behaviors:**
- [What the system must do to support this]
```

### 9. Generate Functional Requirements (if requested)

Save to: `research/[concept-name]-functional-requirements.md`

**Critical: Map against existing system.** Read `user-guide-ru/00-system-overview.md` to identify:
- What already exists and can be reused as-is
- What needs minor extension (new field, new option)
- What's genuinely new (new model, new UI component, new API endpoint)

**File structure:**
```markdown
# [Concept] — Functional Requirements

## What Already Exists (no changes needed)
| Feature | How it supports [concept] | Reference |
|---------|--------------------------|-----------|

## New Features Required

### FR-1: [Feature Name]
**Priority:** High/Medium/Low
**Why:** [Why this is needed]
**Requirements:**
- [ ] [Specific requirement]
**Existing to reuse:** [What can be extended]

[...more FRs...]

## Data Model Changes Summary
### Modified Models
| Model | Field Added | Type | Notes |
### New Models
| Model | Fields | Purpose |

## Implementation Phases
### Phase 1: MVP
### Phase 2: Engagement
### Phase 3: Viral/Advanced

## API Considerations
### New Endpoints
### Existing Endpoints to Extend

## Open Questions for Product Decision
1. [Decision needed]
```

### 10. Update Memory

Add a brief reference to `the project auto-memory file (MEMORY.md)`:
- Concept name and file path
- One-line description
- Key architectural decision

### 11. Summary Output to User

After generating, provide:

1. **Files created** — paths and brief descriptions
2. **Concept summary** — 3-4 bullets
3. **Reuse ratio** — "X of Y features build on existing client mechanics"
4. **Key decisions made** — what was decided during brainstorming
5. **Open questions** — what still needs product team input
6. **Next steps** — suggested follow-up actions

## Quality Rules

### Grounding Rules
- Every feature must reference how it connects to existing client capabilities
- Don't invent new UI paradigms when existing patterns work
- Functional requirements must include "What Already Exists" section — it forces grounding
- Use client terminology consistently (see MEMORY.md for UI terms, roles, statuses)

### Scope Rules
- A brainstorm session should produce ONE concept, not a portfolio
- If the idea branches into multiple concepts, ask the user which to pursue first
- Functional requirements should be scoped to what's needed for the concept, not general improvements
- Phase 1 (MVP) should be implementable with minimal new models/endpoints

### Bilingual Rules
- Concept docs are in English (internal documentation)
- User-facing names/taglines should include both EN and RU versions
- Use client RU terminology from MEMORY.md

### File Naming
- Concept doc: `research/[concept-name].md` (kebab-case)
- Use cases: `research/[concept-name]-use-cases.md`
- Functional requirements: `research/[concept-name]-functional-requirements.md`

### Context Management
- Brainstorming is token-intensive. If the session is getting long:
  - Save progress to files early (don't wait for "perfect")
  - Use AskUserQuestion to make decisions rather than exploring all options
  - Prefer writing to a file and refining over keeping everything in conversation

## Anti-Patterns to Avoid

1. **Over-engineering in brainstorm** — Don't design database schemas during ideation. Architecture sketch is enough.
2. **Asking too many questions at once** — Max 3 questions per round. Let the user think.
3. **Solving implementation during concept** — "How" comes after "what" and "why" are clear.
4. **Ignoring existing features** — The best ideas extend what exists. Always check the system overview first.
5. **Scope creep** — If the user keeps adding features, ask "What's the minimum version that delivers value?"
6. **Premature documentation** — Don't write the concept doc until the idea has been refined at least once with the user.
