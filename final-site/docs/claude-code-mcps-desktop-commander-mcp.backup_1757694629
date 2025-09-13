---
title: "桌面指挥官 MCP | ClaudeLog"
---

# 桌面指挥官 MCP | ClaudeLog

**通过 MCP 集成实现终端命令、文件操作和跨平台工作流管理的全面系统控制和开发自动化服务器。**

**作者**: [wonderwhy-er](https://github.com/wonderwhy-er)  |  [GitHub 仓库](https://github.com/wonderwhy-er/DesktopCommanderMCP)  |  4.3k 星标|475 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

桌面指挥官 MCP 通过模型上下文协议提供全面的系统级控制和开发自动化。它使 AI 模型能够执行终端命令、执行文件操作、分析数据，并跨 Windows、macOS 和 Linux 平台管理开发工作流。该服务器将 AI 助手转化为功能强大的系统自动化工具，同时保持安全边界。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **终端命令执行** - 直接从 AI 对话中运行 shell 命令、脚本和系统实用程序
-   **跨平台文件操作** - 跨操作系统的文件读取、写入、搜索和操作
-   **多语言代码执行** - 支持 Python、JavaScript、shell 脚本和其他语言
-   **数据分析能力** - CSV 处理、统计分析和数据转换工具
-   **开发工作流自动化** - Git 操作、构建过程和部署脚本
-   **安全控制** - 可配置的权限系统和命令验证

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   Node.js 18.0.0+ 用于 MCP 服务器功能
-   npm 包管理器
-   兼容的 MCP 客户端（Claude Desktop、VS Code、Cursor）

**推荐安装（自动更新）**

```bash
# 使用 npx 快速设置（推荐）

npx @wonderwhy-er/desktop-commander@latest setup

# 调试模式（如需要）

npx @wonderwhy-er/desktop-commander@latest setup --debug

```

**手动配置**

```bash
{

  "mcpServers": {

    "desktop-commander": {

      "command": "npx",

      "args": [

        "-y",

        "@wonderwhy-er/desktop-commander"

      ]

    }

  }

}

```

**替代安装方法**

```bash
# macOS bash 脚本安装

curl -fsSL https://raw.githubusercontent.com/wonderwhy-er/DesktopCommanderMCP/refs/heads/main/install.sh | bash

# Smithery CLI 安装

npx -y @smithery/cli install @wonderwhy-er/desktop-commander --client claude

# 本地开发设置

git clone https://github.com/wonderwhy-er/DesktopCommanderMCP.git

cd DesktopCommanderMCP

npm run setup

```

**配置位置**

-   **macOS**: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
-   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
-   **Linux**: `~/.config/Claude/claude_desktop_config.json`

**注意**: 安装后重启 Claude Desktop。配置在服务器重启间保持。

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**系统管理**

```bash
# AI 交互示例：

# "检查系统磁盘使用情况并清理临时文件"

# "监控运行中的进程并识别高 CPU 使用率"

# "为项目目录创建备份脚本"

# "更新系统包并重启服务"

```

该服务器通过对话式 AI 界面实现自然语言系统管理和开发自动化。你可以管理文件、执行复杂工作流、分析系统性能，并自动化重复性任务。

**开发工作流**

-   **代码分析**: 分析代码库、生成报告并识别模式
-   **构建自动化**: 执行构建脚本、运行测试并部署应用程序
-   **Git 操作**: 提交更改、管理分支并处理合并冲突
-   **数据处理**: 解析日志、处理 CSV 文件并生成洞察

* * *

##### 社区见解

桌面指挥官 MCP 为开发者提供经济有效的系统自动化。用户反馈"以极小的价格获得类似 Claude Code 的功能"，具有出色的跨平台支持。

<img src="/img/discovery/023_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*桌面指挥官 MCP 由 wonderwhy-er 开发，是开源项目。如需技术支持、功能请求和社区贡献，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)