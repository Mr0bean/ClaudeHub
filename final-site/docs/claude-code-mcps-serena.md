---
title: "Serena | Claude Hub"
---

# Serena | Claude Hub

**强大的免费 AI 编程代理工具包，提供语义代码检索、智能编辑和语言服务器集成，作为昂贵编程助手的替代方案。**

**作者**: [oraios](https://github.com/oraios)  |  [GitHub 仓库](https://github.com/oraios/serena)  |  9.8k 星标|676 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

Serena 是一个全面的 AI 编程代理工具包，通过语言服务器集成提供语义代码理解和智能编辑功能。作为 Cursor 和 Windsurf 等昂贵编程助手的免费替代方案，它通过与 Claude Code 和其他 AI 平台的 MCP 集成提供符号级代码理解、多语言支持和高级项目分析。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **语义代码检索** - 通过语言服务器集成和符号分析实现高级代码理解
-   **符号级智能** - 跨代码库的函数、类和变量级理解
-   **多语言支持** - 支持 Python、JavaScript、TypeScript、Rust、Go 等 8+ 种编程语言
-   **类 IDE 功能** - 通过 AI 交互提供 IDE 级功能，无需复杂设置
-   **MCP 集成** - 与 Claude Code 和其他兼容 MCP 的 AI 客户端无缝集成
-   **免费开源** - 无订阅费用或使用限制，社区驱动的开发

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   Python 3.11+（特别地，不是 3.12+）与 uv 包管理器
-   用于仓库克隆的 Git
-   目标编程语言的语言服务器（自动安装）
-   Claude Code 或兼容的 MCP 客户端

**推荐安装（UVX）**

```bash
# 从 GitHub 直接执行（推荐用于 MCP）

# Windows:

uvx --from git+https://github.com/oraios/serena serena-mcp-server.exe

# Linux/macOS:

uvx --from git+https://github.com/oraios/serena serena-mcp-server

```

**MCP 配置**

```bash
{

  "mcpServers": {

    "serena": {

      "command": "uvx",

      "args": 

        "--from",

        "git+https://github.com/oraios/serena",

        "serena-mcp-server"

      
    }

  }

}

```

**替代方案：本地开发设置**

```bash
# 1. 克隆仓库（必需）

git clone https://github.com/oraios/serena

cd serena

# 2. 可选：复制配置模板

cp src/serena/resources/serena_config.template.yml serena_config.yml

# 3. 运行 MCP 服务器

uv run serena-mcp-server

```

**本地安装的 MCP 配置**

```bash
{

  "mcpServers": {

    "serena": {

      "command": "/absolute/path/to/uv",

      "args": 

        "run",

        "--directory",

        "/absolute/path/to/serena",

        "serena-mcp-server"

      
    }

  }

}

```

**语言服务器设置**

```bash
# Serena 自动为以下语言安装语言服务器：

# Python (pylsp)、JavaScript/TypeScript (typescript-language-server)

# Rust (rust-analyzer)、Go (gopls) 及其他 8+ 种语言

# 无需手动配置

```

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**语义代码分析**

```bash
# 通过 Claude Code 的 AI 交互示例：

# "分析此项目中的身份验证流程"

# "找出所有处理用户数据验证的函数"

# "解释这些类之间的关系"

# "重构此模块以改善关注点分离"

```

Serena 提供深度代码理解，超越简单的文本分析。它通过语言服务器集成理解代码结构、关系和语义，通过自然语言交互实现复杂的代码分析和智能编辑建议。

**高级功能**

-   **项目理解**: 分析整个代码库并理解架构模式
-   **智能编辑**: 基于语义理解进行精确的代码更改
-   **交叉引用分析**: 跟踪函数调用、导入和依赖关系
-   **代码质量评估**: 识别潜在问题和改进机会

* * *

##### 社区见解

Serena 已成为受欢迎的免费替代方案，用户反馈"在没有订阅费用的情况下获得 Cursor/Windsurf 90% 的功能"。用户称赞其代码理解能力。

<img src="/img/discovery/025.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Serena 由 oraios 开发，是开源项目。如需技术支持、语言服务器配置和社区贡献，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)