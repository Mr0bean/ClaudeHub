---
title: "Desktop Commander MCP | ClaudeLog"
---

# Desktop Commander MCP | ClaudeLog

**Comprehensive system control and development automation server enabling terminal commands, file operations, and cross-platform workflow management through MCP integration.**

**Author**: [wonderwhy-er](https://github.com/wonderwhy-er)  |  [GitHub Repo](https://github.com/wonderwhy-er/DesktopCommanderMCP)  |  4.3k Stars|475 Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

Desktop Commander MCP provides comprehensive system-level control and development automation through the Model Context Protocol. It enables AI models to execute terminal commands, perform file operations, analyze data, and manage development workflows across Windows, macOS, and Linux platforms. This server transforms AI assistants into powerful system automation tools while maintaining security boundaries.

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **Terminal Command Execution** - Run shell commands, scripts, and system utilities directly from AI conversations
-   **Cross-Platform File Operations** - File reading, writing, searching, and manipulation across operating systems
-   **Multi-Language Code Execution** - Support for Python, JavaScript, shell scripts, and other languages
-   **Data Analysis Capabilities** - CSV processing, statistical analysis, and data transformation tools
-   **Development Workflow Automation** - Git operations, build processes, and deployment scripts
-   **Security Controls** - Configurable permission system and command validation

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Prerequisites**

-   Node.js 18.0.0+ for MCP server functionality
-   npm package manager
-   Compatible MCP client (Claude Desktop, VS Code, Cursor)

**Recommended Installation (Auto-Updates)**

```bash
# Quick setup with npx (recommended)

npx @wonderwhy-er/desktop-commander@latest setup

# Debug mode (if needed)

npx @wonderwhy-er/desktop-commander@latest setup --debug

```

**Manual Configuration**

```bash
{

  "mcpServers": {

    "desktop-commander": {

      "command": "npx",

      "args": [

        "-y",

        "@wonderwhy-er/desktop-commander"

      ]

    }

  }

}

```

**Alternative Installation Methods**

```bash
# macOS bash script installation

curl -fsSL https://raw.githubusercontent.com/wonderwhy-er/DesktopCommanderMCP/refs/heads/main/install.sh | bash

# Smithery CLI installation

npx -y @smithery/cli install @wonderwhy-er/desktop-commander --client claude

# Local development setup

git clone https://github.com/wonderwhy-er/DesktopCommanderMCP.git

cd DesktopCommanderMCP

npm run setup

```

**Configuration Locations**

-   **macOS**: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
-   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
-   **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Note**: Restart Claude Desktop after installation. Configuration persists between server restarts.

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**System Administration**

```bash
# Example AI interactions:

# "Check system disk usage and clean up temporary files"

# "Monitor running processes and identify high CPU usage"

# "Create a backup script for the project directory"

# "Update system packages and restart services"

```

The server enables natural language system administration and development automation. You can manage files, execute complex workflows, analyze system performance, and automate repetitive tasks through conversational AI interfaces.

**Development Workflows**

-   **Code Analysis**: Analyze codebases, generate reports, and identify patterns
-   **Build Automation**: Execute build scripts, run tests, and deploy applications
-   **Git Operations**: Commit changes, manage branches, and handle merge conflicts
-   **Data Processing**: Parse logs, process CSV files, and generate insights

* * *

##### Community Insight

Desktop Commander MCP provides cost-effective system automation for developers. Users report "Claude Code-like capabilities for a fraction of the price" with excellent cross-platform support.

<img src="/img/discovery/023_excite.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Desktop Commander MCP is developed by wonderwhy-er and is open-source. For technical support, feature requests, and community contributions, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)