---
title: "健全性检查 | Claude Hub"
---

# 健全性检查 | Claude Hub

> 原文：在 AI 代理之前，我们运行的健全性检查类似于：

```bash
console.log("sanity")

```

```bash
print("sanity")

```

```bash
Log.d("test", "sanity")

```

* * *

* * *

与 AI 代理协作时，我们必须执行不同类型的健全性检查。

在你的 `CLAUDE.md` 顶部添加你的名字：

**CLAUDE.md**

```bash
# 我的名字是 {NAME}

这个文件为 Claude Code 在处理此仓库时提供指导。

## 项目概述

这是一个使用 TypeScript 和 Vite 构建的 React 应用程序。

...

```

然后询问 Claude：

```bash
我的名字是什么？

```

* * *

这可以作为快速的健全性检查。如果 Claude 知道你的名字，一切正常。如果不知道，那么就有问题了。

有多种情况可能出错：

-   忘记设置 `CLAUDE.md`
-   将 `CLAUDE.md` 放在错误的文件夹中
-   意外删除了 `CLAUDE.md` 的部分内容
-   拼写错误为 `CLAUSE.md`
-   上下文窗口用尽（有时不可避免）

"健全性检查"配置的最简单方法是在 `CLAUDE.md` 顶部放置你的名字，然后询问 Claude 你的名字。

##### 实验

写这篇文章时的随机想法：在你的 `CLAUDE.md` 中分散设置"健全性检查点"可能会很有趣，这样你就可以在上下文窗口填满时检查它们的完整性。


* * *

**另请参见**：[CLAUDE.md 至上](/mechanics-claude-md-supremacy.html)|[配置](/configuration.html)|[上下文窗口约束](/mechanics-context-window-constraints-as-training.html)

