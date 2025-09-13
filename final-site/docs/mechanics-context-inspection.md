---
title: "上下文检查 | Claude Hub"
---

# 上下文检查 | Claude Hub

`/context` 斜杠命令是在 Claude Code 中推出的新功能，它允许你查看不同组件的上下文使用情况的近似值：

-   **系统提示** - 核心指令和行为定义
-   **系统工具** - 内置的 Claude Code 功能
-   **MCP 工具** - Model Context Protocol 服务器集成
-   **内存文件** - `CLAUDE.md` 和项目上下文
-   **自定义代理** - 专业化子代理定义
-   **消息** - 当前对话历史

它显示了使用了多少令牌以及剩余多少百分比的上下文窗口。

> 这是进行上下文工程的终极工具。

* * *

* * *

### 战略性上下文工程[​](#strategic-context-engineering)

我特别感兴趣的是轻松访问关于[自定义代理](/mechanics-custom-agents.html)和[MCP 工具](/claude-code-mcps.html)的指标。鉴于[基于上下文窗口的性能下降](/mechanics-context-window-depletion.html)的存在，作为上下文工程师，我们必须尽可能高效地设计上下文。

我们现在可以战略性地启用/禁用 MCP 工具功能，同时完全了解消耗了多少令牌。不再需要猜测那个 MCP 服务器功能是否值得上下文开销。

同样的原则适用于 Custom Agents，它们由 Claude Code 设计为易于发现、共享、下载和调用。正如我在[代理工程](/mechanics-custom-agents.html)中提到的，重要的是要优化你的代理，使它们能够轻松激活，但也要让它们在上下文上高效。`/context` 命令允许我们更好地内省我们的 Custom Agents 的效率。

* * *

* * *

### 当前限制和未来潜力[​](#current-limitations-and-future-potential)

初步使用表明上下文计算的准确性有时可能不准确。然而，我认为价值更多在于工程化基本上在你上下文中的内容，这会影响你的基线性能。我预期随着 Anthropic 对上下文计算方式进行细微调整，该工具的准确性会随着时间的推移而改善。

该用户界面的潜在升级将是能够使用箭头键导航项目并将它们切换开/关，这样我们就可以有效地分配上下文内的空间。这可能需要 Claude Code 重新加载，但它将创造更无缝的上下文工程体验。

### 与其他机制的集成[​](#integration-with-other-mechanics)

这个工具与诸如自动释放与工具调用相关的上下文窗口空间的功能相结合，有助于在长时间会话中创建更流畅的上下文高效管理体验。

* * *

* * *

### 交互式上下文分析[​](#interactive-context-analysis)

我探索的一个很酷的事情是，在生成上下文数据后，我询问 Claude：

> 我的上下文在哪里可能效率不高？

他提供了关于如何设计上下文以提高效率的建议。这创建了一个反馈循环，你可以识别瓶颈并相应地进行优化。

**机制优势：**

-   **令牌可见性**：清晰分解所有组件的上下文消耗
-   **战略优化**：基于数据驱动的 MCP 工具和自定义代理决策
-   **性能工程**：在上下文膨胀影响响应质量之前识别它
-   **基线意识**：了解你的基本上下文开销以便更好的规划
-   **交互式分析**：要求 Claude 审查并建议上下文改进

##### 上下文工程

要求 Claude 审查你的上下文使用情况并建议优化。结合使用[计划模式](/mechanics-plan-mode.html)和[超级思考](/mechanics-ultrathink-plus-plus.html)进行全面分析："我的上下文在哪里可能效率不高，我该如何优化它？"


* * *

**另见**：[上下文窗口衰竭](/mechanics-context-window-depletion.html)|[代理工程](/mechanics-custom-agents.html)|[自定义代理](/mechanics-custom-agents.html)


-   [战略性上下文工程](#strategic-context-engineering)
-   [当前限制和未来潜力](#current-limitations-and-future-potential)
-   [与其他机制的集成](#integration-with-other-mechanics)
-   [交互式上下文分析](#interactive-context-analysis)