---
title: "动态内存"
---

# 动态内存

当 Claude Code 处于交互模式时，你可以让 Claude 临时修改自己的 `CLAUDE.md` 以在特定上下文中运行任务。任务完成后，你可以要求 Claude 将 `CLAUDE.md` 恢复到之前的状态。有几种方法可以备份 `CLAUDE.md`：

-   **Git 版本控制**：在更改之前使用 git stash 或 commit 以便轻松回滚
-   **文件复制**：让 Claude 复制到备份文件名，如 `CLAUDE.md.backup`

要更改通过 `CLAUDE.md` 接口持久化的信息，你可以使用带 # 的"快速内存"。

* * *

* * *

如果你有一个 `CLAUDE.md` 库，其中指定了执行不同任务的流程，这种机制就很有用。不幸的是，Claude 目前无法将对其 `CLAUDE.md` 的更改读入"内存"，除非它使用明确的命令，例如：

-   **快速内存**：使用 # 命令临时更改持久化信息
-   **内存刷新命令**：明确要求 Claude 重新读取修改后的 `CLAUDE.md`
-   **会话重启**：启动新的 Claude Code 会话以获取更改
-   **显式文件读取**：使用读取命令加载更新的内容

这促使我探索让 Claude 在具有不同 `CLAUDE.md` 的目录中生成另一个自身实例。好处包括：

-   **更清晰的上下文分离**：每个生成的实例都使用自己特定的 `CLAUDE.md` 上下文运行
-   **无内存重新加载问题**：新实例会自动加载其目录的 `CLAUDE.md`
-   **并行处理**：多个上下文可以同时运行而不会相互干扰
-   **减少上下文污染**：之前会话的上下文不会渗透到新的专门任务中

**注意：** Claude 实例会自动向上爬取目录结构并读取它们遇到的任何 `CLAUDE.md` 文件。因此，为了确保上下文的严格分离，请确保项目目录的 `CLAUDE.md` 是轻量级且非特定的。

##### 目录爬取

Claude 实例会自动向上爬取目录结构并读取它们遇到的任何 `CLAUDE.md` 文件。因此，为了确保上下文的严格分离，请确保项目目录的 `CLAUDE.md` 是轻量级且非特定的。

<img src="/img/directory-crawling.png" alt="Directory crawling behavior visualization" style="max-width: 400px; height: auto; display: block; margin: 20px auto;" />

* * *

**另请参阅**：[CLAUDE.md 至高无上](/mechanics-claude-md-supremacy.html)|[上下文窗口约束](/mechanics-context-window-depletion.html)|[上下文窗口耗尽](/mechanics-context-window-depletion.html)
