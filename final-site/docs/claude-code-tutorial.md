---
title: "教程 | Claude Hub"
---

# 教程 | Claude Hub

现在您已经安装了 Claude Code，让我们设置您的项目并学习使用 Claude Code 来增强开发工作流程的基础知识。这个适合初学者的 Claude Code 教程涵盖了新用户的基本命令、示例、最佳实践和工作流程优化。

* * *

* * *

## Claude Code 项目设置和配置[​](#claude-code-project-setup-and-configuration "Direct link to Claude Code Project Setup and Configuration")

在深入了解命令和示例之前，让我们配置您的项目以便与 Claude Code 最佳配合。正确的设置可确保 Claude 从一开始就理解您的项目结构、编码标准和开发工作流程。

### CLAUDE.md 配置[​](#claudemd-configuration "Direct link to CLAUDE.md Configuration")

在项目根目录创建一个 `CLAUDE.md` 文件来帮助 Claude 理解您的项目。这是最重要的 Claude Code 最佳实践之一：

```bash
# CLAUDE.md

## 项目概述

项目的简要描述、目的和主要技术。

## 开发指南

- 编码标准和规范

- 文件结构偏好

- 测试方法

## 重要命令

- 构建命令

- 测试命令

- 开发服务器命令

```

Claude Code 启动时会自动读取此文件以提供项目上下文。

* * *

* * *

## 您的第一个 Claude Code 会话：分步教程[​](#your-first-claude-code-session-step-by-step-tutorial "Direct link to Your First Claude Code Session: Step-by-Step Tutorial")

Claude Code 提供两种主要的交互方式：

**交互模式：** 运行 `claude` 启动 REPL 会话 **一次性模式：** 使用 `claude "your question"` 进行快速命令

### 交互模式[​](#interactive-mode "Direct link to Interactive Mode")

在项目目录中启动 Claude Code：

```bash
cd your-project

claude

```

您将看到 Claude Code 提示符，准备协助您的开发任务。

### 一次性模式[​](#one-shot-mode "Direct link to One-shot Mode")

用于快速查询而无需启动完整会话：

```bash
claude -p "显示此目录中的文件"

claude -p "这是什么类型的项目？"

```

此模式非常适合快速提问或需要快速答案而不进入交互式会话时使用。

* * *

* * *

## Claude Code 示例：初学者的快速入门[​](#claude-code-examples-quick-wins-for-beginners "Direct link to Claude Code Examples: Quick Wins for Beginners")

以下是一些简单的请求，让您熟悉 Claude Code：

### 理解您的项目[​](#understanding-your-project "Direct link to Understanding Your Project")

```bash
显示此目录中的文件

```

Claude Code 将列出您的项目文件并解释它发现了什么。

```bash
这是什么类型的项目？

```

Claude 将分析您的项目结构并告诉您这是什么类型的应用程序。

```bash
解释这个项目的作用

```

基于您的文件和文档，Claude 将总结项目的目的。

### 快速分析[​](#quick-analysis "Direct link to Quick Analysis")

```bash
显示主入口点

```

Claude 将识别并显示启动应用程序的主要文件。

```bash
这个项目有哪些依赖项？

```

Claude 将读取您的 package.json、requirements.txt 或类似文件并列出依赖项。

```bash
如何运行这个项目？

```

Claude 将查找脚本和文档来告诉您如何启动项目。

### 您的第一个文件创建[​](#your-first-file-creation "Direct link to Your First File Creation")

让我们使用 Claude Code 创建您的第一个文件：

```bash
创建一个包含问候消息的 hello_world.txt 文件

```

Claude Code 将创建文件，向您展示它写了什么，并确认创建。这展示了 Claude 理解自然语言并在您的项目中执行实际操作的能力。

* * *

* * *

## 基本的 Claude Code 命令和示例[​](#essential-claude-code-commands-and-examples "Direct link to Essential Claude Code Commands and Examples")

### 文件操作[​](#file-operations "Direct link to File Operations")

```bash
# 读取文件

read src/components/Button.js

# 编辑文件

edit src/components/Button.js

# 创建新文件

write src/components/NewComponent.js

```

### 代码分析[​](#code-analysis "Direct link to Code Analysis")

```bash
# 分析代码结构

analyze this codebase

# 查找特定模式

find all React components

# 解释代码

explain how authentication works

```

### 开发任务[​](#development-tasks "Direct link to Development Tasks")

```bash
# 添加新功能

add a dark mode toggle to the app

# 修复错误

fix the memory leak in the data fetcher

# 重构代码

refactor the user service to use TypeScript

# 编写测试

write unit tests for the Button component

```

* * *

* * *

## 如何使用 Claude Code：自然语言命令[​](#how-to-use-claude-code-natural-language-commands "Direct link to How to Use Claude Code: Natural Language Commands")

Claude Code 理解自然语言请求，使其比传统开发工具更容易使用：

```bash
# 而不是复杂的 git 命令

"为我对用户认证做的所有更改创建一个提交"

# 而不是手动文件操作

"更新所有组件以使用新的主题系统"

# 而不是搜索文档

"如何在这个项目中设置数据库迁移？"

```

##### 欢迎来到未来

您刚刚迈出了使用 Claude Code 进行 AI 驱动开发的第一步。前方的旅程将带来软件开发中前所未有的生产力和创造力。


* * *

**另请参阅**: [定价计划](/claude-code-pricing.html)|[计划模式](/mechanics-plan-mode.html)|[MCPs 和附加组件](/claude-code-mcps.html)|[常见问题](/faq.html)
