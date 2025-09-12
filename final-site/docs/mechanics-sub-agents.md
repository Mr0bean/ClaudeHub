---
title: "子代理 | ClaudeLog"
---

# 子代理 | ClaudeLog

Claude Code 中的子代理使用已经从手动编排演变为智能自动化。本指南涵盖了子代理利用的两种方法：`手动子代理`和`自定义代理`。

* * *

### 手动子代理[​](#manual-sub-agents "Direct link to Manual Sub-agents")

使用 [Task 工具](/mechanics-task-agent-tools/) 进行显式并行处理的原始方法：

```bash
Use 3 sub-agents to analyze these files:

1. Security analysis of auth.ts

2. Performance review of cache system

3. Type checking of utils.ts

```

**优势**：直接控制、可预测的行为 **劣势**：手动编排开销、无法控制 `工具/MCP 选择`、共享 `系统提示` 继承、所有任务使用相同的 `模型`

* * *

* * *

### 自定义代理[​](#custom-agents "Direct link to Custom Agents")

具有隔离上下文、自定义 `系统提示` 和 `工具选择` 的专用代理，能够自动激活（详细配置请参见 [自定义代理](/mechanics-custom-agents/)）：

```bash
---

name: security-reviewer

description: Security analysis specialist for authentication and authorization code

tools: Read, Grep, Bash

model: opus

---

You are a security expert specializing in authentication vulnerabilities...

```

**优势**：自动激活、隔离的上下文、令牌效率 **劣势**：设置开销、配置复杂性

* * *

### 决策框架[​](#decision-framework "Direct link to Decision Framework")

根据您的特定需求和工作流程要求选择正确的子代理方法：

**何时使用手动子代理**：

-   **简单的并行操作**：文件读取、搜索、基本分析
-   **一次性分析**：多视角审查，您希望准确指定使用哪些视角
-   **需要快速周转**：无设置开销
-   **您想要显式控制**：直接编排哪些子代理处理哪些任务
-   **非破坏性工作**：研究、分析、比较矩阵

**何时使用自定义代理**：

-   **重复需要专业知识**：您在多个项目中进行的代码审查、安全分析、性能优化
-   **特定领域的工作**：UX 审查、SEO 优化、技术写作、可访问性审计
-   **需要特定角色的工具访问**：只能访问 Read 和 Grep 工具的安全代理，而不是文件修改工具
-   **长期可重用性**：一次构建，随处使用
-   **您更喜欢自动委派**：让 Claude 根据上下文智能地将任务路由到正确的专家
-   **团队标准化**：在整个团队中共享相同的代理配置
-   **跨项目部署**：在新代码库中立即工作的精炼代理

构建您的代理工具库

随着您在项目中的进展，积累一系列专用代理。记录常见模式，使用子代理指南更新您的 `CLAUDE.md`，并为重复需要的专业知识创建[自定义代理](/mechanics-custom-agents/)。

##### 协调智能

现代子代理使用既提供了手动委派的直接控制，又提供了自动专业化的效率。像高性能开发团队一样设计您的代理生态系统，让每个专家在其领域中表现出色。

<img src="/img/discovery/033_energy_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另请参阅**：[Task 代理工具](/mechanics-task-agent-tools/)|[自定义代理](/mechanics-custom-agents/)|[代理工程](/mechanics-agent-engineering/)|[子代理策略](/mechanics-sub-agent-tactics/)

**作者**：[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|[Command Stick](https://commandstick.com) CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAI) 版主

-   [手动子代理](#manual-sub-agents)
-   [自定义代理](#custom-agents)
-   [决策框架](#decision-framework)