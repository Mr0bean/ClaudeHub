---
title: "GitHub MCP 服务器 | Claude Hub"
---

# GitHub MCP 服务器 | Claude Hub

**官方 MCP 服务器，为高级自动化和 AI 驱动的开发工作流提供无缝 GitHub API 集成。**

**作者**: [GitHub](https://github.com/github)  |  [GitHub 仓库](https://github.com/github/github-mcp-server)  |  21.6k 星标|2.2k 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

GitHub MCP 服务器是 GitHub 集成的官方模型上下文协议实现，使 AI 模型能够直接与 GitHub 生态系统交互。它通过标准化的 MCP 界面提供对仓库、议题、拉取请求、操作和安全功能的全面访问，改变了开发者自动化和管理 GitHub 工作流的方式。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **全面的 GitHub API 访问** - 通过精选工具集与 GitHub 的 REST 和 GraphQL API 进行广泛集成
-   **灵活的部署选项** - 远程托管服务器或本地 Docker 安装
-   **精细权限控制** - 对工具访问和功能的细粒度控制
-   **企业支持** - GitHub 企业服务器兼容性及自定义配置
-   **动态工具发现** - 自动适应可用的 GitHub 功能
-   **多工具集支持** - Actions、安全、议题、PR、仓库、通知

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   VS Code 1.101+（用于远程服务器）或 Docker（用于本地安装）
-   具有适当权限的 GitHub 个人访问令牌

**方法一：远程服务器（推荐）**

在 VS Code 中通过一键按钮直接安装：

-   [为 Claude Desktop 安装](vscode:extension/modelcontextprotocol.servers)
-   [为 Continue 安装](vscode:extension/modelcontextprotocol.servers)

**方法二：Claude Desktop 配置**

```bash
{

  "mcpServers": {

    "github": {

      "command": "docker",

      "args": [

        "run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",

        "ghcr.io/github/github-mcp-server"

      ],

      "env": {

        "GITHUB_PERSONAL_ACCESS_TOKEN": "&lt;YOUR_TOKEN&gt;"

      }

    }

  }

}

```

**方法三：本地 Docker 安装**

```bash
# 本地运行 GitHub MCP 服务器

docker run -i --rm \

  -e GITHUB_PERSONAL_ACCESS_TOKEN=&lt;your-token&gt; \

  -e GITHUB_TOOLSETS="context,repos,issues,pull_requests" \

  ghcr.io/github/github-mcp-server

```

**可用的 GITHUB_TOOLSETS**

-   **`context`** - 仓库上下文（推荐用于大多数用例）
-   **`repos`** - 仓库管理和操作
-   **`issues`** - GitHub Issues API 访问
-   **`pull_requests`** - 拉取请求管理
-   **`actions`** - GitHub Actions 工作流集成
-   **`code_security`** - 安全扫描和漏洞管理
-   **`notifications`** - GitHub 通知管理
-   **`orgs`** - 组织管理
-   **`secret_protection`** - 密钥扫描和保护
-   **`users`** - 用户账户操作
-   **`experiments`** - 实验性 GitHub 功能（可选）
-   **`all`** - 启用所有可用工具集

**注意**: 推荐大多数用户使用 `context` 工具集。仅指定需要的工具集以帮助 LLM 进行工具选择并减少上下文大小。如果未指定 `GITHUB_TOOLSETS`，默认启用所有工具集。

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**仓库管理**

```bash
# 通过 AI 客户端的交互示例：

# "列出我的仓库及其最新提交"

# "为功能分支创建新的拉取请求"

# "显示所有带 bug 标签的开放议题"

# "检查 GitHub Actions 运行状态"

```

该服务器通过对话式 AI 界面实现与 GitHub 完整功能集的自然语言交互。你可以管理仓库、自动化议题跟踪、审查代码更改、监控 CI/CD 流水线和处理安全警报。

**配置选项**

-   **工具集选择**: 选择要公开的特定 GitHub 功能
-   **只读模式**: 限制为安全的非修改操作
-   **自定义权限**: 为安全配置 OAuth 范围
-   **企业设置**: 连接到 GitHub 企业实例

* * *

##### 社区见解

官方 MCP 服务器改变了开发者的工作流，用户反馈："我用它来与议题和 MR 交互，在编辑代码时寻找相关议题。"官方性质确保了社区替代方案通常缺乏的可靠性。


* * *

*GitHub MCP 服务器由模型上下文协议组织开发和维护。如需技术支持、功能请求和企业配置，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)