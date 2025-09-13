---
title: "紧密反馈循环 | Claude Hub"
---

# 紧密反馈循环

紧密反馈循环使 Claude 能够可靠地构建模块化功能。

> 有多紧密？

Claude 编写一个 bash 脚本，执行它，如果失败，Claude 会根据错误输出进行迭代，直到按要求工作为止，没有编译步骤，没有框架设置，没有构建过程，只是编写、执行、迭代。

这种设置创建了我所观察到的最紧密的智能体调试循环，得益于结果立即出现在 Claude 工作的同一终端中，为他提供了自主行动所需的所有必要数据。Bash 的轻量级特性意味着零启动时间、无运行时开销，以及没有抽象层的即时反馈。

目前，我主要使用这种设置来构建数据可视化工具和实验性编排框架。今天是第零天，我相信我们还没有触及这种设置能力的表面。

* * *

* * *

**与 Claude 和自主生成脚本协作的技巧：**

-   指示 Claude 记录脚本创建过程中遇到的任何异常行为、边缘情况或实现怪癖。这为未来的修改和调试会话创建了宝贵的上下文。
    
-   保持脚本专注和模块化，以便舒适地适应 Claude 的上下文窗口。
    
-   自己设计整体系统架构，然后将各个脚本组件委托给 Claude。你定义和指定预期的输入和输出签名越清晰越好。
    
-   指示 Claude 为使用 bash 脚本创建一个指南文档（如 CLAUDE.md 文件）。当他用你的提示测试脚本时，让他根据实际使用过程中发现的任何问题迭代更新指南文档。
    

我可以想象一个未来，数十个脚本无缝协作，Claude 在任务执行期间按需自主生成临时问题解决脚本。临时脚本甚至可以由一个子代理创建并由另一个子代理使用，创建一个自主工具生成和消费的动态生态系统，解决方案有机地涌现。

##### 临时脚本

开发的未来可能涉及 Claude 在任务执行期间自主生成临时问题解决脚本，创建一个工具生成和消费的动态生态系统。

<img src="/img/discovery/015_cl_orange.png" alt="Tight Feedback Loops Discovery" style="max-width: 165px; height: auto;" />

* * *

**另见**: [你是主线程](/mechanics-humanising-agents.html)|[待办事项列表作为指令镜像](/mechanics-todo-lists-as-instruction-mirrors.html)|[Git Clone 只是开始](/mechanics-git-clone-is-just-the-beginning.html)

**作者**:[<img src="/img/profile/inventorblack.png" alt="InventorBlack" style="width: 25px; height: 25px; border-radius: 50%;" /> InventorBlack](https://github.com/inventorblack)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/claudeai)