---
title: "自动接受权限 | Claude Hub"
---

# 自动接受权限 | Claude Hub

自动接受权限是 Claude Code 中的一项机制，它消除了确认提示，使 Claude 能够立即执行操作，而无需中断流程以获得批准。

激活后，UI 会显示"auto-accept edit on"，Claude 在进行文件编辑、运行命令或其他操作之前不会暂停请求权限。权限请求界面通常在 Claude 判断某项任务可能存在潜在危险并需要明确批准时出现。

您可以通过更新 `claude_code_config.json` 配置来调整哪些工具可以通过自动接受模式使用（详见 [Claude Code 配置指南](/mechanics-dangerous-skip-permissions.html)）。

您可以通过反复按 `Cmd+J` 来激活它，以循环切换模式：普通模式、自动接受编辑开启和计划模式开启，如 Claude Code UI 中所示。

这一机制代表了与[计划模式](/mechanics-planning-mode.html)相反的安全光谱端，优先考虑速度和不间断执行，而不是谨慎验证。无缝的键盘切换使得根据工作流程需求轻松切换模式变得容易。

* * *

* * *

### 使用自动接受之前[​](#使用自动接受之前)

我发现自己在权限提示出现时，需要不断按 `Enter` 来批准 Claude 的操作，无论是文件修改、命令执行还是系统交互。

虽然这些提示具有重要的安全功能，但当您对 Claude 的方法有信心并希望不间断执行时，它们会产生摩擦。

[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) 上的用户也表达了对持续权限请求的类似挫败感，特别是在重构等重复性任务期间，或者在尝试实现 10-40 分钟的长时间代理冲刺时。

### 使用自动接受之后[​](#使用自动接受之后)

自动接受将 Claude Code 转变为无缝执行环境（假设您的 `claude_code_config.json` 设置正确）。Claude 立即进行文件编辑、命令执行和其他操作，而不会中断流程。

当我有明确的方向时，自动接受允许我让 Claude 自主工作，而我专注于其他任务。我可以专注于不同的工作，只有当他通过[铃声通知](/mechanics-notifications.html)系统联系我时才检查 Claude。

我观察到这在以下情况下特别有价值：

-   研究代码库和文档
-   跨多个文件的大型重构操作
-   遵循已经彻底检查过的长期计划

结果是迭代周期大大加快，并保持对问题的关注，而不是不断的批准决策。

* * *

* * *

### 安全注意事项[​](#安全注意事项)

请谨慎使用自动接受。没有权限提示，Claude 将立即执行所有建议的更改。文件修改无需确认即可进行，bash 命令立即运行，潜在的破坏性操作无需暂停即可发生。跨多个文件的大规模修改按顺序发生，如果出现问题会造成复合风险。

### 权限模式循环[​](#权限模式循环)

按 `Cmd+J` 可循环切换 Claude Code 的权限模式：

-   **普通模式** - 所有操作的标准权限提示
-   **自动接受编辑开启** - 自动接受任何操作的所有权限
-   **计划模式开启** - 只读研究和规划模式

UI 清楚地指示哪种模式处于活动状态，在您循环切换每个状态时显示确切的术语。

##### 执行流程

一旦启用自动接受，Claude 会保持持续的执行动力。我观察到，与普通模式的审慎验证节奏相比，这创造了一种明显不同的工作流程节奏。

<img src="/img/discovery/036_cl_orange.png" alt="Auto-accept permissions flow diagram" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[计划模式](/mechanics-planning-mode.html)|[允许的工具配置](/mechanics-dangerous-skip-permissions.html)|[危险的跳过权限](/mechanics-dangerous-skip-permissions.html)

**作者**：[<img src="/img/profiles/inventorblack.png" alt="InventorBlack" style="width: 25px; height: 25px; border-radius: 50%; vertical-align: middle;" /> InventorBlack](/contact.html)|[Command Stick](https://commandstick.com) 的 CTO|[r/ClaudeAi](https://www.reddit.com/r/ClaudeAI/) 版主

-   [使用自动接受之前](#使用自动接受之前)
-   [使用自动接受之后](#使用自动接受之后)
-   [安全注意事项](#安全注意事项)
-   [权限模式循环](#权限模式循环)