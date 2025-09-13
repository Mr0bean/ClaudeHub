---
title: "Browser Tools MCP | ClaudeLog"
---

# Browser Tools MCP | ClaudeLog

**全面的浏览器自动化和监控工具包，通过 MCP 集成提供实时网页调试、性能分析和自动化测试。**

**作者**: [AgentDeskAI](https://github.com/AgentDeskAI)  |  [GitHub 仓库](https://github.com/AgentDeskAI/browser-tools-mcp)  |  6.3k Stars|468 Forks|MIT License|Updated Aug 24, 2025

* * *

### 概述[​](#overview "Direct link to Overview")

Browser Tools MCP 通过模型上下文协议集成提供了一套全面的浏览器自动化和监控工具。它能够实现实时浏览器日志监控、自动化性能分析，以及用于网页开发工作流程的无缝 IDE 集成。该服务器将浏览器自动化功能与详细的调试工具相结合，提升开发生产力。

* * *

* * *

### 功能特性[​](#features "Direct link to Features")

-   **实时浏览器监控** - 直接从 IDE 监控控制台日志、网络请求和错误
-   **全面的审计套件** - 通过 Lighthouse 集成实现 SEO、性能、可访问性分析
-   **Chrome 扩展集成** - 用于无缝数据收集和自动粘贴功能的浏览器扩展
-   **WCAG 合规性检查** - 自动化可访问性测试和合规报告
-   **Cursor 集成** - 主要为 Cursor 设计，具有自动粘贴功能
-   **自动化测试** - 基于 Puppeteer 的端到端测试场景自动化

* * *

* * *

### 安装[​](#installation "Direct link to Installation")

**前置要求**

-   Node.js 14 或更高版本
-   Chrome 浏览器用于扩展功能
-   兼容 MCP 的 IDE（推荐 Cursor、VS Code、Claude Desktop）

**Chrome 扩展设置**

1.  从以下地址下载扩展 ZIP 文件：[https://github.com/AgentDeskAI/browser-tools-mcp/releases/download/v1.2.0/BrowserTools-1.2.0-extension.zip](https://github.com/AgentDeskAI/browser-tools-mcp/releases/download/v1.2.0/BrowserTools-1.2.0-extension.zip)
2.  解压 ZIP 文件
3.  打开 Chrome → 扩展程序 → 启用"开发者模式"
4.  点击"加载已解压的扩展程序"并选择解压后的扩展文件夹
5.  启用扩展以使用浏览器自动化功能

**MCP 服务器设置**

```bash
# 安装并运行 MCP 服务器（终端 1）

npx @agentdeskai/browser-tools-mcp@1.2.0

# 启动本地服务器（终端 2）

npx @agentdeskai/browser-tools-server@1.2.0

```

**Claude Desktop 配置**

```bash
{

  "mcpServers": {

    "browser-tools": {

      "command": "npx",

      "args": ["@agentdeskai/browser-tools-mcp@1.2.0"]

    }

  }

}

```

**重要说明**

-   同时保持两个服务器运行
-   确保只打开一个 Chrome DevTools 面板
-   如果出现连接问题，请重启 Chrome

* * *

* * *

### 使用方法[​](#usage "Direct link to Usage")

**开发工作流程**

```bash
# 通过 AI 进行 MCP 交互示例：

# "监控当前页面的控制台错误"

# "运行 Lighthouse 审计进行性能分析"

# "检查表单元素的可访问性合规性"

# "捕获登录流程的网络请求"

```

该服务器在浏览器调试和 AI 辅助开发之间提供无缝集成。您可以监控实时浏览器活动、自动化测试程序并分析网页性能 - 所有这些都可以通过与 AI 编码助手的自然语言交互来完成。

**高级功能**

-   **自动粘贴集成**：浏览器扩展自动将捕获的数据粘贴到 Cursor 中
-   **性能监控**：实时指标收集和分析
-   **错误跟踪**：全面的 JavaScript 错误监控和报告
-   **可访问性审计**：带有详细报告的 WCAG 2.1 合规性检查

* * *

##### 社区洞察

Browser Tools MCP 获得了 4.8/5 星评级，用户称赞其自动粘贴功能"通过自动将浏览器数据发送到 Cursor 来简化调试工作流程"。实时监控已被证明对前端开发人员非常宝贵。

<img src="/img/discovery/022_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Browser Tools MCP 由 AgentDeskAI 开发并且是开源的。如需技术支持、功能请求和社区讨论，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)