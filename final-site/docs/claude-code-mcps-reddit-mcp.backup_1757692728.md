---
title: "Reddit MCP | ClaudeLog"
---

# Reddit MCP | ClaudeLog

**为 Claude Code 工作流提供 Reddit 内容访问和分析功能**

**作者**: [Hawstein](https://github.com/Hawstein)  |  [GitHub 仓库](https://github.com/Hawstein/mcp-server-reddit)  |  93 星标|15 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

Reddit MCP 为 Claude Code 提供对 Reddit 公开 API 的访问，通过模型上下文协议实现内容分析、社区研究和社交媒体洞察。无缝浏览子版块、阅读帖子和评论，并分析 Reddit 讨论。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **首页访问** - 浏览 Reddit 首页和热门帖子
-   **子版块浏览** - 从任何子版块访问帖子、评论和社区数据
-   **热门帖子获取** - 获取特定社区中最受欢迎的帖子
-   **帖子详情** - 获取特定帖子及其元数据的详细信息
-   **评论树** - 访问评论线程和讨论层次结构
-   **公开 API 访问** - 公开内容无需身份验证

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   MCP 服务器的 Python 环境

**设置 MCP 服务器**

```bash
# 通过 Python 安装

python -m pip install mcp-server-reddit

# 或从源码克隆并安装

git clone https://github.com/Hawstein/mcp-server-reddit.git

cd mcp-server-reddit

pip install -e .

```

**Claude Code 配置**

```bash
{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "reddit": {

          "type": "stdio",

          "command": "node",

          "args": [

            "/path/to/reddit-mcp-server/build/index.js"

          ],

          "env": {}

        }

      }

    }

  }

}

```

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**内容发现**

```bash
# 浏览 Reddit 首页

claude "显示 Reddit 首页当前的热门帖子"

# 访问特定子版块内容

claude "获取今天 r/programming 的前10个热门帖子"

```

**社区分析**

```bash
# 分析帖子参与度

claude "分析 r/MachineLearning 帖子中的评论模式"

# 跟踪技术讨论

claude "在相关子版块中查找关于 AI 编程工具的讨论"

```

**研究和监控**

```bash
# 竞争研究

claude "研究开发者对不同代码编辑器的看法"

# 趋势分析

claude "分析 Web 开发讨论中的最新趋势"

```

完整的 API 参考和高级使用模式，请参阅[官方文档](https://github.com/Hawstein/mcp-server-reddit)。

##### 可扩展性

Reddit MCP 为额外功能提供了良好的基础。该仓库可以轻松扩展以适应默认 API 方法之外的自定义功能。

<img src="/img/discovery/003.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Reddit MCP 由 Hawstein 作为社区项目开发。如需技术支持和更新，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)