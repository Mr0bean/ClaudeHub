---
title: "Zen MCP 服务器 | Claude Hub"
---

# Zen MCP 服务器 | Claude Hub

**多 AI 编排平台，使 Claude Code 能够与 Gemini Pro、OpenAI O3、Grok 和其他领先 AI 模型无缝协作，增强开发工作流。**

**作者**: [BeehiveInnovations](https://github.com/BeehiveInnovations)  |  [GitHub 仓库](https://github.com/BeehiveInnovations/zen-mcp-server)  |  644 星标|571 分叉|Apache 2.0 许可证|更新于 2025年8月24日

* * *

### 概述[​](#概述)

Zen MCP 服务器创建了一个统一的编排层，使 Claude Code 能够与多个 AI 模型同时协作。通过智能地将任务路由到最适合的 AI 模型，它通过专业知识和跨模型验证大幅增强了开发工作流。该平台在不同模型间保持上下文连续性，同时为调试、代码审查和分析提供专门的开发者工作流。

* * *

* * *

### 功能特性[​](#功能特性)

-   **多模型编排** - 无缝集成 Claude、Gemini 2.5 Pro、OpenAI O3、Grok、OpenRouter 和 Ollama
-   **智能模型选择** - 基于任务要求自动路由到最优模型
-   **上下文保持** - 在不同 AI 模型和会话间维护对话上下文
-   **专业开发工作流** - 内置代码审查、调试、提交前验证和分析工具
-   **跨模型验证** - 比较不同 AI 模型的输出和方法以提高可靠性
-   **专家模式路由** - 将复杂问题路由到专门模型（O3 处理逻辑，Gemini 处理架构）

* * *

* * *

### 安装[​](#安装)

**前置要求**

-   Python 3.9+（推荐 3.11）与 UV 包管理器
-   所需 AI 服务的 API 密钥（至少需要一个：OpenAI、Gemini、OpenRouter 等）
-   Claude Code 或兼容的 MCP 客户端
-   Windows 用户：需要 WSL2

**推荐：UVX 快速安装**

```bash
uvx zen-mcp-server
```

**Claude Code 配置** 添加到你的 Claude Code 配置中：

```json
{
  "mcpServers": {
    "zen": {
      "command": "uvx",
      "args": "zen-mcp-server"
    }
  }
}
```

**API 密钥配置** 在项目目录中创建 `.env` 文件或设置环境变量：

```bash
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_gemini_key
OPENROUTER_API_KEY=your_openrouter_key
```

**替代方案：传统安装**

```bash
pip install zen-mcp-server
zen-mcp-server
```

* * *

* * *

### 使用方法[​](#使用方法)

**多模型开发工作流**

```
用户："使用不同的模型来设计和实现这个功能"
Claude：使用 Gemini 进行架构设计，O3 处理复杂逻辑，Claude 整合输出
```

该平台智能管理模型选择和上下文流，使开发者能够在单个对话中利用不同 AI 模型的独特优势。Zen MCP 在提供每个模型专门功能访问的同时保持对话连续性。

**专业开发工具**

-   **代码审查**：具有不同视角的多模型代码审查
-   **调试分析**：将调试任务路由到具有特定优势的模型
-   **提交前验证**：使用最优模型进行全面验证
-   **架构规划**：利用 Gemini 的架构推理能力

* * *

##### 社区见解

Zen MCP 服务器凭借一篇获得 800+ 赞的 Reddit 帖子获得了大量关注。用户反馈多模型编排提供了"捕获单个模型遗漏问题的不同视角"。

<img src="/img/discovery/024_zen_mcp_server.png" alt="Multi-AI orchestration through Zen MCP Server" style="max-width: 165px; height: auto;" />

* * *

*Zen MCP 服务器由 BeehiveInnovations 开发，是开源项目。如需技术支持、多模型配置和社区讨论，请参考官方 GitHub 仓库。*

-   [概述](#概述)
-   [功能特性](#功能特性)
-   [安装](#安装)
-   [使用方法](#使用方法)