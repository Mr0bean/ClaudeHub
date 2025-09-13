#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Detailed fix for claude-code-changelog.md translation issues
Fix all the specific mixed language problems
"""

import re

def detailed_changelog_fix():
    """Fix all the detailed mixed language issues in changelog"""
    
    with open('final-site/docs/claude-code-changelog.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix title and header issues
    content = content.replace('ClaudeCode更新日志 | ClaudeHub', 'Claude Code 更新日志 | Claude Hub')
    content = content.replace('# ClaudeCode更新日志 | ClaudeHub', '# Claude Code 更新日志 | Claude Hub')
    content = content.replace('ClaudeCode发布的完整版本历史', 'Claude Code 发布的完整版本历史')
    content = content.replace('恢复ClaudeCode版本', '恢复 Claude Code 版本')
    
    # Fix specific problematic entries
    specific_fixes = {
        # Line 118-122 issues
        '修复工具\_use/工具\_result网络不稳定时的ID不匹配错误': '修复了网络不稳定时 tool_use/tool_result 的 ID 不匹配错误',
        '修复Claude有时在完成任务时忽略实时引导': '修复了 Claude 有时在完成任务时忽略实时引导的问题',
        '@-mention: Add ~/.claude/\\* filestosuggestionsforeasieragent, outputstyle, andslash命令editing': '@-mention: 为更容易的代理、输出样式和 slash 命令编辑添加了 ~/.claude/* 文件建议',
        '默认使用内置ripgrep; 要退出此行为, setUSE\_BUILTIN\_RIPGREP=0': '默认使用内置 ripgrep；要退出此行为，设置 USE_BUILTIN_RIPGREP=0',
        
        # Line 129-130 issues  
        'Auto-complete: 允许提及 ~/.claude/\\* files': '自动补全：允许提及 ~/.claude/* 文件',
        '新增闪烁的旋转器': '新增了闪烁的旋转器',
        
        # Line 139 issue
        'SDK: 新增了添加itionalDirectories搜索自定义路径的选项，改进了slash命令处理': 'SDK: 新增了 additionalDirectories 搜索自定义路径的选项，改进了 slash 命令处理',
        
        # Line 150-152 issues
        '发布了输出样式, 包括新的内置教育输出样式 "Explanatory" and "Learning"': '发布了输出样式，包括新的内置教育输出样式 "Explanatory" 和 "Learning"',
        '修复代理文件无法解析时的自定义代理加载': '修复了代理文件无法解析时的自定义代理加载',
        
        # Line 169-173 issues
        'Bash工具: 修复heredoc和多行字符串转义, 改进stderr重定向处理': 'Bash 工具：修复了 heredoc 和多行字符串转义，改进了 stderr 重定向处理',
        'SDK: Add会话支持和权限拒绝跟踪': 'SDK: 添加了会话支持和权限拒绝跟踪',
        '修复对话总结中的令牌限制错误': '修复了对话总结中的令牌限制错误',
        'Opus计划模式: 新增settingin `/model` 仅在计划模式下运行Opus，否则运行Sonnet': 'Opus 计划模式：在 `/model` 中新增设置，仅在计划模式下运行 Opus，否则运行 Sonnet',
        
        # Line 180 issue
        'MCP: 支持通过 `--mcp-configfile1.jsonfile2.json` 使用多个配置文件': 'MCP: 支持通过 `--mcp-config file1.json file2.json` 使用多个配置文件',
        
        # Line 192 issue
        '询问权限：让ClaudeCode始终要求确认使用特定工具 `/permissions`': '询问权限：让 Claude Code 始终要求确认使用特定工具 `/permissions`',
        
        # Line 201 issue
        '可自定义状态行：使用 `/statusline` 将您的终端提示符添加到ClaudeCode': '可自定义状态行：使用 `/statusline` 将您的终端提示符添加到 Claude Code',
        
        # Line 203 issue
        '[BackgroundCommands](/faqs/what-are-background-命令.html)': '[后台命令](/faqs/what-are-background-commands.html)',
        '[CustomizableStatusLine](/faqs/status-line-claude-code.html)': '[可自定义状态行](/faqs/status-line-claude-code.html)',
        
        # Line 209 issue
        'Performance: Optimizedmessagerenderingforbetterperformancewithlargecontexts': '性能：优化了消息渲染以在大上下文中获得更好的性能',
        
        # Line 213 issue
        '[WindowsInstallation](/faqs/how-to-install-claude-code-on-windows.html)': '[Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)',
        '[CustomSlashCommands](/faqs/what-is-slash-命令-in-claude-code.html)': '[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)',
        '[CustomAgents](/mechanics-custom-agents.html)': '[自定义代理](/mechanics-custom-agents.html)',
        
        # Line 221 issue
        'UpgradedOpustoversion4.1': '升级了 Opus 到版本 4.1',
        
        # Line 223 issue
        '[Claude4.1Opus](/faqs/what-is-claude-4-1-opus.html)': '[Claude 4.1 Opus](/faqs/what-is-claude-4-1-opus.html)',
        
        # Line 230-231 issues
        '. Thismaycreatea newprojectentryin `.claude.json` - manuallymergethehistoryfieldifdesired.': '。这可能会在 `.claude.json` 中创建新的项目条目 - 如果需要，请手动合并历史字段。',
        '改进了子进程生成，消除了运行pnpm等命令时的"Nosuchfileordirectory"错误': '改进了子进程生成，消除了运行 pnpm 等命令时的 "No such file or directory" 错误',
        
        # Line 232 issue
        '增强了 `/doctor` 命令，添加了CLAUDE.md和 MCP工具上下文以供自助调试': '增强了 `/doctor` 命令，添加了 CLAUDE.md 和 MCP 工具上下文以供自助调试',
        
        # Line 233-234 issues
        'SDK: 添加了canUseTool回调支持以进行工具确认': 'SDK: 添加了 canUseTool 回调支持以进行工具确认',
        '添加了 `disableAllHooks` setting': '添加了 `disableAllHooks` 设置',
        
        # Line 237 issue
        '[ClaudeCodeSDK](https://docs.anthropic.com/en/docs/claude-code-sdk)': '[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)',
        
        # Line 244 issue
        '修复了没有 .bashrc文件用户的shell环境设置': '修复了没有 .bashrc 文件用户的 shell 环境设置',
        
        # Many more similar fixes needed...
        'ClaudeCode始终要求': 'Claude Code 始终要求',
        'ClaudeCode可以继续工作': 'Claude Code 可以继续工作',
        'ClaudeCode': 'Claude Code',
        
        # Fix URLs and references
        'background-命令': 'background-commands',
        'slash-命令-in-claude-code': 'slash-commands-in-claude-code',
        'what-are-background-命令': 'what-are-background-commands',
        
        # Fix spacing issues
        '添加了 /context帮助用户': '添加了 /context 帮助用户',
        'Statusline输入现在': 'Status line 输入现在',
        '8月21, 2025': '8月 21, 2025',
        '8月20, 2025': '8月 20, 2025',
        '8月19, 2025': '8月 19, 2025',
        '8月18, 2025': '8月 18, 2025',
        '8月16, 2025': '8月 16, 2025',
        '8月14, 2025': '8月 14, 2025',
        '8月13, 2025': '8月 13, 2025',
        '8月12, 2025': '8月 12, 2025',
        '8月8, 2025': '8月 8, 2025',
        '8月7, 2025': '8月 7, 2025',
        
        # Fix mixed language phrases throughout
        'files': '文件',
        'setting': '设置',
        'settings': '设置',
        'output': '输出',
        'input': '输入',
        'support': '支持',
        'supported': '支持',
        'command': '命令',
        'commands': '命令',
        'tool': '工具',
        'tools': '工具',
        'added': '添加了',
        'fixed': '修复了',
        'improved': '改进了',
        'updated': '更新了',
        'enabled': '启用了',
        'disabled': '禁用了',
        'removed': '移除了',
        
        # Fix technical terms
        'ripgrep': 'ripgrep',
        'SDK': 'SDK',
        'MCP': 'MCP',
        'API': 'API',
        'UI': 'UI',
        'CLI': 'CLI',
        'JSON': 'JSON',
        'OAuth': 'OAuth',
        'SSL': 'SSL',
        'HTTP': 'HTTP',
        'HTTPS': 'HTTPS',
        'URL': 'URL',
        'UUID': 'UUID',
        'TTL': 'TTL',
        'IDE': 'IDE',
        
        # Fix status line references  
        'Statusline': 'Status line'
    }
    
    # Apply all specific fixes
    for en_text, zh_text in specific_fixes.items():
        content = content.replace(en_text, zh_text)
    
    # Pattern-based fixes for common issues
    # Fix broken English words mixed in Chinese
    content = re.sub(r'(\w+)([a-z])([A-Z])([a-z]+)', r'\1 \2\3\4', content)
    content = re.sub(r'([a-z]+)([A-Z][a-z]+)', r'\1 \2', content)
    
    # Fix specific broken word patterns
    content = re.sub(r'添加itional', '额外的', content)
    content = re.sub(r'改进ments', '改进', content)
    content = re.sub(r'问题s', '问题', content)
    content = re.sub(r'错误s', '错误', content)
    content = re.sub(r'修复es', '修复', content)
    content = re.sub(r'工具s', '工具', content)
    content = re.sub(r'命令s', '命令', content)
    content = re.sub(r'文件s', '文件', content)
    
    # Fix concatenated words
    content = re.sub(r'([a-z]+)([A-Z][a-z]*)', r'\1 \2', content)
    content = re.sub(r'([a-z])([A-Z])', r'\1 \2', content)
    
    # Fix dates
    content = re.sub(r'(\d+月)(\d+),', r'\1 \2,', content)
    
    # Fix spacing around punctuation
    content = re.sub(r'([^\\])_([^\\])', r'\1\_\2', content)  # Fix unescaped underscores
    content = re.sub(r'\\\\(.)', r'\\\1', content)  # Fix double backslashes
    
    with open('final-site/docs/claude-code-changelog.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Applied detailed changelog translation fixes")
    print("📄 File saved: final-site/docs/claude-code-changelog.md")

if __name__ == "__main__":
    detailed_changelog_fix()