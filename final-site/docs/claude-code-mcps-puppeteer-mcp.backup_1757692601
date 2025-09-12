---
title: "Puppeteer MCP | ClaudeLog"
---

# Puppeteer MCP | ClaudeLog

**为 Claude Code 提供 AI 视觉能力的网页自动化工具**

**作者**: [模型上下文协议](https://github.com/modelcontextprotocol)  |  [GitHub 仓库](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)  |  65.5k 星标|7.7k 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

Puppeteer MCP 通过模型上下文协议为 Claude Code 带来强大的网页自动化功能。控制无头 Chrome 浏览器，抓取动态内容，并通过 AI 视觉能力自动化复杂的网页工作流，自动处理 cookie、验证码和交互元素。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **AI 视觉集成** - 自动处理 cookie、验证码和交互元素
-   **无头浏览器控制** - 以编程方式启动和控制 Chrome/Chromium 实例
-   **动态内容抓取** - 从 JavaScript 重度和 SPA 应用程序中提取数据
-   **高质量 Markdown** - 将网页转换为格式良好的 markdown
-   **截图和 PDF 生成** - 捕获视觉内容并生成文档
-   **表单自动化** - 填写表单、提交数据并处理用户交互

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   安装 Chrome 或 Chromium 浏览器（NPX 方法自动安装）

**设置 MCP 服务器**

```bash
# 通过 NPX 安装（推荐）

npx -y @modelcontextprotocol/server-puppeteer

```

**Claude Code 配置**

```bash
{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "puppeteer": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-puppeteer"]

        }

      }

    }

  }

}

```

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**基础网页自动化**

```bash
# 通过 AI 视觉导航和提取内容

claude "浏览产品页面并提取所有价格信息"

# 自动处理复杂交互

claude "导航登录表单并提取用户仪表板数据"

```

**高级自动化**

```bash
# AI 驱动的表单填写

claude "填写注册表单并处理任何验证码"

# Markdown 转换

claude "将文档页面转换为高质量的 markdown"

```

有关详细的自动化示例和 API 参考，请参考[官方文档](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)。

##### 社区反馈

开发者发现 Puppeteer MCP 对于基础抓取工具无法处理的复杂网页交互非常有价值。特别适用于导航动态内容、JavaScript 重度网站和自动化多步骤工作流。

<img src="/img/discovery/018.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Puppeteer MCP 是官方模型上下文协议服务器的一部分，采用 MIT 许可证。如需技术支持和更新，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)