---
title: "Tactical Model Selection | ClaudeLog"
---

# Tactical Model Selection | ClaudeLog

I have seen a trend amongst developers of opting to use Opus for everything. Not only is this a costly habit, but Claude Opus is not necessarily the best model for every operation. Behind the scenes, Anthropic tactically chooses when to utilise Claude Haiku 3.5 to perform routine grunt work which requires minimal intelligence.

* * *

* * *

## Model Selection Strategy[​](#model-selection-strategy "Direct link to Model Selection Strategy")

**Context Window Considerations:**

-   **Standard Models**: 200K tokens (Opus, Sonnet 3.5, Haiku)
-   **Sonnet 4 via API**: 1M tokens (5x larger context window)

**Opus (Most Expensive, Highest Capability, 200K Context):**

-   Complex architectural decisions requiring deep reasoning
-   Multi-step logical problems with intricate dependencies
-   Creative tasks requiring nuanced understanding
-   Code reviews requiring architectural judgment
-   Complex refactoring across multiple systems

**Sonnet 4 (Balanced Cost-Performance, 1M Context via API):**

-   Ideal for large codebases - 1M token window eliminates context constraints
-   Standard feature implementation and development tasks
-   Most debugging and troubleshooting scenarios
-   Code generation with moderate complexity
-   Documentation writing and editing
-   Task coordination and workflow management
-   Extended development sessions without context resets

**Haiku (Cheapest, Fastest):**

-   Simple file reads and basic content extraction
-   Routine formatting and style corrections
-   Basic syntax validation and linting
-   Simple text transformations and data parsing
-   Quick status checks and basic analysis

**Opus Plan Mode (Hybrid Intelligence):**

-   Complex planning with economical execution
-   Architectural decisions requiring Opus-level reasoning
-   Large refactoring projects with cost constraints

* * *

* * *

## Cost Optimization Approach[​](#cost-optimization-approach "Direct link to Cost Optimization Approach")

I would set Claude 4 Sonnet as the base model and for specific tasks instruct Claude to launch a Claude Opus instance with `claude --model claude-opus-4-20250514`. This would allow specific processes to run Opus as their base model.

**Context Window Strategy:**

-   **For large projects**: Use Sonnet 4 via API to leverage the 1M token context window
-   **For complex reasoning**: Switch to Opus when architectural decisions require superior analysis
-   **For simple tasks**: Use Haiku for basic operations to minimize costs

This tactic can potentially offer huge cost savings over having Opus drive all processes. Due to Claude 4 Opus being approximately 5x more expensive than Claude 4 Sonnet, there is substantial financial budget for exploring orchestration configurations with sub-agents to bring costs down whilst retaining performance. Sonnet 4's massive 1M token context via API often eliminates the need for Opus in large codebase scenarios.

**Note:** When spawning Claude instances in print mode you may need to increase the `max turns` so that the process completes: `claude -p --model claude-opus-4-20250514 --max-turns 20`

##### Cost Optimization

Strategic model selection can reduce Claude Code usage costs by up to 80% while maintaining output quality for most development tasks.

<img src="/img/discovery/019.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**See Also**: [Model Comparison](/model-comparison/)|[Context Window Depletion](/mechanics/context-window-depletion/)|[Plan Mode](/mechanics/plan-mode/)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [Model Selection Strategy](#model-selection-strategy)
-   [Cost Optimization Approach](#cost-optimization-approach)