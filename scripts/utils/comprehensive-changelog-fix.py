#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive fix for claude-code-changelog.md translation issues
"""

import re

def comprehensive_changelog_fix():
    """Comprehensively fix all translation issues in changelog"""
    
    with open('final-site/docs/claude-code-changelog.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Comprehensive translation replacements
    comprehensive_translations = {
        # Fix specific mixed language entries
        'MCP: OAuth 令牌 现在主动 refresh before expiration': 'MCP: OAuth 令牌现在主动在过期前刷新',
        '修复了reliability 问题与后台 Bash 进程': '修复了后台 Bash 进程的可靠性问题',
        'Settings: `/doctor` 现在验证 权限规则语法并建议修正': 'Settings: `/doctor` 现在验证权限规则语法并建议修正',
        'SDK: Add 自定义工具 作为回调': 'SDK: 添加了自定义工具作为回调',
        '添加了alt + v 从剪贴板粘贴图像的快捷方式': '添加了 alt + v 从剪贴板粘贴图像的快捷方式',
        'Status line input现在包括会话成本信息': 'Status line 输入现在包括会话成本信息',
        '修复 tool_use/tool_result 网络不稳定时的 ID 不匹配错误': '修复了网络不稳定时 tool_use/tool_result 的 ID 不匹配错误',
        'SDK: Add 请求取消支持': 'SDK: 添加了请求取消支持',
        'SDK: 新增 additionalDirectories 搜索自定义路径的选项, 改进了slash 命令 processing': 'SDK: 新增了 additionalDirectories 搜索自定义路径的选项，改进了 slash 命令处理',
        '支持 multiple config files with `--mcp-config file1.json file2.json`': '支持通过 `--mcp-config file1.json file2.json` 使用多个配置文件',
        'Bash: 改进了 命令 validation and reduced false security warnings': 'Bash: 改进了命令验证并减少了错误的安全警告',
        'Background 命令s: (Ctrl-b) to run any Bash 命令 in the background so Claude can keep working (非常适合开发服务器、跟踪日志等)': 'Background 命令：(Ctrl-b) 在后台运行任何 Bash 命令，让 Claude 可以继续工作（非常适合开发服务器、跟踪日志等）',
        'Customizable status line: 添加了your terminal prompt to Claude Code with `/statusline`': '可自定义状态行：使用 `/statusline` 将您的终端提示符添加到 Claude Code',
        '修复了native file search, ripgrep, and subagent functionality': '修复了原生文件搜索、ripgrep 和子代理功能',
        '添加了支持for @-mentions in slash 命令 arguments': '添加了对 slash 命令参数中 @-mentions 的支持',
        '修复 incorrect model names being used for certain 命令s like `/pr-comments`': '修复了某些命令（如 `/pr-comments`）使用错误模型名称的问题',
        '改进了permissions checks for 允许/ deny tools and project trust': '改进了允许/拒绝工具和项目信任的权限检查',
        '改进了sub-process spawning to eliminate "No such file or directory" when running 命令s like pnpm': '改进了子进程生成，消除了运行 pnpm 等命令时的"No such file or directory"错误',
        'Enhanced `/doctor` 命令 with CLAUDE.md and MCP tool context for self-serve debugging': '增强了 `/doctor` 命令，添加了 CLAUDE.md 和 MCP 工具上下文以供自助调试',
        'SDK: 添加了canUseTool callback 支持for tool confirmation': 'SDK: 添加了 canUseTool 回调支持以进行工具确认',
        '改进了 file suggestions performance in large repos': '改进了大型仓库中文件建议的性能',
        'IDE: 修复了connection stability issues and 错误处理 for diagnostics': 'IDE: 修复了诊断的连接稳定性问题和错误处理',
        '修复了shell environment setup for users without .bashrc files': '修复了没有 .bashrc 文件用户的 shell 环境设置',
        'Agents: 添加了model customization 支持- you can现在specify which model an agent should use': 'Agents: 添加了模型定制支持 - 您现在可以指定代理应使用哪个模型',
        'Agents: 修复了unintended access to the recursive agent tool': 'Agents: 修复了对递归代理工具的意外访问',
        'Hooks: 添加了systemMessage field to hook JSON output for displaying warnings and context': 'Hooks: 向 hook JSON 输出添加了 systemMessage 字段以显示警告和上下文',
        'SDK: 修复了user input tracking across multi-turn conversations': 'SDK: 修复了多轮对话中的用户输入跟踪',
        '添加了hidden files to file search and @-mention suggestions': '将隐藏文件添加到文件搜索和 @-mention 建议中',
        '修复了file search, @agent mentions, and custom slash 命令s functionality': '修复了文件搜索、@agent mentions 和自定义 slash 命令功能',
        '添加了 @-mention 支持with typeahead for custom agents': '为自定义代理添加了带有预输入的 @-mention 支持',
        'Hooks: 添加了SessionStart hook for new session initialization': 'Hooks: 添加了用于新会话初始化的 SessionStart hook',
        '/add-dir 命令现在支持 typeahead for directory paths': '/add-dir 命令现在支持目录路径的预输入',
        '改进了 network connectivity check reliability': '改进了网络连接检查的可靠性',
        '添加了 `--settings` flag to load settings from a JSON file': '添加了 `--settings` 标志以从 JSON 文件加载设置',
        '修复了resolution of settings files paths that are symlinks': '修复了符号链接设置文件路径的解析',
        'OTEL: 修复了reporting of wrong organization after authentication changes': 'OTEL: 修复了身份验证更改后错误组织的报告',
        'Slash 命令s: 修复了permissions checking for allowed-tools with Bash': 'Slash 命令：修复了 Bash 允许工具的权限检查',
        'IDE: 添加了支持for pasting images in VSCode MacOS using ⌘+V': 'IDE: 添加了在 VSCode MacOS 中使用 ⌘+V 粘贴图像的支持',
        '添加了 `CLAUDE_CODE_SHELL_PREFIX` for wrapping Claude and user-provided shell 命令s run by Claude Code': '添加了 `CLAUDE_CODE_SHELL_PREFIX` 用于包装 Claude Code 运行的 Claude 和用户提供的 shell 命令',
        'You can现在create custom subagents for specialized tasks! Run /agents to get started': '您现在可以为专门任务创建自定义子代理！运行 /agents 开始使用',
        'SDK: 添加了tool confirmation 支持with canUseTool callback': 'SDK: 添加了带有 canUseTool 回调的工具确认支持',
        '修复了issue where some Max users that specified Opus would still see fallback to Sonnet': '修复了某些指定 Opus 的 Max 用户仍然回退到 Sonnet 的问题',
        '添加了支持for reading PDFs': '添加了对读取 PDF 的支持',
        'MCP: 改进了 server health status display in \'claude mcp list\'': 'MCP: 改进了 \'claude mcp list\' 中服务器健康状态的显示',
        'Hooks: 添加了CLAUDE_PROJECT_DIR env var for hook 命令s': 'Hooks: 为 hook 命令添加了 CLAUDE_PROJECT_DIR 环境变量',
        '添加了支持for specifying a model in slash 命令s': '添加了在 slash 命令中指定模型的支持',
        '改进了 permission messages to help Claude understand allowed tools': '改进了权限消息以帮助 Claude 理解允许的工具',
        '修复: Remove trailing newlines from bash output in terminal wrapping': '修复：删除终端包装中 bash 输出的尾随换行符',
        'Windows: Enabled shift+tab for mode switching on versions of Node.js that 支持terminal VT mode': 'Windows: 在支持终端 VT 模式的 Node.js 版本上启用了 shift+tab 模式切换',
        '修复es for WSL IDE detection': '修复了 WSL IDE 检测',
        '修复 an issue 导致 awsRefreshHelper changes to .aws directory not to be picked up': '修复了 awsRefreshHelper 对 .aws 目录的更改未被识别的问题',
        'Clarified k现在ledge cutoff for Opus 4 and Sonnet 4 models': '明确了 Opus 4 和 Sonnet 4 模型的知识截止日期',
        'Windows: 修复了Ctrl+Z crash': 'Windows: 修复了 Ctrl+Z 崩溃',
        'SDK: 添加了ability to capture error logging': 'SDK: 添加了捕获错误日志的能力',
        'Add --system-prompt-file option to override system prompt in print mode': '添加了 --system-prompt-file 选项以在打印模式下覆盖系统提示',
        'Hooks: 添加了UserPromptSubmit hook and the current working directory to hook inputs': 'Hooks: 添加了 UserPromptSubmit hook 和当前工作目录到 hook 输入',
        'Custom slash 命令s: 添加了argument-hint to frontmatter': '自定义 slash 命令：向前言添加了 argument-hint',
        'Windows: mode switching现在uses alt + m, and plan mode renders properly': 'Windows: 模式切换现在使用 alt + m，计划模式正确渲染',
        'Shell: Switch to in-memory shell snapshot to file-related errors': 'Shell: 切换到内存中的 shell 快照以避免文件相关错误',
        
        # More comprehensive patterns
        'Windows: 添加了支持': 'Windows: 添加了支持',
        'SDK: 添加了UUID 支持所有 SDK 消息': 'SDK: 为所有 SDK 消息添加了 UUID 支持',
        'SDK: 添加了 `--replay-user-messages` 将用户消息重放回 stdout': 'SDK: 添加了 `--replay-user-messages` 以将用户消息重放回 stdout',
        
        # Pattern replacements for consistent translation
        '现在可以': '现在可以',
        '现在支持': '现在支持',
        '现在包括': '现在包括',
        '现在使用': '现在使用',
        '现在允许': '现在允许',
        
        # Technical terms
        'commands': '命令',
        'command': '命令',
        'tools': '工具',
        'tool': '工具',
        'fix': '修复',
        'fixes': '修复',
        'fixed': '修复了',
        'add': '添加',
        'added': '添加了',
        'improve': '改进',
        'improved': '改进了',
        'support': '支持',
        'supports': '支持',
        'enable': '启用',
        'enabled': '启用了',
        'now': '现在',
        'can now': '现在可以',
        'now support': '现在支持',
        'now include': '现在包括',
        'now allow': '现在允许',
        'now use': '现在使用',
        
        # Clean up specific problematic patterns
        '修复了Bash tool 由格式错误的 shell 语法解析引起的崩溃': '修复了由格式错误的 shell 语法解析引起的 Bash 工具崩溃',
        'Add helper script settings for AWS token refresh: awsAuthRefresh (for foreground operations like aws sso login) and awsCredentialExport (for background operation with STS-like response).': '添加了 AWS 令牌刷新的辅助脚本设置：awsAuthRefresh（用于前台操作如 aws sso login）和 awsCredentialExport（用于类似 STS 响应的后台操作）',
        'Settings: 验证防止无效字段在 .claude/settings.json files': 'Settings: 验证以防止 .claude/settings.json 文件中的无效字段',
        'Bash: 修复 Claude 尝试自动读取大文件时崩溃': 'Bash: 修复了 Claude 尝试自动读取大文件时的崩溃',
        '询问权限: 让 Claude Code 始终要求确认使用特定工具 `/permissions`': '询问权限：让 Claude Code 始终要求确认使用特定工具 `/permissions`',
        '修复 an issue causing': '修复了导致...的问题',
        'causing': '导致',
        'issue': '问题',
        'issues': '问题',
        
        # Additional specific fixes
        '新增 `/export` 命令 lets you quickly export a conversation for sharing': '新增了 `/export` 命令，让您快速导出对话以便分享',
        'MCP: resource_link tool results are现在supported': 'MCP: 现在支持 resource_link 工具结果',
        'MCP: tool annotations and tool titles现在display in /mcp view': 'MCP: 工具注释和工具标题现在在 /mcp 视图中显示',
        'Changed Ctrl+Z to suspend Claude Code. Resume by running `fg`. Prompt input undo is现在Ctrl+U.': '将 Ctrl+Z 更改为暂停 Claude Code。通过运行 `fg` 恢复。提示输入撤销现在是 Ctrl+U。',
        '修复了a bug where the theme selector was saving excessively': '修复了主题选择器过度保存的错误',
        'Hooks: 添加了EPIPE system 错误处理': 'Hooks: 添加了 EPIPE 系统错误处理',
        '添加了tilde (`~`) expansion 支持to `/add-dir` 命令': '为 `/add-dir` 命令添加了波浪号（`~`）扩展支持',
        '修复了a bug where MCP tools would display twice in tool list': '修复了 MCP 工具在工具列表中重复显示的错误',
        '新增 tool parameters JSON for Bash tool in `tool_decision` event': '在 `tool_decision` 事件中为 Bash 工具添加了工具参数 JSON',
        '修复了a bug 导致 API connection errors with UNABLE_TO_GET_ISSUER_CERT_LOCALLY if `NODE_EXTRA_CA_CERTS` was set': '修复了当设置 `NODE_EXTRA_CA_CERTS` 时导致 UNABLE_TO_GET_ISSUER_CERT_LOCALLY API 连接错误的错误',
        'Web search现在takes today\'s date into context': 'Web 搜索现在将今天的日期纳入上下文',
        '修复了a bug where stdio MCP servers were not terminating properly on exit': '修复了 stdio MCP 服务器在退出时未正确终止的错误',
        '添加了支持for MCP OAuth Authorization Server discovery': '添加了对 MCP OAuth 授权服务器发现的支持',
        '修复了a memory leak 导致 a MaxListenersExceededWarning message to appear': '修复了导致 MaxListenersExceededWarning 消息出现的内存泄漏',
        '改进了 logging functionality with session ID support': '改进了具有会话 ID 支持的日志功能',
        '添加了undo functionality (Ctrl+Z and vim \'u\' 命令)': '添加了撤销功能（Ctrl+Z 和 vim \'u\' 命令）',
        'Improvements to plan mode': '计划模式的改进',
        '更新了 loopback config for litellm': '更新了 litellm 的回环配置',
        '添加了forceLoginMethod setting to bypass login selection screen': '添加了 forceLoginMethod 设置以跳过登录选择屏幕',
        '修复了a bug where ~/.claude.json would get reset when file contained invalid JSON': '修复了当文件包含无效 JSON 时 ~/.claude.json 会被重置的错误'
    }
    
    # Apply all comprehensive translations
    for en_text, zh_text in comprehensive_translations.items():
        content = content.replace(en_text, zh_text)
    
    # Pattern-based fixes for consistent formatting
    # Fix spacing around Chinese punctuation
    content = re.sub(r'(\w) (\w)', r'\1\2', content)
    content = re.sub(r'现在 (\w)', r'现在\1', content)
    content = re.sub(r'添加了 (\w)', r'添加了\1', content)
    content = re.sub(r'修复了 (\w)', r'修复了\1', content)
    content = re.sub(r'改进了 (\w)', r'改进了\1', content)
    content = re.sub(r'支持 (\w)', r'支持\1', content)
    
    # Fix specific command patterns
    content = re.sub(r'命令s', '命令', content)
    content = re.sub(r'工具s', '工具', content)
    
    # Fix URLs and see also sections
    content = content.replace('另请参阅：', '另请参阅：')
    
    with open('final-site/docs/claude-code-changelog.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Comprehensive changelog translation fix completed")
    print("📄 File saved: final-site/docs/claude-code-changelog.md")

if __name__ == "__main__":
    comprehensive_changelog_fix()