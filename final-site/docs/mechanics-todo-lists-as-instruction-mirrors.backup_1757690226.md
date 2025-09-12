---
title: "待办事项列表作为指令镜像 | ClaudeLog"
---

# 待办事项列表作为指令镜像 | ClaudeLog

待办事项列表工具是我第二喜欢的 Claude Code 工具，仅次于任务/代理工具。待办事项列表工具的作用不仅仅是跟踪进度，它还揭示了 Claude 如何解释你的指令。

我经常用 Claude 的待办事项来基准测试我的指令，特别是对于我期望得到镜像般反映的分步流程。当他的待办事项反映我的意图时，我知道我的指令被理解了。当他的待办事项出现偏差时，它标志着我的沟通中可能需要改进的地方。

* * *

* * *

**待办事项列表差异**

-   **顺序错误**：指令指定先做步骤 A 然后是 B，但 Claude 的待办事项列出先 B 后 A
-   **缺少待办事项**：指令提到运行测试，但 Claude 的待办事项列表完全省略了这一步
-   **额外的待办事项**：Claude 添加了"备份现有文件"，而指令从未提及这一点
-   **错误的粒度**：指令说"更新文档"，但 Claude 为每个单独的文件创建了单独的待办事项
-   **误解的步骤**：指令说"审查更改"，但 Claude 列出的是"提交更改"

**实时引导**

Claude 的待办事项列表传达了实时引导 Claude 目标的效果。当 Claude 在任务中审查你的提示并使用它们来更新他的计划时，你可以引导未来的待办事项。

考虑一个改变元素颜色的基本示例。正确利用待办事项列表可以更清晰地引导未来的待办事项，因为你可以准确地看到他计划做什么。

**引导前：**

-    修复导航菜单对齐
-    更新页脚文本
-    添加新的联系表单验证
-    将按钮背景颜色更改为 `blue`
-    更新文档

**任务中引导：**

```bash
实际上把它改成绿色

```

**引导后：**

-    修复导航菜单对齐
-    更新页脚文本
-    添加新的联系表单验证
-    将按钮背景颜色更改为 `green`
-    更新文档

##### 实验

尝试鼓励 Claude 在他的待办事项中更加细致。与其说"设置导航栏样式"，不如让 Claude 揭示具体的调整："将高度从 60px 更改为 80px"，"将 padding-top 从 16px 减少到 12px"，"将背景从 #ffffff 调整为 rgba(255,255,255,0.95)"。这种透明度在他做出设计决策之前就暴露了 Claude 的设计决策，让你可以批准或重新定向他的美学选择。

<img src="/img/discovery/024_excite_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

**另见**：[你是主线程](/mechanics-you-are-the-main-thread/)|[紧密的反馈循环](/mechanics-tight-feedback-loops/)|[CLAUDE.md 至上](/mechanics-claude-md-supremacy/)

**作者**：[<img src="/img/claudes-greatest-soldier.png" alt="InventorBlack profile" style="width: 25px; height: 25px; display: inline-block; vertical-align: middle; margin: 0 3px; border-radius: 50%;" />InventorBlack](https://www.linkedin.com/in/wilfredkasekende/)|CTO at [Command Stick](https://commandstick.com)|Mod at [r/ClaudeAi](https://reddit.com/r/ClaudeAI)