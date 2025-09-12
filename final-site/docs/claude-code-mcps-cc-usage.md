---
title: "CC Usage | ClaudeLog"
---

# CC Usage | ClaudeLog

**Monitor your Claude Code API usage and costs with detailed analytics**

**Author**: [@ryoppippi](https://github.com/ryoppippi)  |  [GitHub Repo](https://github.com/ryoppippi/ccusage)  |  7.2k Stars|215 Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

CC Usage is a command-line tool that helps you track and analyze your Claude Code API consumption. Get detailed insights into your usage patterns, costs, and optimize your Claude Code workflows.

* * *

* * *

<!-- Screenshot temporarily removed due to missing asset -->

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **Daily & Monthly Reports** - View token usage and costs aggregated by date or month
-   **5-Hour Block Monitoring** - Track usage within Claude's billing windows with active block monitoring
-   **Live Dashboard** - Real-time monitoring showing active session progress and token burn rate
-   **Model Tracking** - See which Claude models you're using with per-model cost breakdown
-   **Date Filtering** - Filter reports by date range and export data in JSON format
-   **MCP Integration** - Built-in Model Context Protocol server for integration with other tools

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Quick Start (Recommended)**

```bash
npx ccusage@latest  # or: bunx ccusage  # or: pnpm dlx ccusage

```

**Global Installation**

```bash
npm install -g ccusage && ccusage daily

```

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**Daily Usage Report**

```bash
# View daily token usage and costs

ccusage daily

```

**Monthly Reports**

```bash
# Monthly usage summary

ccusage monthly

```

For additional options and advanced usage, read the [official documentation](https://github.com/ryoppippi/ccusage).

* * *

### Integration with Claude Code[​](#integration-with-claude-code "Direct link to Integration with Claude Code")

CC Usage works alongside your existing Claude Code setup to provide transparency into your API consumption patterns.

**Workflow Integration**

-   Track usage during development sessions
-   Optimize prompt efficiency based on usage data
-   See how much money you saved with Claude Max or Pro

##### Community Need

Developers on Claude Pro and Max subscriptions frequently express frustration about hitting usage limits without understanding consumption patterns. CC Usage provides visibility into subscription usage, helping optimize workflows and track value.

<img src="/img/discovery/013.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*CC Usage is an independent community project. For technical support and updates, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Integration with Claude Code](#integration-with-claude-code)