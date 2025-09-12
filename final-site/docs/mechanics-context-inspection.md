---
title: "Context Inspection | ClaudeLog"
---

# Context Inspection | ClaudeLog

The `/context` slash command is a new feature which dropped in `v1.0.86` which allows you to see an approximation of your context usage across different components:

-   **System Prompt** - Core instructions and behavior definitions
-   **System tools** - Built-in Claude Code functionality
-   **MCP tools** - Model Context Protocol server integrations
-   **Memory files** - `CLAUDE.md` and project context
-   **Custom Agents** - Specialized sub-agent definitions
-   **Messages** - Current conversation history

It shows how many tokens are used and what percentage of your context window is remaining.

> This is the ultimate tool for `Context Engineers`.

* * *

* * *

### Strategic Context Engineering[​](#strategic-context-engineering "Direct link to Strategic Context Engineering")

I am particularly interested in the ease of access to metrics about [Custom agents](/mechanics/custom-agents/) and [MCP tools](/claude-code-mcps/). Given the existence of [context window based performance depletion](/mechanics/context-window-depletion/), it is important for us as context engineers to craft the context as efficiently as possible.

We can now tactically enable/disable MCP tool functions with full knowledge about how many tokens are being consumed. No more guessing whether that MCP server functions is worth the context overhead.

The same principle applies to `Custom Agents` which are designed by Anthropic to be easily discovered, shared, downloaded and invoked. As I mentioned in [Agent Engineering](/mechanics/agent-engineering/), it is important to refine your agents so that they can easily be activated but also so that they are context efficient. The `/context` command allows us to have better introspection into how efficient our `Custom Agents` are.

* * *

* * *

### Current Limitations and Future Potential[​](#current-limitations-and-future-potential "Direct link to Current Limitations and Future Potential")

Initial use has flagged that the accuracy for context calculations can sometimes be off. However, I believe the value lies more in engineering what is fundamentally in your context, which affects your baseline performance. I anticipate the accuracy of the tool improving over time as Anthropic makes subtle adjustments to the way context is computed.

A potential upgrade of this user interface would be being able to use the arrow keys to navigate through the items and toggle them on/off so we can effectively `free up` space within the context. This would likely require a Claude reload but it would create a more seamless `Context Engineering` experience.

### Integration with Other Mechanics[​](#integration-with-other-mechanics "Direct link to Integration with Other Mechanics")

This tool in combination with features like the `Micro compact` feature which automatically frees up space within the context window related to tool calls helps create a more streamlined experience for managing context efficiently throughout long sessions.

* * *

* * *

### Interactive Context Analysis[​](#interactive-context-analysis "Direct link to Interactive Context Analysis")

A cool thing I explored is after generating the context data, I asked Claude:

> Where is my context potentially inefficient?

And he provided suggestions about how the context could be engineered to be more efficient. This creates a feedback loop where you can identify bottlenecks and optimize accordingly.

**Mechanic Benefits:**

-   **Token visibility**: Clear breakdown of context consumption across all components
-   **Strategic optimization**: Data-driven decisions about MCP tools and Custom Agents
-   **Performance engineering**: Identify context bloat before it impacts response quality
-   **Baseline awareness**: Understand your fundamental context overhead for better planning
-   **Interactive analysis**: Ask Claude to review and suggest context improvements

##### Context Engineering

Ask Claude to review your context usage and suggest optimizations. Use [Plan Mode](/mechanics/plan-mode/) combined with [ultrathink](/faqs/what-is-ultrathink/) for comprehensive analysis: "Where is my context potentially inefficient and how can I optimize it?"

<img src="/img/discovery/013_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Context Window Depletion](/mechanics/context-window-depletion/)|[Agent Engineering](/mechanics/agent-engineering/)|[Custom Agents](/mechanics/custom-agents/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [Strategic Context Engineering](#strategic-context-engineering)
-   [Current Limitations and Future Potential](#current-limitations-and-future-potential)
-   [Integration with Other Mechanics](#integration-with-other-mechanics)
-   [Interactive Context Analysis](#interactive-context-analysis)