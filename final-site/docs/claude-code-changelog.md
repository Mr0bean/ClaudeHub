---
title: "Claude Code 更新日志 | Claude Hub"
---

# Claude Code 更新日志 | Claude Hub

Claude Code 发布的完整版本历史，从早期测试版到最新稳定版。每个版本都包含功能添加、错误修复和相关文档链接。 **需要降级？** 请查看我们的 [恢复 Claude Code 版本](/faqs/revert-claude-code-version.html)指南。

* * *

* * *

### v1.0.111[​](#v10111 "直接链接到v1.0.111")

-   `/model` 现在验证提供的模型名称
-   修复了 Bash 工具由格式错误的 shell 语法解析引起的崩溃

9月 11, 2025

* * *

### v1.0.110[​](#v10110 "直接链接到v1.0.110")

-   `/terminal-setup` 命令现在支持 WezTerm
-   MCP: OAuth令牌现在主动在过期前刷新
-   修复了后台Bash进程的可靠性问题

9月 10, 2025

* * *

### v1.0.109[​](#v10109 "直接链接到v1.0.109")

-   SDK: 添加了通过 --include-partial-messages CLI 标志支持部分消息流

9月 10, 2025

* * *

### v1.0.106[​](#v10106 "直接链接到v1.0.106")

-   Windows: 修复了路径权限匹配以一致使用POSIX格式 (e.g., Read(//c/Users/...))

9月 5, 2025

* * *

### v1.0.97[​](#v1097 "直接链接到v1.0.97")

-   Settings: `/doctor` 现在验证权限规则语法并建议修正

8月 29, 2025

* * *

### v1.0.94[​](#v1094 "直接链接到v1.0.94")

-   Vertex: 为支持的模型添加了全局端点支持
-   `/memory` 命令现在允许直接编辑所有导入的内存文件
-   SDK: 添加了自定义工具作为回调
-   添加了 `/todos` 命令列出当前待办事项

8月 28, 2025

* * *

### v1.0.93[​](#v1093 "直接链接到v1.0.93")

-   Windows: 添加了alt + v从剪贴板粘贴图像的快捷方式
-   支持NO\_PROXY环境变量以绕过指定主机名和IP的代理

8月 26, 2025

* * *

### v1.0.90[​](#v1090 "直接链接到v1.0.90")

-   设置文件更改立即生效 - 无需重启

8月 25, 2025

* * *

* * *

### v1.0.88[​](#v1088 "直接链接到v1.0.88")

-   修复了导致 "OAuth身份验证当前不受支持" 的问题
-   Status line 输入现在包括 `exceeds_200k_tokens`
-   修复了 /cost 中不正确的使用跟踪
-   引入了 `ANTHROPIC_DEFAULT_SONNET_MODEL` 和 `ANTHROPIC_DEFAULT_OPUS_MODEL` 用于控制模型别名 opusplan、opus 和 sonnet
-   Bedrock: 更新了默认Sonnet模型为Sonnet4

8月 22, 2025

* * *

### v1.0.86[​](#v1086 "直接链接到v1.0.86")

-   添加了 /context 帮助用户自助调试上下文问题
-   SDK: 为所有SDK消息添加了UUID支持
-   SDK: 添加了 `--replay-user-messages` 以将用户消息重放回stdout

8月 21, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.85[​](#v1085 "直接链接到v1.0.85")

-   Status line 输入现在包括会话成本信息

8月 20, 2025

* * *

### v1.0.84[​](#v1084 "直接链接到v1.0.84")

-   修复了网络不稳定时 tool_use/tool_result 的 ID 不匹配错误
-   修复了 Claude 有时在完成任务时忽略实时引导的问题
-   @-mention: 为更容易的代理、输出样式和 slash 命令编辑添加了 ~/.claude/* 文件建议
-   默认使用内置 ripgrep；要退出此行为，设置 USE_BUILTIN_RIPGREP=0

8月 19, 2025

* * *

### v1.0.83[​](#v1083 "直接链接到v1.0.83")

-   自动补全：允许提及 ~/.claude/* 文件
-   新增了闪烁的旋转器

8月 18, 2025

* * *

### v1.0.82[​](#v1082 "直接链接到v1.0.82")

-   SDK: 添加了请求取消支持
-   SDK: 新增了 additionalDirectories 搜索自定义路径的选项，改进了 slash 命令处理
-   Settings: 验证以防止 .claude/settings.json 文件中的无效字段
-   MCP: 改进了工具名称一致性
-   Bash: 修复了 Claude 尝试自动读取大文件时的崩溃

8月 16, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[配置](/configuration.html)|[MCP服务器](/faqs/what-is-mcp-server-in-claude-code.html)

* * *

### v1.0.81[​](#v1081 "直接链接到v1.0.81")

-   发布了输出样式，包括新的内置教育输出样式 "Explanatory" 和 "Learning"
-   Agents: 修复了代理文件无法解析时的自定义代理加载

8月 14, 2025|另请参阅： [输出样式](https://docs.anthropic.com/en/docs/claude-code-output-styles)

* * *

### v1.0.80[​](#v1080 "直接链接到v1.0.80")

-   UI改进: 修复自定义子代理颜色的文本对比度和旋转器渲染问题

8月 14, 2025

* * *

* * *

### v1.0.77[​](#v1077 "直接链接到v1.0.77")

-   Bash 工具：修复了 heredoc 和多行字符串转义，改进了 stderr 重定向处理
-   SDK: 添加了会话支持和权限拒绝跟踪
-   修复了对话总结中的令牌限制错误
-   Opus 计划模式：在 `/model` 中新增设置，仅在计划模式下运行 Opus，否则运行 Sonnet

8月 13, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.73[​](#v1073 "直接链接到v1.0.73")

-   MCP: 支持通过 `--mcp-config file1.json file2.json` 使用多个配置文件
-   MCP: 按Esc取消OAuth身份验证流程
-   Bash: 改进了命令验证并减少了错误的安全警告
-   UI: 增强的旋转器动画和状态行视觉层次
-   Linux: 添加了支持Alpine和基于musl的发行版 (需要单独安装ripgrep)

8月 12, 2025|另请参阅： [MCP服务器](/faqs/what-is-mcp-server-in-claude-code.html)

* * *

### v1.0.72[​](#v1072 "直接链接到v1.0.72")

-   询问权限：让 Claude Code 始终要求确认使用特定工具 `/permissions`

8月 12, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.71[​](#v1071 "直接链接到v1.0.71")

-   Background 命令：(Ctrl-b) 在后台运行任何 Bash 命令，让 Claude 可以继续工作（非常适合开发服务器、跟踪日志等）
-   可自定义状态行：使用 `/statusline` 将您的终端提示符添加到 Claude Code

8月 8, 2025|另请参阅： [后台命令](/faqs/what-are-background-commands.html)|[可自定义状态行](/faqs/status-line-claude-code.html)

* * *

### v1.0.70[​](#v1070 "直接链接到v1.0.70")

-   性能：优化了消息渲染以在大上下文中获得更好的性能
-   Windows: 修复了原生文件搜索、ripgrep和子代理功能
-   添加了对 slash 命令参数中 @-mentions 的支持

8月 7, 2025|另请参阅： [Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)|[自定义代理](/mechanics-custom-agents.html)

* * *

* * *

### v1.0.69[​](#v1069 "直接链接到v1.0.69")

-   升级了 Opus 到版本 4.1

8月 5, 2025|另请参阅： [Claude 4.1 Opus](/faqs/what-is-claude-4-1-opus.html)

* * *

### v1.0.68[​](#v1068 "直接链接到v1.0.68")

-   修复了某些命令（如 `/pr-comments`）使用错误模型名称的问题
-   Windows: 改进了允许/拒绝工具和项目信任的权限检查。这可能会在 `.claude.json` 中创建新的项目条目 - 如果需要，请手动合并历史字段。
-   Windows: 改进了子进程生成，消除了运行 pnpm 等命令时的 "No such file or directory" 错误
-   增强了 `/doctor` 命令，添加了 CLAUDE.md 和 MCP 工具上下文以供自助调试
-   SDK: 添加了 canUseTool 回调支持以进行工具确认
-   添加了 `disableAllHooks` 设置
-   改进了大型仓库中文件建议的性能

05/08/2025|另请参阅： [Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[Hooks](/mechanics-hooks.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.65[​](#v1065 "直接链接到v1.0.65")

-   IDE: 修复了诊断的连接稳定性问题和错误处理
-   Windows: 修复了没有 .bashrc 文件用户的 shell 环境设置

01/08/25|另请参阅： [Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)

* * *

### v1.0.64[​](#v1064 "直接链接到v1.0.64")

-   Agents: 添加了模型定制支持 - 您现在可以指定代理应使用哪个模型
-   Agents: 修复了对递归代理工具的意外访问
-   Hooks: 向hook JSON 输出添加了systemMessage字段以显示警告和上下文
-   SDK: 修复了多轮对话中的用户输入跟踪
-   将隐藏文件添加到文件搜索和 @-mention建议中

July30, 2025|另请参阅： [自定义代理](/mechanics-custom-agents.html)|[Hooks](/mechanics-hooks.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.63[​](#v1063 "直接链接到v1.0.63")

-   Windows: 修复了文件搜索、@agent mentions 和自定义 slash 命令功能

July29, 2025|另请参阅： [Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[自定义代理](/mechanics-custom-agents.html)|[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)

* * *

### v1.0.62[​](#v1062 "直接链接到v1.0.62")

-   为自定义代理添加了带有预输入的 @-mention支持. @&lt;your-custom-agent&gt; 来调用它
-   Hooks: 添加了用于新会话初始化的SessionStarthook
-   /添加-dir命令现在支持目录路径的预输入
-   改进了网络连接检查的可靠性

July28, 2025|另请参阅： [Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.61[​](#v1061 "直接链接到v1.0.61")

-   Transcript 模式 (Ctrl+R): 更改了 Esc 键为退出 transcript 模式而不是中断
-   Settings: 添加了 `--settings` 标志以从JSON文件加载设置
-   Settings: 修复了符号链接设置文件路径的解析
-   OTEL: 修复了身份验证更改后错误组织的报告
-   Slash 命令：修复了 Bash 允许工具的权限检查
-   IDE: 添加了在 VSCode macOS 中使用 ⌘+V 粘贴图像的支持
-   IDE: 添加了 `CLAUDE_CODE_AUTO_CONNECT_IDE=false` 用于禁用 IDE 自动连接
-   添加了 `CLAUDE_CODE_SHELL_PREFIX` 用于包装 Claude Code 运行的 Claude 和用户提供的 shell 命令

July25, 2025|另请参阅： [配置](/configuration.html)|[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)

* * *

### v1.0.60[​](#v1060 "直接链接到v1.0.60")

-   您现在可以为专门任务创建自定义子代理！运行 /agents开始使用

July24, 2025|另请参阅： [Task Agent Tools](/mechanics-task-agent-工具.html)|[Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)

* * *

* * *

### v1.0.59[​](#v1059 "直接链接到v1.0.59")

-   SDK: 添加了带有canUseTool回调的工具确认支持
-   SDK: 允许为生成的进程指定环境
-   Hooks: 向 hooks 公开了 PermissionDecision (including "ask")
-   Hooks: UserPromptSubmit现在支持添加额外上下文在高级 JSON 输出
-   修复了某些指定Opus的 Max用户仍然回退到Sonnet的问题

July23, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.58[​](#v1058 "直接链接到v1.0.58")

-   添加了对读取PDF的支持
-   MCP: 改进了 'claudemcplist' 中服务器健康状态的显示
-   Hooks: 添加了CLAUDE\_PROJECT\_DIRenvvarforhook命令

July23, 2025|另请参阅： [Hooks](/mechanics-hooks.html)|[MCPs](/claude-code-mcps.html)

* * *

### v1.0.57[​](#v1057 "直接链接到v1.0.57")

-   添加了在slash命令中指定模型的支持
-   改进了权限消息以帮助Claude理解允许的工具
-   修复：删除终端包装中bash输出的尾随换行符

July23, 2025|另请参阅： [自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)|[Auto-Accep t Permissions](/mechanics-auto-accept-permissions.html)

* * *

### v1.0.56[​](#v1056 "直接链接到v1.0.56")

-   Windows: 在支持终端VT模式的Node.js版本上启用了shift+tab模式切换
-   修复了WSLIDE检测
-   修复了aws Refres h Helper对 .aws目录的更改未被识别的问题

July23, 2025|另请参阅： [Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[配置](/configuration.html)

* * *

### v1.0.55[​](#v1055 "直接链接到v1.0.55")

-   明确了Opus4 和Sonnet4 模型的知识截止日期
-   Windows: 修复了Ctrl+Z崩溃
-   SDK: 添加了捕获错误日志的能力
-   添加了 --system-prompt-file选项以在打印模式下覆盖系统提示

July23, 2025|另请参阅： [Mode l Comparison](/model-comparison.html)|[Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.54[​](#v1054 "直接链接到v1.0.54")

-   Hooks: 添加了User Promp t Submithook和当前工作目录到hook输入
-   自定义slash命令：向前言添加了argument-hint
-   Windows: OAuthusesport45454andproperlyconstructsbrowser URL
-   Windows: 模式切换现在使用alt + m，计划模式正确渲染
-   Shell: 切换到内存中的shell快照以避免文件相关错误

July19, 2025|另请参阅： [Hooks](/mechanics-hooks.html)|[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)|[Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)

* * *

### v1.0.53[​](#v1053 "直接链接到v1.0.53")

-   更新了 @-mentionfiletruncationfrom100linesto2000lines
-   添加了AWS令牌刷新的辅助脚本设置：aws Aut h Refresh（用于前台操作如awsssologin）和aws Credentia l Export（用于类似STS响应的后台操作）

July18, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.52[​](#v1052 "直接链接到v1.0.52")

-   添加了支持for MCPserverinstructions

July18, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.51[​](#v1051 "直接链接到v1.0.51")

-   添加了支持fornativ e Windows (requires Gitfo r Windows)
-   添加了支持fo r Bedrock APIkeysthroughenvironmentvariable AWS\_BEARER\_TOKEN\_BEDROCK
-   Settings: /doctorcan现在helpyouidentifyand修复了invalid设置文件
-   `--append-system-prompt` can现在beusedininteractivemode, notjust --print/-p.
-   Increasedauto-compactwarningthresholdfrom60% to80%
-   修复了an问题withhandlinguserdirectorieswithspacesforshellsnapshots
-   OTELresource现在包括os.type, os.version, host.arch, andwsl.version (ifrunningon Windows Subsystemfo r Linux)
-   Customslash命令: 修复了user-level命令insubdirectories
-   Planmode: 修复了问题whererejectedplanfromsub-taskwouldgetdiscarded

July11, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)|[Windows 安装](/faqs/how-to-install-claude-code-on-windows.html)|[自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)

* * *

* * *

### v1.0.48[​](#v1048 "直接链接到v1.0.48")

-   修复了abugin [v1.0.45](#v1045) wheretheappwouldsometimesfreezeonlaunch
-   添加了progressmessagest o Bash工具basedonthelast5 linesof命令输出
-   添加了expandingvariables支持for MCPserverconfiguration
-   Movedshellsnapshotsfrom /tmpto ~/.claudeformorereliabl e Bash工具calls
-   改进了IDEextensionpathhandlingwhe n Claude Coderunsin WSL
-   Hooks: 添加了a Pr e Compacthook
-   Vimmode: 添加了c, f/F, t/T

July10, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.45[​](#v1045 "直接链接到v1.0.45")

-   Redesigne d Search (Grep) 工具withnew工具输入parametersandfeatures
-   Disabled IDEdiffsfornotebook文件, 修复ing "Timeoutwaitingafter1000ms" error
-   修复了configfilecorruption问题byenforcingatomicwrites
-   更新了prompt输入undot o Ctrl+\_toavoidbreakingexistin g Ctrl+Ubehavior, matchingzsh'sundo快捷方式
-   Sto p Hooks: 修复了transcriptpathafter /clearand修复了triggeringwhenloopendswith工具call
-   Customslash命令: Restorednamespacingin命令namesbasedonsubdirectories. Forexample, .claude/frontend/component.mdis现在 /frontend:component, not /component.

July9, 2025|另请参阅： [自定义 Slash 命令](/faqs/what-is-slash-commands-in-claude-code.html)|[Hooks](/mechanics-hooks.html)

* * *

### v1.0.44[​](#v1044 "直接链接到v1.0.44")

-   新增了 `/export` 命令，让您快速导出对话以便分享
-   MCP: resource\_link工具resultsare现在支持ed
-   MCP: 工具annotationsand工具titles现在displayin /mcpview
-   将Ctrl+Z更改为暂停Claude Code。通过运行 `fg` 恢复。提示输入撤销现在是Ctrl+U。

July7, 2025|另请参阅： [MCPs](/claude-code-mcps.html)|[Suspend/Resume](/faqs/how-to-suspend-claude-code.html)

* * *

### v1.0.43[​](#v1043 "直接链接到v1.0.43")

-   修复了主题选择器过度保存的错误
-   Hooks: 添加了EPIPE系统错误处理

July3, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.42[​](#v1042 "直接链接到v1.0.42")

-   添加了tilde (`~`) expansion支持to `/添加-dir` 命令

July3, 2025|另请参阅： [/添加-dir FAQ](/faqs/--添加-dir.html)

* * *

### v1.0.41[​](#v1041 "直接链接到v1.0.41")

-   Hooks: Split Stophooktriggeringinto Stopand Subagen t Stop
-   Hooks: Enabledoptionaltimeoutconfigurationforeach命令
-   Hooks: 添加了 "hook\_event\_name" tohook输入
-   修复了abugwhere MCP工具woulddisplaytwicein工具list
-   新增工具parameters JSONfo r Bash工具in `工具\_decision` event

另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.40[​](#v1040 "直接链接到v1.0.40")

-   修复了abug导致APIconnectionerrorswith UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLYif `NODE\_EXTRA\_CA\_CERTS` wasset

* * *

* * *

### v1.0.39[​](#v1039 "直接链接到v1.0.39")

-   新增Active Timemetricin Ope n Telemetrylogging

July2, 2025

* * *

### v1.0.38[​](#v1038 "直接链接到v1.0.38")

-   Released [hooks](https://docs.anthropic.com/en/docs/claude-code-hooks). Specialthankstocommunity输入in [Githu b Issues](https://github.com/anthropics/claude-code-问题/712)

July2, 2025|另请参阅： [Hooks](/mechanics-hooks.html)

* * *

### v1.0.37[​](#v1037 "直接链接到v1.0.37")

-   Removeabilitytoset `Proxy-Authorization` headervia ANTHROPIC\_AUTH\_TOKENorapi Ke y Helper

July2, 2025

* * *

### v1.0.36[​](#v1036 "直接链接到v1.0.36")

-   Web搜索现在将今天的日期纳入上下文
-   修复了stdio MCP服务器在退出时未正确终止的错误

July2, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.35[​](#v1035 "直接链接到v1.0.35")

-   添加了对MCPOAuth授权服务器发现的支持

June25, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.34[​](#v1034 "直接链接到v1.0.34")

-   修复了导致Max Listeners Exceede d Warning消息出现的内存泄漏

June24, 2025

* * *

### v1.0.33[​](#v1033 "直接链接到v1.0.33")

-   改进了loggingfunctionalitywithsession ID支持
-   添加了撤销功能（Ctrl+Z和 vim 'u' 命令）
-   计划模式的改进

June24, 2025|另请参阅： [计划模式](/mechanics-plan-mode.html)

* * *

### v1.0.32[​](#v1032 "直接链接到v1.0.32")

-   更新了litellm的回环配置
-   添加了force Logi n Method设置以跳过登录选择屏幕

June24, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.31[​](#v1031 "直接链接到v1.0.31")

-   修复了当文件包含无效JSON时 ~/.claude.json会被重置的错误

June24, 2025

* * *

### v1.0.30[​](#v1030 "直接链接到v1.0.30")

-   Customslash命令: Runbash输出, @-mention文件, 启用thinkingwiththinkingkeywords
-   改进了filepathautocompletewithfilenamematching
-   添加了timestampsi n Ctrl-rmodeand修复了Ctrl-chandling
-   Enhancedjqregex支持forcomplexfilterswithpipesandselect

June24, 2025|另请参阅： [Slas h Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令)

* * *

* * *

### v1.0.29[​](#v1029 "直接链接到v1.0.29")

-   改进了CJKcharacter支持incursornavigationandrendering

June24, 2025

* * *

### v1.0.28[​](#v1028 "直接链接到v1.0.28")

-   Slash命令: 修复selectordisplayduringhistorynavigation
-   Resizesimagesbeforeuploadtoprevent APIsizelimiterrors
-   添加了XDG\_CONFIG\_HOME支持toconfigurationdirectory
-   Performanceoptimizationsformemoryusage
-   新增attributes (terminal.type, language) in Ope n Telemetrylogging

June24, 2025|另请参阅： [配置](https://docs.anthropic.com/en/docs/claude-code-设置s)

* * *

### v1.0.27[​](#v1027 "直接链接到v1.0.27")

-   Streamable HTTPMCPserversare现在支持ed
-   Remote MCPservers (SSEand HTTP) 现在支持OAuth
-   MCPresourcescan现在be @-mentioned

June18, 2025|另请参阅： [MCPResources](https://docs.anthropic.com/en/docs/claude-code-mcp#use-mcp-resources)

* * *

### v1.0.25[​](#v1025 "直接链接到v1.0.25")

-   Slash命令: moved "project" and "user" pre修复todescriptions
-   Slash命令: 改进了reliabilityfor命令discovery
-   改进了支持fo r Ghostty
-   改进了websearchreliability

June16, 2025|另请参阅： [Slas h Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令)

* * *

### v1.0.24[​](#v1024 "直接链接到v1.0.24")

-   改进了 `/mcp` 输出
-   修复了abugwhere设置sarraysgotoverwritteninsteadofmerged

June16, 2025|另请参阅： [MCPs](/claude-code-mcps.html)

* * *

### v1.0.23[​](#v1023 "直接链接到v1.0.23")

-   Released Typ e Script SDK: `import @anthropic-ai/claude-code` togetstarted
-   Release d Python SDK: `pipinstallclaude-code-sdk` togetstarted

June16, 2025|另请参阅： [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.22[​](#v1022 "直接链接到v1.0.22")

-   SDK: Renamed `total\_cost` to `total\_cost\_usd`

June12, 2025|另请参阅： [CCUsage](/claude-code-mcps/cc-usage.html)

* * *

### v1.0.21[​](#v1021 "直接链接到v1.0.21")

-   改进了editingof文件withtab-basedindentation
-   修复for `工具\_use` withoutmatching `工具\_result` errors
-   修复了abugwherestdio MCPserverprocesseswouldlingerafterquittin g Claude Code

June12, 2025

* * *

* * *

### v1.0.18[​](#v1018 "直接链接到v1.0.18")

-   添加了 `--添加-dir` CLIargumentforspecifying额外的workingdirectories
-   添加了streaming输入支持withoutrequire `-p` flag
-   改进了startupperformanceandsessionstorageperformance
-   添加了 `CLAUDE\_BASH\_MAINTAIN\_PROJECT\_WORKING\_DIR` environmentvariabletofreezeworkingdirectoryforbash命令
-   添加了detailed MCPserver工具display (`/mcp`)
-   MCPauthenticationandpermission改进
-   添加了auto-reconnectionfor MCPSSEconnectionsondisconnect
-   修复了问题wherepastedcontentwaslostwhendialogsappeared

June10, 2025|另请参阅： [配置](/configuration/#mcp-configuration.html)|[Additional Workin g Directories](https://docs.anthropic.com/en/docs/claude-code-common-workflows#额外的-working-directories)|[MCPs](/claude-code-mcps.html)

* * *

### v1.0.17[​](#v1017 "直接链接到v1.0.17")

-   We现在emitmessagesfromsub-tasksin `-p` mode

June10, 2025

* * *

### v1.0.16[​](#v1016 "直接链接到v1.0.16")

-   Additional改进and错误修复 (lookforthe `parent\_工具\_use\_id` property)
-   修复了crasheswhenthe VSCodediff工具isinvokedmultipletimesquickly
-   MCPserverlist UI改进
-   Updat e Claude Codeprocesstitletodisplay `claude` insteadof `node`

June6, 2025

* * *

### v1.0.11[​](#v1011 "直接链接到v1.0.11")

-   Claude Codecan现在alsobeusedwitha Claud e Prosubscription
-   添加了 `/upgrade` forsmootherswitchingto Claud e Maxplans
-   改进了UIforauthenticationfrom APIkeysan d Bedrock/Vertex/externalauthtokens
-   改进了shellconfiguration错误处理
-   改进了todolisthandlingduringcompaction

June4, 2025|另请参阅： [Pricing](/claude-code-pricing.html)|[Mode l Comparison](/model-comparison.html)|[Installation](/install-claude-code.html)

* * *

### v1.0.10[​](#v1010 "直接链接到v1.0.10")

-   添加了markdowntable支持
-   改进了streamingperformance

June3, 2025

* * *

### v1.0.8[​](#v108 "直接链接到v1.0.8")

-   修复了Vertex AIregionfallbackwhenusing `CLOUD\_ML\_REGION`
-   Increaseddefaultotelintervalfrom1s -> 5s
-   修复了edgecaseswhere `MCP\_TIMEOUT` and `MCP\_TOOL\_TIMEOUT` weren'tbeingrespected
-   修复了aregressionwheresearch工具unnecessarilyaskedforpermissions
-   添加了支持fortriggeringthinkingnon-Englishlanguages
-   改进了compacting UI

June2, 2025|另请参阅： [Restartin g Claude Code](/faqs/restarting-claude-code.html)|[Context Windo w Depletion](/mechanics-context-window-depletion.html)

* * *

### v1.0.7[​](#v107 "直接链接到v1.0.7")

-   Renamed `/allowed-工具` -> `/permissions`
-   Migrated `allowe d Tools` and `ignor e Patterns` from `.claude.json` -> `设置s.json`
-   Deprecated `claudeconfig` 命令infavorofediting `设置s.json`
-   修复了abugwhere `--dangerously-skip-permissions` sometimesdidn'tworkin `--print` mode
-   改进了错误处理for `/install-github-app`
-   Bug修复, UIpolish, and工具reliability改进

June2, 2025|另请参阅： [Auto-Accep t Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v1.0.6[​](#v106 "直接链接到v1.0.6")

-   改进了editreliabilityfortab-indented文件
-   Respect `CLAUDE\_CONFIG\_DIR` everywhere
-   Reducedunnecessary工具permissionprompts
-   添加了支持forsymlinksin `@file` typeahead
-   Bug修复, UIpolish, and工具reliability改进

June2, 2025|另请参阅： [配置](/configuration.html)

* * *

### v1.0.4[​](#v104 "直接链接到v1.0.4")

-   修复了abugwhere MCP工具errorsweren'tbeingparsedcorrectly

5月 28, 2025

* * *

### v1.0.1[​](#v101 "直接链接到v1.0.1")

-   添加了 `DISABLE\_INTERLEAVED\_THINKING` togiveuserstheoptiontooptoutofinterleavedthinking
-   改进了modelreferencestoshowprovider-specificnames (Sonnet3.7fo r Bedrock, Sonnet4 fo r Console)
-   更新了documentationlinksand OAuthprocessdescriptions

5月 22, 2025|另请参阅： [配置](/configuration.html)

* * *

* * *

### v1.0.0[​](#v100 "直接链接到v1.0.0")

-   Claude Codeis现在generallyavailable
-   Introducin g Sonnet4 an d Opus4 models

5月 22, 2025|另请参阅： [Mode l Comparison](/model-comparison.html)|[Installation](/install-claude-code.html)|[Gettin g Started](/claude-code-tutorial.html)

* * *

### v0.2.125[​](#v02125 "直接链接到v0.2.125")

-   Breakingchange: Bedrock ARNpassedto `ANTHROPIC\_MODEL` or `ANTHROPIC\_SMALL\_FAST\_MODEL` shouldnolongercontainanescapedslash (specify / insteadof %2F)
-   Removed `DEBUG=true` infavorof `ANTHROPIC\_LOG=debug`, tologallrequests

5月 21, 2025|另请参阅： [配置](/configuration.html)

* * *

### v0.2.117[​](#v02117 "直接链接到v0.2.117")

-   Breakingchange: `--print` JSON 输出现在returnsnestedmessageobjects, forforwards-compatibilityasweintroducenewmetadatafields
-   引入了 `设置s.cleanup Perio d Days`
-   引入了 `CLAUDE\_CODE\_API\_KEY\_HELPER\_TTL\_MS` envvar
-   引入了 `--debug` mode

5月 18, 2025

* * *

### v0.2.108[​](#v02108 "直接链接到v0.2.108")

-   Youcan现在sendmessagesto Claudewhileitworkstostee r Claudeinreal-time
-   引入了 `BASH\_DEFAULT\_TIMEOUT\_MS` and `BASH\_MAX\_TIMEOUT\_MS` envvars
-   修复了abugwherethinkingwasnotworkingin `-p` mode
-   修复了aregressionin `/cost` reporting
-   Deprecated MCPwizardinterfaceinfavorofother MCP命令
-   Lotsofotherbug修复and改进

5月 13, 2025

* * *

### v0.2.107[​](#v02107 "直接链接到v0.2.107")

-   `CLAUDE.md` 文件can现在importother文件. Add `@path/to/file.md` to `./CLAUDE.md` toload额外的文件onlaunch

5月 9, 2025|另请参阅： [CLAUDE.m d Supremacy](/mechanics-claude-md-supremacy.html)

* * *

### v0.2.106[​](#v02106 "直接链接到v0.2.106")

-   MCPSSEserverconfigscan现在specifycustomheaders
-   修复了abugwhere MCPpermissionpromptdidn'talwaysshowcorrectly

5月 9, 2025

* * *

### v0.2.105[​](#v02105 "直接链接到v0.2.105")

-   Claudecan现在searchtheweb
-   Movedsystem & accountstatusto `/status`
-   添加了wordmovementkeybindingsfo r Vim
-   改进了latencyforstartup, todo工具, andfileedits

5月 8, 2025

* * *

### v0.2.102[​](#v02102 "直接链接到v0.2.102")

-   改进了thinkingtriggeringreliability
-   改进了 `@mention` reliabilityforimagesandfolders
-   Youcan现在pastemultiplelargechunksintooneprompt

5月 5, 2025

* * *

### v0.2.100[​](#v02100 "直接链接到v0.2.100")

-   修复了acrashcausedbya stackoverflowerror
-   Madedbstorageoptional; missingdb支持disables `--continue` and `--resume`

* * *

### v0.2.98[​](#v0298 "直接链接到v0.2.98")

-   修复了an问题whereauto-compactwasrunningtwice

5月 2, 2025

* * *

### v0.2.95[​](#v0295 "直接链接到v0.2.95")

-   Claude Codecan现在alsobeusedwitha [Claud e Maxsubscription](https://claude.ai/upgrade)
-   Claude Codecan现在alsobeusedwitha [Claud e Maxsubscription](https://claude.ai/upgrade)

5月 1, 2025

* * *

### v0.2.93[​](#v0293 "直接链接到v0.2.93")

-   Resumeconversationsfromwhereyouleftofffromwith `claude --continue` and `claude --resume`
-   Claude现在hasaccesstoa Todolistthathelpsitstayontrackandbemoreorganized

April30, 2025

* * *

### v0.2.82[​](#v0282 "直接链接到v0.2.82")

-   添加了支持for `--disallowe d Tools`
-   Renamed工具forconsistency: `LSTool` -> `LS`, `View` -> `Read`, etc.

April25, 2025|另请参阅： [Auto-Accep t Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v0.2.75[​](#v0275 "直接链接到v0.2.75")

-   Hit Entertoqueueup额外的messageswhil e Claudeisworking
-   Draginorcopy/pasteimage文件directlyintotheprompt
-   `@-mention` 文件todirectly添加了themtocontext
-   Runone-off MCPserverswith `claude --mcp-config &lt;path-to-file&gt;`
-   改进了performanceforfilenameauto-complete

April21, 2025|另请参阅： [MCPs & Add-ons](/claude-code-mcps.html)|[配置](/configuration/#mcp-configuration.html)

* * *

### v0.2.7[​](#v027 "直接链接到v0.2.7")

-   Additionalupdatesand修复
-   添加了支持forrefreshingdynamicallygenerated APIkeys (via `api Ke y Helper`), witha 5minute TTL
-   Task工具can现在performwritesandrunbash命令

April17, 2025

* * *

### v0.2.72[​](#v0272 "直接链接到v0.2.72")

-   更新了spinnertoindicatetokensloadedand工具usage

April18, 2025

* * *

### v0.2.70[​](#v0270 "直接链接到v0.2.70")

-   Network命令like `curl` are现在availablefo r Claudetouse
-   Claudecan现在runmultiplewebqueriesinparallel
-   Pressing ESConceimmediatelyinterrupts Claudei n Auto-acceptmode

* * *

### v0.2.69[​](#v0269 "直接链接到v0.2.69")

-   修复了UIglitcheswith改进了Selectcomponentbehavior
-   Enhancedterminal输出displaywithbettertexttruncationlogic

* * *

### v0.2.67[​](#v0267 "直接链接到v0.2.67")

-   Sharedprojectpermissionrulescanbesavedin `.claude/设置s.json`

* * *

### v0.2.66[​](#v0266 "直接链接到v0.2.66")

-   Printmode (`-p`) 现在支持streaming输出via `--输出-format=stream-json`
-   修复了问题wherepastingcouldtriggermemoryorbashmodeunexpectedly

* * *

### v0.2.63[​](#v0263 "直接链接到v0.2.63")

-   修复了an问题where MCP工具wereloadedtwice, whichcaused工具callerrors

* * *

### v0.2.61[​](#v0261 "直接链接到v0.2.61")

-   Navigatemenuswithvim-stylekeys (`j`/`k`) orbash/emacs快捷方式s (`Ctrl+n`/`p`) forfasterinteraction
-   Enhancedimagedetectionformorereliableclipboardpastefunctionality
-   修复了an问题where ESCkeycouldcrashtheconversationhistoryselector

* * *

### v0.2.59[​](#v0259 "直接链接到v0.2.59")

-   Copy+pasteimagesdirectlyintoyourprompt
-   改进了progressindicatorsforbashandfetch工具
-   Bug修复fornon-interactivemode (`-p`)

* * *

### v0.2.54[​](#v0254 "直接链接到v0.2.54")

-   Quickly添加了t o Memorybystartingyourmessagewith `#`
-   Press `ctrl+r` toseefull输出forlong工具results
-   添加了支持for MCPSSEtransport

* * *

### v0.2.53[​](#v0253 "直接链接到v0.2.53")

-   新增webfetch工具let s Claudeview URLsthatyoupastein
-   修复了abugwith JPEGdetection

* * *

### v0.2.50[​](#v0250 "直接链接到v0.2.50")

-   新增MCP "project" scope现在允许youto添加了MCPserversto `.mcp.json` 文件andcommitthemtoyourrepository

* * *

### v0.2.49[​](#v0249 "直接链接到v0.2.49")

-   Previous MCPserverscopeshavebeenrenamed: previous "project" scopeis现在 "local" and "global" scopeis现在 "user"

* * *

### v0.2.47[​](#v0247 "直接链接到v0.2.47")

-   Pres s Tabtoauto-completefileandfoldernames
-   Pres s Shift + Tabtotoggleauto-acceptforfileedits
-   Automaticconversationcompactionforinfiniteconversationlength (togglewith `/config`)

另请参阅： [Auto-Accep t Permissions](/mechanics-auto-accept-permissions.html)

* * *

### v0.2.44[​](#v0244 "直接链接到v0.2.44")

-   As k Claudetomakea planwiththinkingmode: justsay 'think' or 'thinkharder' oreven 'ultrathink'

* * *

### v0.2.41[​](#v0241 "直接链接到v0.2.41")

-   MCPserverstartuptimeoutcan现在beconfiguredvia `MCP\_TIMEOUT` environmentvariable
-   MCPserverstartupnolongerblockstheappfromstartingup

* * *

### v0.2.37[​](#v0237 "直接链接到v0.2.37")

-   新增 `/release-notes` 命令letsyouviewreleasenotesatanytime
-   `claudeconfig添加/remove` 命令现在acceptmultiplevaluesseparatedbycommasorspaces

* * *

### v0.2.36[​](#v0236 "直接链接到v0.2.36")

-   Import MCPserversfrom Claud e Desktopwith `claudemcp添加-from-claude-desktop`
-   Add MCPserversas JSONstringswith `claudemcp添加-json &lt;n&gt; &lt;json&gt;`

April21, 2025|另请参阅： [MCPs & Add-ons](/claude-code-mcps.html)|[配置](/configuration/#mcp-configuration.html)

* * *

### v0.2.34[​](#v0234 "直接链接到v0.2.34")

-   Vimbindingsfortext输入 - 启用with `/vim` or `/config`

* * *

### v0.2.32[​](#v0232 "直接链接到v0.2.32")

-   Interactive MCPsetupwizard: Run `claudemcp添加` to添加了MCPserverswitha step-by-stepinterface
-   修复forsome Persisten t Shell问题

* * *

### v0.2.31[​](#v0231 "直接链接到v0.2.31")

-   Customslash命令: Markdown文件in `.claude/命令/` directories现在appearascustomslash命令toinsertpromptsintoyourconversation
-   MCPdebugmode: Runwith `--mcp-debug` flagtogetmoreinformationabout MCPservererrors

另请参阅： [CLAUDE.m d Supremacy](/mechanics-claude-md-supremacy.html) | [Slas h Commands](https://docs.anthropic.com/en/docs/claude-code-slash-命令)

* * *

### v0.2.30[​](#v0230 "直接链接到v0.2.30")

-   添加了ANSIcolorthemeforbetterterminalcompatibility
-   修复了问题whereslash命令argumentsweren'tbeingsentproperly
-   (Mac-only) APIkeysare现在storedinmac OSKeychain

* * *

### v0.2.26[​](#v0226 "直接链接到v0.2.26")

-   新增 `/approved-工具` 命令formanaging工具permissions
-   Word-leveldiffdisplayfor改进了codereadability
-   Fuzzymatchingforslash命令

April21, 2025|另请参阅： [Auto-Accep t Permissions](/mechanics-auto-accept-permissions.html)|[配置](/configuration.html)

* * *

### v0.2.21[​](#v0221 "直接链接到v0.2.21")

-   Fuzzymatchingfor `/命令`

* * *

##### 非凡的进展

令人惊讶的是，Claude Code 在如此短的时间内取得了如此大的进步。从早期的测试版本到一个拥有 MCP、自动权限、计划模式、实时指导和复杂工作流程的综合开发平台——创新的步伐非常惊人。


* * *
