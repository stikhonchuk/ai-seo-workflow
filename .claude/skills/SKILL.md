---
name: skills
description: Overview of all available custom skills for [YOUR-DOMAIN] SEO project
user-invocable: false
---

# Custom Skills for [YOUR-DOMAIN] SEO Project

This directory contains custom Claude Code skills that automate common workflows for the [YOUR-DOMAIN] SEO project.

## Available Skills

### Session Management

**start-session** - Load project context at session start
- Reads: active-context.md, progress.md, memory-bank.md
- Provides status summary with priorities, completions, blockers
- Usage: `/start-session`

**end-session** - Save progress and commit at session end
- Updates progress.md and active-context.md
- Commits all changes to git with detailed message
- Provides session summary
- Usage: `/end-session`

### Reporting & Analysis

**monthly-report** - Generate monthly SEO performance report structure
- Creates report template from REPORT_TEMPLATE.md
- Sets up data snapshot directory
- Provides checklist for data collection
- Usage: `/monthly-report` or `/monthly-report 2026-02`

**analyze-webmaster** - Analyze Yandex Webmaster reports
- Processes .zip exports with comprehensive metrics
- Analyzes queries, pages, devices, geography
- Identifies growth opportunities
- Generates detailed analysis report
- Usage: `/analyze-webmaster` or `/analyze-webmaster 2026-01-27`

**analyze-gsc** - Analyze Google Search Console query trends
- Processes .csv.gz query trend exports (7-day data)
- Analyzes impression trends and patterns
- Categorizes queries by intent and type
- Cross-references with Yandex data
- Usage: `/analyze-gsc` or `/analyze-gsc 2026-01-27`

### Content Quality

**review-article** - Run multi-critic review on content drafts
- Runs 8 specialized critics: SEO, Russian Language, English Language, E-E-A-T, User Intent, Readability, Commercial, Image Prompts
- Generates comprehensive review report with scores
- Provides prioritized fix list and revision checklist
- Usage: `/review-article` (most recent draft)
- Usage: `/review-article [filename]` (specific file)
- Usage: `/review-article --critic=seo` (single critic)
- Usage: `/review-article --quick` (summary only)

**Critics Available:**
- **SEO Critic**: Technical SEO compliance (keywords, meta, structure, links)
- **Russian Language Critic**: Native-level language quality (grammar, phrasing, register)
- **E-E-A-T Critic**: Experience, Expertise, Authority, Trust signals
- **User Intent Critic**: Search intent satisfaction and completeness
- **Readability Critic**: Scannability, structure, sentence/paragraph analysis
- **Commercial Critic**: CTAs, product integration, conversion path
- **Image Prompt Critic**: AI image prompt validation, brand consistency, technical specs

## Skill Locations

All skill implementations are in subdirectories:
- `start-session/SKILL.md`
- `end-session/SKILL.md`
- `monthly-report/SKILL.md`
- `analyze-webmaster/SKILL.md`
- `analyze-gsc/SKILL.md`
- `review-article/SKILL.md`

Critic definitions are in `.claude/critics/`:
- `seo-critic.md`
- `russian-language-critic.md`
- `english-language-critic.md`
- `eeat-critic.md`
- `user-intent-critic.md`
- `readability-critic.md`
- `commercial-critic.md`
- `image-prompt-critic.md`
- `image-prompt-critic.md`

## How Skills Work

- **Model-invoked**: Claude can automatically load skills when relevant
- **User-invoked**: Use `/skill-name` to invoke directly
- **Context-aware**: Skills load based on conversation context and description

## Adding New Skills

To add a new skill:
1. Create directory: `.claude/skills/my-skill/`
2. Create `SKILL.md` with YAML frontmatter and instructions
3. Test with `/my-skill` or let Claude invoke automatically

For detailed documentation, see [.claude/README.md](../README.md)
