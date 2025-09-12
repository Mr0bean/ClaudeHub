---
title: "Claude Code Changelog | ClaudeLog"
---

# Claude Code Changelog | ClaudeLog

Complete version history of Claude Code releases, from early beta versions to the latest stable release. Each version includes feature additions, bug fixes, and links to relevant documentation. **Need to downgrade?** See our [Revert Claude Code Version](/faqs/revert-claude-code-version/) guide.

* * *

* * *

### v1.0.111[​](#v10111 "Direct link to v1.0.111")

-   `/model` now validates provided model names
-   Fixed Bash tool crashes caused by malformed shell syntax parsing

Sep 11, 2025

* * *

### v1.0.110[​](#v10110 "Direct link to v1.0.110")

-   `/terminal-setup` command now supports WezTerm
-   MCP: OAuth tokens now proactively refresh before expiration
-   Fixed reliability issues with background Bash processes

Sep 10, 2025

* * *

### v1.0.109[​](#v10109 "Direct link to v1.0.109")

-   SDK: Added partial message streaming support via --include-partial-messages CLI flag

Sep 10, 2025

* * *

### v1.0.106[​](#v10106 "Direct link to v1.0.106")

-   Windows: Fixed path permission matching to consistently use POSIX format (e.g., Read(//c/Users/...))

Sep 5, 2025

* * *

### v1.0.97[​](#v1097 "Direct link to v1.0.97")

-   Settings: `/doctor` now validates permission rule syntax and suggests corrections

Aug 29, 2025

* * *

### v1.0.94[​](#v1094 "Direct link to v1.0.94")

-   Vertex: add support for global endpoints for supported models
-   `/memory` command now allows direct editing of all imported memory files
-   SDK: Add custom tools as callbacks
-   Added `/todos` command to list current todo items

Aug 28, 2025

* * *

### v1.0.93[​](#v1093 "Direct link to v1.0.93")

-   Windows: Add alt + v shortcut for pasting images from clipboard
-   Support NO\_PROXY environment variable to bypass proxy for specified hostnames and IPs

Aug 26, 2025

* * *

### v1.0.90[​](#v1090 "Direct link to v1.0.90")

-   Settings file changes take effect immediately - no restart required

Aug 25, 2025

* * *

* * *

### v1.0.88[​](#v1088 "Direct link to v1.0.88")

-   Fixed issue causing "OAuth authentication is currently not supported"
-   Status line input now includes `exceeds_200k_tokens`
-   Fixed incorrect usage tracking in /cost.
-   Introduced `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_OPUS_MODEL` for controlling model aliases opusplan, opus, and sonnet.
-   Bedrock: Updated default Sonnet model to Sonnet 4

Aug 22, 2025

* * *

### v1.0.86[​](#v1086 "Direct link to v1.0.86")

-   Added /context to help users self-serve debug context issues
-   SDK: Added UUID support for all SDK messages
-   SDK: Added `--replay-user-messages` to replay user messages back to stdout

Aug 21, 2025|See Also: [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.85[​](#v1085 "Direct link to v1.0.85")

-   Status line input now includes session cost info

Aug 20, 2025

* * *

### v1.0.84[​](#v1084 "Direct link to v1.0.84")

-   Fix tool\_use/tool\_result id mismatch error when network is unstable
-   Fix Claude sometimes ignoring real-time steering when wrapping up a task
-   @-mention: Add ~/.claude/\* files to suggestions for easier agent, output style, and slash command editing
-   Use built-in ripgrep by default; to opt out of this behavior, set USE\_BUILTIN\_RIPGREP=0

Aug 19, 2025

* * *

### v1.0.83[​](#v1083 "Direct link to v1.0.83")

-   Auto-complete: allow mentioning ~/.claude/\* files
-   New shimmering spinner

Aug 18, 2025

* * *

### v1.0.82[​](#v1082 "Direct link to v1.0.82")

-   SDK: Add request cancellation support
-   SDK: New additionalDirectories option to search custom paths, improved slash command processing
-   Settings: Validation prevents invalid fields in .claude/settings.json files
-   MCP: Improve tool name consistency
-   Bash: Fix crash when Claude tries to automatically read large files

Aug 16, 2025|See Also: [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[Configuration](/configuration/)|[MCP Servers](/faqs/what-is-mcp-server-in-claude-code/)

* * *

### v1.0.81[​](#v1081 "Direct link to v1.0.81")

-   Released output styles, including new built-in educational output styles "Explanatory" and "Learning"
-   Agents: Fix custom agent loading when agent files are unparsable

Aug 14, 2025|See Also: [Output Styles](https://docs.anthropic.com/en/docs/claude-code-output-styles)

* * *

### v1.0.80[​](#v1080 "Direct link to v1.0.80")

-   UI improvements: Fix text contrast for custom subagent colors and spinner rendering issues

Aug 14, 2025

* * *

* * *

### v1.0.77[​](#v1077 "Direct link to v1.0.77")

-   Bash tool: Fix heredoc and multiline string escaping, improve stderr redirection handling
-   SDK: Add session support and permission denial tracking
-   Fix token limit errors in conversation summarization
-   Opus Plan Mode: New setting in `/model` to run Opus only in plan mode, Sonnet otherwise

Aug 13, 2025|See Also: [Plan Mode](/mechanics-plan-mode/)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.73[​](#v1073 "Direct link to v1.0.73")

-   MCP: Support multiple config files with `--mcp-config file1.json file2.json`
-   MCP: Press Esc to cancel OAuth authentication flows
-   Bash: Improved command validation and reduced false security warnings
-   UI: Enhanced spinner animations and status line visual hierarchy
-   Linux: Added support for Alpine and musl-based distributions (requires separate ripgrep installation)

Aug 12, 2025|See Also: [MCP Servers](/faqs/what-is-mcp-server-in-claude-code/)

* * *

### v1.0.72[​](#v1072 "Direct link to v1.0.72")

-   Ask permissions: have Claude Code always ask for confirmation to use specific tools with `/permissions`

Aug 12, 2025|See Also: [Configuration](/configuration/)

* * *

### v1.0.71[​](#v1071 "Direct link to v1.0.71")

-   Background commands: (Ctrl-b) to run any Bash command in the background so Claude can keep working (great for dev servers, tailing logs, etc.)
-   Customizable status line: add your terminal prompt to Claude Code with `/statusline`

Aug 8, 2025|See Also: [Background Commands](/faqs/what-are-background-commands/)|[Customizable Status Line](/faqs/status-line-claude-code/)

* * *

### v1.0.70[​](#v1070 "Direct link to v1.0.70")

-   Performance: Optimized message rendering for better performance with large contexts
-   Windows: Fixed native file search, ripgrep, and subagent functionality
-   Added support for @-mentions in slash command arguments

Aug 7, 2025|See Also: [Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)|[Custom Agents](/mechanics-custom-agents/)

* * *

* * *

### v1.0.69[​](#v1069 "Direct link to v1.0.69")

-   Upgraded Opus to version 4.1

05/08/2025|See Also: [Claude 4.1 Opus](/faqs/what-is-claude-4-1-opus/)

* * *

### v1.0.68[​](#v1068 "Direct link to v1.0.68")

-   Fix incorrect model names being used for certain commands like `/pr-comments`
-   Windows: improve permissions checks for allow / deny tools and project trust. This may create a new project entry in `.claude.json` - manually merge the history field if desired.
-   Windows: improve sub-process spawning to eliminate "No such file or directory" when running commands like pnpm
-   Enhanced `/doctor` command with CLAUDE.md and MCP tool context for self-serve debugging
-   SDK: Added canUseTool callback support for tool confirmation
-   Added `disableAllHooks` setting
-   Improved file suggestions performance in large repos

05/08/2025|See Also: [Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Hooks](/mechanics-hooks/)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.65[​](#v1065 "Direct link to v1.0.65")

-   IDE: Fixed connection stability issues and error handling for diagnostics
-   Windows: Fixed shell environment setup for users without .bashrc files

01/08/25|See Also: [Windows Installation](/faqs/how-to-install-claude-code-on-windows/)

* * *

### v1.0.64[​](#v1064 "Direct link to v1.0.64")

-   Agents: Added model customization support - you can now specify which model an agent should use
-   Agents: Fixed unintended access to the recursive agent tool
-   Hooks: Added systemMessage field to hook JSON output for displaying warnings and context
-   SDK: Fixed user input tracking across multi-turn conversations
-   Added hidden files to file search and @-mention suggestions

July 30, 2025|See Also: [Custom Agents](/mechanics-custom-agents/)|[Hooks](/mechanics-hooks/)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.63[​](#v1063 "Direct link to v1.0.63")

-   Windows: Fixed file search, @agent mentions, and custom slash commands functionality

July 29, 2025|See Also: [Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Custom Agents](/mechanics-custom-agents/)|[Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)

* * *

### v1.0.62[​](#v1062 "Direct link to v1.0.62")

-   Added @-mention support with typeahead for custom agents. @&lt;your-custom-agent&gt; to invoke it
-   Hooks: Added SessionStart hook for new session initialization
-   /add-dir command now supports typeahead for directory paths
-   Improved network connectivity check reliability

July 28, 2025|See Also: [Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)|[Hooks](/mechanics-hooks/)

* * *

### v1.0.61[​](#v1061 "Direct link to v1.0.61")

-   Transcript mode (Ctrl+R): Changed Esc to exit transcript mode rather than interrupt
-   Settings: Added `--settings` flag to load settings from a JSON file
-   Settings: Fixed resolution of settings files paths that are symlinks
-   OTEL: Fixed reporting of wrong organization after authentication changes
-   Slash commands: Fixed permissions checking for allowed-tools with Bash
-   IDE: Added support for pasting images in VSCode MacOS using ⌘+V
-   IDE: Added `CLAUDE_CODE_AUTO_CONNECT_IDE=false` for disabling IDE auto-connection
-   Added `CLAUDE_CODE_SHELL_PREFIX` for wrapping Claude and user-provided shell commands run by Claude Code

July 25, 2025|See Also: [Configuration](/configuration/)|[Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)

* * *

### v1.0.60[​](#v1060 "Direct link to v1.0.60")

-   You can now create custom subagents for specialized tasks! Run /agents to get started

July 24, 2025|See Also: [Task Agent Tools](/mechanics-task-agent-tools/)|[Custom Subagents](https://docs.anthropic.com/en/docs/claude-code-subagents)

* * *

* * *

### v1.0.59[​](#v1059 "Direct link to v1.0.59")

-   SDK: Added tool confirmation support with canUseTool callback
-   SDK: Allow specifying env for spawned process
-   Hooks: Exposed PermissionDecision to hooks (including "ask")
-   Hooks: UserPromptSubmit now supports additionalContext in advanced JSON output
-   Fixed issue where some Max users that specified Opus would still see fallback to Sonnet

July 23, 2025|See Also: [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)|[Hooks](/mechanics-hooks/)

* * *

### v1.0.58[​](#v1058 "Direct link to v1.0.58")

-   Added support for reading PDFs
-   MCP: Improved server health status display in 'claude mcp list'
-   Hooks: Added CLAUDE\_PROJECT\_DIR env var for hook commands

July 23, 2025|See Also: [Hooks](/mechanics-hooks/)|[MCPs](/claude-code-mcps/)

* * *

### v1.0.57[​](#v1057 "Direct link to v1.0.57")

-   Added support for specifying a model in slash commands
-   Improved permission messages to help Claude understand allowed tools
-   Fix: Remove trailing newlines from bash output in terminal wrapping

July 23, 2025|See Also: [Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)|[Auto-Accept Permissions](/mechanics-auto-accept-permissions/)

* * *

### v1.0.56[​](#v1056 "Direct link to v1.0.56")

-   Windows: Enabled shift+tab for mode switching on versions of Node.js that support terminal VT mode
-   Fixes for WSL IDE detection
-   Fix an issue causing awsRefreshHelper changes to .aws directory not to be picked up

July 23, 2025|See Also: [Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Configuration](/configuration/)

* * *

### v1.0.55[​](#v1055 "Direct link to v1.0.55")

-   Clarified knowledge cutoff for Opus 4 and Sonnet 4 models
-   Windows: fixed Ctrl+Z crash
-   SDK: Added ability to capture error logging
-   Add --system-prompt-file option to override system prompt in print mode

July 23, 2025|See Also: [Model Comparison](/model-comparison/)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.54[​](#v1054 "Direct link to v1.0.54")

-   Hooks: Added UserPromptSubmit hook and the current working directory to hook inputs
-   Custom slash commands: Added argument-hint to frontmatter
-   Windows: OAuth uses port 45454 and properly constructs browser URL
-   Windows: mode switching now uses alt + m, and plan mode renders properly
-   Shell: Switch to in-memory shell snapshot to file-related errors

July 19, 2025|See Also: [Hooks](/mechanics-hooks/)|[Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows/)

* * *

### v1.0.53[​](#v1053 "Direct link to v1.0.53")

-   Updated @-mention file truncation from 100 lines to 2000 lines
-   Add helper script settings for AWS token refresh: awsAuthRefresh (for foreground operations like aws sso login) and awsCredentialExport (for background operation with STS-like response).

July 18, 2025|See Also: [Configuration](/configuration/)

* * *

### v1.0.52[​](#v1052 "Direct link to v1.0.52")

-   Added support for MCP server instructions

July 18, 2025|See Also: [MCPs](/claude-code-mcps/)

* * *

### v1.0.51[​](#v1051 "Direct link to v1.0.51")

-   Added support for native Windows (requires Git for Windows)
-   Added support for Bedrock API keys through environment variable AWS\_BEARER\_TOKEN\_BEDROCK
-   Settings: /doctor can now help you identify and fix invalid setting files
-   `--append-system-prompt` can now be used in interactive mode, not just --print/-p.
-   Increased auto-compact warning threshold from 60% to 80%
-   Fixed an issue with handling user directories with spaces for shell snapshots
-   OTEL resource now includes os.type, os.version, host.arch, and wsl.version (if running on Windows Subsystem for Linux)
-   Custom slash commands: Fixed user-level commands in subdirectories
-   Plan mode: Fixed issue where rejected plan from sub-task would get discarded

July 11, 2025|See Also: [Plan Mode](/mechanics-plan-mode/)|[Windows Installation](/faqs/how-to-install-claude-code-on-windows/)|[Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)

* * *

* * *

### v1.0.48[​](#v1048 "Direct link to v1.0.48")

-   Fixed a bug in [v1.0.45](#v1045) where the app would sometimes freeze on launch
-   Added progress messages to Bash tool based on the last 5 lines of command output
-   Added expanding variables support for MCP server configuration
-   Moved shell snapshots from /tmp to ~/.claude for more reliable Bash tool calls
-   Improved IDE extension path handling when Claude Code runs in WSL
-   Hooks: Added a PreCompact hook
-   Vim mode: Added c, f/F, t/T

July 10, 2025|See Also: [Hooks](/mechanics-hooks/)

* * *

### v1.0.45[​](#v1045 "Direct link to v1.0.45")

-   Redesigned Search (Grep) tool with new tool input parameters and features
-   Disabled IDE diffs for notebook files, fixing "Timeout waiting after 1000ms" error
-   Fixed config file corruption issue by enforcing atomic writes
-   Updated prompt input undo to Ctrl+\_ to avoid breaking existing Ctrl+U behavior, matching zsh's undo shortcut
-   Stop Hooks: Fixed transcript path after /clear and fixed triggering when loop ends with tool call
-   Custom slash commands: Restored namespacing in command names based on subdirectories. For example, .claude/frontend/component.md is now /frontend:component, not /component.

July 9, 2025|See Also: [Custom Slash Commands](/faqs/what-is-slash-commands-in-claude-code/)|[Hooks](/mechanics-hooks/)

* * *

### v1.0.44[​](#v1044 "Direct link to v1.0.44")

-   New `/export` command lets you quickly export a conversation for sharing
-   MCP: resource\_link tool results are now supported
-   MCP: tool annotations and tool titles now display in /mcp view
-   Changed Ctrl+Z to suspend Claude Code. Resume by running `fg`. Prompt input undo is now Ctrl+U.

July 7, 2025|See Also: [MCPs](/claude-code-mcps/)|[Suspend/Resume](/faqs/how-to-suspend-claude-code/)

* * *

### v1.0.43[​](#v1043 "Direct link to v1.0.43")

-   Fixed a bug where the theme selector was saving excessively
-   Hooks: Added EPIPE system error handling

July 3, 2025|See Also: [Hooks](/mechanics-hooks/)

* * *

### v1.0.42[​](#v1042 "Direct link to v1.0.42")

-   Added tilde (`~`) expansion support to `/add-dir` command

July 3, 2025|See Also: [/add-dir FAQ](/faqs/--add-dir/)

* * *

### v1.0.41[​](#v1041 "Direct link to v1.0.41")

-   Hooks: Split Stop hook triggering into Stop and SubagentStop
-   Hooks: Enabled optional timeout configuration for each command
-   Hooks: Added "hook\_event\_name" to hook input
-   Fixed a bug where MCP tools would display twice in tool list
-   New tool parameters JSON for Bash tool in `tool_decision` event

See Also: [Hooks](/mechanics-hooks/)

* * *

### v1.0.40[​](#v1040 "Direct link to v1.0.40")

-   Fixed a bug causing API connection errors with UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY if `NODE_EXTRA_CA_CERTS` was set

* * *

* * *

### v1.0.39[​](#v1039 "Direct link to v1.0.39")

-   New Active Time metric in OpenTelemetry logging

July 2, 2025

* * *

### v1.0.38[​](#v1038 "Direct link to v1.0.38")

-   Released [hooks](https://docs.anthropic.com/en/docs/claude-code-hooks). Special thanks to community input in [Github Issues](https://github.com/anthropics/claude-code-issues/712)

July 2, 2025|See Also: [Hooks](/mechanics-hooks/)

* * *

### v1.0.37[​](#v1037 "Direct link to v1.0.37")

-   Remove ability to set `Proxy-Authorization` header via ANTHROPIC\_AUTH\_TOKEN or apiKeyHelper

July 2, 2025

* * *

### v1.0.36[​](#v1036 "Direct link to v1.0.36")

-   Web search now takes today's date into context
-   Fixed a bug where stdio MCP servers were not terminating properly on exit

July 2, 2025|See Also: [MCPs](/claude-code-mcps/)

* * *

### v1.0.35[​](#v1035 "Direct link to v1.0.35")

-   Added support for MCP OAuth Authorization Server discovery

June 25, 2025|See Also: [MCPs](/claude-code-mcps/)

* * *

### v1.0.34[​](#v1034 "Direct link to v1.0.34")

-   Fixed a memory leak causing a MaxListenersExceededWarning message to appear

June 24, 2025

* * *

### v1.0.33[​](#v1033 "Direct link to v1.0.33")

-   Improved logging functionality with session ID support
-   Added undo functionality (Ctrl+Z and vim 'u' command)
-   Improvements to plan mode

June 24, 2025|See Also: [Plan Mode](/mechanics-plan-mode/)

* * *

### v1.0.32[​](#v1032 "Direct link to v1.0.32")

-   Updated loopback config for litellm
-   Added forceLoginMethod setting to bypass login selection screen

June 24, 2025|See Also: [Configuration](/configuration/)

* * *

### v1.0.31[​](#v1031 "Direct link to v1.0.31")

-   Fixed a bug where ~/.claude.json would get reset when file contained invalid JSON

June 24, 2025

* * *

### v1.0.30[​](#v1030 "Direct link to v1.0.30")

-   Custom slash commands: Run bash output, @-mention files, enable thinking with thinking keywords
-   Improved file path autocomplete with filename matching
-   Added timestamps in Ctrl-r mode and fixed Ctrl-c handling
-   Enhanced jq regex support for complex filters with pipes and select

June 24, 2025|See Also: [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-commands)

* * *

* * *

### v1.0.29[​](#v1029 "Direct link to v1.0.29")

-   Improved CJK character support in cursor navigation and rendering

June 24, 2025

* * *

### v1.0.28[​](#v1028 "Direct link to v1.0.28")

-   Slash commands: Fix selector display during history navigation
-   Resizes images before upload to prevent API size limit errors
-   Added XDG\_CONFIG\_HOME support to configuration directory
-   Performance optimizations for memory usage
-   New attributes (terminal.type, language) in OpenTelemetry logging

June 24, 2025|See Also: [Configuration](https://docs.anthropic.com/en/docs/claude-code-settings)

* * *

### v1.0.27[​](#v1027 "Direct link to v1.0.27")

-   Streamable HTTP MCP servers are now supported
-   Remote MCP servers (SSE and HTTP) now support OAuth
-   MCP resources can now be @-mentioned

June 18, 2025|See Also: [MCP Resources](https://docs.anthropic.com/en/docs/claude-code-mcp#use-mcp-resources)

* * *

### v1.0.25[​](#v1025 "Direct link to v1.0.25")

-   Slash commands: moved "project" and "user" prefixes to descriptions
-   Slash commands: improved reliability for command discovery
-   Improved support for Ghostty
-   Improved web search reliability

June 16, 2025|See Also: [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-commands)

* * *

### v1.0.24[​](#v1024 "Direct link to v1.0.24")

-   Improved `/mcp` output
-   Fixed a bug where settings arrays got overwritten instead of merged

June 16, 2025|See Also: [MCPs](/claude-code-mcps/)

* * *

### v1.0.23[​](#v1023 "Direct link to v1.0.23")

-   Released TypeScript SDK: `import @anthropic-ai/claude-code` to get started
-   Released Python SDK: `pip install claude-code-sdk` to get started

June 16, 2025|See Also: [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code-sdk)

* * *

### v1.0.22[​](#v1022 "Direct link to v1.0.22")

-   SDK: Renamed `total_cost` to `total_cost_usd`

June 12, 2025|See Also: [CC Usage](/claude-code-mcps/cc-usage/)

* * *

### v1.0.21[​](#v1021 "Direct link to v1.0.21")

-   Improved editing of files with tab-based indentation
-   Fix for `tool_use` without matching `tool_result` errors
-   Fixed a bug where stdio MCP server processes would linger after quitting Claude Code

June 12, 2025

* * *

* * *

### v1.0.18[​](#v1018 "Direct link to v1.0.18")

-   Added `--add-dir` CLI argument for specifying additional working directories
-   Added streaming input support without require `-p` flag
-   Improved startup performance and session storage performance
-   Added `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` environment variable to freeze working directory for bash commands
-   Added detailed MCP server tools display (`/mcp`)
-   MCP authentication and permission improvements
-   Added auto-reconnection for MCP SSE connections on disconnect
-   Fixed issue where pasted content was lost when dialogs appeared

June 10, 2025|See Also: [Configuration](/configuration/#mcp-configuration.html)|[Additional Working Directories](https://docs.anthropic.com/en/docs/claude-code-common-workflows#additional-working-directories)|[MCPs](/claude-code-mcps/)

* * *

### v1.0.17[​](#v1017 "Direct link to v1.0.17")

-   We now emit messages from sub-tasks in `-p` mode

June 10, 2025

* * *

### v1.0.16[​](#v1016 "Direct link to v1.0.16")

-   Additional improvements and bug fixes (look for the `parent_tool_use_id` property)
-   Fixed crashes when the VS Code diff tool is invoked multiple times quickly
-   MCP server list UI improvements
-   Update Claude Code process title to display `claude` instead of `node`

June 6, 2025

* * *

### v1.0.11[​](#v1011 "Direct link to v1.0.11")

-   Claude Code can now also be used with a Claude Pro subscription
-   Added `/upgrade` for smoother switching to Claude Max plans
-   Improved UI for authentication from API keys and Bedrock/Vertex/external auth tokens
-   Improved shell configuration error handling
-   Improved todo list handling during compaction

June 4, 2025|See Also: [Pricing](/claude-code-pricing/)|[Model Comparison](/model-comparison/)|[Installation](/install-claude-code/)

* * *

### v1.0.10[​](#v1010 "Direct link to v1.0.10")

-   Added markdown table support
-   Improved streaming performance

June 3, 2025

* * *

### v1.0.8[​](#v108 "Direct link to v1.0.8")

-   Fixed Vertex AI region fallback when using `CLOUD_ML_REGION`
-   Increased default otel interval from 1s -> 5s
-   Fixed edge cases where `MCP_TIMEOUT` and `MCP_TOOL_TIMEOUT` weren't being respected
-   Fixed a regression where search tools unnecessarily asked for permissions
-   Added support for triggering thinking non-English languages
-   Improved compacting UI

June 2, 2025|See Also: [Restarting Claude Code](/faqs/restarting-claude-code/)|[Context Window Depletion](/mechanics-context-window-depletion/)

* * *

### v1.0.7[​](#v107 "Direct link to v1.0.7")

-   Renamed `/allowed-tools` -> `/permissions`
-   Migrated `allowedTools` and `ignorePatterns` from `.claude.json` -> `settings.json`
-   Deprecated `claude config` commands in favor of editing `settings.json`
-   Fixed a bug where `--dangerously-skip-permissions` sometimes didn't work in `--print` mode
-   Improved error handling for `/install-github-app`
-   Bugfixes, UI polish, and tool reliability improvements

June 2, 2025|See Also: [Auto-Accept Permissions](/mechanics-auto-accept-permissions/)|[Configuration](/configuration/)

* * *

### v1.0.6[​](#v106 "Direct link to v1.0.6")

-   Improved edit reliability for tab-indented files
-   Respect `CLAUDE_CONFIG_DIR` everywhere
-   Reduced unnecessary tool permission prompts
-   Added support for symlinks in `@file` typeahead
-   Bugfixes, UI polish, and tool reliability improvements

June 2, 2025|See Also: [Configuration](/configuration/)

* * *

### v1.0.4[​](#v104 "Direct link to v1.0.4")

-   Fixed a bug where MCP tool errors weren't being parsed correctly

May 28, 2025

* * *

### v1.0.1[​](#v101 "Direct link to v1.0.1")

-   Added `DISABLE_INTERLEAVED_THINKING` to give users the option to opt out of interleaved thinking
-   Improved model references to show provider-specific names (Sonnet 3.7 for Bedrock, Sonnet 4 for Console)
-   Updated documentation links and OAuth process descriptions

May 22, 2025|See Also: [Configuration](/configuration/)

* * *

* * *

### v1.0.0[​](#v100 "Direct link to v1.0.0")

-   Claude Code is now generally available
-   Introducing Sonnet 4 and Opus 4 models

May 22, 2025|See Also: [Model Comparison](/model-comparison/)|[Installation](/install-claude-code/)|[Getting Started](/claude-code-tutorial/)

* * *

### v0.2.125[​](#v02125 "Direct link to v0.2.125")

-   Breaking change: Bedrock ARN passed to `ANTHROPIC_MODEL` or `ANTHROPIC_SMALL_FAST_MODEL` should no longer contain an escaped slash (specify / instead of %2F)
-   Removed `DEBUG=true` in favor of `ANTHROPIC_LOG=debug`, to log all requests

May 21, 2025|See Also: [Configuration](/configuration/)

* * *

### v0.2.117[​](#v02117 "Direct link to v0.2.117")

-   Breaking change: `--print` JSON output now returns nested message objects, for forwards-compatibility as we introduce new metadata fields
-   Introduced `settings.cleanupPeriodDays`
-   Introduced `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` env var
-   Introduced `--debug` mode

May 18, 2025

* * *

### v0.2.108[​](#v02108 "Direct link to v0.2.108")

-   You can now send messages to Claude while it works to steer Claude in real-time
-   Introduced `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` env vars
-   Fixed a bug where thinking was not working in `-p` mode
-   Fixed a regression in `/cost` reporting
-   Deprecated MCP wizard interface in favor of other MCP commands
-   Lots of other bugfixes and improvements

May 13, 2025

* * *

### v0.2.107[​](#v02107 "Direct link to v0.2.107")

-   `CLAUDE.md` files can now import other files. Add `@path/to/file.md` to `./CLAUDE.md` to load additional files on launch

May 9, 2025|See Also: [CLAUDE.md Supremacy](/mechanics-claude-md-supremacy/)

* * *

### v0.2.106[​](#v02106 "Direct link to v0.2.106")

-   MCP SSE server configs can now specify custom headers
-   Fixed a bug where MCP permission prompt didn't always show correctly

May 9, 2025

* * *

### v0.2.105[​](#v02105 "Direct link to v0.2.105")

-   Claude can now search the web
-   Moved system & account status to `/status`
-   Added word movement keybindings for Vim
-   Improved latency for startup, todo tool, and file edits

May 8, 2025

* * *

### v0.2.102[​](#v02102 "Direct link to v0.2.102")

-   Improved thinking triggering reliability
-   Improved `@mention` reliability for images and folders
-   You can now paste multiple large chunks into one prompt

May 5, 2025

* * *

### v0.2.100[​](#v02100 "Direct link to v0.2.100")

-   Fixed a crash caused by a stack overflow error
-   Made db storage optional; missing db support disables `--continue` and `--resume`

* * *

### v0.2.98[​](#v0298 "Direct link to v0.2.98")

-   Fixed an issue where auto-compact was running twice

May 2, 2025

* * *

### v0.2.95[​](#v0295 "Direct link to v0.2.95")

-   Claude Code can now also be used with a [Claude Max subscription](https://claude.ai/upgrade)
-   Claude Code can now also be used with a [Claude Max subscription](https://claude.ai/upgrade)

May 1, 2025

* * *

### v0.2.93[​](#v0293 "Direct link to v0.2.93")

-   Resume conversations from where you left off from with `claude --continue` and `claude --resume`
-   Claude now has access to a Todo list that helps it stay on track and be more organized

April 30, 2025

* * *

### v0.2.82[​](#v0282 "Direct link to v0.2.82")

-   Added support for `--disallowedTools`
-   Renamed tools for consistency: `LSTool` -> `LS`, `View` -> `Read`, etc.

April 25, 2025|See Also: [Auto-Accept Permissions](/mechanics-auto-accept-permissions/)|[Configuration](/configuration/)

* * *

### v0.2.75[​](#v0275 "Direct link to v0.2.75")

-   Hit Enter to queue up additional messages while Claude is working
-   Drag in or copy/paste image files directly into the prompt
-   `@-mention` files to directly add them to context
-   Run one-off MCP servers with `claude --mcp-config &lt;path-to-file&gt;`
-   Improved performance for filename auto-complete

April 21, 2025|See Also: [MCPs & Add-ons](/claude-code-mcps/)|[Configuration](/configuration/#mcp-configuration.html)

* * *

### v0.2.7[​](#v027 "Direct link to v0.2.7")

-   Additional updates and fixes
-   Added support for refreshing dynamically generated API keys (via `apiKeyHelper`), with a 5 minute TTL
-   Task tool can now perform writes and run bash commands

April 17, 2025

* * *

### v0.2.72[​](#v0272 "Direct link to v0.2.72")

-   Updated spinner to indicate tokens loaded and tool usage

April 18, 2025

* * *

### v0.2.70[​](#v0270 "Direct link to v0.2.70")

-   Network commands like `curl` are now available for Claude to use
-   Claude can now run multiple web queries in parallel
-   Pressing ESC once immediately interrupts Claude in Auto-accept mode

* * *

### v0.2.69[​](#v0269 "Direct link to v0.2.69")

-   Fixed UI glitches with improved Select component behavior
-   Enhanced terminal output display with better text truncation logic

* * *

### v0.2.67[​](#v0267 "Direct link to v0.2.67")

-   Shared project permission rules can be saved in `.claude/settings.json`

* * *

### v0.2.66[​](#v0266 "Direct link to v0.2.66")

-   Print mode (`-p`) now supports streaming output via `--output-format=stream-json`
-   Fixed issue where pasting could trigger memory or bash mode unexpectedly

* * *

### v0.2.63[​](#v0263 "Direct link to v0.2.63")

-   Fixed an issue where MCP tools were loaded twice, which caused tool call errors

* * *

### v0.2.61[​](#v0261 "Direct link to v0.2.61")

-   Navigate menus with vim-style keys (`j`/`k`) or bash/emacs shortcuts (`Ctrl+n`/`p`) for faster interaction
-   Enhanced image detection for more reliable clipboard paste functionality
-   Fixed an issue where ESC key could crash the conversation history selector

* * *

### v0.2.59[​](#v0259 "Direct link to v0.2.59")

-   Copy+paste images directly into your prompt
-   Improved progress indicators for bash and fetch tools
-   Bugfixes for non-interactive mode (`-p`)

* * *

### v0.2.54[​](#v0254 "Direct link to v0.2.54")

-   Quickly add to Memory by starting your message with `#`
-   Press `ctrl+r` to see full output for long tool results
-   Added support for MCP SSE transport

* * *

### v0.2.53[​](#v0253 "Direct link to v0.2.53")

-   New web fetch tool lets Claude view URLs that you paste in
-   Fixed a bug with JPEG detection

* * *

### v0.2.50[​](#v0250 "Direct link to v0.2.50")

-   New MCP "project" scope now allows you to add MCP servers to `.mcp.json` files and commit them to your repository

* * *

### v0.2.49[​](#v0249 "Direct link to v0.2.49")

-   Previous MCP server scopes have been renamed: previous "project" scope is now "local" and "global" scope is now "user"

* * *

### v0.2.47[​](#v0247 "Direct link to v0.2.47")

-   Press Tab to auto-complete file and folder names
-   Press Shift + Tab to toggle auto-accept for file edits
-   Automatic conversation compaction for infinite conversation length (toggle with `/config`)

See Also: [Auto-Accept Permissions](/mechanics-auto-accept-permissions/)

* * *

### v0.2.44[​](#v0244 "Direct link to v0.2.44")

-   Ask Claude to make a plan with thinking mode: just say 'think' or 'think harder' or even 'ultrathink'

* * *

### v0.2.41[​](#v0241 "Direct link to v0.2.41")

-   MCP server startup timeout can now be configured via `MCP_TIMEOUT` environment variable
-   MCP server startup no longer blocks the app from starting up

* * *

### v0.2.37[​](#v0237 "Direct link to v0.2.37")

-   New `/release-notes` command lets you view release notes at any time
-   `claude config add/remove` commands now accept multiple values separated by commas or spaces

* * *

### v0.2.36[​](#v0236 "Direct link to v0.2.36")

-   Import MCP servers from Claude Desktop with `claude mcp add-from-claude-desktop`
-   Add MCP servers as JSON strings with `claude mcp add-json &lt;n&gt; &lt;json&gt;`

April 21, 2025|See Also: [MCPs & Add-ons](/claude-code-mcps/)|[Configuration](/configuration/#mcp-configuration.html)

* * *

### v0.2.34[​](#v0234 "Direct link to v0.2.34")

-   Vim bindings for text input - enable with `/vim` or `/config`

* * *

### v0.2.32[​](#v0232 "Direct link to v0.2.32")

-   Interactive MCP setup wizard: Run `claude mcp add` to add MCP servers with a step-by-step interface
-   Fix for some PersistentShell issues

* * *

### v0.2.31[​](#v0231 "Direct link to v0.2.31")

-   Custom slash commands: Markdown files in `.claude/commands/` directories now appear as custom slash commands to insert prompts into your conversation
-   MCP debug mode: Run with `--mcp-debug` flag to get more information about MCP server errors

See Also: [CLAUDE.md Supremacy](/mechanics-claude-md-supremacy/) | [Slash Commands](https://docs.anthropic.com/en/docs/claude-code-slash-commands)

* * *

### v0.2.30[​](#v0230 "Direct link to v0.2.30")

-   Added ANSI color theme for better terminal compatibility
-   Fixed issue where slash command arguments weren't being sent properly
-   (Mac-only) API keys are now stored in macOS Keychain

* * *

### v0.2.26[​](#v0226 "Direct link to v0.2.26")

-   New `/approved-tools` command for managing tool permissions
-   Word-level diff display for improved code readability
-   Fuzzy matching for slash commands

April 21, 2025|See Also: [Auto-Accept Permissions](/mechanics-auto-accept-permissions/)|[Configuration](/configuration/)

* * *

### v0.2.21[​](#v0221 "Direct link to v0.2.21")

-   Fuzzy matching for `/commands`

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