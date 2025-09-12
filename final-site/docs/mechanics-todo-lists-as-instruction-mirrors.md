---
title: "待办清单作为指令镜子 | ClaudeLog"
---

# 待办清单作为指令镜子 | ClaudeLog

待办清单工具是我第二喜欢的 Claude Code 工具，仅次于任务/代理工具。待办清单工具不仅仅是跟踪进度——它揭示了 Claude 如何解释你的指令。

我经常使用 Claude 的待办清单来衡量我的指令，特别是对于那些我期望能够镜像反映的分步过程。当他的待办清单反映了我的意图时，我知道我的指令被理解了。当他的待办清单偏离时，它标志着我沟通中可能需要改进的地方。

* * *

* * *

**待办清单差异**

-   **错误顺序**：指令指定先做步骤A再做B，但 Claude 的待办清单列出B然后A
-   **缺失待办**：指令提到运行测试，但 Claude 的待办清单完全忽略了这一步
-   **额外待办**：Claude 添加"备份现有文件"，而指令从未提及此事
-   **错误粒度**：指令说"更新文档"，但 Claude 为每个单独的文件创建单独的待办
-   **误解步骤**：指令说"审查更改"，但 Claude 列出"提交更改"

**实时引导**

Claude 的待办清单传达了实时引导 Claude 目标的效果。当 Claude 在任务中期审查你的提示并用它们来更新他的计划时，你可以引导未来的待办。

考虑一个更改元素颜色的基本例子。正确利用待办清单可以更清楚地引导未来的待办，因为你可以确切看到他计划做什么。

**引导前：**

-    修复导航菜单对齐
-    更新页脚文本
-    添加新的联系表单验证
-    将按钮背景颜色更改为 `#ff0000`
-    更新文档

**任务中期引导：**

```
Actually, let's change the button color to blue (#0066cc) instead of red
```

**引导后：**

-    修复导航菜单对齐
-    更新页脚文本
-    添加新的联系表单验证
-    将按钮背景颜色更改为 `#0066cc`
-    更新文档

##### 实验

尝试鼓励 Claude 在他的待办中更加精细。不是"设置导航栏样式"，让 Claude 揭示具体的调整："将高度从60px改为80px"，"将padding-top从16px减少到12px"，"将背景从#ffffff调整为rgba(255,255,255,0.9)"。这种透明度在 Claude 做出设计决定之前就暴露了他的决定，让你能够批准或重新引导他的美学选择。

<img src="/img/supporters/inventorblack.jpg" alt="InventorBlack" style="max-width: 25px; height: 25px; border-radius: 50%;" />

* * *

**另见**：[你是主线程](/mechanics-you-are-the-main-thread.html)|[紧密反馈循环](/mechanics-tight-feedback-loops.html)|[CLAUDE.md 至上](/mechanics-claude-md-supremacy.html)

**作者**：[<img src="/img/supporters/inventorblack.jpg" alt="InventorBlack" style="max-width: 25px; height: 25px; border-radius: 50%;" />InventorBlack](https://x.com/InventorBlack)|[Command Stick](https://commandstick.com) 首席技术官|[r/ClaudeAi](https://reddit.com/r/ClaudeAi) 版主