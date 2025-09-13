---
title: "Claude Code 更新日志 | Claude Hub"
---

# Claude Code 更新日志 | Claude Hub

Claude Code 发布的完整版本历史，从早期测试版到最新稳定版。每个版本都包含功能添加、错误修复和相关文档链接。 **需要降级？** 请查看我们的 [恢复 Claude Code 版本](/faqs/revert-claude-code-version.html)指南。

* * *

* * *

### v1.0.111[​](#v10111 "直接链接到 v1.0.111")

-   `/model` 现在 验证提供的模型名称
-   修复了 Bash tool 由格式错误的 shell 语法解析引起的崩溃

9月 11, 2025

* * *

### v1.0.110[​](#v10110 "直接链接到 v1.0.110")

-   `/terminal-setup` 命令 现在 supports WezTerm
-   MCP: OAuth tokens 现在 proactively refresh before expiration
-   修复了 reliability issues 后台 Bash 进程

9月 10, 2025

* * *

### v1.0.109[​](#v10109 "直接链接到 v1.0.109")

-   SDK: 添加了 通过以下方式支持部分消息流 --include-partial-messages CLI 标志

9月 10, 2025

* * *

### v1.0.106[​](#v10106 "直接链接到 v1.0.106")

-   Windows: 修复了 路径权限匹配以一致使用 POSIX 格式 (e.g., Read(//c/Users/...))

9月 5, 2025

* * *

### v1.0.97[​](#v1097 "直接链接到 v1.0.97")

-   Settings: `/doctor` 现在 validates permission rule syntax and suggests corrections

8月 29, 2025

* * *

### v1.0.94[​](#v1094 "直接链接到 v1.0.94")

-   Vertex: 为支持的模型添加全局端点支持
-   `/memory` 命令 现在 允许直接编辑所有导入的内存文件
-   SDK: Add custom tools 作为回调
-   添加了 `/todos` 命令 列出当前待办事项

8月 28, 2025

* * *

### v1.0.93[​](#v1093 "直接链接到 v1.0.93")

-   Windows: Add alt + v 从剪贴板粘贴图像的快捷方式
-   支持 NO\_PROXY 环境变量以绕过指定主机名和 IP 的代理

8月 26, 2025

* * *

### v1.0.90[​](#v1090 "直接链接到 v1.0.90")

-   设置文件更改立即生效 - 无需重启

8月 25, 2025

* * *

* * *

### v1.0.88[​](#v1088 "直接链接到 v1.0.88")

-   修复了 issue 导致 "OAuth 身份验证当前不受支持"
-   Status line input 现在 includes `exceeds_200k_tokens`
-   修复了 不正确的使用跟踪在 /cost.
-   引入了 `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_OPUS_MODEL` 用于控制模型别名 opusplan, opus, and sonnet.
-   Bedrock: 更新了 默认 Sonnet 模型为 Sonnet 4

8月 22, 2025

* * *

### v1.0.86[​](#v1086 "直接链接到 v1.0.86")

-   添加了 /context 帮助用户自助调试上下文问题
-   SDK: 添加了 UUID 支持所有 SDK 消息
-   SDK: 添加了 `--replay-user-messages` 将用户消息重放回 stdout

8月 21, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.85[​](#v1085 "直接链接到 v1.0.85")

-   Status line input 现在 includes 会话成本信息

8月 20, 2025

* * *

### v1.0.84[​](#v1084 "直接链接到 v1.0.84")

-   修复 tool\_use/tool\_result 网络不稳定时的 ID 不匹配错误
-   修复 Claude 有时在完成任务时忽略实时引导
-   @-mention: Add ~/.claude/\* files to suggestions for easier agent, output style, and slash 命令 editing
-   默认使用内置 ripgrep; 要退出此行为, set USE\_BUILTIN\_RIPGREP=0

8月 19, 2025

* * *

### v1.0.83[​](#v1083 "直接链接到 v1.0.83")

-   Auto-complete: 允许提及 ~/.claude/\* files
-   新增 闪烁的旋转器

8月 18, 2025

* * *

### v1.0.82[​](#v1082 "直接链接到 v1.0.82")

-   SDK: Add 请求取消支持
-   SDK: 新增 additionalDirectories 搜索自定义路径的选项, improved slash 命令 processing
-   Settings: 验证防止无效字段在 .claude/settings.json files
-   MCP: 改进工具名称一致性
-   Bash: 修复 Claude 尝试自动读取大文件时崩溃

8月 16, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[配置](/configuration.html)|[MCP 服务器](/faqs/what-is-mcp-server-in-claude-code.html)

* * *

### v1.0.81[​](#v1081 "直接链接到 v1.0.81")

-   发布了输出样式, 包括新的内置教育输出样式 "Explanatory" and "Learning"
-   Agents: 修复 代理文件无法解析时的自定义代理加载

8月 14, 2025|另请参阅： [输出样式](https://docs.anthropic.com/en/docs/claude-code-output-styles)

* * *

### v1.0.80[​](#v1080 "直接链接到 v1.0.80")

-   UI 改进: 修复 自定义子代理颜色的文本对比度和旋转器渲染问题

8月 14, 2025

* * *

* * *

### v1.0.77[​](#v1077 "直接链接到 v1.0.77")

-   Bash tool: 修复 heredoc 和多行字符串转义, 改进 stderr 重定向处理
-   SDK: Add 会话支持和权限拒绝跟踪
-   修复 对话总结中的令牌限制错误
-   Opus 计划模式: 新增 setting in `/model` 仅在计划模式下运行 Opus，否则运行 Sonnet

8月 13, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.73[​](#v1073 "直接链接到 v1.0.73")

-   MCP: 支持 multiple config files with `--mcp-config file1.json file2.json`
-   MCP: 按 Esc 取消 OAuth 身份验证流程
-   Bash: 改进了 命令 validation and reduced false security warnings
-   UI: 增强的旋转器动画和状态行视觉层次
-   Linux: 添加了 支持 Alpine 和基于 musl 的发行版 (需要单独安装 ripgrep)

8月 12, 2025|另请参阅： [MCP 服务器](/faqs/what-is-mcp-server-in-claude-code.html)

* * *

### v1.0.72[​](#v1072 "直接链接到 v1.0.72")

-   询问权限: 让 Claude Code 始终要求确认使用特定工具 `/permissions`

8月 12, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.71[​](#v1071 "直接链接到 v1.0.71")

-   Background 命令s: (Ctrl-b) to run any Bash 命令 in the background so Claude can keep working (非常适合开发服务器、跟踪日志等)
-   Customizable status line: add your terminal prompt to Claude Code with `/statusline`

8月 8, 2025|另请参阅： [Background Commands](/faqs/what-are-background-命令s.html)|[Customizable Status Line](/faqs/status-line-claude-code.html)

* * *

### v1.0.70[​](#v1070 "直接链接到 v1.0.70")

-   Performance: Optimized message rendering for better performance with large contexts
-   Windows: 修复了 native file search, ripgrep, and subagent functionality
-   添加了 support for @-mentions in slash 命令 arguments

8月 7, 2025|另请参阅： [Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)|[Custom Agents](/mechanics-custom-agents.html)

* * *

* * *

### v1.0.69[​](#v1069 "直接链接到 v1.0.69")

-   Upgraded Opus to version 4.1

05/08/2025|另请参阅： [Claude 4.1 Opus](/faqs/what-is-claude-4-1-opus.html)

* * *

### v1.0.68[​](#v1068 "直接链接到 v1.0.68")

-   修复 incorrect model names being used for certain 命令s like `/pr-comments`
-   Windows: improve permissions checks for allow / deny tools and project trust. This may create a new project entry in `.claude.json` - manually merge the history field if desired.
-   Windows: improve sub-process spawning to eliminate "No such file or directory" when running 命令s like pnpm
-   Enhanced `/doctor` 命令 with CLAUDE.md and MCP tool context for self-serve debugging
-   SDK: 添加了 canUseTool callback support for tool confirmation
-   添加了 `disableAllHooks` setting
-   改进了 file suggestions performance in large repos

05/08/2025|另请参阅： [Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[Hooks](/mechanics-hooks.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.65[​](#v1065 "直接链接到 v1.0.65")

-   IDE: 修复了 connection stability issues and error handling for diagnostics
-   Windows: 修复了 shell environment setup for users without .bashrc files

01/08/25|另请参阅： [Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)

* * *

### v1.0.64[​](#v1064 "直接链接到 v1.0.64")

-   Agents: 添加了 model customization support - you can 现在 specify which model an agent should use
-   Agents: 修复了 unintended access to the recursive agent tool
-   Hooks: 添加了 systemMessage field to hook JSON output for displaying warnings and context
-   SDK: 修复了 user input tracking across multi-turn conversations
-   添加了 hidden files to file search and @-mention suggestions

July 30, 2025|另请参阅： [Custom Agents](/mechanics-custom-agents.html)|[Hooks](/mechanics-hooks.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.63[​](#v1063 "直接链接到 v1.0.63")

-   Windows: 修复了 file search, @agent mentions, and custom slash 命令s functionality

July 29, 2025|另请参阅： [Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[Custom Agents](/mechanics-custom-agents.html)|[Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)

* * *

### v1.0.62[​](#v1062 "直接链接到 v1.0.62")

-   添加了 @-mention support with typeahead for custom agents. @&lt;your-custom-agent&gt; to invoke it
-   Hooks: 添加了 SessionStart hook for new session initialization
-   /add-dir 命令 现在 supports typeahead for directory paths
-   改进了 network connectivity check reliability

July 28, 2025|另请参阅： [Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.61[​](#v1061 "直接链接到 v1.0.61")

-   Transcript mode (Ctrl+R): Changed Esc to exit transcript mode rather than interrupt
-   Settings: 添加了 `--settings` flag to load settings from a JSON file
-   Settings: 修复了 resolution of settings files paths that are symlinks
-   OTEL: 修复了 reporting of wrong organization after authentication changes
-   Slash 命令s: 修复了 permissions checking for allowed-tools with Bash
-   IDE: 添加了 support for pasting images in VSCode MacOS using ⌘+V
-   IDE: 添加了 `CLAUDE_CODE_AUTO_CONNECT_IDE=false` for disabling IDE auto-connection
-   添加了 `CLAUDE_CODE_SHELL_PREFIX` for wrapping Claude and user-provided shell 命令s run by Claude Code

July 25, 2025|另请参阅： [配置](/configuration.html)|[Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)

* * *

### v1.0.60[​](#v1060 "直接链接到 v1.0.60")

-   You can 现在 create custom subagents for specialized tasks! Run /agents to get started

July 24, 2025|另请参阅： [Task Agent Tools](/mechanics-task-agent-tools.html)|[Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)

* * *

* * *

### v1.0.59[​](#v1059 "直接链接到 v1.0.59")

-   SDK: 添加了 tool confirmation support with canUseTool callback
-   SDK: Allow specifying env for spawned process
-   Hooks: Exposed PermissionDecision to hooks (including "ask")
-   Hooks: UserPromptSubmit 现在 supports additionalContext in advanced JSON output
-   修复了 issue where some Max users that specified Opus would still see fallback to Sonnet

July 23, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.58[​](#v1058 "直接链接到 v1.0.58")

-   添加了 support for reading PDFs
-   MCP: 改进了 server health status display in 'claude mcp list'
-   Hooks: 添加了 CLAUDE\_PROJECT\_DIR env var for hook 命令s

July 23, 2025|另请参阅： [Hooks](/mechanics-hooks.html)|[MCPs](/claude-code-mcps.html)

* * *

### v1.0.57[​](#v1057 "直接链接到 v1.0.57")

-   添加了 support for specifying a model in slash 命令s
-   改进了 permission messages to help Claude understand allowed tools
-   修复: Remove trailing newlines from bash output in terminal wrapping

July 23, 2025|另请参阅： [Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)|[Auto-Accept Permissions](/mechanics-auto-accept-permissions.html)

* * *

### v1.0.56[​](#v1056 "直接链接到 v1.0.56")

-   Windows: Enabled shift+tab for mode switching on versions of Node.js that support terminal VT mode
-   修复es for WSL IDE detection
-   修复 an issue 导致 awsRefreshHelper changes to .aws directory not to be picked up

July 23, 2025|另请参阅： [Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[配置](/configuration.html)

* * *

### v1.0.55[​](#v1055 "直接链接到 v1.0.55")

-   Clarified k现在ledge cutoff for Opus 4 and Sonnet 4 models
-   Windows: fixed Ctrl+Z crash
-   SDK: 添加了 ability to capture error logging
-   Add --system-prompt-file option to override system prompt in print mode

July 23, 2025|另请参阅： [Model Comparison](/model-comparison.html)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.54[​](#v1054 "直接链接到 v1.0.54")

-   Hooks: 添加了 UserPromptSubmit hook and the current working directory to hook inputs
-   Custom slash 命令s: 添加了 argument-hint to frontmatter
-   Windows: OAuth uses port 45454 and properly constructs browser URL
-   Windows: mode switching 现在 uses alt + m, and plan mode renders properly
-   Shell: Switch to in-memory shell snapshot to file-related errors

July 19, 2025|另请参阅： [Hooks](/mechanics-hooks.html)|[Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)

* * *

### v1.0.53[​](#v1053 "直接链接到 v1.0.53")

-   更新了 @-mention file truncation from 100 lines to 2000 lines
-   Add helper script settings for AWS token refresh: awsAuthRefresh (for foreground operations like aws sso login) and awsCredentialExport (for background operation with STS-like response).

July 18, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.52[​](#v1052 "直接链接到 v1.0.52")

-   添加了 support for MCP server instructions

July 18, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.51[​](#v1051 "直接链接到 v1.0.51")

-   添加了 support for native Windows (requires Git for Windows)
-   添加了 support for Bedrock API keys through environment variable AWS\_BEARER\_TOKEN\_BEDROCK
-   Settings: /doctor can 现在 help you identify and fix invalid setting files
-   `--append-system-prompt` can 现在 be used in interactive mode, not just --print/-p.
-   Increased auto-compact warning threshold from 60% to 80%
-   修复了 an issue with handling user directories with spaces for shell snapshots
-   OTEL resource 现在 includes os.type, os.version, host.arch, and wsl.version (if running on Windows Subsystem for Linux)
-   Custom slash 命令s: 修复了 user-level 命令s in subdirectories
-   Plan mode: 修复了 issue where rejected plan from sub-task would get discarded

July 11, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows.html)|[Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)

* * *

* * *

### v1.0.48[​](#v1048 "直接链接到 v1.0.48")

-   修复了 a bug in [v1.0.45](#v1045) where the app would sometimes freeze on launch
-   添加了 progress messages to Bash tool based on the last 5 lines of 命令 output
-   添加了 expanding variables support for MCP server configuration
-   Moved shell snapshots from /tmp to ~/.claude for more reliable Bash tool calls
-   改进了 IDE extension path handling when Claude Code runs in WSL
-   Hooks: 添加了 a PreCompact hook
-   Vim mode: 添加了 c, f/F, t/T

July 10, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.45[​](#v1045 "直接链接到 v1.0.45")

-   Redesigned Search (Grep) tool with new tool input parameters and features
-   Disabled IDE diffs for notebook files, fixing "Timeout waiting after 1000ms" error
-   修复了 config file corruption issue by enforcing atomic writes
-   更新了 prompt input undo to Ctrl+\_ to avoid breaking existing Ctrl+U behavior, matching zsh's undo shortcut
-   Stop Hooks: 修复了 transcript path after /clear and fixed triggering when loop ends with tool call
-   Custom slash 命令s: Restored namespacing in 命令 names based on subdirectories. For example, .claude/frontend/component.md is 现在 /frontend:component, not /component.

July 9, 2025|另请参阅： [Custom Slash Commands](/faqs/what-is-slash-命令s-in-claude-code.html)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.44[​](#v1044 "直接链接到 v1.0.44")

-   新增 `/export` 命令 lets you quickly export a conversation for sharing
-   MCP: resource\_link tool results are 现在 supported
-   MCP: tool annotations and tool titles 现在 display in /mcp view
-   Changed Ctrl+Z to suspend Claude Code. Resume by running `fg`. Prompt input undo is 现在 Ctrl+U.

July 7, 2025|另请参阅： [MCPs](/claude-code-mcps.html)|[Suspend/Resume](/faqs/how-to-suspend-claude-code.html)

* * *

### v1.0.43[​](#v1043 "直接链接到 v1.0.43")

-   修复了 a bug where the theme selector was saving excessively
-   Hooks: 添加了 EPIPE system error handling

July 3, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.42[​](#v1042 "直接链接到 v1.0.42")

-   添加了 tilde (`~`) expansion support to `/add-dir` 命令

July 3, 2025|另请参阅： [/add-dir FAQ](/faqs/--add-dir.html)

* * *

### v1.0.41[​](#v1041 "直接链接到 v1.0.41")

-   Hooks: Split Stop hook triggering into Stop and SubagentStop
-   Hooks: Enabled optional timeout configuration for each 命令
-   Hooks: 添加了 "hook\_event\_name" to hook input
-   修复了 a bug where MCP tools would display twice in tool list
-   新增 tool parameters JSON for Bash tool in `tool_decision` event

另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.40[​](#v1040 "直接链接到 v1.0.40")

-   修复了 a bug 导致 API connection errors with UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY if `NODE_EXTRA_CA_CERTS` was set

* * *

* * *

### v1.0.39[​](#v1039 "直接链接到 v1.0.39")

-   新增 Active Time metric in OpenTelemetry logging

July 2, 2025

* * *

### v1.0.38[​](#v1038 "直接链接到 v1.0.38")

-   Released [hooks](https://docs.anthropic.com/en/docs/claude-code-hooks). Special thanks to community input in [Github Issues](https://github.com/anthropics/claude-code-issues/712)

July 2, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.37[​](#v1037 "直接链接到 v1.0.37")

-   Remove ability to set `Proxy-Authorization` header via ANTHROPIC\_AUTH\_TOKEN or apiKeyHelper

July 2, 2025

* * *

### v1.0.36[​](#v1036 "直接链接到 v1.0.36")

-   Web search 现在 takes today's date into context
-   修复了 a bug where stdio MCP servers were not terminating properly on exit

July 2, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.35[​](#v1035 "直接链接到 v1.0.35")

-   添加了 support for MCP OAuth Authorization Server discovery

June 25, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.34[​](#v1034 "直接链接到 v1.0.34")

-   修复了 a memory leak 导致 a MaxListenersExceededWarning message to appear

June 24, 2025

* * *

### v1.0.33[​](#v1033 "直接链接到 v1.0.33")

-   改进了 logging functionality with session ID support
-   添加了 undo functionality (Ctrl+Z and vim 'u' 命令)
-   Improvements to plan mode

June 24, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)

* * *

### v1.0.32[​](#v1032 "直接链接到 v1.0.32")

-   更新了 loopback config for litellm
-   添加了 forceLoginMethod setting to bypass login selection screen

June 24, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.31[​](#v1031 "直接链接到 v1.0.31")

-   修复了 a bug where ~/.claude.json would get reset when file contained invalid JSON

June 24, 2025

* * *

### v1.0.30[​](#v1030 "直接链接到 v1.0.30")

-   Custom slash 命令s: Run bash output, @-mention files, enable thinking with thinking keywords
-   改进了 file path autocomplete with filename matching
-   添加了 timestamps in Ctrl-r mode and fixed Ctrl-c handling
-   Enhanced jq regex support for complex filters with pipes and select

June 24, 2025|另请参阅： [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令s)

* * *

* * *

### v1.0.29[​](#v1029 "直接链接到 v1.0.29")

-   改进了 CJK character support in cursor navigation and rendering

June 24, 2025

* * *

### v1.0.28[​](#v1028 "直接链接到 v1.0.28")

-   Slash 命令s: 修复 selector display during history navigation
-   Resizes images before upload to prevent API size limit errors
-   添加了 XDG\_CONFIG\_HOME support to configuration directory
-   Performance optimizations for memory usage
-   新增 attributes (terminal.type, language) in OpenTelemetry logging

June 24, 2025|另请参阅： [配置](https://docs.anthropic.com/en/docs/claude-code-settings)

* * *

### v1.0.27[​](#v1027 "直接链接到 v1.0.27")

-   Streamable HTTP MCP servers are 现在 supported
-   Remote MCP servers (SSE and HTTP) 现在 support OAuth
-   MCP resources can 现在 be @-mentioned

June 18, 2025|另请参阅： [MCP Resources](https://docs.anthropic.com/en/docs/claude-code-mcp#use-mcp-resources)

* * *

### v1.0.25[​](#v1025 "直接链接到 v1.0.25")

-   Slash 命令s: moved "project" and "user" prefixes to descriptions
-   Slash 命令s: improved reliability for 命令 discovery
-   改进了 support for Ghostty
-   改进了 web search reliability

June 16, 2025|另请参阅： [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令s)

* * *

### v1.0.24[​](#v1024 "直接链接到 v1.0.24")

-   改进了 `/mcp` output
-   修复了 a bug where settings arrays got overwritten instead of merged

June 16, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.23[​](#v1023 "直接链接到 v1.0.23")

-   Released TypeScript SDK: `import @anthropic-ai/claude-code` to get started
-   Released Python SDK: `pip install claude-code-sdk` to get started

June 16, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.22[​](#v1022 "直接链接到 v1.0.22")

-   SDK: Renamed `total_cost` to `total_cost_usd`

June 12, 2025|另请参阅： [CC Usage](/claude-code-mcps/cc-usage.html)

* * *

### v1.0.21[​](#v1021 "直接链接到 v1.0.21")

-   改进了 editing of files with tab-based indentation
-   修复 for `tool_use` without matching `tool_result` errors
-   修复了 a bug where stdio MCP server processes would linger after quitting Claude Code

June 12, 2025

* * *

* * *

### v1.0.18[​](#v1018 "直接链接到 v1.0.18")

-   添加了 `--add-dir` CLI argument for specifying additional working directories
-   添加了 streaming input support without require `-p` flag
-   改进了 startup performance and session storage performance
-   添加了 `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` environment variable to freeze working directory for bash 命令s
-   添加了 detailed MCP server tools display (`/mcp`)
-   MCP authentication and permission improvements
-   添加了 auto-reconnection for MCP SSE connections on disconnect
-   修复了 issue where pasted content was lost when dialogs appeared

June 10, 2025|另请参阅： [配置](/configuration/#mcp-configuration.html)|[Additional Working Directories](https://docs.anthropic.com/en/docs/claude-code-common-workflows#additional-working-directories)|[MCPs](/claude-code-mcps.html)

* * *

### v1.0.17[​](#v1017 "直接链接到 v1.0.17")

-   We 现在 emit messages from sub-tasks in `-p` mode

June 10, 2025

* * *

### v1.0.16[​](#v1016 "直接链接到 v1.0.16")

-   Additional improvements and bug fixes (look for the `parent_tool_use_id` property)
-   修复了 crashes when the VS Code diff tool is invoked multiple times quickly
-   MCP server list UI 改进
-   Update Claude Code process title to display `claude` instead of `node`

June 6, 2025

* * *

### v1.0.11[​](#v1011 "直接链接到 v1.0.11")

-   Claude Code can 现在 also be used with a Claude Pro subscription
-   添加了 `/upgrade` for smoother switching to Claude Max plans
-   改进了 UI for authentication from API keys and Bedrock/Vertex/external auth tokens
-   改进了 shell configuration error handling
-   改进了 todo list handling during compaction

June 4, 2025|另请参阅： [Pricing](/claude-code-pricing.html)|[Model Comparison](/model-comparison.html)|[Installation](/install-claude-code.html)

* * *

### v1.0.10[​](#v1010 "直接链接到 v1.0.10")

-   添加了 markdown table support
-   改进了 streaming performance

June 3, 2025

* * *

### v1.0.8[​](#v108 "直接链接到 v1.0.8")

-   修复了 Vertex AI region fallback when using `CLOUD_ML_REGION`
-   Increased default otel interval from 1s -> 5s
-   修复了 edge cases where `MCP_TIMEOUT` and `MCP_TOOL_TIMEOUT` weren't being respected
-   修复了 a regression where search tools unnecessarily asked for permissions
-   添加了 support for triggering thinking non-English languages
-   改进了 compacting UI

June 2, 2025|另请参阅： [Restarting Claude Code](/faqs/restarting-claude-code.html)|[Context Window Depletion](/mechanics-context-window-depletion.html)

* * *

### v1.0.7[​](#v107 "直接链接到 v1.0.7")

-   Renamed `/allowed-tools` -> `/permissions`
-   Migrated `allowedTools` and `ignorePatterns` from `.claude.json` -> `settings.json`
-   Deprecated `claude config` 命令s in favor of editing `settings.json`
-   修复了 a bug where `--dangerously-skip-permissions` sometimes didn't work in `--print` mode
-   改进了 error handling for `/install-github-app`
-   Bugfixes, UI polish, and tool reliability improvements

June 2, 2025|另请参阅： [Auto-Accept Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v1.0.6[​](#v106 "直接链接到 v1.0.6")

-   改进了 edit reliability for tab-indented files
-   Respect `CLAUDE_CONFIG_DIR` everywhere
-   Reduced unnecessary tool permission prompts
-   添加了 support for symlinks in `@file` typeahead
-   Bugfixes, UI polish, and tool reliability improvements

June 2, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.4[​](#v104 "直接链接到 v1.0.4")

-   修复了 a bug where MCP tool errors weren't being parsed correctly

5月 28, 2025

* * *

### v1.0.1[​](#v101 "直接链接到 v1.0.1")

-   添加了 `DISABLE_INTERLEAVED_THINKING` to give users the option to opt out of interleaved thinking
-   改进了 model references to show provider-specific names (Sonnet 3.7 for Bedrock, Sonnet 4 for Console)
-   更新了 documentation links and OAuth process descriptions

5月 22, 2025|另请参阅： [配置](/configuration.html)

* * *

* * *

### v1.0.0[​](#v100 "直接链接到 v1.0.0")

-   Claude Code is 现在 generally available
-   Introducing Sonnet 4 and Opus 4 models

5月 22, 2025|另请参阅： [Model Comparison](/model-comparison.html)|[Installation](/install-claude-code.html)|[Getting Started](/claude-code-tutorial.html)

* * *

### v0.2.125[​](#v02125 "直接链接到 v0.2.125")

-   Breaking change: Bedrock ARN passed to `ANTHROPIC_MODEL` or `ANTHROPIC_SMALL_FAST_MODEL` should no longer contain an escaped slash (specify / instead of %2F)
-   Removed `DEBUG=true` in favor of `ANTHROPIC_LOG=debug`, to log all requests

5月 21, 2025|另请参阅： [配置](/configuration.html)

* * *

### v0.2.117[​](#v02117 "直接链接到 v0.2.117")

-   Breaking change: `--print` JSON output 现在 returns nested message objects, for forwards-compatibility as we introduce new metadata fields
-   引入了 `settings.cleanupPeriodDays`
-   引入了 `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` env var
-   引入了 `--debug` mode

5月 18, 2025

* * *

### v0.2.108[​](#v02108 "直接链接到 v0.2.108")

-   You can 现在 send messages to Claude while it works to steer Claude in real-time
-   引入了 `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` env vars
-   修复了 a bug where thinking was not working in `-p` mode
-   修复了 a regression in `/cost` reporting
-   Deprecated MCP wizard interface in favor of other MCP 命令s
-   Lots of other bugfixes and improvements

5月 13, 2025

* * *

### v0.2.107[​](#v02107 "直接链接到 v0.2.107")

-   `CLAUDE.md` files can 现在 import other files. Add `@path/to/file.md` to `./CLAUDE.md` to load additional files on launch

5月 9, 2025|另请参阅： [CLAUDE.md Supremacy](/mechanics-claude-md-supremacy.html)

* * *

### v0.2.106[​](#v02106 "直接链接到 v0.2.106")

-   MCP SSE server configs can 现在 specify custom headers
-   修复了 a bug where MCP permission prompt didn't always show correctly

5月 9, 2025

* * *

### v0.2.105[​](#v02105 "直接链接到 v0.2.105")

-   Claude can 现在 search the web
-   Moved system & account status to `/status`
-   添加了 word movement keybindings for Vim
-   改进了 latency for startup, todo tool, and file edits

5月 8, 2025

* * *

### v0.2.102[​](#v02102 "直接链接到 v0.2.102")

-   改进了 thinking triggering reliability
-   改进了 `@mention` reliability for images and folders
-   You can 现在 paste multiple large chunks into one prompt

5月 5, 2025

* * *

### v0.2.100[​](#v02100 "直接链接到 v0.2.100")

-   修复了 a crash caused by a stack overflow error
-   Made db storage optional; missing db support disables `--continue` and `--resume`

* * *

### v0.2.98[​](#v0298 "直接链接到 v0.2.98")

-   修复了 an issue where auto-compact was running twice

5月 2, 2025

* * *

### v0.2.95[​](#v0295 "直接链接到 v0.2.95")

-   Claude Code can 现在 also be used with a [Claude Max subscription](https://claude.ai/upgrade)
-   Claude Code can 现在 also be used with a [Claude Max subscription](https://claude.ai/upgrade)

5月 1, 2025

* * *

### v0.2.93[​](#v0293 "直接链接到 v0.2.93")

-   Resume conversations from where you left off from with `claude --continue` and `claude --resume`
-   Claude 现在 has access to a Todo list that helps it stay on track and be more organized

April 30, 2025

* * *

### v0.2.82[​](#v0282 "直接链接到 v0.2.82")

-   添加了 support for `--disallowedTools`
-   Renamed tools for consistency: `LSTool` -> `LS`, `View` -> `Read`, etc.

April 25, 2025|另请参阅： [Auto-Accept Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v0.2.75[​](#v0275 "直接链接到 v0.2.75")

-   Hit Enter to queue up additional messages while Claude is working
-   Drag in or copy/paste image files directly into the prompt
-   `@-mention` files to directly add them to context
-   Run one-off MCP servers with `claude --mcp-config &lt;path-to-file&gt;`
-   改进了 performance for filename auto-complete

April 21, 2025|另请参阅： [MCPs & Add-ons](/claude-code-mcps.html)|[配置](/configuration/#mcp-configuration.html)

* * *

### v0.2.7[​](#v027 "直接链接到 v0.2.7")

-   Additional updates and fixes
-   添加了 support for refreshing dynamically generated API keys (via `apiKeyHelper`), with a 5 minute TTL
-   Task tool can 现在 perform writes and run bash 命令s

April 17, 2025

* * *

### v0.2.72[​](#v0272 "直接链接到 v0.2.72")

-   更新了 spinner to indicate tokens loaded and tool usage

April 18, 2025

* * *

### v0.2.70[​](#v0270 "直接链接到 v0.2.70")

-   Network 命令s like `curl` are 现在 available for Claude to use
-   Claude can 现在 run multiple web queries in parallel
-   Pressing ESC once immediately interrupts Claude in Auto-accept mode

* * *

### v0.2.69[​](#v0269 "直接链接到 v0.2.69")

-   修复了 UI glitches with improved Select component behavior
-   Enhanced terminal output display with better text truncation logic

* * *

### v0.2.67[​](#v0267 "直接链接到 v0.2.67")

-   Shared project permission rules can be saved in `.claude/settings.json`

* * *

### v0.2.66[​](#v0266 "直接链接到 v0.2.66")

-   Print mode (`-p`) 现在 supports streaming output via `--output-format=stream-json`
-   修复了 issue where pasting could trigger memory or bash mode unexpectedly

* * *

### v0.2.63[​](#v0263 "直接链接到 v0.2.63")

-   修复了 an issue where MCP tools were loaded twice, which caused tool call errors

* * *

### v0.2.61[​](#v0261 "直接链接到 v0.2.61")

-   Navigate menus with vim-style keys (`j`/`k`) or bash/emacs shortcuts (`Ctrl+n`/`p`) for faster interaction
-   Enhanced image detection for more reliable clipboard paste functionality
-   修复了 an issue where ESC key could crash the conversation history selector

* * *

### v0.2.59[​](#v0259 "直接链接到 v0.2.59")

-   Copy+paste images directly into your prompt
-   改进了 progress indicators for bash and fetch tools
-   Bugfixes for non-interactive mode (`-p`)

* * *

### v0.2.54[​](#v0254 "直接链接到 v0.2.54")

-   Quickly add to Memory by starting your message with `#`
-   Press `ctrl+r` to see full output for long tool results
-   添加了 support for MCP SSE transport

* * *

### v0.2.53[​](#v0253 "直接链接到 v0.2.53")

-   新增 web fetch tool lets Claude view URLs that you paste in
-   修复了 a bug with JPEG detection

* * *

### v0.2.50[​](#v0250 "直接链接到 v0.2.50")

-   新增 MCP "project" scope 现在 allows you to add MCP servers to `.mcp.json` files and commit them to your repository

* * *

### v0.2.49[​](#v0249 "直接链接到 v0.2.49")

-   Previous MCP server scopes have been renamed: previous "project" scope is 现在 "local" and "global" scope is 现在 "user"

* * *

### v0.2.47[​](#v0247 "直接链接到 v0.2.47")

-   Press Tab to auto-complete file and folder names
-   Press Shift + Tab to toggle auto-accept for file edits
-   Automatic conversation compaction for infinite conversation length (toggle with `/config`)

另请参阅： [Auto-Accept Permissions](/mechanics-auto-accept-permissions.html)

* * *

### v0.2.44[​](#v0244 "直接链接到 v0.2.44")

-   Ask Claude to make a plan with thinking mode: just say 'think' or 'think harder' or even 'ultrathink'

* * *

### v0.2.41[​](#v0241 "直接链接到 v0.2.41")

-   MCP server startup timeout can 现在 be configured via `MCP_TIMEOUT` environment variable
-   MCP server startup no longer blocks the app from starting up

* * *

### v0.2.37[​](#v0237 "直接链接到 v0.2.37")

-   新增 `/release-notes` 命令 lets you view release notes at any time
-   `claude config add/remove` 命令s 现在 accept multiple values separated by commas or spaces

* * *

### v0.2.36[​](#v0236 "直接链接到 v0.2.36")

-   Import MCP servers from Claude Desktop with `claude mcp add-from-claude-desktop`
-   Add MCP servers as JSON strings with `claude mcp add-json &lt;n&gt; &lt;json&gt;`

April 21, 2025|另请参阅： [MCPs & Add-ons](/claude-code-mcps.html)|[配置](/configuration/#mcp-configuration.html)

* * *

### v0.2.34[​](#v0234 "直接链接到 v0.2.34")

-   Vim bindings for text input - enable with `/vim` or `/config`

* * *

### v0.2.32[​](#v0232 "直接链接到 v0.2.32")

-   Interactive MCP setup wizard: Run `claude mcp add` to add MCP servers with a step-by-step interface
-   修复 for some PersistentShell issues

* * *

### v0.2.31[​](#v0231 "直接链接到 v0.2.31")

-   Custom slash 命令s: Markdown files in `.claude/命令s/` directories 现在 appear as custom slash 命令s to insert prompts into your conversation
-   MCP debug mode: Run with `--mcp-debug` flag to get more information about MCP server errors

另请参阅： [CLAUDE.md Supremacy](/mechanics-claude-md-supremacy.html) | [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令s)

* * *

### v0.2.30[​](#v0230 "直接链接到 v0.2.30")

-   添加了 ANSI color theme for better terminal compatibility
-   修复了 issue where slash 命令 arguments weren't being sent properly
-   (Mac-only) API keys are 现在 stored in macOS Keychain

* * *

### v0.2.26[​](#v0226 "直接链接到 v0.2.26")

-   新增 `/approved-tools` 命令 for managing tool permissions
-   Word-level diff display for improved code readability
-   Fuzzy matching for slash 命令s

April 21, 2025|另请参阅： [Auto-Accept Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v0.2.21[​](#v0221 "直接链接到 v0.2.21")

-   Fuzzy matching for `/命令s`

* * *

##### Remarkable Progress

It's amazing how far Claude Code has come in such a short period of time. From early beta versions to a comprehensive development platform with MCPs, auto-permissions, plan mode, real-time steering, and sophisticated workflows - the pace of innovation has been extraordinary.

<img src="/img/discovery/023_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

-   [v1.0.111](#v10111)
-   [v1.0.110](#v10110)
-   [v1.0.109](#v10109)
-   [v1.0.106](#v10106)
-   [v1.0.97](#v1097)
-   [v1.0.94](#v1094)
-   [v1.0.93](#v1093)
-   [v1.0.90](#v1090)
-   [v1.0.88](#v1088)
-   [v1.0.86](#v1086)
-   [v1.0.85](#v1085)
-   [v1.0.84](#v1084)
-   [v1.0.83](#v1083)
-   [v1.0.82](#v1082)
-   [v1.0.81](#v1081)
-   [v1.0.80](#v1080)
-   [v1.0.77](#v1077)
-   [v1.0.73](#v1073)
-   [v1.0.72](#v1072)
-   [v1.0.71](#v1071)
-   [v1.0.70](#v1070)
-   [v1.0.69](#v1069)
-   [v1.0.68](#v1068)
-   [v1.0.65](#v1065)
-   [v1.0.64](#v1064)
-   [v1.0.63](#v1063)
-   [v1.0.62](#v1062)
-   [v1.0.61](#v1061)
-   [v1.0.60](#v1060)
-   [v1.0.59](#v1059)
-   [v1.0.58](#v1058)
-   [v1.0.57](#v1057)
-   [v1.0.56](#v1056)
-   [v1.0.55](#v1055)
-   [v1.0.54](#v1054)
-   [v1.0.53](#v1053)
-   [v1.0.52](#v1052)
-   [v1.0.51](#v1051)
-   [v1.0.48](#v1048)
-   [v1.0.45](#v1045)
-   [v1.0.44](#v1044)
-   [v1.0.43](#v1043)
-   [v1.0.42](#v1042)
-   [v1.0.41](#v1041)
-   [v1.0.40](#v1040)
-   [v1.0.39](#v1039)
-   [v1.0.38](#v1038)
-   [v1.0.37](#v1037)
-   [v1.0.36](#v1036)
-   [v1.0.35](#v1035)
-   [v1.0.34](#v1034)
-   [v1.0.33](#v1033)
-   [v1.0.32](#v1032)
-   [v1.0.31](#v1031)
-   [v1.0.30](#v1030)
-   [v1.0.29](#v1029)
-   [v1.0.28](#v1028)
-   [v1.0.27](#v1027)
-   [v1.0.25](#v1025)
-   [v1.0.24](#v1024)
-   [v1.0.23](#v1023)
-   [v1.0.22](#v1022)
-   [v1.0.21](#v1021)
-   [v1.0.18](#v1018)
-   [v1.0.17](#v1017)
-   [v1.0.16](#v1016)
-   [v1.0.11](#v1011)
-   [v1.0.10](#v1010)
-   [v1.0.8](#v108)
-   [v1.0.7](#v107)
-   [v1.0.6](#v106)
-   [v1.0.4](#v104)
-   [v1.0.1](#v101)
-   [v1.0.0](#v100)
-   [v0.2.125](#v02125)
-   [v0.2.117](#v02117)
-   [v0.2.108](#v02108)
-   [v0.2.107](#v02107)
-   [v0.2.106](#v02106)
-   [v0.2.105](#v02105)
-   [v0.2.102](#v02102)
-   [v0.2.100](#v02100)
-   [v0.2.98](#v0298)
-   [v0.2.95](#v0295)
-   [v0.2.93](#v0293)
-   [v0.2.82](#v0282)
-   [v0.2.75](#v0275)
-   [v0.2.7](#v027)
-   [v0.2.72](#v0272)
-   [v0.2.70](#v0270)
-   [v0.2.69](#v0269)
-   [v0.2.67](#v0267)
-   [v0.2.66](#v0266)
-   [v0.2.63](#v0263)
-   [v0.2.61](#v0261)
-   [v0.2.59](#v0259)
-   [v0.2.54](#v0254)
-   [v0.2.53](#v0253)
-   [v0.2.50](#v0250)
-   [v0.2.49](#v0249)
-   [v0.2.47](#v0247)
-   [v0.2.44](#v0244)
-   [v0.2.41](#v0241)
-   [v0.2.37](#v0237)
-   [v0.2.36](#v0236)
-   [v0.2.34](#v0234)
-   [v0.2.32](#v0232)
-   [v0.2.31](#v0231)
-   [v0.2.30](#v0230)
-   [v0.2.26](#v0226)
-   [v0.2.21](#v0221)