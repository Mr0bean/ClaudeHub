---
title: "Zen MCP Server | ClaudeLog"
---

# Zen MCP Server | ClaudeLog

**Multi-AI orchestration platform that enables Claude Code to collaborate seamlessly with Gemini Pro, OpenAI O3, Grok, and other leading AI models for enhanced development workflows.**

**Author**: [BeehiveInnovations](https://github.com/BeehiveInnovations)  |  [GitHub Repo](https://github.com/BeehiveInnovations/zen-mcp-server)  |  6.5k Stars|571 Forks|Apache 2.0 License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

Zen MCP Server creates a unified orchestration layer that enables Claude Code to collaborate with multiple AI models simultaneously. By intelligently routing tasks to the most suitable AI model, it dramatically enhances development workflows through specialized expertise and cross-model validation. The platform maintains context continuity across different models while providing specialized developer workflows for debugging, code review, and analysis.

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **Multi-Model Orchestration** - Seamlessly integrate Claude, Gemini 2.5 Pro, OpenAI O3, Grok, OpenRouter, and Ollama
-   **Intelligent Model Selection** - Automatic routing to optimal models based on task requirements
-   **Context Preservation** - Maintain conversation context across different AI models and sessions
-   **Specialized Dev Workflows** - Built-in tools for code review, debugging, pre-commit validation, and analysis
-   **Cross-Model Validation** - Compare outputs and approaches from different AI models for enhanced reliability
-   **Expert Mode Routing** - Route complex problems to specialized models (O3 for logic, Gemini for architecture)

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Prerequisites**

-   Python 3.10+ (3.12 recommended) with UV package manager
-   API keys for desired AI services (at least one required: OpenAI, Gemini, OpenRouter, etc.)
-   Claude Code or compatible MCP client
-   For Windows: WSL2 required

**Recommended: UVX Quick Install**

```bash
# One-line installation - no manual setup required

exec $(which uvx || echo uvx) --from git+https://github.com/BeehiveInnovations/zen-mcp-server.git zen-mcp-server

```

**Claude Code Configuration** Add to your Claude Code configuration:

```bash
{

  "mcpServers": {

    "zen": {

      "command": "sh",

      "args": [

        "-c",

        "exec $(which uvx || echo uvx) --from git+https://github.com/BeehiveInnovations/zen-mcp-server.git zen-mcp-server"

      ],

      "env": {

        "PATH": "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:~/.local/bin",

        "OPENAI_API_KEY": "your_api_key_here",

        "GEMINI_API_KEY": "your_gemini_key_here"

      }

    }

  }

}

```

**API Key Configuration** Create a `.env` file in your project directory or set environment variables:

```bash
# Option 1: Environment variables

export OPENAI_API_KEY="your-openai-key"

export GEMINI_API_KEY="your-gemini-key"

export ANTHROPIC_API_KEY="your-claude-key"

# Option 2: .env file (recommended)

echo "OPENAI_API_KEY=your-openai-key" > .env

echo "GEMINI_API_KEY=your-gemini-key" >> .env

```

**Alternative: Traditional Installation**

```bash
# Only if uvx method doesn't work

git clone https://github.com/BeehiveInnovations/zen-mcp-server.git

cd zen-mcp-server

./run-server.sh  # or ./run-server.ps1 on Windows

```

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**Multi-Model Development Workflows**

```bash
# Example AI orchestration commands:

# "Use Gemini for architecture review and O3 for logic validation"

# "Compare debugging approaches from Claude and GPT-4"

# "Route this complex algorithm to the best mathematical reasoning model"

# "Run pre-commit validation using multiple model perspectives"

```

The platform intelligently manages model selection and context flow, enabling developers to leverage the unique strengths of different AI models within a single conversation. Zen MCP maintains conversation continuity while providing access to specialized capabilities from each model.

**Specialized Developer Tools**

-   **Code Review**: Multi-model code review with diverse perspectives
-   **Debug Analysis**: Route debugging tasks to models with specific strengths
-   **Pre-commit Validation**: Comprehensive validation using optimal models
-   **Architecture Planning**: Leverage Gemini's architectural reasoning capabilities

* * *

##### Community Insight

Zen MCP Server gained massive attention with a Reddit post receiving 800+ upvotes. Users report multi-model orchestration provides "different perspectives that catch issues single models miss."

<img src="/img/discovery/024_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Zen MCP Server is developed by BeehiveInnovations and is open-source. For technical support, multi-model configuration, and community discussions, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)