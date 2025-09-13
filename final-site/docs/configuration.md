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

## 会话中切换模型[​](#model-switching-during-session "Direct link to Model Switching During Session")

您可以使用 `/model` 命令在会话中切换模型，它提供了一个交互式菜单：

```bash
/model

```

**可用选项：**

1.  **默认（推荐）** - Opus 4.1 用于高达 20% 的使用限制，然后使用 Sonnet 4
2.  **Opus** - Opus 4.1 用于复杂任务（更快达到使用限制）
3.  **Sonnet** - Sonnet 4 用于日常使用
4.  **Opus 规划模式** - 在规划模式下使用 Opus 4.1，其他情况下使用 Sonnet 4 ✔

Opus 规划模式根据上下文自动切换模型，在研究和规划阶段使用 Opus 4.1，然后在实施和执行阶段使用 Sonnet 4。

* * *

* * *

## MCP 配置[​](#mcp-configuration "Direct link to MCP Configuration")

模型上下文协议（MCP）允许 Claude Code 连接到外部工具和服务。配置 MCP 服务器以扩展 Claude 的功能：

#### MCP 服务器设置[​](#mcp-server-setup "Direct link to MCP Server Setup")

MCP 配置可以存储在多个位置：

-   **项目特定：** `.claude/settings.local.json`（在您的项目目录中）
-   **用户特定本地：** `~/.claude/settings.local.json`
-   **用户特定全局：** `~/.claude/settings.json`
-   **主 Claude.json：** `~/.claude.json`
-   **专用 MCP 文件：** `~/.claude/mcp_servers.json`

MCP 配置示例：

```bash
// 示例：~/.claude.json（推荐以确保可靠性）

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

**注意：** 如果遵循此示例，请确保更新正确的项目配置。

有关 MCP 之外的其他工具和集成，请探索我们的[插件](/claude-code-mcps.html)。

* * *

* * *

## 允许的工具[​](#allowed-tools "Direct link to Allowed Tools")

#### 允许的工具设置[​](#allowed-tools-setup "Direct link to Allowed Tools Setup")

允许的工具配置可以存储在多个位置：

-   **项目特定：** `.claude/settings.local.json`（在您的项目目录中）
-   **用户特定本地：** `~/.claude/settings.local.json`
-   **用户特定全局：** `~/.claude/settings.json`
-   **主 Claude.json：** `~/.claude.json`

#### 允许的工具配置示例：[​](#example-allowed-tools-configuration "Direct link to Example Allowed Tools configuration:")

```bash
// 示例：~/.claude.json（推荐以确保可靠性）

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

        "Bash",                    // ⚠️ 危险：允许所有系统命令

        "Bash(git log:*)",   // 更安全：仅允许 git log 命令

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

**注意：** 如果遵循此示例，请确保更新正确的项目配置。

#### 交互式权限管理[​](#interactive-permission-management "Direct link to Interactive Permission Management")

要以更用户友好的方式管理工具权限，请在 Claude Code 中使用 `/permissions` 命令：

```bash
# 启动交互式权限 UI

/permissions

```

这个高级界面允许您：

-   **查看当前权限** - 查看当前允许或拒绝的工具
-   **明确允许工具** - 授予特定工具或工具模式的权限
-   **明确拒绝工具** - 阻止访问您想要限制的工具
-   **可视化导航** - 使用直观的 UI 而不是手动编辑 JSON 文件

`/permissions` 界面提供实时权限管理，具有流畅、响应式的体验，使配置更改变得轻松自如——无需重启 Claude Code 或手动编辑配置文件。

提示

由于遗留兼容性，存在多个配置位置 - 您可能会遇到不同的文件名和目录位置。

**建议：** 如上面示例所示，使用 `~/.claude.json` 以确保可靠性。

* * *

* * *

## 额外工作目录 / 扩展工作空间[​](#additional-working-directories--extended-workspace "Direct link to Additional Working Directories / Extended Workspace")

Claude Code 可以访问当前工作目录之外的多个目录，使用：

-   **CLI 参数：** `--add-dir`（在 [v1.0.18](/claude-code-changelog/#v1018.html) 中添加）启动 Claude Code 时使用
-   **斜杠命令：** `/add-dir` 在会话中无缝扩展工作流

这允许您跨多个项目工作或引用外部资源，而无需更改目录或重启会话。

### 用法[​](#usage "Direct link to Usage")

**CLI 参数（启动时）：**

```bash
# 添加单个额外目录

claude --add-dir /path/to/other/project

# 与其他选项组合

claude --add-dir ~/shared/libraries

# 与打印模式一起用于脚本编写

claude --add-dir ../backend -p "验证当前目录中的 API 调用是否与 ../backend 中定义的端点匹配"

```

**斜杠命令（会话中）：**

```bash
# 无需重启会话即可添加目录

/add-dir /path/to/other/project

# 根据需要添加多个目录

/add-dir ~/shared/libraries

/add-dir ../backend-api

```

### 常见用例[​](#common-use-cases "Direct link to Common Use Cases")

**多仓库项目**

```bash
# 启动时：在处理前端的同时引用后端 API

claude --add-dir ../backend-api

# 会话中：当需要引用 API 端点时添加后端

/add-dir ../backend-api

```

**共享资源**

```bash
# 启动时：访问共享配置或文档

claude --add-dir ~/company/shared-configs

# 会话中：需要时添加共享资源

/add-dir ~/company/shared-configs

```

**动态工作流扩展**

```bash
# 从当前项目开始，然后根据需要扩展

# 当您意识到需要额外上下文时无需重启

/add-dir ../related-service

/add-dir ~/templates

```

**注意：** 当前工作目录始终包含在内。通过 `--add-dir` 添加的额外目录中的 CLAUDE.md 文件似乎不会自动读取。

更好的工作流编排

此功能通过使 Claude 能够实现以下功能，显著改善了工作流编排：

-   **跨仓库工作** 同时进行—维护上下文并应用一致的更改
-   **直接引用共享代码** 从库或配置仓库
-   **临时暴露** 代码库供 Claude 分析或修改，而无需更改目录
-   **动态扩展工作空间** 使用 `/add-dir` 而不中断当前会话

`/add-dir` 斜杠命令使这一切特别无缝—您可以从专注于一个项目开始，并随着需求的出现有机地扩展您的工作空间，而不会失去上下文或重启。您可以在同一工作流结构中组合多个仓库，而不是处理多个会话或复制文件—在单个上下文感知会话中编排复杂的多仓库操作。

##### 配置精通

正确的配置是有效使用 Claude Code 的基础。理解这些设置可以实现复杂的工作流，并释放 AI 辅助开发的全部潜力。

<img src="/img/discovery/009.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**: [定价计划](/claude-code-pricing.html)|[CLAUDE.md 指南](/mechanics-claude-md-supremacy.html)|[MCP 与插件](/claude-code-mcps.html)|[常见问题](/faq.html)

-   [API 密钥设置](#api-key-setup)
-   [模型选择](#model-selection)
-   [会话中切换模型](#model-switching-during-session)
-   [MCP 配置](#mcp-configuration)
-   [允许的工具](#allowed-tools)
-   [额外工作目录 / 扩展工作空间](#additional-working-directories--extended-workspace)
    -   [用法](#usage)
    -   [常见用例](#common-use-cases)