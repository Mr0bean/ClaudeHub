---
title: "Claude Code 配置指南"
---

# Claude Code 配置指南

完整的 Claude Code 配置指南，包含 API 密钥设置、模型选择、MCP 服务器、工具权限和多目录工作流的详细配置指导。优化 AI 开发体验的必备设置。

* * *

* * *

## API 密钥设置[​](#api-key-setup "Direct link to API Key Setup")

Claude Code 需要 Anthropic API 密钥才能运行。使用以下方法之一进行设置：

```bash
# 选项 1: 环境变量（推荐）

export ANTHROPIC_API_KEY="your-api-key-here"

# 选项 2: 添加到 shell 配置文件

echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc

source ~/.bashrc

```

* * *

* * *

## 模型选择[​](#model-selection "Direct link to Model Selection")

Claude Code 支持多种模型。您可以指定要使用的模型：

**Claude 4 Sonnet:** 最新的平衡性能和速度

```bash
export ANTHROPIC_MODEL="claude-sonnet-4-20250514"

```

**Claude 4.1 Opus:** 最新的最高性能，具有增强的编码和调试能力

```bash
export ANTHROPIC_MODEL="claude-opus-4-1-20250805"

```

**Claude 4 Opus:** 上一代最高性能模型

```bash
export ANTHROPIC_MODEL="claude-opus-4-20250514"

```

**Claude 3.5 Haiku:** 最快速且最经济实惠

```bash
export ANTHROPIC_MODEL="claude-3-5-haiku-20241022"

```

重要限制：Claude 3.5 Haiku

虽然 Haiku 价格实惠，但在 Claude Code 使用中有显著限制：

-   **推理能力有限** - 在复杂的多步骤规划和架构决策方面存在困难
-   **上下文理解有限** - 在分析大型代码库和跨多文件维护上下文方面效果较差
-   **代码分析简化** - 可能错过现代模型能捕获的细微错误、依赖关系或复杂模式
-   **仅限基础重构** - 不适合复杂的重构或功能实现
-   **框架知识有限** - 在处理复杂框架或新颖编码模式时效果较差

**Haiku 推荐使用场景：**

-   简单的单文件编辑
-   基础语法修正
-   快速代码询问
-   在升级前学习 Claude Code 基础知识

对于严肃的开发工作，Claude 4 Sonnet 或 Opus 能提供显著更好的结果，值得额外投资。

**替代方法：** 您也可以在启动 Claude Code 时直接指定模型：

```bash
claude --model claude-sonnet-4-20250514

claude --model claude-opus-4-1-20250805

claude --model claude-opus-4-20250514

claude --model claude-3-5-haiku-20241022

```

* * *

* * *

## Model Switching During Session[​](#model-switching-during-session "Direct link to Model Switching During Session")

You can switch models mid-session using the `/model` command, which provides an interactive menu:

```bash
/model

```

**Available Options:**

1.  **Default (recommended)** - Opus 4.1 for up to 20% of usage limits, then use Sonnet 4
2.  **Opus** - Opus 4.1 for complex tasks (reaches usage limits faster)
3.  **Sonnet** - Sonnet 4 for daily use
4.  **Opus Plan Mode** - Use Opus 4.1 in plan mode, Sonnet 4 otherwise ✔

The Opus Plan Mode automatically switches between models based on context, using Opus 4.1 for research and planning phases, then Sonnet 4 for implementation and execution.

* * *

* * *

## MCP Configuration[​](#mcp-configuration "Direct link to MCP Configuration")

Model Context Protocol (MCP) allows Claude Code to connect to external tools and services. Configure MCP servers to extend Claude's capabilities:

#### MCP Server Setup[​](#mcp-server-setup "Direct link to MCP Server Setup")

MCP configuration can be stored in multiple locations:

-   **Project-specific:** `.claude/settings.local.json` (in your project directory)
-   **User-specific local:** `~/.claude/settings.local.json`
-   **User-specific global:** `~/.claude/settings.json`
-   **Main Claude.json:** `~/.claude.json`
-   **Dedicated MCP file:** `~/.claude/mcp_servers.json`

Example MCP configuration:

```bash
// Example: ~/.claude.json (recommended for reliability)

{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "filesystem": {

          "command": "npx",

          "args": "-y", "@modelcontextprotocol/server-filesystem", "/Users/username/Desktop", "/path/to/allowed/dir"
        },

        "memory": {

          "command": "npx",

          "args": "-y", "@modelcontextprotocol/server-memory"
        },

        "fetch": {

          "command": "npx",

          "args": "-y", "@modelcontextprotocol/server-fetch"
        }

      }

    }

  },

  ...

}

```

**Note:** If following this example ensure you update the right projects configuration.

For additional tools and integrations beyond MCP, explore our [Add-ons](/claude-code-mcps.html).

* * *

* * *

## Allowed Tools[​](#allowed-tools "Direct link to Allowed Tools")

#### Allowed Tools Setup[​](#allowed-tools-setup "Direct link to Allowed Tools Setup")

Allowed tools configuration can be stored in multiple locations:

-   **Project-specific:** `.claude/settings.local.json` (in your project directory)
-   **User-specific local:** `~/.claude/settings.local.json`
-   **User-specific global:** `~/.claude/settings.json`
-   **Main Claude.json:** `~/.claude.json`

#### Example Allowed Tools configuration:[​](#example-allowed-tools-configuration "Direct link to Example Allowed Tools configuration:")

```bash
// Example: ~/.claude.json (recommended for reliability)

{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "filesystem": {

          "command": "npx",

          "args": "-y", "@modelcontextprotocol/server-filesystem", "/Users/username/Desktop", "/path/to/allowed/dir"
        }

      },

      "allowedTools": 

        "Task",

        "Bash",                    // ⚠️ Dangerous: allows all system commands

        "Bash(git log:*)",   // Safer: only allows git log commands

        "Glob",

        "Grep",

        "LS",

        "Read",

        "Edit",

        "MultiEdit",

        "Write",

        "WebFetch",

        "WebSearch"

      
    }

  },

  ...

}

```

**Note:** If following this example ensure you update the right projects configuration.

#### Interactive Permission Management[​](#interactive-permission-management "Direct link to Interactive Permission Management")

For a more user-friendly approach to managing tool permissions, use the `/permissions` command within Claude Code:

```bash
# Launch the interactive permissions UI

/permissions

```

This advanced interface allows you to:

-   **View current permissions** - See which tools are currently allowed or denied
-   **Explicitly allow tools** - Grant permission to specific tools or tool patterns
-   **Explicitly deny tools** - Block access to tools you want to restrict
-   **Navigate visually** - Use an intuitive UI instead of manually editing JSON files

The `/permissions` interface provides real-time permission management with a fluid, responsive experience that makes configuration changes effortless—no need to restart Claude Code or manually edit configuration files.

tip

Multiple configuration locations exist due to legacy compatibility - you might encounter different file names and directory locations.

**Recommendation:** Use `~/.claude.json` for reliability as shown in the examples above.

* * *

* * *

## Additional Working Directories / Extended Workspace[​](#additional-working-directories--extended-workspace "Direct link to Additional Working Directories / Extended Workspace")

Claude Code can access multiple directories beyond your current working directory using:

-   **CLI argument:** `--add-dir` (added in [v1.0.18](/claude-code-changelog/#v1018.html)) when starting Claude Code
-   **Slash command:** `/add-dir` mid-session for seamless workflow expansion

This allows you to work across multiple projects or reference external resources without changing directories or restarting your session.

### Usage[​](#usage "Direct link to Usage")

**CLI Argument (at startup):**

```bash
# Add a single additional directory

claude --add-dir /path/to/other/project

# Combine with other options

claude --add-dir ~/shared/libraries

# Use with print mode for scripting

claude --add-dir ../backend -p "Validate that API calls in the current directory match endpoints defined in ../backend"

```

**Slash Command (mid-session):**

```bash
# Add directory without restarting your session

/add-dir /path/to/other/project

# Add multiple directories as needed

/add-dir ~/shared/libraries

/add-dir ../backend-api

```

### Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

**Multi-Repository Projects**

```bash
# At startup: Work on frontend while referencing the backend API

claude --add-dir ../backend-api

# Mid-session: Add backend when you need to reference API endpoints

/add-dir ../backend-api

```

**Shared Resources**

```bash
# At startup: Access shared configs or documentation

claude --add-dir ~/company/shared-configs

# Mid-session: Add shared resources when needed

/add-dir ~/company/shared-configs

```

**Dynamic Workflow expansion**

```bash
# Start with current project, then expand as needed

# No need to restart when you realize you need additional context

/add-dir ../related-service

/add-dir ~/templates

```

**Note:** The current working directory is always included. CLAUDE.md files appear to not be read in automatically from additional directories added via `--add-dir`.

Better Workflow Orchestration

This feature significantly improves workflow orchestration by enabling Claude to:

-   **Work across repositories** simultaneously—maintaining context and applying consistent changes
-   **Reference shared code** directly from libraries or configuration repositories
-   **Temporarily expose** a codebase for Claude to analyze or modify without changing directories
-   **Expand workspace dynamically** using `/add-dir` without interrupting your current session

The `/add-dir` slash command makes this particularly seamless—you can start focused on one project and organically expand your workspace as needs emerge, without losing context or restarting. Instead of juggling multiple sessions or copying files, you can compose multiple repositories within the same workflow structure—orchestrating complex multi-repository operations in a single, context-aware session.

##### Configuration Mastery

Proper configuration is the foundation of effective Claude Code usage. Understanding these settings enables sophisticated workflows and unlocks the full potential of AI-assisted development.

<img src="/img/discovery/009.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Pricing Plans](/claude-code-pricing.html)|[CLAUDE.md Guide](/mechanics-claude-md-supremacy.html)|[MCPs & Add-ons](/claude-code-mcps.html)|[FAQs](/faq.html)

-   [API Key Setup](#api-key-setup)
-   [Model Selection](#model-selection)
-   [Model Switching During Session](#model-switching-during-session)
-   [MCP Configuration](#mcp-configuration)
-   [Allowed Tools](#allowed-tools)
-   [Additional Working Directories / Extended Workspace](#additional-working-directories--extended-workspace)
    -   [Usage](#usage)
    -   [Common Use Cases](#common-use-cases)