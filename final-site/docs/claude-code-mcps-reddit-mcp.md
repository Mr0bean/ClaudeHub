---
title: "Reddit MCP | Claude Hub"
---

# Reddit MCP | Claude Hub

**为 Claude Code 工作流提供 Reddit 内容访问和分析功能**

**作者**: [Hawstein](https://github.com/hawstein)  |  [GitHub 仓库](https://github.com/hawstein/reddit-mcp)  |  93 星标|15 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#概述)

Reddit MCP 为 Claude Code 提供对 Reddit 公开 API 的访问，通过模型上下文协议实现内容分析、社区研究和社交媒体洞察。无缝浏览子版块、阅读帖子和评论，并分析 Reddit 讨论。

* * *

* * *

### 功能特性[​](#功能特性)

-   **首页访问** - 浏览 Reddit 首页和热门帖子
-   **子版块浏览** - 从任何子版块访问帖子、评论和社区数据
-   **热门帖子获取** - 获取特定社区中最受欢迎的帖子
-   **帖子详情** - 获取特定帖子及其元数据的详细信息
-   **评论树** - 访问评论线程和讨论层次结构
-   **公开 API 访问** - 公开内容无需身份验证

* * *

* * *

### 安装[​](#安装)

**前置要求**

-   MCP 服务器的 Node.js 环境

**设置 MCP 服务器**

```bash
git clone https://github.com/hawstein/reddit-mcp
cd reddit-mcp
npm install
npm run build
```

**Claude Code 配置**

```json
{
  "mcpServers": {
    "reddit": {
      "command": "node",
      "args": "path/to/reddit-mcp/build/index.js"
    }
  }
}
```

* * *

* * *

### 使用方法[​](#使用方法)

**内容发现**

```
分析 r/technology 中关于 AI 的热门讨论
```

**社区分析**

```
获取 r/programming 中排名前10的帖子并分析趋势
```

**研究和监控**

```
监控 r/MachineLearning 中的新兴主题和讨论
```

完整的 API 参考和高级使用模式，请参阅[官方文档](https://github.com/hawstein/reddit-mcp/blob/main/README.md)。

##### 可扩展性

Reddit MCP 为额外功能提供了良好的基础。该仓库可以轻松扩展以适应默认 MCP 方法之外的自定义功能。

<img src="/img/discovery/036_cl_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Reddit MCP 由 Hawstein 作为社区项目开发。如需技术支持和更新，请参考官方 GitHub 仓库。*

-   [概述](#概述)
-   [功能特性](#功能特性)
-   [安装](#安装)
-   [使用方法](#使用方法)