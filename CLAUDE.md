# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This project scrapes the claudelog.com website and recreates it using VuePress, maintaining the exact structure and hierarchy of the source site. The project includes both English (original) and Chinese (translated) versions.

## ⚠️ COMPREHENSIVE ISSUES AND SOLUTIONS SUMMARY (2024-12)

### 🔴 CRITICAL ISSUES THAT MUST BE FIXED

#### 1. **Malformed Markdown Link Syntax**
- **Problem**: Scraper generates broken markdown with opening brackets `[` on separate lines
- **Symptom**: Raw markdown displayed instead of rendered links
- **Example**: 
  ```markdown
  [
  ## Title
  Description
  ](/url/)
  ```
- **Solution**: Ensure markdown links are on single line: `## [Title](/url.html)`
- **Files Affected**: `claude-code-mcps.md` main navigation page

#### 2. **Image Sizing Issues**
- **Problem**: Images display at wrong sizes, breaking layout
- **Original Site Sizes**:
  - Discovery images: max-width: 165px
  - Profile images: 25x25px with border-radius: 50%
  - Supporter images: max-width: 150px with border-radius: 8px
  - Logo images: max-width: 80px
- **Solution**: Use inline HTML styles in markdown:
  ```html
  <img src="/img/discovery/036_cl_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />
  ```
- **Implementation**: Added Turndown rule in scraper to apply correct sizing during conversion

#### 3. **VuePress URL Routing Issues**
- **Problem**: Directory-style links (`/page/`) cause 404 errors
- **Solution**: All links MUST use `.html` format: `/page.html`
- **Special Cases**:
  - Homepage: Use `/` not `/README.html`
  - Subpages: `/claude-code-mcps-cc-usage.html` not `/claude-code-mcps/cc-usage/`

#### 4. **Vue Component Parsing Errors**
- **Problem**: Angle brackets treated as Vue components causing "Element is missing end tag"
- **Common Patterns**:
  - `<5%` → `&lt;5%`
  - `<session-id>` → `&lt;session-id&gt;`
  - `@<agent>` → `@&lt;agent&gt;`
  - `<path-to-file>` → `&lt;path-to-file&gt;`
- **Solution**: Escape all non-HTML angle brackets in scraper post-processing

#### 5. **Code Block Line Breaks Not Preserved**
- **Problem**: BR tags in code blocks not converted to newlines
- **Symptom**: Commands run together: `cd projectclaude` instead of separate lines
- **Solution**: Pre-process HTML before Turndown, replace BR with newline placeholders

#### 6. **Missing Page Content**
- **Problem**: Scraper missing collapsed sidebar sections
- **Original Issue**: Only scraped 31 pages out of 58+
- **Solution**: Manually specify all pages in getAllLinks() including:
  - Agents section (7 pages)
  - Performance section (6 pages)  
  - Development section (8 pages)
  - MCPs subpages (20+ pages)

#### 7. **Missing H1 Titles**
- **Problem**: Pages missing main H1 header after frontmatter
- **Affected**: All 25+ mechanics pages, tutorial page, homepage
- **Solution**: Add `# Page Title` immediately after frontmatter based on title field

#### 8. **Support Page Layout Issues**
- **Problem**: Profile and supporter images not displaying correctly
- **Solution**: Ensure all image paths are downloaded and use proper inline styling

#### 9. **MCPs Navigation Structure**
- **Problem**: MCPs & Add-ons section missing 20+ subpages
- **Symptoms**: Sidebar only showed main page, not individual MCP tools
- **Solution**: 
  - Add all MCP URLs to scraper getAllinks()
  - Update sidebar config with all MCP subpages
  - Handle 404 errors for non-existent pages gracefully

### 📋 COMPLETE ISSUE PREVENTION CHECKLIST

Before deploying, verify:

1. **Markdown Syntax**
   - [ ] No brackets on separate lines
   - [ ] All links use proper `[text](url)` format
   - [ ] Links use `.html` extension (except homepage which uses `/`)

2. **Image Handling**
   - [ ] All images downloaded to correct directories
   - [ ] Inline styles applied for sizing
   - [ ] Discovery images: max-width: 165px
   - [ ] Profile images: 25x25px

3. **Code Blocks**
   - [ ] Line breaks preserved (no concatenated commands)
   - [ ] BR tags converted to newlines
   - [ ] Code fence blocks properly closed

4. **Special Characters**
   - [ ] Angle brackets escaped: `<` → `&lt;`, `>` → `&gt;`
   - [ ] No unescaped `<xxx>` patterns
   - [ ] Percentages properly escaped: `<5%` → `&lt;5%`

5. **Page Structure**
   - [ ] H1 title present after frontmatter
   - [ ] Frontmatter has proper title field
   - [ ] No "Untitled" pages

6. **Navigation**
   - [ ] All sidebar links working (test 25+ pages minimum)
   - [ ] MCPs section has all subpages
   - [ ] Collapsible sections expand properly

### 🚀 QUICK FIX COMMANDS

```bash
# Fix malformed markdown links
perl -i -pe 's/\[\s*\n\s*##/## \[/g; s/\]\s*\n\s*\(/\](/g' docs/*.md

# Fix image sizing (discovery images)
find docs -name "*.md" -exec perl -pi -e 's|!\[([^\]]*)\]\((/img/discovery/[^\)]+)\)|<img src="$2" alt="$1" style="max-width: 165px; height: auto;" />|g' {} \;

# Fix VuePress URLs in config
sed -i 's|"/\([^/]*\)/"|"/\1.html"|g' docs/.vuepress/config.js
sed -i 's|"/README.html"|"/"|g' docs/.vuepress/config.js

# Escape angle brackets
find docs -name "*.md" -exec perl -pi -e 's/<(\d+%)/&lt;$1/g; s/@<([^>]+)>/@&lt;$1&gt;/g' {} \;

# Add missing H1 titles (based on frontmatter)
for file in docs/mechanics-*.md; do
  title=$(grep "^title:" "$file" | sed 's/title: "\(.*\)"/\1/')
  sed -i "/^---$/,/^---$/! s/^/# $title\n\n/; /^---$/,/^---$/d" "$file"
done
```

### 📊 FINAL STATISTICS

- **Total Pages Scraped**: 68 (out of 72 attempted)
- **404 Pages Excluded**: 4 (CC Statusline, SuperClaude, Brave Search MCP, Twitter/X MCP)
- **Images Downloaded**: 52
- **MCPs Pages Added**: 18 functional pages
- **Mechanics Pages Fixed**: 38 pages total
- **Total Issues Fixed**: 9 major categories

### 🎯 KEY LESSONS LEARNED

1. **Always test with MCP browser tools** - Manual testing catches issues automated tests miss
2. **VuePress has strict requirements** - File extensions, URL formats, and Vue parsing rules
3. **Scraper must handle edge cases** - BR tags, malformed HTML, collapsed sections
4. **Documentation is critical** - This CLAUDE.md prevents repeating same issues
5. **Batch fixes save time** - Script common patterns instead of manual edits

## Project Structure
```
claudelogTranslate/
├── scraper/               
│   └── final-scraper.js  # Consolidated scraper with all fixes
├── final-site/           # Working VuePress site
│   ├── docs/            # 68 markdown files
│   └── .vuepress/       # Config with proper sidebar
└── CLAUDE.md            # This comprehensive guide
```

## Deployment Commands

```bash
# Fresh scrape with all fixes
node scraper/final-scraper.js en final-site

# Start development server
cd final-site
npm install
npm run dev

# Build for production
npm run build
```

## Critical Rules for Future Development

1. **NEVER** commit without testing all sidebar navigation
2. **ALWAYS** escape angle brackets in markdown content
3. **VERIFY** image paths and sizing match original site
4. **TEST** at least 25 pages with MCP browser tools
5. **UPDATE** this CLAUDE.md with any new issues discovered