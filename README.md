# AI SEO Workflow

An AI-assisted SEO content workflow system designed for e-commerce websites. Built with Claude Code integration for automated content planning, creation, and optimization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What This Is

A complete SEO workflow template that uses AI (Claude Code) to:

- **Plan content** based on keyword research and competitor analysis
- **Track progress** across multiple phases (audit → research → creation → monitoring)
- **Automate repetitive tasks** via slash commands (skills)
- **Audit existing content** to prevent duplication and identify gaps
- **Generate reports** for monthly SEO performance tracking

This template was extracted from a real e-commerce SEO project that grew from 0 to 100+ articles with measurable traffic improvements.

## Features

### 🎯 Structured Workflow
- 8-phase SEO workflow from audit to link building
- Content calendar templates
- Keyword research methodology
- Competitor analysis framework

### 🤖 Claude Code Integration
- `/start-session` - Load project context automatically
- `/end-session` - Save progress and commit changes
- `/monthly-report` - Generate monthly SEO reports
- `/analyze-webmaster` - Analyze Yandex Webmaster data
- `/analyze-gsc` - Analyze Google Search Console data
- `/review-article` - Multi-critic content review

### 📊 Content Audit Utility
Python scripts for site-wide content analysis:
- Sitemap parsing and page scraping
- Keyword extraction with Russian language support
- Integration with GSC and Yandex Webmaster data
- Gap analysis, CTR optimization, cannibalization detection

### 📝 Context Management
- `active-context.md` - Current sprint priorities
- `progress.md` - Phase completion tracking
- `memory-bank.md` - Long-term project knowledge

## Quick Start

### 1. Clone and Configure

```bash
# Clone the template
git clone https://github.com/YOUR-USERNAME/ai-seo-workflow.git my-seo-project
cd my-seo-project

# Remove template git history and start fresh
rm -rf .git
git init
```

### 2. Configure for Your Project

```bash
# Copy config template
cp scripts/content_audit/config.example.py scripts/content_audit/config.py

# Edit config.py with your domain
# DOMAIN = "www.your-domain.com"
```

### 3. Update Context Files

Edit these files with your project details:
- `.claude/context/active-context.md` - Replace `[YOUR-PROJECT]`, `[DATE]` placeholders
- `.claude/context/progress.md` - Set your timeline and milestones
- `.claude/memory/memory-bank.md` - Add your business context

### 4. Install Python Dependencies (for content audit)

```bash
cd scripts/content_audit
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 5. Start Using with Claude Code

```bash
# In your project directory
claude

# Start a session
/start-session
```

## Project Structure

```
.
├── .claude/
│   ├── context/           # Current state (active-context.md, progress.md)
│   ├── memory/            # Long-term knowledge (memory-bank.md)
│   ├── skills/            # Slash commands
│   │   ├── start-session/
│   │   ├── end-session/
│   │   ├── monthly-report/
│   │   ├── analyze-gsc/
│   │   ├── analyze-webmaster/
│   │   └── review-article/
│   └── workflows/         # Process documentation
│       ├── SEO_WORKFLOW.md
│       ├── CONTENT_WRITING_GUIDE.md
│       ├── KEYWORD_RESEARCH_TEMPLATE.md
│       └── ...
├── scripts/
│   ├── content_audit/     # Python audit utility
│   └── anonymize.py       # Anonymization helper
├── content/
│   ├── drafts/            # Work in progress
│   ├── published/         # Final content
│   └── calendars/         # Monthly plans
└── research/
    ├── keywords/          # Keyword research data
    ├── competitors/       # Competitor analysis
    ├── analytics/         # Performance data
    └── content-audit/     # Audit outputs
```

## Workflow Overview

### Phase 1: Website Audit
Analyze current site state, identify technical issues, document baseline metrics.

### Phase 2: Keyword Research
Research 100-200 target keywords, prioritize by volume/difficulty/intent.

### Phase 3: Competitor Analysis
Identify 3-5 competitors, analyze their strategies, find content gaps.

### Phase 4: Content Strategy
Create content calendar, define content pillars, plan first month.

### Phase 5: Content Creation
Write articles using templates, run multi-critic reviews, generate images.

### Phase 6: Publishing
Optimize, publish, submit to search engines, share on social.

### Phase 7: Monitoring
Track rankings, analyze performance, update underperforming content.

### Phase 8: Link Building
Internal linking, guest posts, digital PR.

## Using with Multiple Projects

This template supports a "hub and spoke" model for managing multiple SEO projects with shared tooling:

```
┌─────────────────────────────────────────────────────────────────┐
│                     PUBLIC TEMPLATE REPO                        │
│                    ai-seo-workflow (GitHub)                     │
│                                                                 │
│  - External contributors fork & PR here                         │
│  - You cherry-pick improvements from private repos              │
│  - Tagged releases (v1.0, v1.1, v2.0)                          │
└─────────────────────────────────────────────────────────────────┘
         ▲                    │                    ▲
         │ cherry-pick        │ git pull           │ cherry-pick
         │ (anonymized)       │ upstream           │ (anonymized)
         │                    ▼                    │
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│   project-a     │   │   project-b     │   │   project-c     │
│    (private)    │   │    (private)    │   │    (private)    │
└─────────────────┘   └─────────────────┘   └─────────────────┘
```

### Initial Setup for New Private Project

```bash
# Option 1: Clone template (recommended for new projects)
git clone https://github.com/YOUR-USERNAME/ai-seo-workflow.git my-project
cd my-project
rm -rf .git && git init
git remote add origin git@github.com:YOUR-USERNAME/my-project.git
git remote add upstream https://github.com/YOUR-USERNAME/ai-seo-workflow.git

# Option 2: Add upstream to existing project
cd existing-project
git remote add upstream https://github.com/YOUR-USERNAME/ai-seo-workflow.git
```

### Workflow: Pulling Template Updates

```bash
# In your private project
git fetch upstream
git merge upstream/main
# Or cherry-pick specific commits:
git cherry-pick <commit-hash>
```

### Workflow: Contributing Improvements Back to Template

**Step 1: Make and test improvement in private project**
```bash
# In your private project
# Edit files, test changes
git add <files>
git commit -m "Add feature X"
git push origin main
```

**Step 2: Check for sensitive data**
```bash
# Run anonymization check on changed files
python ~/path-to-template/scripts/anonymize.py --check <file-or-directory>
```

**Step 3: Copy to template and anonymize**
```bash
# Copy file to template
cp <file> ~/path-to-template/<same-path>/

# In template directory, run anonymize
cd ~/path-to-template
python scripts/anonymize.py <file-or-directory>

# Review changes
git diff
```

**Step 4: Commit and push to template**
```bash
git add <files>
git commit -m "Add feature X"
git push origin main
```

**Step 5: Pull to other private projects**
```bash
cd ~/other-project
git fetch upstream
git cherry-pick <commit-hash>  # or git merge upstream/main
git push origin main
```

### Anonymization Script

The `scripts/anonymize.py` helps prepare files for public contribution:

```bash
# Check for unanonymized data
python scripts/anonymize.py --check .

# List current replacement patterns
python scripts/anonymize.py --list-patterns

# Dry run - see what would change
python scripts/anonymize.py --dry-run .

# Apply anonymization
python scripts/anonymize.py .
```

**Customize patterns** by editing `REPLACEMENTS` list in `scripts/anonymize.py`:
```python
REPLACEMENTS = [
    (r'your-domain\.com', '[YOUR-DOMAIN]'),
    (r'Your Name', '[OWNER_NAME]'),
    # Add your patterns...
]
```

## Content Audit Utility

### Full Audit

```bash
cd scripts/content_audit
source venv/bin/activate
python main.py --full
```

### Output
- `research/content-audit/site-content-audit.csv` - Excel-friendly report
- `research/content-audit/content-gaps.md` - Pages needing improvement
- Gap analysis: keyword gaps, CTR opportunities, cannibalization

### Monthly Workflow
Run audit on last day of month before generating monthly report.

## Customization

### Adding New Skills

Create folder in `.claude/skills/your-skill/` with:
- `SKILL.md` - Skill definition and instructions

### Modifying Workflows

Edit files in `.claude/workflows/` to match your process.

### Extending Content Audit

Modify Python modules in `scripts/content_audit/`:
- `config.py` - Domain and patterns
- `sitemap_parser.py` - URL parsing logic
- `page_scraper.py` - Content extraction
- `gap_analyzer.py` - SEO analysis

## Requirements

- **Claude Code** - Anthropic's CLI tool
- **Python 3.8+** - For content audit scripts
- **Git** - Version control

### Python Dependencies
```
requests>=2.28.0
beautifulsoup4>=4.11.0
pymorphy3>=2.0.0  # Russian morphology (optional)
```

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `python scripts/anonymize.py --check .` to ensure no private data
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file.

## Acknowledgments

- Built with [Claude Code](https://claude.ai/code) by Anthropic
- Inspired by real-world e-commerce SEO projects
- Russian language support via [pymorphy3](https://github.com/no-madsoul/pymorphy3)

---

**Note:** This is a template. Replace all `[YOUR-PROJECT]`, `[YOUR-DOMAIN]`, and `[DATE]` placeholders with your actual project details.
