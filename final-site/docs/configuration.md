---
title: "Claude Code Configuration Guide | ClaudeLog"
---

# Claude Code Configuration Guide | ClaudeLog

Complete Claude Code configuration with comprehensive setup guides for API keys, model selection, MCP servers, tool permissions, and multi-directory workflows. Essential settings for optimizing your AI development experience.

* * *

* * *

## API Key Setup[​](#api-key-setup "Direct link to API Key Setup")

Claude Code requires an Anthropic API key to function. Set it up using one of these methods:

```bash
# Option 1: Environment variable (recommended)

export ANTHROPIC_API_KEY="your-api-key-here"

# Option 2: Add to your shell profile

echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc

source ~/.bashrc

```

* * *

* * *

## Model Selection[​](#model-selection "Direct link to Model Selection")

Claude Code supports multiple models. You can specify which model to use:

**Claude 4 Sonnet:** Latest balanced performance and speed

```bash
export ANTHROPIC_MODEL="claude-sonnet-4-20250514"

```

**Claude 4.1 Opus:** Latest maximum capability with enhanced coding and debugging performance

```bash
export ANTHROPIC_MODEL="claude-opus-4-1-20250805"

```

**Claude 4 Opus:** Previous generation maximum capability model

```bash
export ANTHROPIC_MODEL="claude-opus-4-20250514"

```

**Claude 3.5 Haiku:** Fastest and most cost-effective

```bash
export ANTHROPIC_MODEL="claude-3-5-haiku-20241022"

```

Important limitations: Claude 3.5 Haiku

While Haiku is cost-effective, it has significant limitations for Claude Code usage:

-   **Reduced reasoning capabilities** - Struggles with complex multi-step planning and architectural decisions
-   **Limited context understanding** - Less effective at analyzing large codebases and maintaining context across multiple files
-   **Simplified code analysis** - May miss subtle bugs, dependencies, or complex patterns that modern models catch
-   **Basic refactoring only** - Not suitable for sophisticated restructuring or feature implementations
-   **Limited framework knowledge** - Less effective with complex frameworks or novel coding patterns

**Recommended use cases for Haiku:**

-   Simple single-file edits
-   Basic syntax corrections
-   Quick code questions
-   Learning Claude Code basics before upgrading

For serious development work, Claude 4 Sonnet or Opus provide substantially better results and are worth the additional cost.

**Alternative Method:** You can also specify the model directly when starting Claude Code:

```bash
claude --model claude-sonnet-4-20250514

claude --model claude-opus-4-1-20250805

claude --model claude-opus-4-20250514

claude --model claude-3-5-haiku-20241022

```

* * *

* * *

## Model Switching During Session[​](#model-switching-during-session "Direct link to Model Switching During Session")

You can switch models mid-session using the `/model` command, which provides an interactive menu:

```bash
/model

```

**Available Options:**

1.  **Default (recommended)** - Opus 4.1 for up to 20% of usage limits, then use Sonnet 4
2.  **Opus** - Opus 4.1 for complex tasks (reaches usage limits faster)
3.  **Sonnet** - Sonnet 4 for daily use
4.  **Opus Plan Mode** - Use Opus 4.1 in plan mode, Sonnet 4 otherwise ✔

The Opus Plan Mode automatically switches between models based on context, using Opus 4.1 for research and planning phases, then Sonnet 4 for implementation and execution.

* * *

* * *

## MCP Configuration[​](#mcp-configuration "Direct link to MCP Configuration")

Model Context Protocol (MCP) allows Claude Code to connect to external tools and services. Configure MCP servers to extend Claude's capabilities:

#### MCP Server Setup[​](#mcp-server-setup "Direct link to MCP Server Setup")

MCP configuration can be stored in multiple locations:

-   **Project-specific:** `.claude/settings.local.json` (in your project directory)
-   **User-specific local:** `~/.claude/settings.local.json`
-   **User-specific global:** `~/.claude/settings.json`
-   **Main Claude.json:** `~/.claude.json`
-   **Dedicated MCP file:** `~/.claude/mcp_servers.json`

Example MCP configuration:

```bash
// Example: ~/.claude.json (recommended for reliability)

{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "filesystem": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/Desktop", "/path/to/allowed/dir"]

        },

        "memory": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-memory"]

        },

        "fetch": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-fetch"]

        }

      }

    }

  },

  ...

}

```

**Note:** If following this example ensure you update the right projects configuration.

For additional tools and integrations beyond MCP, explore our [Add-ons](/claude-code-mcps/).

* * *

* * *

## Allowed Tools[​](#allowed-tools "Direct link to Allowed Tools")

#### Allowed Tools Setup[​](#allowed-tools-setup "Direct link to Allowed Tools Setup")

Allowed tools configuration can be stored in multiple locations:

-   **Project-specific:** `.claude/settings.local.json` (in your project directory)
-   **User-specific local:** `~/.claude/settings.local.json`
-   **User-specific global:** `~/.claude/settings.json`
-   **Main Claude.json:** `~/.claude.json`

#### Example Allowed Tools configuration:[​](#example-allowed-tools-configuration "Direct link to Example Allowed Tools configuration:")

```bash
// Example: ~/.claude.json (recommended for reliability)

{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "filesystem": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/Desktop", "/path/to/allowed/dir"]

        }

      },

      "allowedTools": [

        "Task",

        "Bash",                    // ⚠️ Dangerous: allows all system commands

        "Bash(git log:*)",   // Safer: only allows git log commands

        "Glob",

        "Grep",

        "LS",

        "Read",

        "Edit",

        "MultiEdit",

        "Write",

        "WebFetch",

        "WebSearch"

      ]

    }

  },

  ...

}

```

**Note:** If following this example ensure you update the right projects configuration.

#### Interactive Permission Management[​](#interactive-permission-management "Direct link to Interactive Permission Management")

For a more user-friendly approach to managing tool permissions, use the `/permissions` command within Claude Code:

```bash
# Launch the interactive permissions UI

/permissions

```

This advanced interface allows you to:

-   **View current permissions** - See which tools are currently allowed or denied
-   **Explicitly allow tools** - Grant permission to specific tools or tool patterns
-   **Explicitly deny tools** - Block access to tools you want to restrict
-   **Navigate visually** - Use an intuitive UI instead of manually editing JSON files

The `/permissions` interface provides real-time permission management with a fluid, responsive experience that makes configuration changes effortless—no need to restart Claude Code or manually edit configuration files.

tip

Multiple configuration locations exist due to legacy compatibility - you might encounter different file names and directory locations.

**Recommendation:** Use `~/.claude.json` for reliability as shown in the examples above.

* * *

* * *

## Additional Working Directories / Extended Workspace[​](#additional-working-directories--extended-workspace "Direct link to Additional Working Directories / Extended Workspace")

Claude Code can access multiple directories beyond your current working directory using:

-   **CLI argument:** `--add-dir` (added in [v1.0.18](/claude-code-changelog/#v1018)) when starting Claude Code
-   **Slash command:** `/add-dir` mid-session for seamless workflow expansion

This allows you to work across multiple projects or reference external resources without changing directories or restarting your session.

### Usage[​](#usage "Direct link to Usage")

**CLI Argument (at startup):**

```bash
# Add a single additional directory

claude --add-dir /path/to/other/project

# Combine with other options

claude --add-dir ~/shared/libraries

# Use with print mode for scripting

claude --add-dir ../backend -p "Validate that API calls in the current directory match endpoints defined in ../backend"

```

**Slash Command (mid-session):**

```bash
# Add directory without restarting your session

/add-dir /path/to/other/project

# Add multiple directories as needed

/add-dir ~/shared/libraries

/add-dir ../backend-api

```

### Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

**Multi-Repository Projects**

```bash
# At startup: Work on frontend while referencing the backend API

claude --add-dir ../backend-api

# Mid-session: Add backend when you need to reference API endpoints

/add-dir ../backend-api

```

**Shared Resources**

```bash
# At startup: Access shared configs or documentation

claude --add-dir ~/company/shared-configs

# Mid-session: Add shared resources when needed

/add-dir ~/company/shared-configs

```

**Dynamic Workflow expansion**

```bash
# Start with current project, then expand as needed

# No need to restart when you realize you need additional context

/add-dir ../related-service

/add-dir ~/templates

```

**Note:** The current working directory is always included. CLAUDE.md files appear to not be read in automatically from additional directories added via `--add-dir`.

Better Workflow Orchestration

This feature significantly improves workflow orchestration by enabling Claude to:

-   **Work across repositories** simultaneously—maintaining context and applying consistent changes
-   **Reference shared code** directly from libraries or configuration repositories
-   **Temporarily expose** a codebase for Claude to analyze or modify without changing directories
-   **Expand workspace dynamically** using `/add-dir` without interrupting your current session

The `/add-dir` slash command makes this particularly seamless—you can start focused on one project and organically expand your workspace as needs emerge, without losing context or restarting. Instead of juggling multiple sessions or copying files, you can compose multiple repositories within the same workflow structure—orchestrating complex multi-repository operations in a single, context-aware session.

##### Configuration Mastery

Proper configuration is the foundation of effective Claude Code usage. Understanding these settings enables sophisticated workflows and unlocks the full potential of AI-assisted development.

<img src="/img/discovery/009.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Pricing Plans](/claude-code-pricing/)|[CLAUDE.md Guide](/mechanics/claude-md-supremacy/)|[MCPs & Add-ons](/claude-code-mcps/)|[FAQs](/faq/)

-   [API Key Setup](#api-key-setup)
-   [Model Selection](#model-selection)
-   [Model Switching During Session](#model-switching-during-session)
-   [MCP Configuration](#mcp-configuration)
-   [Allowed Tools](#allowed-tools)
-   [Additional Working Directories / Extended Workspace](#additional-working-directories--extended-workspace)
    -   [Usage](#usage)
    -   [Common Use Cases](#common-use-cases)