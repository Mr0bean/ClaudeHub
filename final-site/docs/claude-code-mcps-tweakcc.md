---
title: "TweakCC | Claude Hub"
---

# TweakCC | Claude Hub

**用于个性化 Claude Code 界面的轻量级 MCP 工具，支持自定义主题和视觉增强**

**作者**: [@Piebald-AI](https://github.com/Piebald-AI)  |  [GitHub 仓库](https://github.com/Piebald-AI/tweakcc)  |  69 星标|4 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#概述)

TweakCC 通过全面的界面个性化改变你的 Claude Code 体验。这个轻量级 MCP 工具允许你自定义颜色、动画、消息和样式，创建反映个人偏好的独特开发环境。

基于 React 和 Ink 构建，TweakCC 提供交互式终端界面，用于创建自定义主题、从 70+ 种动画中选择，并个性化 Claude Code CLI 体验的每个方面。

* * *

* * *


* * *

* * *

### 功能特性[​](#功能特性)

-   **自定义主题创建** - 交互式 HSL/RGB 色彩选择器，完全自定义界面
-   **70+ 思考动画** - 从大量旋转和处理动画集合中选择
-   **个性化思考动词** - 在 Claude 处理状态期间显示的自定义消息
-   **Markdown 元素样式** - 自定义响应中 markdown 元素的外观（开发中）
-   **用户消息样式** - 个性化你的消息在聊天历史中的显示方式
-   **横幅文本自定义** - 使用 figlet 字体样式更改横幅文本
-   **跨平台支持** - 兼容 Windows、macOS 和 Linux
-   **持久化配置** - 设置保存在 `~/.claude-code/config.json` 中，并在更新后保持

* * *

* * *

### 安装[​](#安装)

**快速开始（推荐）**

```bash
npx tweakcc
```

**替代包管理器**

```bash
# 使用 yarn
yarn dlx tweakcc

# 使用 pnpm  
pnpm dlx tweakcc

# 全局安装
npm install -g tweakcc
tweakcc
```

* * *

* * *

### 使用方法[​](#使用方法)

**交互式主题创建**

```bash
tweakcc
```

按照交互式提示进行：

-   **使用可视化选择器选择自定义颜色**
-   **从 70+ 种动画中选择** 处理状态动画
-   **设置个性化思考动词** 用于自定义消息
-   **配置 markdown 样式** 用于响应格式（WIP 功能）

**配置管理**

TweakCC 通过修补 Claude Code 的 `config.json` 文件工作，并将你的偏好保存到 `~/.claude-code/tweakcc-config.json`。你的自定义包括：

-   **颜色主题** - 界面元素的 HSL/RGB 值
-   **动画选择** - 首选的思考/处理动画
-   **自定义消息** - 个性化的思考动词和横幅文本
-   **样式覆盖** - Markdown 和用户消息样式偏好

**环境集成**

-   运行 Claude Code 时自动应用你的自定义
-   配置在 Claude Code 更新后保持
-   重新运行 tweakcc 以修改或更新你的主题
-   兼容 Claude Code 版本 1.0+

有关详细配置选项和高级主题定制，请参阅[官方文档](https://github.com/Piebald-AI/tweakcc/blob/main/README.md)。

* * *

### 与 Claude Code 的集成[​](#与-claude-code-的集成)

TweakCC 与你的 Claude Code 安装无缝集成，提供个性化界面而不影响核心功能。

**增强的开发体验**

-   与你的开发环境匹配的视觉自定义
-   个性化动画和消息，获得独特的 AI 体验
-   在 Claude Code 更新后保持的持久主题
-   使自定义对所有用户都易于访问的交互式配置

##### CLI 个性化

开发者在 CLI 环境中花费大量时间，TweakCC 满足了对个性化、视觉上吸引人的界面的需求。该工具让 Claude Code 感觉独一无二，同时保持所有强大功能。

<img src="/img/supporters/piebald-ai.png" alt="Piebald AI Logo" style="max-width: 80px; height: auto;" />

* * *

*TweakCC 由 Piebald LLC 作为社区项目开发。如需技术支持和更新，请参考官方 GitHub 仓库。*
