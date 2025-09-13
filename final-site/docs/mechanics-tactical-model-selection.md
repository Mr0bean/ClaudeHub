---
title: "战术模型选择 | Claude Hub"
---

# 战术模型选择 | Claude Hub

我注意到开发者中有一种趋势，就是选择在所有情况下都使用 Opus。这不仅是一个成本高昂的习惯，而且 Claude Opus 也不一定是每个操作的最佳模型。在幕后，Anthropic 会策略性地选择何时使用 Claude Haiku 3.5 来执行只需要最少智能的常规工作。

* * *

* * *

## 模型选择策略[​](#model-selection-strategy "Direct link to 模型选择策略")

**上下文窗口考虑因素：**

-   **标准模型**：200K 令牌（Opus、Sonnet 3.5、Haiku）
-   **通过 API 的 Sonnet 4**：1M 令牌（5倍大的上下文窗口）

**Opus（最昂贵、最高能力、200K 上下文）：**

-   需要深度推理的复杂架构决策
-   具有复杂依赖关系的多步骤逻辑问题
-   需要细致理解的创造性任务
-   需要架构判断的代码审查
-   跨多个系统的复杂重构

**Sonnet 4（成本性能平衡、通过 API 提供 1M 上下文）：**

-   理想用于大型代码库 - 1M 令牌窗口消除了上下文限制
-   标准功能实现和开发任务
-   大多数调试和故障排除场景
-   中等复杂度的代码生成
-   文档编写和编辑
-   任务协调和工作流管理
-   无需重置上下文的扩展开发会话

**Haiku（最便宜、最快）：**

-   简单的文件读取和基本内容提取
-   常规格式化和样式修正
-   基本语法验证和代码检查
-   简单的文本转换和数据解析
-   快速状态检查和基本分析

**Opus 计划模式（混合智能）：**

-   经济执行的复杂规划
-   需要 Opus 级推理的架构决策
-   具有成本约束的大型重构项目

* * *

* * *

## 成本优化方法[​](#cost-optimization-approach "Direct link to 成本优化方法")

我会将 Claude 4 Sonnet 设置为基础模型，并针对特定任务指示 Claude 使用 `claude --model claude-opus-4-20250514` 启动 Claude Opus 实例。这将允许特定进程以 Opus 作为其基础模型运行。

**上下文窗口策略：**

-   **对于大型项目**：通过 API 使用 Sonnet 4 以利用 1M 令牌上下文窗口
-   **对于复杂推理**：当架构决策需要卓越分析时切换到 Opus
-   **对于简单任务**：使用 Haiku 执行基本操作以最小化成本

这种策略相比让 Opus 驱动所有进程可能会带来巨大的成本节省。由于 Claude 4 Opus 的价格大约是 Claude 4 Sonnet 的 5 倍，因此有大量的财务预算可用于探索子代理的编排配置，以在保持性能的同时降低成本。Sonnet 4 通过 API 提供的巨大 1M 令牌上下文通常消除了在大型代码库场景中对 Opus 的需求。

**注意：** 在打印模式下生成 Claude 实例时，您可能需要增加 `max turns` 以确保进程完成：`claude -p --model claude-opus-4-20250514 --max-turns 20`

##### 成本优化

战略性的模型选择可以将 Claude Code 使用成本降低高达 80%，同时在大多数开发任务中保持输出质量。

<img src="/img/discovery/019.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[模型比较](/model-comparison.html)|[上下文窗口耗尽](/mechanics-context-window-depletion.html)|[计划模式](/mechanics-plan-mode.html)

**作者**：[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|[Command Stick](https://commandstick.com) CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAI) 版主

-   [模型选择策略](#model-selection-strategy)
-   [成本优化方法](#cost-optimization-approach)
```` but not the actual English content to translate. 

Could you please provide the actual English document content that needs to be translated to Chinese? Once you share the content, I'll translate it following all the rules you specified:

1. Keep all markdown formatting unchanged
2. Preserve all URL links
3. Keep proper nouns like Claude, VuePress, GitHub, API, CLI, JSON, MCP
4. Preserve code blocks and command line content
5. Translate title in frontmatter, keep other fields original
6. Keep HTML tags and attributes unchanged  
7. Use accurate technical terminology

Please share the English document content and I'll provide the Chinese translation directly.
```
