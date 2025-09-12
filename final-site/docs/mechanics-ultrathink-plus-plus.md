---
title: "Ultrathink++ | ClaudeLog"
---

# Ultrathink++

如果你还没有听说过，你可以调整 Claude 利用测试时计算的程度。在你的提示中添加 `<think>` 会告诉 Claude 他应该在思考方面全力以赴。

### Ultrathink 与计划模式[​](#ultrathink-与计划模式)

我个人在使用 `<think>` 时，通过 `<think>` + `plan mode` 获得了出色的结果。当你不想使用 `cursor` 时，这个组合特别有用。我发现它通常可以弥补复杂任务的智能差距，当这还不够时，我会选择通过执行多轮批判性的 `<think>` + `plan mode` 来"加速"模型。

### 加速引擎[​](#加速引擎)

加速引擎意味着指示 Claude 在 `<think>` 中创建一个计划，然后系统地批判该计划的遗漏边缘情况、冗余方面和排序低效问题。这个迭代过程推动模型通过多个思考周期来达到更高的性能。

* * *

* * *

### 终极堆栈[​](#终极堆栈)

如果你难以从 `<think>` + `plan mode` + `multi-round` + `criticism` 中获得性能，你可以将 `sub-agents` 加入其中。请求 Claude 使用 `sub-agents` 来分析任务或计划，其中每个子代理都有不同的角色，这会影响其对计划的建议。

这种策略由于使用 Claude 而具有标记效率，并且在使用多少子代理/角色以及应用的思考程度方面具有可扩展性。

* * *

* * *

### 为什么先用 Ultrathink 而不是 Opus[​](#为什么先用-ultrathink-而不是-opus)

`<think>` 是一个必须使用的机制，理想情况下应该在使用像 Opus 这样的高级模型之前与其他可用机制结合使用。

为什么？因为否则你就是在不必要地依赖一个贵 5 倍但没有提供 5 倍价值的模型。

### 完整堆栈[​](#完整堆栈)

-   **基础**：`<think>` 用于增强思考
-   **规划**：`plan mode` 用于结构化方法
-   **迭代**：`multi-round criticism` 用于多轮批判
-   **视角**：`sub-agents` 用于多样化分析
-   **混合智能**：`haiku` 用于自动 Haiku 规划与 Claude 执行

##### 计算优化

上述机制揭示了系统化机制堆叠中隐藏的潜力。通过组合 `<think>`、`plan mode`、`criticism` 和 `sub-agents`，你可以解锁智能放大，从而改变复杂问题的解决方式。

<img src="/img/discovery/036_cl_orange.png" alt="ClaudeLog 发现" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[计划模式](/mechanics-plan-mode.html)|[分角色子代理](/mechanics-split-role-sub-agents.html)|[什么是 UltraThink](/mechanics-ultrathink-plus-plus.html)

**作者**：[<img src="/img/profiles/inventorblack.jpg" alt="InventorBlack" style="width: 25px; height: 25px; border-radius: 50%;" />InventorBlack](https://x.com/inventorblack)|[Command Stick](https://commandstick.com) CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAI) 版主

-   [Ultrathink 与计划模式](#ultrathink-与计划模式)
-   [加速引擎](#加速引擎)
-   [终极堆栈](#终极堆栈)
-   [为什么先用 Ultrathink 而不是 Opus](#为什么先用-ultrathink-而不是-opus)
-   [完整堆栈](#完整堆栈)