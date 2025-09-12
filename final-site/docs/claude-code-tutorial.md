---
title: "Tutorial | ClaudeLog"
---

# Tutorial | ClaudeLog

Now that you have Claude Code installed, let's set up your project and learn the basics of using Claude Code to enhance your development workflow. This beginner-friendly Claude Code tutorial covers essential commands, examples, best practices, and workflow optimization for new users.

* * *

* * *

## Claude Code Project Setup and Configuration[​](#claude-code-project-setup-and-configuration "Direct link to Claude Code Project Setup and Configuration")

Before diving into commands and examples, let's configure your project to work optimally with Claude Code. Proper setup ensures Claude understands your project structure, coding standards, and development workflow from the start.

### CLAUDE.md Configuration[​](#claudemd-configuration "Direct link to CLAUDE.md Configuration")

Create a `CLAUDE.md` file in your project root to help Claude understand your project. This is one of the most important Claude Code best practices:

```bash
# CLAUDE.md

## Project Overview

Brief description of your project, its purpose, and main technologies.

## Development Guidelines

- Coding standards and conventions

- File structure preferences

- Testing approaches

## Important Commands

- Build commands

- Test commands

- Development server commands

```

Claude Code automatically reads this file when it starts to provide project context.

* * *

* * *

## Your First Claude Code Session: Step-by-Step Tutorial[​](#your-first-claude-code-session-step-by-step-tutorial "Direct link to Your First Claude Code Session: Step-by-Step Tutorial")

Claude Code provides two main ways to interact:

**Interactive mode:** Run `claude` to start a REPL session **One-shot mode:** Use `claude -p "query"` for quick commands

### Interactive Mode[​](#interactive-mode "Direct link to Interactive Mode")

Start Claude Code in your project directory:

```bash
cd your-project

claude

```

You'll see the Claude Code prompt, ready to assist with your development tasks.

### One-shot Mode[​](#one-shot-mode "Direct link to One-shot Mode")

For quick queries without starting a full session:

```bash
claude -p "Show me the files in this directory"

claude -p "What kind of project is this?"

```

This mode is perfect for quick questions or when you need fast answers without entering an interactive session.

* * *

* * *

## Claude Code Examples: Quick Wins for Beginners[​](#claude-code-examples-quick-wins-for-beginners "Direct link to Claude Code Examples: Quick Wins for Beginners")

Here are some simple requests to get you comfortable with Claude Code:

### Understanding Your Project[​](#understanding-your-project "Direct link to Understanding Your Project")

```bash
Show me the files in this directory

```

Claude Code will list your project files and explain what it found.

```bash
What kind of project is this?

```

Claude will analyze your project structure and tell you what type of application it is.

```bash
Explain what this project does

```

Based on your files and documentation, Claude will summarize the project's purpose.

### Quick Analysis[​](#quick-analysis "Direct link to Quick Analysis")

```bash
Show me the main entry point

```

Claude will identify and show you the primary file that starts your application.

```bash
What dependencies does this project have?

```

Claude will read your package.json, requirements.txt, or similar files and list dependencies.

```bash
How do I run this project?

```

Claude will look for scripts and documentation to tell you how to start the project.

### Your First File Creation[​](#your-first-file-creation "Direct link to Your First File Creation")

Let's create your first file with Claude Code:

```bash
Create a hello_world.txt file with a greeting message

```

Claude Code will create the file, show you what it wrote, and confirm the creation. This demonstrates Claude's ability to understand natural language and take real actions in your project.

* * *

* * *

## Essential Claude Code Commands and Examples[​](#essential-claude-code-commands-and-examples "Direct link to Essential Claude Code Commands and Examples")

### File Operations[​](#file-operations "Direct link to File Operations")

```bash
# Read a file

read src/components/Button.js

# Edit a file

edit src/components/Button.js

# Create a new file

write src/components/NewComponent.js

```

### Code Analysis[​](#code-analysis "Direct link to Code Analysis")

```bash
# Analyze code structure

analyze this codebase

# Find specific patterns

find all React components

# Explain code

explain how authentication works

```

### Development Tasks[​](#development-tasks "Direct link to Development Tasks")

```bash
# Add new features

add a dark mode toggle to the app

# Fix bugs

fix the memory leak in the data fetcher

# Refactor code

refactor the user service to use TypeScript

# Write tests

write unit tests for the Button component

```

* * *

* * *

## How to Use Claude Code: Natural Language Commands[​](#how-to-use-claude-code-natural-language-commands "Direct link to How to Use Claude Code: Natural Language Commands")

Claude Code understands natural language requests, making it easier than traditional development tools:

```bash
# Instead of complex git commands

"Create a commit with all the changes I made to the user authentication"

# Instead of manual file operations

"Update all components to use the new theme system"

# Instead of searching through documentation

"How do I set up database migrations in this project?"

```

##### Welcome to the Future

You've just taken your first steps into AI-powered development with Claude Code. The journey ahead leads to unprecedented productivity and creativity in software development.

<img src="/img/discovery/022_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Pricing Plans](/claude-code-pricing/)|[Plan Mode](/mechanics/plan-mode/)|[MCPs & Add-ons](/claude-code-mcps/)|[FAQs](/faq/)

-   [Claude Code Project Setup and Configuration](#claude-code-project-setup-and-configuration)
    -   [CLAUDE.md Configuration](#claudemd-configuration)
-   [Your First Claude Code Session: Step-by-Step Tutorial](#your-first-claude-code-session-step-by-step-tutorial)
    -   [Interactive Mode](#interactive-mode)
    -   [One-shot Mode](#one-shot-mode)
-   [Claude Code Examples: Quick Wins for Beginners](#claude-code-examples-quick-wins-for-beginners)
    -   [Understanding Your Project](#understanding-your-project)
    -   [Quick Analysis](#quick-analysis)
    -   [Your First File Creation](#your-first-file-creation)
-   [Essential Claude Code Commands and Examples](#essential-claude-code-commands-and-examples)
    -   [File Operations](#file-operations)
    -   [Code Analysis](#code-analysis)
    -   [Development Tasks](#development-tasks)
-   [How to Use Claude Code: Natural Language Commands](#how-to-use-claude-code-natural-language-commands)