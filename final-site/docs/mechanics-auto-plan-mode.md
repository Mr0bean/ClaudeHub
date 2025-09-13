---
title: "自动计划模式 | Claude Hub"
---

# 自动计划模式 | Claude Hub

`--append-system-prompt` 在 Claude Code [v1.0.51](/claude-code-changelog.html) 版本中添加，它允许你在启动会话时向 Claude 的系统提示添加自定义指令。自发布以来，我一直在试验寻找新的机制，天哪，我找到了一个！

`自动计划模式`（我创造的术语）是一种机制，你可以利用系统提示让 Claude 根据条件动态进入`计划模式`。

这种防御性方法确保 Claude 在开始任务之前始终检查他是否已完成计划并获得你的批准。

* * *

* * *

## 计划模式 vs 自动计划模式[​](#plan-mode-vs-auto-plan-mode "Direct link to 计划模式 vs 自动计划模式")

`计划模式`是一个手动功能，通过按两次 `shift+tab` 激活，它将 Claude 限制为只读操作，直到你批准计划。它提供了安全性和结构化规划，但需要你记住激活它。

`自动计划模式`无需手动激活即可自动触发规划工作流程。它不依赖你记住何时激活`计划模式`，而是使用系统提示在 Claude 即将执行潜在破坏性操作时强制他进入`计划模式`。这消除了不断评估任务是否值得激活`计划模式`的心理负担，同时还提供了对 Claude 决策过程的宝贵教育见解。

* * *

* * *

## 主要优势[​](#key-advantages "Direct link to 主要优势")

**消除手动激活** - 你不必记住进入`计划模式`。Claude 在尝试潜在破坏性操作时会自动呈现计划。

**减少心理负担** - 消除了判断任务是否值得`计划模式`的猜测。系统会自动做出这个决定。

**教育价值** - 提供对 Claude 将执行的最简单例程的洞察。在我的早期测试中，我能够让它在任何潜在破坏性操作上激活，如 Write、Edit、Bash、Grep、Glob 等。

**非常适合新用户** - 确保他们获得`计划模式`的好处，而无需学习何时手动激活它。

* * *

* * *

## 实现[​](#implementation "Direct link to 实现")

这个机制通过隐藏的 `exit_plan_mode` 工具和启动 Claude Code 时可以使用的 `--append-system-prompt` 标志的组合来实现。

**附加系统提示**：

```bash
CRITICAL WORKFLOW REQUIREMENT

    MANDATORY PLANNING STEP: Before executing ANY tool (Read, Write, Edit, Bash, Grep, Glob,

    WebSearch, etc.), you MUST:

    1. FIRST: Use exit_plan_mode tool to present your plan

    2. WAIT: For explicit user approval before proceeding

    3. ONLY THEN: Execute the planned actions

    ZERO EXCEPTIONS: This applies to EVERY INDIVIDUAL USER REQUEST involving tool usage,

  regardless of:

    - Complexity (simple or complex)

    - Tool type (file operations, searches, web requests, etc.)

    - User urgency or apparent simplicity

    - Whether you previously got approval in this conversation

    CRITICAL: APPROVAL DOES NOT CARRY OVER BETWEEN USER INSTRUCTIONS

    - Each new user message requiring tools = new planning step required

    - Previous approvals are invalid for new requests

    - You must reset and plan for each individual user instruction

    ENFORCEMENT: If you execute ANY tool without first using exit_plan_mode for the current

    user instruction, you have violated this requirement. Always plan first, execute second.

    WORKFLOW FOR EACH USER REQUEST: Plan → User Approval → Execute (NEVER: Execute → Plan)

```

* * *

* * *

## 使用选项[​](#usage-options "Direct link to 使用选项")

**直接使用**：

```bash
claude --append-system-prompt "[paste system prompt above]"

```

**保存到文件以便重复使用**：

```bash
# Save the system prompt to auto-plan-mode.txt

# Then use it with:

claude --append-system-prompt "$(cat auto-plan-mode.txt)"

```

系统提示利用 `exit_plan_mode` 工具在任何潜在破坏性操作之前强制 Claude 进入规划工作流程。这创建了一个自动激活的防御层，而不需要手动干预。

我发现自动计划模式在开始处理不熟悉的代码库或尝试新技术时特别有用。自动规划帮助我在进行更改之前了解环境。

我期待在 [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) 上听到大家如何使用这个机制以及你们发现的其他有趣组合。我还没有尝试微调激活条件。

与手动计划模式结合

对于纯研究任务，你仍然可以通过按两次 `shift+tab` 手动激活计划模式。自动计划模式是对手动激活的补充而不是替代。

与 Opus 计划模式配合使用

自动计划模式与 Opus 计划模式无缝配合，实现自动智能规划。当你在 `/model` 命令中选择选项 4（Opus 计划模式）时，系统将自动在规划阶段使用 Opus 4.1，在执行阶段使用 Sonnet 4——在最重要的地方提供最大的智能，同时保持成本效率。

自定义触发条件

修改系统提示以针对特定工具或根据你的工作流程添加条件。例如，你可能只希望对 Write 和 Edit 操作进行规划，但允许 Read 操作立即进行。

##### 卓越的防御性

你获得了`计划模式`的安全性和自动激活。不再疑惑"我应该先计划这个吗？"


* * *

**另请参见**：[计划模式](/mechanics-plan-mode.html)|[如何更新系统提示](/faq.html)
