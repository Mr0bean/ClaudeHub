---
title: "Claude Code Router | ClaudeLog"
---

# Claude Code Router | ClaudeLog

**Use Claude Code without an Anthropic account through intelligent AI provider routing**

**Author**: [@musistudio](https://github.com/musistudio)  |  [GitHub Repo](https://github.com/musistudio/claude-code-router)  |  15k Stars|1.1k Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

Claude Code Router is a proxy tool that enables Claude Code functionality without requiring an Anthropic account. It intercepts Claude Code requests and routes them to alternative AI providers like OpenRouter, DeepSeek, Ollama, and Gemini, giving you access to Claude Code's interface while using any supported AI model.

* * *

* * *

<!-- Screenshot temporarily removed due to missing asset -->

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **No Anthropic Account Required** - Use Claude Code interface with alternative AI providers
-   **8+ Supported Providers** - OpenRouter, DeepSeek, Ollama, Gemini, VolcEngine, SiliconFlow, ModelScope, DashScope
-   **Dynamic Model Switching** - Change models mid-session with `/model provider,model_name` commands
-   **Context-Based Routing** - Automatic routing for default, background, reasoning, and long-context tasks
-   **Custom Transformers** - Configure request/response transformations for provider compatibility
-   **GitHub Actions Integration** - CI/CD workflow support with automated model routing

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Prerequisites**

-   Node.js runtime environment
-   Claude Code: `npm install -g @anthropic-ai/claude-code`

**Install Router**

```bash
# Install the router globally

npm install -g @musistudio/claude-code-router

```

**Configuration Setup** Create `~/.claude-code-router/config.json` with your preferred AI providers:

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

### Usage[​](#usage "Direct link to Usage")

**Start Claude Code with Router**

```bash
# Use this command instead of regular Claude Code

ccr code

```

**Dynamic Model Switching** During your session, switch models with:

```bash
# Switch to different provider and model

/model deepseek,deepseek-chat

/model openrouter,anthropic/claude-3.5-sonnet

/model ollama,qwen2.5-coder:latest

```

**Context-Based Routing** The router automatically selects models based on task context:

-   **Default**: General development tasks
-   **Background**: Simple, cost-effective operations
-   **Think**: Complex reasoning and analysis
-   **Long Context**: Tasks requiring extensive context windows

For detailed configuration options and routing rules, read the [official documentation](https://github.com/musistudio/claude-code-router).

##### No Anthropic Account Needed

Access Claude Code's interface using alternative AI providers without requiring an Anthropic subscription.

<img src="/img/discovery/004.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Claude Code Router is an independent community project. For technical support and updates, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)