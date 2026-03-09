---
name: skills
description: Overview of all available custom skills for the SEO project
user-invocable: false
---

# Custom Skills — SEO Project

All skills reference `client.md` for client-specific data and are reusable across clients.

## Skills by Workflow Phase

### Session Management
| Skill | Model | Usage |
|-------|-------|-------|
| `/start-session` | — | Load context, show current phase and next actions |
| `/end-session` | — | Save progress, workflow compliance check, retrospective, commit |

### Phase 1: Audit + Phase 4: Strategy
| Skill | Model | Usage |
|-------|-------|-------|
| `/brainstorm` | **Opus** | Structured ideation for content strategy |
| `/brainstorm "topic"` | **Opus** | Start with seed idea |
| `/brainstorm --resume` | **Opus** | Continue previous session |

### Phase 5: Content Creation
| Skill | Model | Usage |
|-------|-------|-------|
| `/writing-guide` | **Sonnet** | Load writing standards and templates |
| `/writing-guide [type]` | **Sonnet** | Load for specific content type |
| `/writing-guide --checklist` | **Sonnet** | Show pre-publishing checklist only |

### Phase 6: Review & Publish
| Skill | Model | Usage |
|-------|-------|-------|
| `/review-article` | **Multi** | Full 8-critic review (Haiku → Sonnet → Opus) |
| `/review-article [file]` | **Multi** | Review specific file |
| `/review-article --critic=seo` | **Sonnet** | Single critic review |
| `/review-article --quick` | **Haiku** | Quick scoring, all critics |

### Phase 7: Social Media Amplification
| Skill | Model | Usage |
|-------|-------|-------|
| `/create-social-posts` | **Sonnet** | Generate posts for all channels |
| `/create-social-posts [file]` | **Sonnet** | From specific article |
| `/create-social-posts --channel=linkedin` | **Sonnet** | Single channel |

### Monthly Close Cycle
| Skill | Model | Usage |
|-------|-------|-------|
| `/analyze-gsc [date]` | **Sonnet** | Analyze Google Search Console exports |
| `/analyze-webmaster [date]` | **Sonnet** | Analyze Yandex Webmaster exports |
| `/monthly-report [YYYY-MM]` | **Sonnet** | Generate monthly performance report |

## Scripts (not skills — run via bash)

| Script | Phase | Usage |
|--------|-------|-------|
| `content_audit/main.py --full --all` | 1, Monthly | Full content audit both sites |
| `process_keywords.py` | 2 | Process keyword CSV exports |

## Critic System (used by /review-article)

| Critic | Model | Focus |
|--------|-------|-------|
| SEO | Sonnet | Keywords, meta, structure, links |
| Russian Language | Opus | Grammar, phrasing, register |
| English Language | Opus | Tone, clarity, professional writing |
| E-E-A-T | Sonnet | Experience, expertise, authority, trust |
| User Intent | Sonnet | Search intent satisfaction |
| Readability | Haiku | Scannability, structure |
| Commercial | Haiku | CTAs, conversion path |
| Image Prompts | Haiku | Visual validation, brand consistency |

## Key Files

- **Client data:** `.claude/client/client.md`
- **Master workflow:** `.claude/workflows/SEO_WORKFLOW.md`
- **SMM workflow:** `.claude/workflows/SMM_WORKFLOW.md`
- **Writing reference:** `.claude/workflows/CONTENT_WRITING_GUIDE.md`
- **Content prompts:** `.claude/prompts/content-generation.md`
- **Critics:** `.claude/critics/*.md`

## Adding New Skills

1. Create directory: `.claude/skills/my-skill/`
2. Create `SKILL.md` with YAML frontmatter and instructions
3. Include model recommendation in skill body
4. Reference `client.md` for any client-specific data
5. Note workflow position (which phase it belongs to)
6. Test with `/my-skill`
