---
title: "TDD Guard | Claude Hub"
---

# TDD Guard | Claude Hub

**为 Claude Code 提供自动化测试驱动开发强制执行**

**作者**: [@nizos](https://github.com/nizos)  |  [GitHub 仓库](https://github.com/nizos/tdd-guard)  |  统计数据不可用

* * *

### 概述[​](#概述)

TDD Guard 是一个实用工具，通过拦截文件修改操作并验证 TDD 遵循情况来为 Claude Code 强制执行测试驱动开发原则。它阻止违反 TDD 规则的操作，特别是防止在没有失败测试的情况下实现功能、超出测试要求的过度实现，以及同时添加多个测试。

* * *

* * *

### 功能特性[​](#功能特性)

-   **测试优先强制执行** - 阻止在没有失败测试的情况下进行实现
-   **过度实现预防** - 防止超出当前测试要求的代码
-   **多重测试检测** - 阻止同时添加多个测试
-   **可自定义规则** - 调整验证规则以匹配你的 TDD 风格
-   **多语言支持** - 支持 JavaScript、Python、PHP、Go 和 Rust
-   **自动化流程强制执行** - 让 TDD Guard 处理纪律性问题，你专注于设计

* * *

* * *

### 安装[​](#安装)

**要求**

-   Node.js 18+
-   Claude Code
-   适用于你的语言的测试框架

**快速开始**

**1. 安装 TDD Guard**

```bash
npm install -g tdd-guard
```

**2. 添加测试报告器** TDD Guard 需要从你的测试运行器捕获测试结果。选择你的语言：

-   **JavaScript/TypeScript**
-   **Python (pytest)**
-   **PHP (PHPUnit)**
-   **Go**
-   **Rust**

请参阅[官方仓库](https://github.com/nizos/tdd-guard)了解特定语言的测试报告器设置。

**3. 配置 Claude Code 钩子** 在 Claude Code 中使用 `/hooks` 命令：

1.  在 Claude Code 中输入 `/hooks`
2.  选择 **PreToolUse - 工具执行前**
3.  选择 **+ 添加新匹配器...** 并输入：`(Edit|Write|MultiEdit)`
4.  选择 **+ 添加新钩子...** 并输入：`tdd-guard validate "$@"`
5.  选择保存位置（推荐项目设置）

请参阅[强化 TDD 执行](https://github.com/nizos/tdd-guard#hardened-tdd-enforcement)以防止代理绕过验证。

* * *

* * *

### 使用方法[​](#使用方法)

TDD Guard 作为独立进程运行，并根据 TDD 原则验证文件修改。它拦截 `Edit`、`Write` 和 `MultiEdit` 操作，检查三种主要 TDD 违规：

1.  在没有失败测试的情况下实现功能
2.  超出测试要求的过度实现
3.  同时添加多个测试

这种自动化让你专注于问题解决和设计，而不是手动监控 TDD 流程遵循情况。

**安全提示** TDD Guard 钩子以你的完整用户权限执行。请仔细审查钩子配置并确保你的开发环境得到适当保护。

有关详细配置选项和高级使用模式，请参阅[官方文档](https://github.com/nizos/tdd-guard/blob/main/README.md)。

* * *

### 优势[​](#优势)

TDD Guard 自动化 TDD 纪律执行，提供几个关键优势：

-   **一致的代码质量** - 防止常见的 AI 编程错误，如直接跳到实现
-   **全面的测试覆盖** - 确保测试优先编写并覆盖所有功能
-   **活文档** - 你的测试套件成为代码库的全面文档
-   **专注设计** - 自动化流程执行让你专注于问题解决
-   **扩展执行** - 可以配置为执行超出 TDD 的额外编程标准

性能注意事项

请注意，TDD Guard 可能会给你的 `Edit`、`Write`、`MultiEdit` 和 `TodoWrite` 操作引入延迟，因为它会根据 TDD 原则验证每个操作。

##### TDD 自动化

TDD Guard 自动化测试驱动开发的纪律性，让你专注于问题解决和设计，同时确保一致地遵循 TDD 原则。


* * *

*TDD Guard 由 Nizar 开发，采用 MIT 许可证开源。如需技术支持、配置帮助和社区讨论，请参考官方 GitHub 仓库。*

-   [概述](#概述)
-   [功能特性](#功能特性)
-   [安装](#安装)
-   [使用方法](#使用方法)
-   [优势](#优势)