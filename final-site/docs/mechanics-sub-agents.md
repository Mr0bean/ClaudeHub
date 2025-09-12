---
title: "Sub-Agents | ClaudeLog"
---

# Sub-Agents | ClaudeLog

Sub-agent usage in Claude Code has evolved from manual orchestration to intelligent automation. This guide covers the two approaches to sub-agent utilization: `manual sub-agents` and `custom agents`.

* * *

### Manual Sub-agents[​](#manual-sub-agents "Direct link to Manual Sub-agents")

The original approach using the [Task tool](/mechanics/task-agent-tools/) for explicit parallel processing:

```bash
Use 3 sub-agents to analyze these files:

1. Security analysis of auth.ts

2. Performance review of cache system

3. Type checking of utils.ts

```

**Benefits**: Direct control, predictable behavior **Drawbacks**: Manual orchestration overhead, no `tool/MCP selection` control, shared `system prompt` inheritance, same `model` for all tasks

* * *

* * *

### Custom Agents[​](#custom-agents "Direct link to Custom Agents")

Specialized agents with isolated contexts, custom `system prompts` and `tool selection` that activate automatically (see [Custom Agents](/mechanics/custom-agents/) for detailed configuration):

```bash
---

name: security-reviewer

description: Security analysis specialist for authentication and authorization code

tools: Read, Grep, Bash

model: opus

---

You are a security expert specializing in authentication vulnerabilities...

```

**Benefits**: Automatic activation, isolated contexts, token efficiency **Drawbacks**: Setup overhead, configuration complexity

* * *

### Decision Framework[​](#decision-framework "Direct link to Decision Framework")

Choose the right sub-agent approach based on your specific needs and workflow requirements:

**Use Manual Sub-agents When**:

-   **Simple parallel operations**: File reads, searches, basic analysis
-   **One-off analysis**: Multi-perspective reviews where you want to specify exactly which viewpoints to use
-   **Quick turnaround needed**: No setup overhead
-   **You want explicit control**: Direct orchestration of which sub-agents handle which tasks
-   **Non-destructive work**: Research, analysis, comparison matrices

**Use Custom Agents When**:

-   **Specialized expertise needed repeatedly**: Code review, security analysis, performance optimization that you do across multiple projects
-   **Domain-specific work**: UX review, SEO optimization, technical writing, accessibility audits
-   **Role-specific tool access required**: Security agents that only have access to Read and Grep tools, not file modification tools
-   **Long-term reusability**: Build once, use everywhere
-   **You prefer automatic delegation**: Let Claude intelligently route tasks to the right specialist based on context
-   **Team standardization**: Share the same agent configurations across your entire team
-   **Cross-project deployment**: Refined agents that work instantly in new codebases

Building Your Agent Arsenal

As you progress through projects, amass a collection of specialized agents. Document common patterns, update your `CLAUDE.md` with sub-agent guidelines, and create [Custom Agents](/mechanics/custom-agents/) for repeatedly needed expertise.

##### Orchestrated Intelligence

Modern sub-agent usage provides both direct control of manual delegation and the efficiency of automatic specialization. Design your agent ecosystem like a high-performance development team where each specialist excels at their domain.

<img src="/img/discovery/033_energy_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Task Agent Tools](/mechanics/task-agent-tools/)|[Custom Agents](/mechanics/custom-agents/)|[Agent Engineering](/mechanics/agent-engineering/)|[Sub-agent Tactics](/mechanics/sub-agent-tactics/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [Manual Sub-agents](#manual-sub-agents)
-   [Custom Agents](#custom-agents)
-   [Decision Framework](#decision-framework)