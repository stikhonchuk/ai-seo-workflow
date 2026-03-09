# AI SEO Workflow

An AI-assisted SEO content workflow system for websites. Built with Claude Code integration for automated content planning, creation, review, and optimization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What This Is

A complete SEO workflow template that uses AI (Claude Code) to:

- **Plan content** based on keyword research and competitor analysis
- **Write articles** with model-specific guidance (Opus/Sonnet/Haiku)
- **Review content** through 8 specialized critics before publishing
- **Amplify** via social media repurposing across 5 channels
- **Track progress** across 8 phases (audit → research → creation → monitoring)
- **Audit existing content** to prevent duplication and identify gaps
- **Generate reports** for monthly SEO performance tracking

## Architecture: Client Data vs Process

The key design principle: **client-specific data is separated from reusable process**.

```
.claude/
├── client/
│   └── client.md          ← CHANGE THIS: company, domains, services, CTAs, brand
├── workflows/             ← REUSABLE: SEO phases, writing guide, SMM strategy
├── skills/                ← REUSABLE: slash commands with model recommendations
├── critics/               ← REUSABLE: content review criteria
├── prompts/               ← REUSABLE: article generation templates
├── context/               ← CURRENT STATE: phase, sprint, priorities
└── memory/                ← LEARNINGS: strategic insights
```

**To start a new project:** Copy `client/client.example.md` → `client/client.md` and fill in your data. Everything else works immediately.

## Features

### 8-Phase SEO Workflow
```
INITIAL SETUP (once):
  Phase 1: Audit → Phase 2: Keywords → Phase 3: Competitors → Phase 4: Strategy
                                                                      │
MONTHLY CYCLE (repeat): ◄────────────────────────────────────────────┘
  Phase 5: Write → Phase 6: Review & Publish → Phase 7: Amplify (SMM)
      │                                                   │
      └──── Monthly Close: Audit → Report → Plan ─────────┘
```

### Skills with Model Recommendations

| Skill | Model | Phase | Purpose |
|-------|-------|-------|---------|
| `/start-session` | — | Start | Load context, show current phase |
| `/brainstorm` | **Opus** | 1, 4 | Content ideation |
| `/writing-guide` | **Sonnet** | 5 | Load writing standards |
| `/review-article` | **Multi** | 6 | 8-critic content review |
| `/create-social-posts` | **Sonnet** | 7 | Social media repurposing |
| `/monthly-report` | **Sonnet** | Monthly | Performance report |
| `/analyze-gsc` | **Sonnet** | Monthly | Google Search Console analysis |
| `/analyze-webmaster` | **Sonnet** | Monthly | Yandex Webmaster analysis |
| `/end-session` | — | End | Save progress, compliance check, commit |

### 8-Critic Content Review System

| Critic | Model | Focus |
|--------|-------|-------|
| SEO | Sonnet | Keywords, meta, structure, links |
| Russian Language | Opus | Grammar, phrasing, native quality |
| English Language | Opus | Tone, clarity, professional writing |
| E-E-A-T | Sonnet | Authority signals, trust |
| User Intent | Sonnet | Search intent satisfaction |
| Readability | Haiku | Scannability, structure |
| Commercial | Haiku | CTAs, conversion path |
| Image Prompts | Haiku | Visual validation, brand consistency |

### Content Audit Scripts
Python scripts for site-wide content analysis:
- Sitemap parsing and page scraping
- Keyword extraction with Russian language support (pymorphy3)
- Integration with GSC and Yandex Webmaster data
- Gap analysis, CTR optimization, cannibalization detection

## Quick Start

### 1. Clone and Configure

```bash
git clone https://github.com/stikhonchuk/ai-seo-workflow.git my-seo-project
cd my-seo-project
rm -rf .git && git init
```

### 2. Set Up Client Profile

```bash
cp .claude/client/client.example.md .claude/client/client.md
```

Edit `client.md` with your project details:
- Company name, domains, services
- Target audiences and content pillars
- CTAs, brand colors, social channels
- Seed keywords, competitors

### 3. Configure Content Audit

```bash
cp scripts/content_audit/config.example.py scripts/content_audit/config.py
# Edit config.py with your domains
```

### 4. Install Python Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r scripts/content_audit/requirements.txt
```

### 5. Start Using

```bash
claude           # Start Claude Code
/start-session   # Load context, see current phase
```

## Project Structure

```
.
├── .claude/
│   ├── client/              # Client-specific data (change per project)
│   │   └── client.md        # Company, domains, services, CTAs, brand
│   ├── context/             # Current state
│   │   ├── active-context.md  # Phase, sprint, priorities
│   │   └── progress.md       # Phase completion, milestones
│   ├── memory/              # Long-term knowledge
│   │   └── memory-bank.md
│   ├── skills/              # Slash commands (reusable)
│   │   ├── start-session/
│   │   ├── end-session/
│   │   ├── brainstorm/
│   │   ├── writing-guide/
│   │   ├── review-article/
│   │   ├── create-social-posts/
│   │   ├── monthly-report/
│   │   ├── analyze-gsc/
│   │   └── analyze-webmaster/
│   ├── critics/             # Content review criteria (reusable)
│   ├── workflows/           # Process documentation (reusable)
│   │   ├── SEO_WORKFLOW.md            # Master workflow
│   │   ├── SMM_WORKFLOW.md            # Social media strategy
│   │   ├── CONTENT_WRITING_GUIDE.md   # Writing standards
│   │   ├── KEYWORD_RESEARCH_TEMPLATE.md
│   │   ├── CONTENT_CALENDAR_TEMPLATE.md
│   │   ├── MONTHLY_REPORT_TEMPLATE.md
│   │   └── monthly-content-audit.md
│   └── prompts/             # Article generation templates
│       └── content-generation.md
├── scripts/
│   ├── content_audit/       # Python audit utility
│   ├── process_keywords.py  # Keyword CSV processor
│   └── anonymize.py         # Anonymization helper
├── content/
│   ├── drafts/              # Work in progress
│   ├── published/           # Final content
│   ├── reviews/             # Critic review reports
│   ├── social/              # Social media posts
│   └── calendars/           # Monthly plans
└── research/
    ├── keywords/            # Keyword research data
    ├── competitors/         # Competitor analysis
    ├── analytics/           # Performance data
    └── content-audit/       # Audit outputs
```

## Using with Multiple Projects

With client data separated into `client.md`, managing multiple projects is straightforward:

```
┌─────────────────────────────────────────────┐
│         PUBLIC TEMPLATE REPO                 │
│        ai-seo-workflow (GitHub)              │
│                                              │
│  client/client.example.md  ← placeholder    │
│  workflows, skills, critics ← reusable      │
└─────────────────────────────────────────────┘
         ▲                    │
         │ push improvements  │ clone/pull
         │ (already generic)  │ (just fill client.md)
         │                    ▼
┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│  project-a     │  │  project-b     │  │  project-c     │
│  client.md: A  │  │  client.md: B  │  │  client.md: C  │
│  (private)     │  │  (private)     │  │  (private)     │
└────────────────┘  └────────────────┘  └────────────────┘
```

### Contributing Back to Template

Since workflows/skills/critics are already generic (they reference `client.md`), contributing improvements back is simple:

```bash
# 1. Make improvement in your project (it's already generic)
# 2. Copy changed files to template repo
cp .claude/skills/my-skill/SKILL.md ~/ai-seo-workflow/.claude/skills/my-skill/SKILL.md

# 3. Verify no client data leaked
python scripts/anonymize.py --check .

# 4. Commit and push to template
cd ~/ai-seo-workflow
git add . && git commit -m "Add my-skill"
git push origin main
```

## Customization

### Adding New Skills
1. Create `.claude/skills/my-skill/SKILL.md`
2. Include model recommendation in body text
3. Reference `client.md` for any client-specific data
4. Note workflow position (which phase it belongs to)

### client.md Sections
Your `client.md` should include these sections (see `client.example.md`):
- `#company` — name, tagline, industry
- `#domains` — sites, languages, search engines
- `#services` — what the business offers
- `#target-audiences` — personas
- `#content-pillars` — topic categories
- `#ctas` — call-to-action language (EN + RU)
- `#brand` — colors, visual style, image requirements
- `#social-media-channels` — platforms, tones, rules
- `#site-structure` — URL patterns for link validation
- `#publishing-schedule` — frequency, days, content mix
- `#content-standards` — word count, density, link requirements

## Requirements

- **Claude Code** — Anthropic's CLI tool
- **Python 3.8+** — For content audit scripts
- **Git** — Version control

### Python Dependencies
```
requests>=2.28.0
beautifulsoup4>=4.11.0
pymorphy3>=2.0.0  # Russian morphology (optional)
```

## License

MIT License — see [LICENSE](LICENSE) file.

## Acknowledgments

- Built with [Claude Code](https://claude.ai/code) by Anthropic
- Russian language support via [pymorphy3](https://github.com/no-madsoul/pymorphy3)

---

**Note:** Copy `client.example.md` → `client.md` and fill in your project details to get started.
