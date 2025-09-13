---
title: "从约束中学习 | Claude Hub"
---

# 从约束中学习 | Claude Hub

在撰写本文时（2025年6月），约20万token的上下文窗口被视为一个负面的技术约束。但情况不必如此：约束可以成为培养有效利用更大上下文技能的训练场。

* * *

* * *

### 训练效应[​](#the-training-effect "Direct link to The Training Effect")

在token限制内工作迫使我们对包含什么内容、如何组织信息以及何时重新开始做出深思熟虑的选择。就像为较慢的硬件优化代码一样，这些约束培养了基本技能。

**没有限制时：**

-   毫无筛选地将整个代码库倾倒到上下文中
-   "以防万一"地包含切线信息
-   依赖模型来筛选噪音和不相关的细节
-   编写模糊的提示，期望模型自己理解意图

**有约束时：**

-   **显式文件选择** - 根据相关性有意地包含/排除特定文件
-   **明确任务定义** - 将目标分解为具体的、可操作的步骤
-   **上下文大小的分块** - 将大任务分割成适合token限制的片段
-   **模块化重构** - 将代码构建为精简、专注的模块，可以选择性地读取
-   **简洁示例** - 提供最少但有代表性的示例让模型学习模式
-   **精确提示** - 编写有针对性的请求，准确指定需要什么以及按什么顺序
-   **基于优先级的组织** - 将最关键的细节放在首位来组织信息

* * *

* * *

### 性能退化[​](#performance-degradation "Direct link to Performance Degradation")

随着上下文窗口填满，LLM的性能实际上会下降。模型变得不那么精确，更容易出错，在接近token限制时难以进行复杂推理。

目标是提供有效执行任务所需的最少上下文。这种方法同时最大化了性能、token效率和成本效率。

就像优化算法以获得更好的时间复杂度一样，你通过减少信息开销来消除不必要的操作，同时保持相同的有效输出。

### 可扩展的技能[​](#skills-that-scale "Direct link to Skills That Scale")

Token约束教会你：

-   识别必要上下文，同时积极过滤掉无关细节
-   利用 `CLAUDE.md` 获得更好的结果
-   理解不同信息片段之间的连接和依赖关系
-   区分项目特定上下文和模型已拥有的通用知识
-   选择高效展示模式的示例，而不是穷尽地覆盖所有情况

这些技能即使在无限上下文的情况下也会让你更有效。

### 悖论[​](#the-paradox "Direct link to The Paradox")

在无限上下文中学习的开发者可能会养成低效的习惯。而拥抱约束的人无论上下文大小如何都会成为更好的协作者。

在限制内工作教会了超越任何技术约束的基本原理。

##### 悖论

在无限上下文中学习的开发者可能会养成低效的习惯。而拥抱约束的人无论上下文大小如何都会成为更好的协作者。

<img src="/img/discovery/008.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另见**: [上下文窗口耗尽](/mechanics-context-window-depletion.html)|[动态内存](/mechanics-dynamic-memory.html)|[战术模型选择](/mechanics-tactical-model-selection.html)

**Author**:[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)

-   [训练效应](#the-training-effect)
-   [性能退化](#performance-degradation)
-   [可扩展的技能](#skills-that-scale)
-   [悖论](#the-paradox)