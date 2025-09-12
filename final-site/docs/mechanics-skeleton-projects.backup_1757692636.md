---
title: "骨架项目 | ClaudeLog"
---

# 骨架项目 | ClaudeLog

当我想要实现某个功能或快速编码一个完整项目时，我发现没有什么比为 Claude 提供一个优秀的骨架项目更高效了，这个骨架项目定义了一个经过实战验证的结构供他迭代。这种方法在你使用不熟悉的语言时特别强大，因为骨架提供了你可能缺乏的架构基础和最佳实践。

* * *

* * *

### 骨架策略[​](#the-skeleton-strategy "Direct link to 骨架策略")

识别 GitHub 骨架项目的过程可以由 Claude 和一组[子代理](/mechanics-split-role-sub-agents/)来承担，以进一步提高流程效率。我倾向于用以下两种方式之一来处理：

### 方法 1：并行源研究[​](#method-1-parallel-source-research "Direct link to 方法 1：并行源研究")

让[子代理](/mechanics-split-role-sub-agents/)从不同来源并行查找资源：

-   **代理 1** - 利用 Reddit MCP
-   **代理 2** - 使用 Brave 搜索
-   **代理 3** - 使用 Bing 搜索
-   **代理 4** - 直接搜索 GitHub

### 方法 2：评估子代理[​](#method-2-evaluation-sub-agents "Direct link to 方法 2：评估子代理")

让一个 Claude 进行研究，然后分配多个[子代理](/mechanics-split-role-sub-agents/)不同的角色来评估所有发现的仓库：

-   **安全角色** - 漏洞评估
-   **可扩展性角色** - 修改和扩展的难易程度
-   **相关性角色** - 与用例的匹配程度
-   **实现角色** - 如何添加所需功能
-   **语言选择角色** - 最优技术栈
-   **文档角色** - 指南和示例的质量

* * *

* * *

### 效率倍增器[​](#the-efficiency-multiplier "Direct link to 效率倍增器")

上述策略让我能够快速完成研究任务，并为 Claude 提供一个经过全面测试的骨架供其工作，这个骨架已经过审查，同时为他提供了实现你所请求功能的[计划](/mechanics-plan-mode/)。

如果 Claude 无法基于特定骨架项目生成所需功能，你可以尝试其他备选仓库，或者如果你感觉雄心勃勃，可以克隆最好的两个仓库并同时构建它们。

我们的想象力是唯一的限制因素。

### 骨架选择标准[​](#skeleton-selection-criteria "Direct link to 骨架选择标准")

评估潜在的骨架项目时，请考虑：

-   **经过实战检验** - 在生产环境中得到验证
-   **文档完善** - 清晰的设置和使用说明
-   **积极维护** - 最近的提交和响应积极的维护者
-   **模块化结构** - 易于理解和修改
-   **技术对齐** - 匹配你的技术栈偏好

##### 基础策略

一个优秀的骨架项目价值连城，可以节省大量开发时间。Claude 无需从零开始，而是可以在经过验证的结构中迭代，大大减少设置开销，专注于核心价值交付。

<img src="/img/discovery/018_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另见**：[Git 克隆只是开始](/mechanics-git-clone-is-just-the-beginning/)|[分角色子代理](/mechanics-split-role-sub-agents/)|[任务代理工具](/mechanics-task-agent-tools/)

**作者**：[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|[Command Stick](https://commandstick.com) CTO|[r/ClaudeAi](https://reddit.com/r/ClaudeAI) 版主

-   [骨架策略](#the-skeleton-strategy)
-   [方法 1：并行源研究](#method-1-parallel-source-research)
-   [方法 2：评估子代理](#method-2-evaluation-sub-agents)
-   [效率倍增器](#the-efficiency-multiplier)
-   [骨架选择标准](#skeleton-selection-criteria)
