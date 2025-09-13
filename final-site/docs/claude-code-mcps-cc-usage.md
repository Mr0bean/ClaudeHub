---
title: "CC Usage | Claude Hub"
---

# CC Usage | Claude Hub

**使用详细分析监控您的 Claude Code 使用情况和成本**

**作者**: [@ryoppippi](https://github.com/ryoppippi)  |  [GitHub 仓库](https://github.com/ryoppippi/cc-usage)  |  725 Stars|215 Forks|MIT License|Updated Aug 24, 2025

* * *

### 概述[​](#overview)

CC Usage 是一个命令行工具，帮助您跟踪和分析您的 Claude Code 消耗。获取有关使用模式、成本的详细见解，并优化您的 Claude Code 工作流程。

* * *

* * *


* * *

* * *

### 功能特性[​](#features)

-   **每日和每月报告** - 查看按日期或月份汇总的令牌使用情况和成本
-   **5 小时区块监控** - 通过活动区块监控跟踪 Claude 计费窗口内的使用情况
-   **实时仪表板** - 实时监控显示活动会话进度和令牌消耗率
-   **模型跟踪** - 查看您正在使用的 Claude 模型以及每个模型的成本明细
-   **日期过滤** - 按日期范围过滤报告并以 JSON 格式导出数据
-   **MCP 集成** - 内置模型上下文协议服务器，用于与其他工具集成

* * *

* * *

### 安装[​](#installation)

**快速开始（推荐）**

```bash
npx cc-usage
```

**全局安装**

```bash
npm install -g cc-usage
```

* * *

* * *

### 使用方法[​](#usage)

**每日使用报告**

```bash
cc-usage daily
```

**每月报告**

```bash
cc-usage monthly
```

有关其他选项和高级用法，请阅读[官方文档](https://github.com/ryoppippi/cc-usage#readme)。

* * *

### 与 Claude Code 集成[​](#claude-code-integration)

CC Usage 与您现有的 Claude Code 设置配合使用，为您的 Claude 消耗模式提供透明度。

**工作流程集成**

-   在开发会话期间跟踪使用情况
-   根据使用数据优化提示效率
-   查看您使用 Claude Max 或 Pro 节省了多少钱

##### 社区需求

Claude Pro 和 Max 订阅的开发者经常对在不了解消耗模式的情况下达到使用限制感到沮丧。CC Usage 提供订阅使用的可见性，帮助优化工作流程并跟踪价值。

<img src="/img/profiles/ryoppippi.jpg" alt="@ryoppippi" style="width: 25px; height: 25px; border-radius: 50%;" />

* * *

*CC Usage 是一个独立的社区项目。有关技术支持和更新，请参考官方 GitHub 仓库。*
