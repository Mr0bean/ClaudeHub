---
title: "子代理策略 | ClaudeLog"
---

# 子代理策略 | ClaudeLog

[Claude AI 子版块](https://www.reddit.com/r/ClaudeAI/)上的许多朋友一直在问：

> 我如何利用 `子代理` 来执行任务？

### 理解任务类型[​](#understanding-task-types "Direct link to Understanding Task Types")

在使用 `子代理` 之前，您必须考虑不同的方面。首先，任务是非破坏性的还是潜在破坏性的，以及您打算执行的任务中存在什么样的依赖关系。

* * *

* * *

### 完美可并行化的任务[​](#perfect-parallelizable-tasks "Direct link to Perfect Parallelizable Tasks")

如果您有一个任务，想让 Claude 研究 8 个不同的 MCP，并撰写一份关于它们的优缺点以及如何适用于您在 `vision.md` 中定义的目标的报告。这是一个完美的并行化任务，因为每个 Claude 都在独立工作，不会干扰现有的代码库或彼此，它们可以将所有发现提供给主 Claude 代理，或者编写单独的发现文件，这些文件可以被主 Claude 代理读取和整合。

这个任务是非破坏性的且易于并行化，是您应该立即使用 `子代理` 的那种任务。

### 培养并行化的直觉[​](#developing-an-itch-for-parallelism "Direct link to Developing an Itch for Parallelism")

在执行多个这种类型的并行任务后，您应该开始培养一种 `并行化的直觉`。

另一个例子是在提交之前审查差异。我经常利用 `子代理` 来执行并行的冗余、安全、事实性、时间复杂度检查。毕竟，它们是并行运行的，所以实例化 `子代理` 并没有坏处。在实例化 `子代理` 之前，我会进入 `计划模式` 以确保任务以非破坏性的方式执行，因为 `子代理` 可能会尝试进行文件更改。

* * *

* * *

### 整合策略[​](#the-consolidation-strategy "Direct link to The Consolidation Strategy")

我使用这种策略的目标是整合建议，然后从单个 Claude 模型中对它们采取行动，通常是在清除上下文之后，让它以最佳状态开始。

日复一日，周复一周，我发现自己正在学习以越来越有创意的方式使用 `子代理`！谁知道下周会带来什么新的机制。

### 如何使用子代理[​](#how-to-use-sub-agents "Direct link to How to Use Sub-agents")

要回答最初的问题：您可以通过声明 `使用 3 个子代理来处理这个任务` 或 `为每个需要更新的文件创建一个子代理` 来明确请求 `子代理` 的数量。Claude 也会在适当的时候自动为非破坏性任务使用 `子代理`，但明确说明可以让您控制并行化策略。

##### 并行处理

像 AI 代理的 CPU 调度器一样思考。排队非破坏性任务，生成多个 `子代理`，然后整合它们的发现，并在交互模式下监督 Claude 逐步执行它们的建议。

<img src="/img/discovery/022_excite_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[任务代理工具](/mechanics-task-agent-tools/)|[分割角色子代理](/mechanics-split-role-sub-agents/)

**作者**：[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|[Command Stick](https://commandstick.com) CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAI) 版主

-   [理解任务类型](#understanding-task-types)
-   [完美可并行化的任务](#perfect-parallelizable-tasks)
-   [培养并行化的直觉](#developing-an-itch-for-parallelism)
-   [整合策略](#the-consolidation-strategy)
-   [如何使用子代理](#how-to-use-sub-agents)
