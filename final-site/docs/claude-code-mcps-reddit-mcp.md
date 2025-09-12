---
title: "Reddit MCP | ClaudeLog"
---

# Reddit MCP | ClaudeLog

**Reddit content access and analysis for Claude Code workflows**

**Author**: [Hawstein](https://github.com/Hawstein)  |  [GitHub Repo](https://github.com/Hawstein/mcp-server-reddit)  |  93 Stars|15 Forks|MIT License|Updated Aug 24, 2025

* * *

### Overview[​](#overview "Direct link to Overview")

Reddit MCP provides access to Reddit's public API for Claude Code, enabling content analysis, community research, and social media insights through the Model Context Protocol. Browse subreddits, read posts and comments, and analyze Reddit discussions seamlessly.

* * *

* * *

### Features[​](#features "Direct link to Features")

-   **Frontpage Access** - Browse Reddit's frontpage and trending posts
-   **Subreddit Browsing** - Access posts, comments, and community data from any subreddit
-   **Hot Posts Retrieval** - Get the most popular posts from specific communities
-   **Post Details** - Fetch detailed information about specific posts and their metadata
-   **Comment Trees** - Access comment threads and discussion hierarchies
-   **Public API Access** - No authentication required for public content

* * *

* * *

### Installation[​](#installation "Direct link to Installation")

**Prerequisites**

-   Python environment for the MCP server

**Setup MCP Server**

```bash
# Install via Python

python -m pip install mcp-server-reddit

# Or clone and install from source

git clone https://github.com/Hawstein/mcp-server-reddit.git

cd mcp-server-reddit

pip install -e .

```

**Claude Code Configuration**

```bash
{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "reddit": {

          "type": "stdio",

          "command": "node",

          "args": [

            "/path/to/reddit-mcp-server/build/index.js"

          ],

          "env": {}

        }

      }

    }

  }

}

```

* * *

* * *

### Usage[​](#usage "Direct link to Usage")

**Content Discovery**

```bash
# Browse Reddit frontpage

claude "Show me the current top posts on Reddit's frontpage"

# Access specific subreddit content

claude "Get the top 10 posts from r/programming today"

```

**Community Analysis**

```bash
# Analyze post engagement

claude "Analyze the comment patterns in r/MachineLearning posts"

# Track technology discussions

claude "Find discussions about AI coding tools across relevant subreddits"

```

**Research and Monitoring**

```bash
# Competitive research

claude "Research what developers are saying about different code editors"

# Trend analysis

claude "Analyze recent trends in web development discussions"

```

For complete API reference and advanced usage patterns, see the [official documentation](https://github.com/Hawstein/mcp-server-reddit).

##### Extensibility

Reddit MCP provides a great foundation for additional functionality. The repository can be easily extended to accommodate custom functionality beyond the default API methods.

<img src="/img/discovery/003.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Reddit MCP is developed by Hawstein as a community project. For technical support and updates, please refer to the official GitHub repository.*

-   [Overview](#overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)