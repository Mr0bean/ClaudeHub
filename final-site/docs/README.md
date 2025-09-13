---
title: "Claude Code 文档、指南与最佳实践 | Claude Hub"
---

# Claude Code 文档、指南与最佳实践 | Claude Hub


##### 最新文章

`/inspect` 版本中的 `context` 命令是上下文工程师的终极工具。获取MCP工具、自定义代理和内存文件的详细token分解，优化您的Claude Code性能。[了解更多关于上下文检查的信息](mechanics-context-inspection.html)

## 什么是Claude？[​](#什么是claude)

Claude是由[Anthropic](https://www.anthropic.com/)开发的AI助手，旨在服务人类的长期福祉。通过网页聊天、桌面和移动应用以及API提供服务，Claude提供编程、研究、写作、客户支持和AI代理开发等功能。通过Claude Sonnet 4和Claude Haiku 4等模型，Claude致力于负责任的AI开发，注重安全性和可靠性。

有关最新文档，请访问[Anthropic的Claude文档](https://docs.anthropic.com/en/docs/intro-to-claude)

* * *

* * *

## 什么是Claude Code？[​](#什么是claude-code)

Claude Code是一个智能化编程工具，它存在于您的终端中，理解您的代码库，并通过自然语言命令帮助您更快地编写代码。通过直接与您的开发环境集成，Claude Code无需额外的服务器或复杂设置即可简化您的工作流程。

Claude Code提供：

-   **终端集成**：直接在您的终端中运行，理解项目上下文并采取实际行动
-   **多文件能力**：在理解您的代码库和依赖关系的基础上，进行强大的多文件编辑
-   **企业集成**：与Amazon Bedrock或Google Vertex AI无缝连接，实现安全、合规的部署
-   **Git工作流管理**：读取问题、编写代码、运行测试和提交PR——全部在您的终端中完成
-   **扩展思考**：处理复杂的架构决策、具有挑战性的错误和多步骤实现

有关最新文档，请访问[Claude Code文档](https://docs.anthropic.com/en/docs/claude-code/overview)

* * *

* * *

## 转折点[​](#转折点)

当我第一次体验Claude Code时，它像一个破坏球一样击中了我，这项技术及其背后的机制可能会从根本上改变一切。与大多数AI编程工具定义的复制粘贴工作流不同，Claude Code引入了一个完全不同的范式，您可以设置任务、实时监控和引导进度，并审查已完成的工作，而不是反复手动地在AI环境之间复制粘贴信息。现在AI的环境直接与您的开发环境集成。

作为产品设计、发明、HCI设计的实践者以及Command Stick™的开发者，我真的只有一个问题...

> 它有多可靠？

在Command Stick™，我们开发了几个用于功能和主题的定制框架，所以我认为让Claude在新框架内开发功能将是一个很好的测试！

我兴奋极了！它用复选框指示其行动计划，传达其进度，并在必要时请求创建/编辑文件的权限。然而，当我尝试编译代码时，Android Studio抛出了错误。

我并没有因为错误而沮丧，相反，我很感兴趣并且兴高采烈！

> 如果我能让它遵循指令，我就能赚大钱了，我可以自动化功能和主题生成。

在失败的尝试之后，我迭代了[`CLAUDE.md`](mechanics-claude-md-supremacy.html)，将其细化为任务上下文、规则、编号步骤和示例的模块，这引导Claude走向成功。这成为了本指南中记录的许多Claude Code最佳实践和优化技术的基础。

当它工作时，就像魔法一样！

我继续让它生成各种功能片段，有些反复生成以查看实现中的差异程度，这也很有趣（稍后讨论）。

我抵制了开始生成大型项目的诱惑，专注于尝试理解是什么让Claude的按钮运转（就可靠性和速度而言），并将分享我的个人观察以及从[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI)收集的观察。

这个日志将通过实用的见解和技术帮助您从Claude和Claude Code中获得更多价值。

##### 旅程开始

欢迎来到Claude Hub，您掌握Claude Code的全面指南。这里的每一个技术、机制和见解都来自社区，并已在真实开发场景中由社区测试！


* * *

## Claude Code设置[​](#claude-code设置)

如果您需要安装Claude Code，我们的[安装指南](install-claude-code.html)可以帮助您。有关高级设置和优化，请参阅我们的[配置指南](configuration.html)。

-   [什么是Claude？](#什么是claude)
-   [什么是Claude Code？](#什么是claude-code)
-   [转折点](#转折点)
-   [Claude Code设置](#claude-code设置)