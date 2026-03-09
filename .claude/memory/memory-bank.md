# Memory Bank

## Purpose
Long-term strategic insights and learnings accumulated across sessions. Updated by `/end-session` retrospectives.

→ See [client.md](../client/client.md) for client-specific project data.

## Architecture
- Client data separated from process: `client/client.md` is the single source of truth
- Workflows, skills, and critics reference client.md via `→ See client.md#section` markers
- To switch clients: update only client.md

## Key Files
- `client/client.md` — company, domains, services, audiences, CTAs, brand
- `workflows/SEO_WORKFLOW.md` — master workflow (8 phases + monthly cycle)
- `workflows/SMM_WORKFLOW.md` — social media (Phase 7)
- `workflows/CONTENT_WRITING_GUIDE.md` — full writing reference
- `prompts/content-generation.md` — article type prompt templates

## Skills & Models
| Skill | Model | Phase |
|-------|-------|-------|
| /brainstorm | Opus | 1, 4 |
| /writing-guide | Sonnet | 5 |
| /review-article | Multi (Haiku→Sonnet→Opus) | 6 |
| /create-social-posts | Sonnet | 7 |
| /monthly-report | Sonnet | Monthly |
| /analyze-gsc | Sonnet | Monthly |
| /analyze-webmaster | Sonnet | Monthly |

## Lessons Learned

*Add learnings here as you work. Updated by `/end-session` retrospectives.*

### Technical
- Read tool required before Write in same session
- `model:` attribute NOT supported in SKILL.md YAML frontmatter — put model recs in skill body text
- WebFetch may fail on some URLs (JS-only widgets) — ask user for content

### Content
- EN/RU articles should stay independent (no cross-references in content)
- hreflang tags for cross-linking between language versions

---

**Last Updated:** [DATE]
