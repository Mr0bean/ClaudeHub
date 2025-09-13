import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'
import { viteBundler } from '@vuepress/bundler-vite'

export default defineUserConfig({
  lang: 'en',
  title: '⭐ 星科文档 | Claude Hub',
  description: 'Claude Code docs, guides, tutorials & best practices',
  
  base: '/',
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }]
  ],

  bundler: viteBundler(),
  
  theme: defaultTheme({
    logo: '/img/claude_log_star.svg',
    
    navbar: [
      { text: '首页', link: '/' },
      { text: '指南', link: '/guide.html' },
      { text: '安装', link: '/install-claude-code.html' },
      { text: '教程', link: '/claude-code-tutorial.html' },
      { text: 'MCPs 扩展', link: '/claude-code-mcps.html' }
    ],
    
    sidebar: [
    {
        "text": "快速开始",
        "collapsible": false,
        "children": [
            "/",
            "/guide.html",
            "/install-claude-code.html",
            "/claude-code-tutorial.html",
            "/configuration.html"
        ]
    },
    {
        "text": "核心机制",
        "collapsible": true,
        "children": [
            {
                "text": "基础概念",
                "collapsible": true,
                "children": [
                    "/mechanics-you-are-the-main-thread.html",
                    "/mechanics-claude-md-supremacy.html",
                    "/mechanics-plan-mode.html",
                    "/mechanics-auto-plan-mode.html",
                    "/mechanics-always-be-experimenting.html",
                    "/mechanics-poison-context-awareness.html",
                    "/mechanics-context-window-constraints-as-training.html",
                    "/mechanics-context-inspection.html",
                    "/mechanics-dynamic-memory.html",
                    "/mechanics-sanity-check.html",
                    "/mechanics-output-styles.html",
                    "/mechanics-permutation-frameworks.html"
                ]
            },
            {
                "text": "智能代理",
                "collapsible": true,
                "children": [
                    "/mechanics-task-agent-tools.html",
                    "/mechanics-sub-agents.html",
                    "/mechanics-agent-first-design.html",
                    "/mechanics-split-role-sub-agents.html",
                    "/mechanics-custom-agents.html",
                    "/mechanics-agent-engineering.html",
                    "/mechanics-humanising-agents.html"
                ]
            },
            {
                "text": "性能优化",
                "collapsible": true,
                "children": [
                    "/mechanics-ultrathink-plus-plus.html",
                    "/mechanics-bash-scripts.html",
                    "/mechanics-context-window-depletion.html",
                    "/mechanics-tactical-model-selection.html",
                    "/mechanics-rev-the-engine.html",
                    "/mechanics-sub-agent-tactics.html"
                ]
            },
            {
                "text": "开发实践",
                "collapsible": true,
                "children": [
                    "/mechanics-hooks.html",
                    "/mechanics-dangerous-skip-permissions.html",
                    "/mechanics-git-clone-is-just-the-beginning.html",
                    "/mechanics-claude-usage.html",
                    "/mechanics-todo-lists-as-instruction-mirrors.html",
                    "/mechanics-skeleton-projects.html"
                ]
            }
        ]
    },
    {
        "text": "CLAUDE.md 文档库",
        "collapsible": true,
        "children": [
            "/watch-control.html"
        ]
    },
    {
        "text": "MCPs 插件与扩展",
        "collapsible": true,
        "children": [
            "/claude-code-mcps.html",
            "/claude-code-mcps-cc-usage.html",
            "/claude-code-mcps-tdd-guard.html",
            "/claude-code-mcps-tweakcc.html",
            "/claude-code-mcps-claude-code-router.html",
            "/claude-code-mcps-claudia.html",
            "/claude-code-mcps-context7-mcp.html",
            "/claude-code-mcps-puppeteer-mcp.html",
            "/claude-code-mcps-reddit-mcp.html",
            "/claude-code-mcps-whatsapp-mcp.html",
            "/claude-code-mcps-awesome-mcp-servers.html",
            { text: "精选 Claude Code 资源", link: "/claude-code-mcps-awesome-claude-code.html" },
            "/claude-code-mcps-github-mcp-server.html",
            "/claude-code-mcps-blender-mcp.html",
            "/claude-code-mcps-desktop-commander-mcp.html",
            "/claude-code-mcps-zen-mcp-server.html",
            "/claude-code-mcps-serena.html",
            "/claude-code-mcps-awesome-claude-prompts.html"
        ]
    },
    {
        "text": "资源",
        "children": [
            "/faq.html",
            "/claude-code-pricing.html",
            "/claude-code-changelog.html",
            "/claude-news.html"
        ]
    },
    {
        "text": "法律条款",
        "children": [
            "/privacy-policy.html",
            "/terms-of-service.html",
            "/disclaimer.html"
        ]
    }
],
    
    sidebarDepth: 3,
    
    editLink: false,
    lastUpdated: true,
    contributors: false
  })
})