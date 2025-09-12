---
title: "Split Role Sub-Agents | ClaudeLog"
---

# Split Role Sub-Agents | ClaudeLog

A fascinating mechanic the [Reddit community](https://www.reddit.com/r/ClaudeAI/) brought to my attention is the ability to designate different roles to sub-agents.

### The Role Foundation[​](#the-role-foundation "Direct link to The Role Foundation")

Anthropic have [openly discussed](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts) providing Claude with a `Role` which helps get him in the zone for the task at hand, for example:

> Your role is as a seasoned security expert which specialises in pen testing.

Multiple members of the community have created sophisticated tools for orchestrating sub-agent roles. [SuperClaude](/claude-code-mcps/super-claude/) provides **9 cognitive personas** (architect, frontend, backend, security, analyzer, qa, performance, refactorer, mentor) that can be applied as universal flags to any command. [Claudia](/claude-code-mcps/claudia/) offers **custom AI agents** with tailored system prompts through a GUI interface for coordinating different agent roles.

* * *

* * *

### Native Implementation[​](#native-implementation "Direct link to Native Implementation")

However, I am old school and love exploring a tool's raw mechanics without third-party dependencies. So I experimented with asking Claude to `Utilise multiple sub-agents to validate this code from multiple perspectives`.

**Sub-Agent Coordination Strategy:**

1.  **Setup Phase** - Ensure Claude is in [Plan Mode](/mechanics/plan-mode/) and that [ultrathink](/mechanics/ultrathink-plus-plus/) is instantiated
2.  **Role Suggestion** - Claude automatically suggests various relevant roles applicable to the task
3.  **Perspective Selection** - Select the kind of perspectives you want the task reviewed from
4.  **Parallel Analysis** - Sub-agents complete their review using their specialized approaches
5.  **Consolidation** - Findings are consolidated and presented by Claude

**Perspective Selection Examples:**

After multiple successful attempts it becomes second nature to suggest quirky perspectives for Claude to analyse tasks/problems from different perspectives.

**Code Review Tasks:**

```bash
Create sub-agents and analyse the problem from the following perspectives:

factual, senior engineer, security expert, consistency reviewer, redundancy checker

```

**User Experience Tasks:**

```bash
Create sub-agents and analyse the problem from a:

creative, nooby user, designer, marketing, seo perspective

```

**Documentation Tasks:**

```bash
Create sub-agents to review this documentation from the following perspectives:

technical accuracy, beginner accessibility, SEO optimization, content clarity

```

Interestingly enough each perspective naturally gravitates toward different tools based on their role and problem-solving approach. This creates a more comprehensive analysis as different agents instinctively choose the most relevant combination of tools for their domain of expertise.

**Performance & Cost Optimization:**

This mechanic delivers exceptional value by maximizing Claude 4 Sonnet's capabilities through strategic orchestration. Rather than reaching for the 5x more expensive Opus model, split role sub-agents combined with [ultrathink](/mechanics/ultrathink-plus-plus/) unlock sophisticated analysis at Sonnet pricing. The parallel nature of [Task](/mechanics/task-agent-tools/) execution means multiple expert roles can analyze the same problem simultaneously, creating multiple insights that would be difficult to achieve through single-role analysis (due to previous roles and context influencing the context window).

### Beyond Coding Applications[​](#beyond-coding-applications "Direct link to Beyond Coding Applications")

This mechanic applies beyond coding! I have used noob, seo, engineer, vibe coder, non-coder perspectives to get additional opinions on aspects of ClaudeLog and it all happens in parallel safely within [Plan Mode](/mechanics/plan-mode/).

The beauty of split role sub-agents lies in their scalability - you can adapt the perspective combinations to any domain or problem type. Start with the fundamental technical perspectives, then experiment with creative combinations as you discover what insights each role type reveals. [A.B.E](/mechanics/always-be-experimenting/) (Always be experimenting)

##### Multi-Perspective Analysis

The power of split role sub-agents lies in their ability to surface insights you neither a single Claude instance could surface alone. Each perspective uses different tools and approaches, creating a comprehensive analysis that dramatically improves decision quality.

&lt;img src="/img/discovery/023_excite_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" /&gt;

##### Pushing the Limit

Utilise `Claude 4 Sonnet` + [Plan Mode](/mechanics/plan-mode/) + `ultrathink` + `role sub-agents` to extract the maximum performance from the Claude 4 Sonnet model, prior to reaching for the 5x more expensive and often overkill Claude 4 Opus model.

<img src="/img/discovery/037_sonnet_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Plan Mode](/mechanics/plan-mode/)|[Task Agent Tools](/mechanics/task-agent-tools/)|[Tactical Model Selection](/mechanics/tactical-model-selection/)|[Always Be Experimenting](/mechanics/always-be-experimenting/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [The Role Foundation](#the-role-foundation)
-   [Native Implementation](#native-implementation)
-   [Beyond Coding Applications](#beyond-coding-applications)