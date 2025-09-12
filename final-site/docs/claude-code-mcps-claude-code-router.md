---
title: "Claude Code 路由器 | ClaudeLog"
---

# Claude Code 路由器 | ClaudeLog

**通过智能 AI 提供商路由，无需 Anthropic 账户即可使用 Claude Code**

**作者**: [@musistudio](https://github.com/musistudio)  |  [GitHub 仓库](https://github.com/musistudio/claude-code-router)  |  15k Stars|1.1k Forks|MIT License|Updated Aug 24, 2025

* * *

### 概述[​](#概述 "直接链接到概述")

Claude Code 路由器是一个代理工具，无需 Anthropic 账户即可启用 Claude Code 功能。它拦截 Claude Code 请求并将其路由到替代 AI 提供商，如 OpenRouter、DeepSeek、Ollama 和 Gemini，让您在使用任何支持的 AI 模型的同时访问 Claude Code 的界面。

* * *

* * *

<!-- Screenshot temporarily removed due to missing asset -->

* * *

* * *

### 功能特性[​](#功能特性 "直接链接到功能特性")

-   **无需 Anthropic 账户** - 使用替代 AI 提供商的 Claude Code 界面
-   **支持 8+ 个提供商** - OpenRouter、DeepSeek、Ollama、Gemini、VolcEngine、SiliconFlow、ModelScope、DashScope
-   **动态模型切换** - 使用 `/model provider,model_name` 命令在会话中切换模型
-   **基于上下文的路由** - 为默认、后台、推理和长上下文任务自动路由
-   **自定义转换器** - 配置请求/响应转换以实现提供商兼容性
-   **GitHub Actions 集成** - 支持自动模型路由的 CI/CD 工作流

* * *

* * *

### 安装[​](#安装 "直接链接到安装")

**先决条件**

-   Node.js 运行环境
-   Claude Code: `npm install -g @anthropic-ai/claude-code`

**安装路由器**

```bash
# 全局安装路由器

npm install -g @musistudio/claude-code-router

```

**配置设置** 创建 `~/.claude-code-router/config.json` 配置您喜欢的 AI 提供商：

```bash
{

  "Providers": [

    {

      "name": "openrouter",

      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",

      "api_key": "sk-xxx",

      "models": ["anthropic/claude-3.5-sonnet", "google/gemini-2.5-pro-preview"]

    },

    {

      "name": "deepseek",

      "api_base_url": "https://api.deepseek.com/chat/completions",

      "api_key": "sk-xxx",

      "models": ["deepseek-chat", "deepseek-reasoner"]

    }

  ],

  "Router": {

    "default": "deepseek,deepseek-chat",

    "background": "deepseek,deepseek-chat",

    "think": "deepseek,deepseek-reasoner",

    "longContext": "openrouter,google/gemini-2.5-pro-preview"

  }

}

```

* * *

* * *

### 使用方法[​](#使用方法 "直接链接到使用方法")

**使用路由器启动 Claude Code**

```bash
# 使用此命令代替常规 Claude Code

ccr code

```

**动态模型切换** 在会话期间，使用以下命令切换模型：

```bash
# 切换到不同的提供商和模型

/model deepseek,deepseek-chat

/model openrouter,anthropic/claude-3.5-sonnet

/model ollama,qwen2.5-coder:latest

```

**基于上下文的路由** 路由器根据任务上下文自动选择模型：

-   **默认**：常规开发任务
-   **后台**：简单、经济高效的操作
-   **思考**：复杂的推理和分析
-   **长上下文**：需要大量上下文窗口的任务

有关详细的配置选项和路由规则，请阅读[官方文档](https://github.com/musistudio/claude-code-router)。

##### 无需 Anthropic 账户

使用替代 AI 提供商访问 Claude Code 的界面，无需 Anthropic 订阅。

<img src="/img/discovery/004.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Claude Code 路由器是一个独立的社区项目。如需技术支持和更新，请参考官方 GitHub 仓库。*

-   [概述](#概述)
-   [功能特性](#功能特性)
-   [安装](#安装)
-   [使用方法](#使用方法)
