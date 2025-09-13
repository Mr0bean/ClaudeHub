# ClaudeHub - Chinese Documentation Portal

![ClaudeHub Banner](./docs/project-banner.png)

## 🌟 Project Overview

**ClaudeHub** is a comprehensive Chinese localization of claudelog.com, providing the Chinese Claude developer community with professional documentation support. This project includes intelligent web scraping, automated translation, and VuePress website generation, covering 68+ pages of technical documentation while maintaining the complete structure and functionality of the original site.

### Core Features

- **🕸️ Intelligent Web Scraping** - Complete extraction of all pages and resources from the original site
- **🔄 Automated Translation** - Batch translation workflow integrated with multiple translation engines
- **📚 VuePress Generation** - Generate fully functional static websites
- **🖼️ Resource Management** - Automatic download and optimization of image resources
- **🔗 Link Management** - Smart handling of internal links and navigation structure

## 📁 Project Structure

```
claudelogTranslate/
├── docs/                       # 📚 Project documentation
│   ├── TRANSLATION-GUIDE.md    # Translation guidelines
│   └── project-requirements.md # Project requirements
├── scripts/                    # 🛠️ Script toolkit
│   ├── scraper/               # Web scraping tools
│   │   └── final-scraper.js   # Main scraper script
│   ├── translation/           # Translation tools
│   │   ├── claude-translator.py      # Claude translator
│   │   ├── translate-all.sh          # Batch translation script
│   │   └── translation-checker.py    # Translation quality checker
│   ├── utils/                 # Utility scripts
│   │   ├── check-links.py           # Link checker
│   │   ├── fix-formatting.py       # Format fixer
│   │   └── cleanup.py              # Cleanup tools
│   └── validation/            # Validation tools
│       ├── comprehensive-scanner.py # Comprehensive scanner
│       └── quality-checker.py      # Quality checker
├── tools/                      # 🔧 Development tools
│   ├── test_file.md           # Test files
│   └── temp_prompt.txt        # Temporary prompt files
├── backups/                    # 💾 Backup files
│   ├── translation-backups/   # Translation backups
│   ├── final-site-backups/   # Website backups
│   └── working-copies/       # Working copies
├── final-site/                 # 🌐 VuePress website
│   ├── docs/                  # Markdown content files
│   │   ├── .vuepress/        # VuePress configuration
│   │   │   ├── config.js     # Website configuration
│   │   │   └── public/       # Static resources
│   │   ├── img/              # Image resources
│   │   └── *.md              # Page content (68+ pages)
│   └── package.json          # VuePress dependencies
├── CLAUDE.md                   # Claude Code development guide
├── README.md                   # Project documentation
├── package.json                # Project dependencies
└── .gitignore                  # Git ignore configuration
```

## 🛠️ Tech Stack

### Frontend Technologies
- **Framework**: VuePress 2.0 + Vite build tool
- **Language**: JavaScript + Markdown
- **Theme**: VuePress default theme + custom configuration
- **Styling**: CSS + inline HTML styles

### Backend Tools
- **Scraping**: Node.js + Puppeteer/Cheerio
- **Translation**: Python + Claude API/GPT API
- **Data Processing**: Turndown.js (HTML to Markdown)
- **File Management**: Node.js filesystem operations

### Development Tools
- **Package Manager**: npm
- **Version Control**: Git
- **Code Standards**: ESLint + Prettier
- **Quality Assurance**: Custom Python scripts

## 🚀 Quick Start

### Prerequisites
- Node.js >= 16.0.0
- Python >= 3.8
- npm >= 8.0.0

### Installation
```bash
# Clone the repository
git clone https://github.com/Mr0bean/ClaudeHub.git
cd ClaudeHub

# Install dependencies
npm install
```

### Web Scraping
```bash
# Run comprehensive scraper (scrape English original site)
node scripts/scraper/final-scraper.js

# Scraper automatically executes:
# - Download all pages and images
# - Convert HTML to Markdown
# - Maintain code formatting
# - Escape Vue syntax conflicts
# - Generate VuePress configuration
```

### Translation Workflow
```bash
# Batch translate all pages
bash scripts/translation/translate-all.sh

# Single file translation
python scripts/translation/claude-translator.py <file-path>

# Check translation quality
python scripts/translation/translation-checker.py
```

### Development Environment
```bash
# Start VuePress development server
cd final-site
npm install
npm run dev    # Visit http://localhost:8080

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📊 Project Statistics

- **Total Pages**: 68+ (including all MCPs subpages)
- **Image Resources**: 50+ images with automatic size optimization
- **Sidebar Sections**: 10 main sections with multi-level nesting
- **Code Block Fixes**: 25+ with maintained line break formatting
- **Navigation Links**: 100+ all verified and functional
- **Translation Progress**: 95% complete, continuously updating

## 🐛 Known Issues & Solutions

### 1. Image Display Issues
**Problem**: Images showing as broken links
**Solution**: Scraper automatically downloads images and updates paths

### 2. Sidebar Navigation 404 Errors
**Problem**: Directory-style links causing 404 errors
**Solution**: All links converted to .html format in config.js

### 3. Code Block Line Break Loss
**Problem**: Line breaks lost during HTML to Markdown conversion
**Solution**: Pre-process BR tags before Turndown conversion

### 4. Vue Parsing Errors
**Problem**: Angle brackets causing "element missing end tag" errors
**Solution**: Automatically escape angle brackets in markdown

### 5. Image Sizing Issues
**Problem**: Images too large (400px instead of 165px)
**Solution**: Apply inline HTML styles and max-width during scraping

## ✅ Quality Assurance

### Applied Automatic Fixes
- ✅ Scraped all 68 pages from source site
- ✅ Downloaded images and adjusted to correct sizes
- ✅ Code blocks maintain line break formatting
- ✅ Resolved Vue syntax conflicts
- ✅ Complete sidebar navigation functionality
- ✅ Included MCPs subpages (20+)
- ✅ Fixed homepage routing
- ✅ Corrected malformed markdown links

### Testing Checklist
- [x] All sidebar links navigate correctly
- [x] Images display at correct sizes
- [x] Code blocks render with formatting
- [x] No Vue parsing errors
- [x] All MCPs pages accessible
- [x] Homepage loads correctly
- [x] Support page layout matches original site

## 📝 Core Implementation Details

### Image Processing
```html
<!-- Images use inline HTML for VuePress compatibility -->
<img src="/img/example.png" style="max-width: 165px; height: auto;" />
```

### Code Block Protection
```javascript
// BR tags pre-processed before markdown conversion
html = html.replace(/<br\s*\/?>/gi, '___LINEBREAK___');
// Later converted to actual line breaks in markdown
```

### Vue Conflict Resolution
```javascript
// Escape angle brackets to prevent parsing errors
markdown = markdown.replace(/<(\d+%)/g, '&lt;$1');
```

## 🚧 Future Improvement Plans

### Completed Features
- [x] Chinese translation support (95% complete)
- [x] Automated testing suite
- [x] Quality assurance workflow
- [x] Batch processing tools

### Planned Features
- [ ] CI/CD automatic update workflow
- [ ] Interactive chart reproduction
- [ ] Site-wide search functionality
- [ ] Dark mode support
- [ ] Mobile optimization
- [ ] Multi-language switching

## 📋 Code Standards

### File Naming Conventions
```
# Python scripts: kebab-case
translate-all.py
check-links.py

# JavaScript files: camelCase
finalScraper.js
configUtils.js

# Documentation files: UPPERCASE
README.md
CLAUDE.md
```

### Git Commit Standards
```bash
# Commit format: <type>(<scope>): <description>

# Type descriptions
feat:     new feature
fix:      bug fix
docs:     documentation update
refactor: code refactoring
script:   script update
trans:    translation update

# Examples
feat(scraper): add automatic image optimization
fix(translation): fix code block translation issues
docs(readme): update project structure documentation
script(utils): optimize link checking script
trans(pages): complete FAQ page translation
```

## 📄 License

This project is for educational and learning purposes only. Original content copyright belongs to claudelog.com.

## 🤝 Contributing Guidelines

1. Test changes locally with `npm run dev`
2. Verify all links work correctly
3. Check image sizes match original site
4. Ensure no Vue parsing errors
5. Update CLAUDE.md to record new issues/solutions

## 📚 Related Documentation

- **[CLAUDE.md](./CLAUDE.md)** - Comprehensive development guide and issue tracking
- **[Translation Guide](./docs/TRANSLATION-GUIDE.md)** - Translation workflow and standards
- **[scripts/](./scripts/)** - Inline documentation for various scripts
- **[final-site/.vuepress/config.js](./final-site/.vuepress/config.js)** - Sidebar structure documentation

## 🔍 Troubleshooting

If you encounter issues:

1. **Broken Images**: Re-run scraper to download missing images
2. **404 Errors**: Check sidebar links use .html format
3. **Build Errors**: Ensure `npm install` installed all dependencies
4. **Vue Errors**: Look for unescaped angle brackets in markdown
5. **Missing Pages**: Verify scraper includes all URLs in getAllLinks()

For detailed troubleshooting, refer to the comprehensive issue documentation and solutions in CLAUDE.md.

## 🔗 Related Links

- **Original Site**: [https://claudelog.com](https://claudelog.com)
- **Development Documentation**: [./CLAUDE.md](./CLAUDE.md)
- **Project Repository**: [https://github.com/Mr0bean/ClaudeHub](https://github.com/Mr0bean/ClaudeHub)

---

**ClaudeHub - Professional documentation support for the Chinese Claude developer community**

*Last Updated: September 13, 2025*
*Total Development Time: ~20 hours*
*Issues Resolved: 30+*
*Successfully Migrated Pages: 68+*