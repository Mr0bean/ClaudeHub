#!/usr/bin/env python3
import re

def translate_changelog():
    file_path = 'final-site/docs/claude-code-changelog.md'
    
    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate main content
    translations = {
        # Header and intro
        'title: "Claude Code Changelog | Claude Hub"': 'title: "Claude Code 更新日志 | Claude Hub"',
        '# Claude Code Changelog | Claude Hub': '# Claude Code 更新日志 | Claude Hub',
        'Complete version history of Claude Code releases, from early beta versions to the latest stable release. Each version includes feature additions, bug fixes, and links to relevant documentation.': 'Claude Code 发布的完整版本历史，从早期测试版到最新稳定版。每个版本都包含功能添加、错误修复和相关文档链接。',
        '**Need to downgrade?**': '**需要降级？**',
        'See our': '请查看我们的',
        'Revert Claude Code Version': '恢复 Claude Code 版本',
        ' guide.': '指南。',
        
        # Common terms
        'Direct link to': '直接链接到',
        'See Also:': '另请参阅：',
        
        # Dates (months)
        'Sep ': '9月 ',
        'Aug ': '8月 ',
        'Jul ': '7月 ',
        'Jun ': '6月 ',
        'May ': '5月 ',
        'Apr ': '4月 ',
        'Mar ': '3月 ',
        'Feb ': '2月 ',
        'Jan ': '1月 ',
        'Dec ': '12月 ',
        'Nov ': '11月 ',
        'Oct ': '10月 ',
        
        # Common changelog entries
        'Fixed': '修复了',
        'Added': '添加了',
        'Improved': '改进了',
        'Updated': '更新了',
        'Support': '支持',
        'New': '新增',
        'Fix': '修复',
        'now': '现在',
        'command': '命令',
        'Fixed issue': '修复了问题',
        'Fixed reliability issues': '修复了可靠性问题',
        
        # Specific features and tools
        'validates provided model names': '验证提供的模型名称',
        'crashes caused by malformed shell syntax parsing': '由格式错误的 shell 语法解析引起的崩溃',
        'now supports': '现在支持',
        'OAuth tokens now proactively refresh before expiration': 'OAuth 令牌现在会在过期前主动刷新',
        'with background Bash processes': '后台 Bash 进程',
        'partial message streaming support via': '通过以下方式支持部分消息流',
        'CLI flag': 'CLI 标志',
        'path permission matching to consistently use POSIX format': '路径权限匹配以一致使用 POSIX 格式',
        'now validates permission rule syntax and suggests corrections': '现在验证权限规则语法并提出修正建议',
        'add support for global endpoints for supported models': '为支持的模型添加全局端点支持',
        'allows direct editing of all imported memory files': '允许直接编辑所有导入的内存文件',
        'as callbacks': '作为回调',
        'to list current todo items': '列出当前待办事项',
        'shortcut for pasting images from clipboard': '从剪贴板粘贴图像的快捷方式',
        'environment variable to bypass proxy for specified hostnames and IPs': '环境变量以绕过指定主机名和 IP 的代理',
        'Settings file changes take effect immediately - no restart required': '设置文件更改立即生效 - 无需重启',
        'causing': '导致',
        'OAuth authentication is currently not supported': 'OAuth 身份验证当前不受支持',
        'Status line input now includes': '状态行输入现在包括',
        'incorrect usage tracking in': '不正确的使用跟踪在',
        'Introduced': '引入了',
        'for controlling model aliases': '用于控制模型别名',
        'default Sonnet model to Sonnet 4': '默认 Sonnet 模型为 Sonnet 4',
        'to help users self-serve debug context issues': '帮助用户自助调试上下文问题',
        'support for all SDK messages': '支持所有 SDK 消息',
        'to replay user messages back to stdout': '将用户消息重放回 stdout',
        'session cost info': '会话成本信息',
        'id mismatch error when network is unstable': '网络不稳定时的 ID 不匹配错误',
        'sometimes ignoring real-time steering when wrapping up a task': '有时在完成任务时忽略实时引导',
        'files to suggestions for easier agent, output style, and slash command editing': '文件到建议，以便更轻松地编辑代理、输出样式和斜杠命令',
        'Use built-in ripgrep by default': '默认使用内置 ripgrep',
        'to opt out of this behavior': '要退出此行为',
        'allow mentioning': '允许提及',
        'shimmering spinner': '闪烁的旋转器',
        'request cancellation support': '请求取消支持',
        'option to search custom paths': '搜索自定义路径的选项',
        'improved slash command processing': '改进的斜杠命令处理',
        'Validation prevents invalid fields in': '验证防止无效字段在',
        'Improve tool name consistency': '改进工具名称一致性',
        'crash when Claude tries to automatically read large files': 'Claude 尝试自动读取大文件时崩溃',
        'Released output styles': '发布了输出样式',
        'including new built-in educational output styles': '包括新的内置教育输出样式',
        'custom agent loading when agent files are unparsable': '代理文件无法解析时的自定义代理加载',
        'UI improvements': 'UI 改进',
        'text contrast for custom subagent colors and spinner rendering issues': '自定义子代理颜色的文本对比度和旋转器渲染问题',
        'heredoc and multiline string escaping': 'heredoc 和多行字符串转义',
        'improve stderr redirection handling': '改进 stderr 重定向处理',
        'session support and permission denial tracking': '会话支持和权限拒绝跟踪',
        'token limit errors in conversation summarization': '对话总结中的令牌限制错误',
        'New setting in': '新设置在',
        'to run Opus only in plan mode, Sonnet otherwise': '仅在计划模式下运行 Opus，否则运行 Sonnet',
        'Support multiple config files with': '支持多个配置文件',
        'Press Esc to cancel OAuth authentication flows': '按 Esc 取消 OAuth 身份验证流程',
        'Improved command validation and reduced false security warnings': '改进的命令验证和减少误报安全警告',
        'Enhanced spinner animations and status line visual hierarchy': '增强的旋转器动画和状态行视觉层次',
        'support for Alpine and musl-based distributions': '支持 Alpine 和基于 musl 的发行版',
        'requires separate ripgrep installation': '需要单独安装 ripgrep',
        'Ask permissions': '询问权限',
        'have Claude Code always ask for confirmation to use specific tools with': '让 Claude Code 始终要求确认使用特定工具',
        'Background commands': '后台命令',
        'to run any Bash command in the background so Claude can keep working': '在后台运行任何 Bash 命令，以便 Claude 可以继续工作',
        'great for dev servers, tailing logs, etc.': '非常适合开发服务器、跟踪日志等',
        
        # Links
        'Claude Code SDK': 'Claude Code SDK',
        'Configuration': '配置',
        'MCP Servers': 'MCP 服务器',
        'Plan Mode': '计划模式',
        'Output Styles': '输出样式',
    }
    
    # Apply translations
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated changelog: {file_path}")

if __name__ == "__main__":
    translate_changelog()