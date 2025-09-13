---
title: "分角色子代理 | Claude Hub"
---

# 分角色子代理 | Claude Hub

[Reddit 社区](https://www.reddit.com/r/ClaudeAI/)向我介绍了一个令人着迷的机制，即为子代理指定不同角色的能力。

### 角色基础[​](#the-role-foundation "Direct link to 角色基础")

Anthropic [公开讨论过](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)为 Claude 提供一个 `角色`，这有助于让他进入手头任务的状态，例如：

> 你的角色是一位专门从事渗透测试的资深安全专家。

社区的多位成员已经创建了用于编排子代理角色的复杂工具。[SuperClaude](/claude-code-mcps/super-claude.html) 提供了 **9 个认知角色**（架构师、前端、后端、安全、分析师、质量保证、性能、重构者、导师），可以作为通用标志应用于任何命令。[Claudia](/claude-code-mcps/claudia.html) 通过 GUI 界面提供**自定义 AI 代理**，具有定制的系统提示，用于协调不同的代理角色。

* * *

* * *

### 原生实现[​](#native-implementation "Direct link to 原生实现")

然而，我是老派的，喜欢在没有第三方依赖的情况下探索工具的原始机制。所以我尝试让 Claude `利用多个子代理从多个角度验证这段代码`。

**子代理协调策略：**

1.  **设置阶段** - 确保 Claude 处于[计划模式](/mechanics-plan-mode.html)并且 [ultrathink](/mechanics-ultrathink-plus-plus.html) 已实例化
2.  **角色建议** - Claude 自动建议适用于任务的各种相关角色
3.  **视角选择** - 选择你希望从哪种视角审查任务
4.  **并行分析** - 子代理使用其专门的方法完成审查
5.  **整合** - 发现结果由 Claude 整合并呈现

**视角选择示例：**

经过多次成功尝试后，为 Claude 建议古怪的视角来从不同角度分析任务/问题变得自然而然。

**代码审查任务：**

```bash
创建子代理并从以下视角分析问题：

事实性、高级工程师、安全专家、一致性审查员、冗余检查器

```

**用户体验任务：**

```bash
创建子代理并从以下角度分析问题：

创意、新手用户、设计师、营销、SEO 视角

```

**文档任务：**

```bash
创建子代理从以下视角审查此文档：

技术准确性、初学者可访问性、SEO 优化、内容清晰度

```

有趣的是，每个视角会根据其角色和解决问题的方法自然地倾向于不同的工具。这创建了更全面的分析，因为不同的代理本能地为其专业领域选择最相关的工具组合。

**性能与成本优化：**

这个机制通过策略性编排最大化 Claude 4 Sonnet 的能力，提供了卓越的价值。与其使用贵 5 倍的 Opus 模型，分角色子代理结合 [ultrathink](/mechanics-ultrathink-plus-plus.html) 可以以 Sonnet 的价格解锁复杂的分析。[Task](/mechanics-task-agent-tools.html) 执行的并行性质意味着多个专家角色可以同时分析同一问题，创造出通过单角色分析难以实现的多重洞察（由于之前的角色和上下文会影响上下文窗口）。

### 超越编码应用[​](#beyond-coding-applications "Direct link to 超越编码应用")

这个机制的应用超越了编码！我使用过新手、SEO、工程师、氛围编码者、非编码者的视角来获得对 Claude Hub 各个方面的额外意见，这一切都在[计划模式](/mechanics-plan-mode.html)内安全地并行发生。

分角色子代理的美妙之处在于它们的可扩展性 - 你可以将视角组合适应任何领域或问题类型。从基本的技术视角开始，然后在发现每种角色类型揭示的洞察时尝试创造性的组合。[A.B.E](/mechanics-always-be-experimenting.html)（始终保持实验）

##### 多视角分析

分角色子代理的力量在于它们能够揭示单个 Claude 实例无法单独发现的洞察。每个视角使用不同的工具和方法，创建全面的分析，显著提高决策质量。


##### 推向极限

利用 `Claude 4 Sonnet` + [计划模式](/mechanics-plan-mode.html) + `ultrathink` + `角色子代理` 从 Claude 4 Sonnet 模型中提取最大性能，然后再考虑使用贵 5 倍且经常过度的 Claude 4 Opus 模型。


* * *

**另请参阅**：[计划模式](/mechanics-plan-mode.html)|[任务代理工具](/mechanics-task-agent-tools.html)|[战术模型选择](/mechanics-tactical-model-selection.html)|[始终保持实验](/mechanics-always-be-experimenting.html)


-   [角色基础](#the-role-foundation)
-   [原生实现](#native-implementation)
-   [超越编码应用](#beyond-coding-applications)