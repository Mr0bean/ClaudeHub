---
title: "Puppeteer MCP | ClaudeLog"
---

# Puppeteer MCP | ClaudeLog

**Web automation with AI vision capabilities for Claude Code**

**Author**: [Model Context Protocol](https://github.com/modelcontextprotocol)  |  [GitHub Repo](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)  |  65.5k Stars|7.7k Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

Puppeteer MCP brings powerful web automation to Claude Code through the Model Context Protocol. Control headless Chrome browsers, scrape dynamic content, and automate complex web workflows with AI vision capabilities to handle cookies, captchas, and interactive elements automatically.

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **AI Vision Integration** - Automatically handle cookies, captchas, and interactive elements
-   **Headless Browser Control** - Launch and control Chrome/Chromium instances programmatically
-   **Dynamic Content Scraping** - Extract data from JavaScript-heavy and SPA applications
-   **High-Quality Markdown** - Convert web pages to well-formatted markdown
-   **Screenshot & PDF Generation** - Capture visual content and generate documents
-   **Form Automation** - Fill out forms, submit data, and handle user interactions

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Prerequisites**

-   Chrome or Chromium browser installed (auto-installed with NPX method)

**Setup MCP Server**

```bash
# Install via NPX (recommended)

npx -y @modelcontextprotocol/server-puppeteer

```

**Claude Code Configuration**

```bash
{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "puppeteer": {

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-puppeteer"]

        }

      }

    }

  }

}

```

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**Basic Web Automation**

```bash
# Navigate and extract content with AI vision

claude "Browse to the product page and extract all pricing information"

# Handle complex interactions automatically

claude "Navigate the login form and extract user dashboard data"

```

**Advanced Automation**

```bash
# AI-powered form filling

claude "Fill out the registration form and handle any captchas"

# Markdown conversion

claude "Convert the documentation page to high-quality markdown"

```

For detailed automation examples and API reference, refer to the [official documentation](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer).

##### Community Feedback

Developers find Puppeteer MCP valuable for complex web interactions that basic scraping tools can't handle. Particularly useful for navigating dynamic content, JavaScript-heavy sites, and automating multi-step workflows.

<img src="/img/discovery/018.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Puppeteer MCP is part of the official Model Context Protocol servers and is licensed under the MIT License. For technical support and updates, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)