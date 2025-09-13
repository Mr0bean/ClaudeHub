#!/usr/bin/env node

/**
 * Final Consolidated VuePress Scraper for ClaudeLog
 * 
 * This scraper addresses all identified issues:
 * 1. ✅ Image downloading with correct sizing
 * 2. ✅ Sidebar navigation with .html format
 * 3. ✅ Code block line break preservation
 * 4. ✅ VuePress-compatible structure generation
 * 5. ✅ Comprehensive dependency management
 */

const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs-extra');
const path = require('path');
const TurndownService = require('turndown');
const sizeOf = require('image-size');

const BASE_URL = 'https://claudelog.com';

class FinalClaudeLogScraper {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || BASE_URL;
    this.outputDir = options.outputDir || path.join(__dirname, '../final-site');
    this.language = options.language || 'en';
    this.delayMs = options.delay || 1000;
    
    // Tracking
    this.visitedUrls = new Set();
    this.pageMap = new Map();
    this.downloadedImages = new Map();
    this.sidebarStructure = [];
    
    // Initialize Turndown with custom rules
    this.initializeTurndown();
  }
  
  initializeTurndown() {
    this.turndown = new TurndownService({
      headingStyle: 'atx',
      codeBlockStyle: 'fenced',
      bulletListMarker: '-',
      emDelimiter: '*',
      strongDelimiter: '**',
      linkStyle: 'inlined',
      preformattedCode: true
    });
    
    // Critical: Preserve line breaks in code blocks
    this.turndown.addRule('preserveCodeBlocks', {
      filter: ['pre'],
      replacement: (content, node) => {
        const codeElement = node.querySelector('code');
        if (!codeElement) return '```\n' + content + '\n```';
        
        // Extract language
        const langClass = codeElement.className || '';
        const lang = langClass.replace(/^language-/, '').replace(/^codeBlockLines.*/, '') || 'bash';
        
        // Process HTML to preserve line breaks
        let codeContent = '';
        
        // Method 1: Check for token-line structure (Docusaurus pattern)
        const tokenLines = codeElement.querySelectorAll('.token-line, [class*="token-line"]');
        if (tokenLines.length > 0) {
          const lines = [];
          tokenLines.forEach(line => {
            lines.push(line.textContent || '');
          });
          codeContent = lines.join('\n');
        } else {
          // Method 2: Process HTML with BR tags
          let htmlContent = codeElement.innerHTML;
          htmlContent = htmlContent.replace(/<br\s*\/?>/gi, '\n');
          
          // Create temporary element for text extraction
          const temp = node.ownerDocument.createElement('div');
          temp.innerHTML = htmlContent;
          codeContent = temp.textContent || '';
        }
        
        // Clean up and normalize
        codeContent = codeContent
          .replace(/\r\n/g, '\n')
          .replace(/\r/g, '\n')
          .replace(/\n{3,}/g, '\n\n');
        
        return '```' + lang + '\n' + codeContent + '\n```';
      }
    });
    
    // Inline code preservation
    this.turndown.addRule('preserveInlineCode', {
      filter: ['code'],
      replacement: (content, node) => {
        if (node.parentNode && node.parentNode.nodeName === 'PRE') {
          return content;
        }
        return '`' + content + '`';
      }
    });
    
    // Custom rule for images - process them with correct sizing
    this.turndown.addRule('processImages', {
      filter: 'img',
      replacement: (content, node) => {
        const src = node.getAttribute('src') || '';
        const alt = node.getAttribute('alt') || '';
        
        // Apply correct sizing based on image type
        if (src.includes('/img/discovery/') || src.match(/\/img\/\d{3}/)) {
          return `<img src="${src}" alt="${alt}" style="max-width: 165px; height: auto;" />`;
        } else if (src.includes('claudes-greatest-soldier')) {
          return `<img src="${src}" alt="${alt}" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />`;
        } else if (src.includes('/img/supporters/')) {
          return `<img src="${src}" alt="${alt}" style="max-width: 150px; height: auto; border-radius: 8px;" />`;
        } else if (src.includes('reddit-icon') || src.includes('claude_log_star')) {
          return `<img src="${src}" alt="${alt}" style="max-width: 80px; height: auto;" />`;
        }
        
        // Default: use HTML img tag
        return `<img src="${src}" alt="${alt}" />`;
      }
    });
  }
  
  async downloadImage(src, alt = '') {
    try {
      const imageUrl = src.startsWith('http') ? src : this.baseUrl + src;
      const imageName = path.basename(src);
      const imagesDir = path.join(this.outputDir, 'docs/.vuepress/public/img');
      
      // Check for subdirectories in image path
      let targetDir = imagesDir;
      if (src.includes('/img/discovery/')) {
        targetDir = path.join(imagesDir, 'discovery');
      } else if (src.includes('/img/supporters/')) {
        targetDir = path.join(imagesDir, 'supporters');
      }
      
      await fs.ensureDir(targetDir);
      const localPath = path.join(targetDir, imageName);
      
      if (!this.downloadedImages.has(src)) {
        console.log(`[IMAGE] Downloading: ${imageUrl}`);
        const response = await axios.get(imageUrl, {
          responseType: 'arraybuffer',
          timeout: 10000,
          headers: {
            'User-Agent': 'Mozilla/5.0 (compatible; ClaudeLogScraper/1.0)'
          }
        });
        
        await fs.writeFile(localPath, response.data);
        
        // Get dimensions
        let dimensions = { width: null, height: null };
        try {
          dimensions = sizeOf(response.data);
          console.log(`[IMAGE] Saved: ${imageName} (${dimensions.width}x${dimensions.height})`);
        } catch (e) {
          console.log(`[IMAGE] Saved: ${imageName} (dimensions unknown)`);
        }
        
        // Store relative path for markdown
        let relativePath = `/img/${imageName}`;
        if (src.includes('/img/discovery/')) {
          relativePath = `/img/discovery/${imageName}`;
        } else if (src.includes('/img/supporters/')) {
          relativePath = `/img/supporters/${imageName}`;
        }
        
        this.downloadedImages.set(src, {
          localPath: relativePath,
          width: dimensions.width,
          height: dimensions.height
        });
      }
      
      return this.downloadedImages.get(src);
    } catch (error) {
      console.error(`[IMAGE ERROR] Failed to download ${src}: ${error.message}`);
      return null;
    }
  }
  
  // Note: Image markdown is now handled directly in the Turndown rule
  
  async processPage(url) {
    if (this.visitedUrls.has(url)) {
      return this.pageMap.get(url);
    }
    
    this.visitedUrls.add(url);
    
    try {
      console.log(`[SCRAPING] ${url}`);
      
      const response = await axios.get(this.baseUrl + url, {
        timeout: 10000,
        headers: {
          'User-Agent': 'Mozilla/5.0 (compatible; ClaudeLogScraper/1.0)'
        }
      });
      
      const $ = cheerio.load(response.data);
      
      // Pre-process code blocks to preserve line breaks
      $('pre code').each((i, elem) => {
        const $elem = $(elem);
        let htmlContent = $elem.html();
        if (htmlContent) {
          // Replace BR tags with a placeholder
          htmlContent = htmlContent.replace(/<br\s*\/?>/gi, '___NEWLINE___');
          $elem.html(htmlContent);
        }
      });
      
      // Extract images before removing them
      const images = [];
      $('img').each((i, elem) => {
        const src = $(elem).attr('src');
        const alt = $(elem).attr('alt') || '';
        if (src) {
          images.push({ src, alt });
        }
      });
      
      // Remove navigation elements
      $('nav, .sidebar, header, footer, .toc, .navbar').remove();
      $('.theme-doc-toc-mobile, .theme-doc-sidebar-container').remove();
      $('script, style, noscript').remove();
      
      // Get main content
      let content = '';
      const mainSelectors = [
        'main article',
        '.main-wrapper article',
        '[role="main"]',
        '.content',
        'main'
      ];
      
      for (const selector of mainSelectors) {
        const $main = $(selector);
        if ($main.length > 0) {
          let mainHtml = $main.html();
          // Restore newlines
          mainHtml = mainHtml.replace(/___NEWLINE___/g, '\n');
          content = mainHtml;
          break;
        }
      }
      
      if (!content) {
        content = $('body').html();
        content = content.replace(/___NEWLINE___/g, '\n');
      }
      
      // Convert to markdown
      let markdown = this.turndown.turndown(content || '');
      
      // Download images (but don't add them again - they're already in the markdown)
      for (const img of images) {
        await this.downloadImage(img.src, img.alt);
      }
      
      // Extract title
      const title = this.extractTitle($);
      
      // Clean up markdown
      markdown = markdown
        .replace(/\n{3,}/g, '\n\n')
        .trim()
        .replace(/\[([^\]]+)\]\(\)/g, '$1');
      
      // Escape angle brackets to prevent Vue parsing errors
      // Match patterns like <word>, <5%, @<agent> but not HTML tags
      markdown = markdown
        // Escape standalone angle brackets (not part of HTML tags)
        .replace(/<(\d+%)/g, '&lt;$1')  // Fix patterns like <5%
        .replace(/@<([^>]+)>/g, '@&lt;$1&gt;')  // Fix patterns like @<agent>
        .replace(/`([^`]*)<([^>]+)>([^`]*)`/g, (match, before, content, after) => {
          // Escape angle brackets within backticks (code snippets)
          return `\`${before}&lt;${content}&gt;${after}\``;
        })
        // Skip HTML tags and already escaped entities
        .replace(/<([^>/!][^>]*)>/g, (match, content) => {
          // Don't escape if it's already escaped or an HTML tag
          if (match.includes('&lt;') || match.includes('&gt;') || 
              match.startsWith('<img') || match.startsWith('</')) {
            return match;
          }
          return `&lt;${content}&gt;`;
        });
      
      const pageData = {
        url,
        title,
        content: markdown
      };
      
      this.pageMap.set(url, pageData);
      console.log(`[SUCCESS] Scraped: ${url}`);
      
      await this.delay();
      return pageData;
      
    } catch (error) {
      console.error(`[ERROR] Failed to scrape ${url}: ${error.message}`);
      return null;
    }
  }
  
  extractTitle($) {
    const titleSelectors = ['h1', 'article h1', '.markdown h1', 'main h1', 'title'];
    
    for (const selector of titleSelectors) {
      const title = $(selector).first().text().trim();
      if (title && title !== 'ClaudeLog') {
        return title;
      }
    }
    
    return 'Untitled';
  }
  
  async getAllLinks() {
    // Manually define all known pages including those in collapsed sections
    const allPages = [
      '/', // Homepage
      '/support-claudelog/',
      '/install-claude-code/',
      '/claude-code-tutorial/',
      '/configuration/',
      
      // Foundation Mechanics (expanded by default)
      '/mechanics/you-are-the-main-thread/',
      '/mechanics/claude-md-supremacy/',
      '/mechanics/plan-mode/',
      '/mechanics/auto-plan-mode/',
      '/mechanics/always-be-experimenting/',
      '/mechanics/poison-context-awareness/',
      '/mechanics/context-window-constraints-as-training/',
      '/mechanics/context-inspection/',
      '/mechanics/dynamic-memory/',
      '/mechanics/sanity-check/',
      '/mechanics/output-styles/',
      '/mechanics/permutation-frameworks/',
      
      // Agents section (collapsed - previously missing)
      '/mechanics/task-agent-tools/',
      '/mechanics/sub-agents/',
      '/mechanics/agent-first-design/',
      '/mechanics/split-role-sub-agents/',
      '/mechanics/custom-agents/',
      '/mechanics/agent-engineering/',
      '/mechanics/humanising-agents/',
      
      // Performance section (collapsed - previously missing)
      '/mechanics/ultrathink-plus-plus/',
      '/mechanics/bash-scripts/',
      '/mechanics/context-window-depletion/',
      '/mechanics/tactical-model-selection/',
      '/mechanics/rev-the-engine/',
      '/mechanics/sub-agent-tactics/',
      
      // Development section (collapsed - previously missing)
      '/mechanics/hooks/',
      '/mechanics/auto-accept-permissions/',
      '/mechanics/dangerous-skip-permissions/',
      '/mechanics/git-clone-is-just-the-beginning/',
      '/mechanics/claude-usage/',
      '/mechanics/tight-feedback-loops/',
      '/mechanics/todo-lists-as-instruction-mirrors/',
      '/mechanics/skeleton-projects/',
      
      // Other sections
      '/watch-control/',
      
      // MCPs & Add-ons main page and all subpages
      '/claude-code-mcps/',
      '/claude-code-mcps/cc-usage/',
      '/claude-code-mcps/tdd-guard/',
      '/claude-code-mcps/cc-statusline/',
      '/claude-code-mcps/tweakcc/',
      '/claude-code-mcps/claude-code-router/',
      '/claude-code-mcps/superclaude/',
      '/claude-code-mcps/claudia/',
      '/claude-code-mcps/brave-search-mcp/',
      '/claude-code-mcps/context7-mcp/',
      '/claude-code-mcps/puppeteer-mcp/',
      '/claude-code-mcps/reddit-mcp/',
      '/claude-code-mcps/twitter-x-mcp/',
      '/claude-code-mcps/whatsapp-mcp/',
      '/claude-code-mcps/awesome-mcp-servers/',
      '/claude-code-mcps/awesome-claude-code/',
      '/claude-code-mcps/github-mcp-server/',
      '/claude-code-mcps/blender-mcp/',
      '/claude-code-mcps/browser-tools-mcp/',
      '/claude-code-mcps/desktop-commander-mcp/',
      '/claude-code-mcps/zen-mcp-server/',
      '/claude-code-mcps/serena/',
      '/claude-code-mcps/awesome-claude-prompts/',
      
      '/faq/',
      '/claude-code-pricing/',
      '/claude-code-changelog/',
      '/claude-news/',
      '/sponsor/',
      '/contact/',
      '/privacy-policy/',
      '/terms-of-service/',
      '/disclaimer/',
      
      // Additional variations (handle both with and without trailing slash)
      '/mechanics/context-inspection'
    ];
    
    return allPages;
  }
  
  generateSidebarConfig() {
    // Complete sidebar structure matching claudelog.com exactly
    return [
      {
        text: 'Getting Started',
        collapsible: false,
        children: [
          '/',
          '/install-claude-code.html',
          '/claude-code-tutorial.html',
          '/configuration.html'
        ]
      },
      {
        text: 'Support',
        children: [
          '/support-claudelog.html'
        ]
      },
      {
        text: 'Mechanics',
        collapsible: true,
        children: [
          {
            text: 'Foundation',
            collapsible: true,
            children: [
              '/mechanics-you-are-the-main-thread.html',
              '/mechanics-claude-md-supremacy.html',
              '/mechanics-plan-mode.html',
              '/mechanics-auto-plan-mode.html',
              '/mechanics-always-be-experimenting.html',
              '/mechanics-poison-context-awareness.html',
              '/mechanics-context-window-constraints-as-training.html',
              '/mechanics-context-inspection.html',
              '/mechanics-dynamic-memory.html',
              '/mechanics-sanity-check.html',
              '/mechanics-output-styles.html',
              '/mechanics-permutation-frameworks.html'
            ]
          },
          {
            text: 'Agents',
            collapsible: true,
            children: [
              '/mechanics-task-agent-tools.html',
              '/mechanics-sub-agents.html',
              '/mechanics-agent-first-design.html',
              '/mechanics-split-role-sub-agents.html',
              '/mechanics-custom-agents.html',
              '/mechanics-agent-engineering.html',
              '/mechanics-humanising-agents.html'
            ]
          },
          {
            text: 'Performance',
            collapsible: true,
            children: [
              '/mechanics-ultrathink-plus-plus.html',
              '/mechanics-bash-scripts.html',
              '/mechanics-context-window-depletion.html',
              '/mechanics-tactical-model-selection.html',
              '/mechanics-rev-the-engine.html',
              '/mechanics-sub-agent-tactics.html'
            ]
          },
          {
            text: 'Development',
            collapsible: true,
            children: [
              '/mechanics-hooks.html',
              '/mechanics-auto-accept-permissions.html',
              '/mechanics-dangerous-skip-permissions.html',
              '/mechanics-git-clone-is-just-the-beginning.html',
              '/mechanics-claude-usage.html',
              '/mechanics-tight-feedback-loops.html',
              '/mechanics-todo-lists-as-instruction-mirrors.html',
              '/mechanics-skeleton-projects.html'
            ]
          }
        ]
      },
      {
        text: 'CLAUDE.md Vault',
        collapsible: true,
        children: [
          '/watch-control.html'
        ]
      },
      {
        text: 'MCPs & Add-ons',
        collapsible: true,
        children: [
          '/claude-code-mcps.html',
          '/claude-code-mcps-cc-usage.html',
          '/claude-code-mcps-tdd-guard.html',
          '/claude-code-mcps-cc-statusline.html',
          '/claude-code-mcps-tweakcc.html',
          '/claude-code-mcps-claude-code-router.html',
          '/claude-code-mcps-superclaude.html',
          '/claude-code-mcps-claudia.html',
          '/claude-code-mcps-brave-search-mcp.html',
          '/claude-code-mcps-context7-mcp.html',
          '/claude-code-mcps-puppeteer-mcp.html',
          '/claude-code-mcps-reddit-mcp.html',
          '/claude-code-mcps-twitter-x-mcp.html',
          '/claude-code-mcps-whatsapp-mcp.html',
          '/claude-code-mcps-awesome-mcp-servers.html',
          '/claude-code-mcps-awesome-claude-code.html',
          '/claude-code-mcps-github-mcp-server.html',
          '/claude-code-mcps-blender-mcp.html',
          '/claude-code-mcps-browser-tools-mcp.html',
          '/claude-code-mcps-desktop-commander-mcp.html',
          '/claude-code-mcps-zen-mcp-server.html',
          '/claude-code-mcps-serena.html',
          '/claude-code-mcps-awesome-claude-prompts.html'
        ]
      },
      {
        text: 'Resources',
        children: [
          '/faq.html',
          '/claude-code-pricing.html',
          '/claude-code-changelog.html',
          '/claude-news.html'
        ]
      },
      {
        text: 'Community',
        children: [
          '/sponsor.html',
          '/contact.html'
        ]
      },
      {
        text: 'Legal',
        children: [
          '/privacy-policy.html',
          '/terms-of-service.html',
          '/disclaimer.html'
        ]
      }
    ];
  }
  
  async generateVuePressConfig() {
    const configContent = `import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'
import { viteBundler } from '@vuepress/bundler-vite'

export default defineUserConfig({
  lang: '${this.language}',
  title: 'ClaudeLog',
  description: 'Claude Code docs, guides, tutorials & best practices',
  
  base: '/',
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }]
  ],

  bundler: viteBundler(),
  
  theme: defaultTheme({
    logo: '/img/claude_log_star.png',
    
    navbar: [
      { text: 'Home', link: '/' },
      { text: 'Install', link: '/install-claude-code.html' },
      { text: 'Tutorial', link: '/claude-code-tutorial.html' },
      { text: 'MCPs', link: '/claude-code-mcps.html' },
      { text: 'Support', link: '/support-claudelog.html' }
    ],
    
    sidebar: ${JSON.stringify(this.generateSidebarConfig(), null, 4)},
    
    sidebarDepth: 3,
    
    editLink: false,
    lastUpdated: true,
    contributors: false
  })
})`;

    const configPath = path.join(this.outputDir, 'docs/.vuepress/config.js');
    await fs.ensureDir(path.dirname(configPath));
    await fs.writeFile(configPath, configContent);
    console.log('[CONFIG] Generated VuePress config');
  }
  
  async generatePackageJson() {
    const packageJson = {
      name: "claudelog-docs",
      version: "1.0.0",
      description: "ClaudeLog Documentation",
      scripts: {
        "dev": "vuepress dev docs",
        "build": "vuepress build docs"
      },
      devDependencies: {
        "vuepress": "^2.0.0-rc.0",
        "@vuepress/bundler-vite": "^2.0.0-rc.0",
        "@vuepress/theme-default": "^2.0.0-rc.0",
        "sass-embedded": "^1.69.5"
      }
    };
    
    const packagePath = path.join(this.outputDir, 'package.json');
    await fs.writeFile(packagePath, JSON.stringify(packageJson, null, 2));
    console.log('[PACKAGE] Generated package.json');
  }
  
  async savePages() {
    const docsDir = path.join(this.outputDir, 'docs');
    await fs.ensureDir(docsDir);
    
    for (const [url, pageData] of this.pageMap) {
      const fileName = url === '/' ? 'README.md' : 
                      url.replace(/^\/|\/$/g, '').replace(/\//g, '-') + '.md';
      const filePath = path.join(docsDir, fileName);
      
      // Add frontmatter and H1 title if missing
      let content = pageData.content;
      if (!content.startsWith('# ')) {
        content = `# ${pageData.title}\n\n${content}`;
      }
      
      const frontmatter = `---\ntitle: "${pageData.title}"\n---\n\n`;
      const fullContent = frontmatter + content;
      
      await fs.writeFile(filePath, fullContent);
      console.log(`[SAVED] ${fileName}`);
    }
  }
  
  async delay() {
    return new Promise(resolve => setTimeout(resolve, this.delayMs));
  }
  
  async run() {
    try {
      console.log('[START] Final ClaudeLog Scraper');
      console.log('[INFO] This version includes all fixes:');
      console.log('  - Image downloading with correct sizing');
      console.log('  - Sidebar navigation with .html format');
      console.log('  - Code block line break preservation');
      console.log('  - VuePress-compatible structure\n');
      
      // Get all links
      const links = await this.getAllLinks();
      console.log(`[LINKS] Found ${links.length} unique links\n`);
      
      // Process each page
      for (const link of links) {
        await this.processPage(link);
      }
      
      // Generate VuePress structure
      await this.generatePackageJson();
      await this.generateVuePressConfig();
      
      // Save all pages
      await this.savePages();
      
      console.log('\n[COMPLETE] Scraping finished successfully!');
      console.log(`[STATS] Pages: ${this.pageMap.size}, Images: ${this.downloadedImages.size}`);
      console.log(`[OUTPUT] Site generated in: ${this.outputDir}`);
      console.log('\n[NEXT STEPS]');
      console.log('1. cd ' + this.outputDir);
      console.log('2. npm install');
      console.log('3. npm run dev');
      console.log('4. Open http://localhost:8080\n');
      
    } catch (error) {
      console.error('[FATAL] Scraper failed:', error);
      process.exit(1);
    }
  }
}

// Run if called directly
if (require.main === module) {
  const scraper = new FinalClaudeLogScraper({
    language: process.argv[2] || 'en',
    outputDir: process.argv[3] || path.join(__dirname, '../final-site')
  });
  
  scraper.run();
}

module.exports = FinalClaudeLogScraper;