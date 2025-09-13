---
title: "Claudia - Claude Code的GUI工具包 | Claude Hub"
---

# Claudia - Claude Code的GUI工具包 | Claude Hub

**Claude Code的图形界面，提供可视化项目管理、自定义AI代理和使用分析**

**作者**: [getAsterisk](https://github.com/getAsterisk)  |  [GitHub仓库](https://github.com/getAsterisk/claudia)  |  14.2k Stars|1k Forks|AGPL-3.0 License|更新于2025年8月24日

* * *

### 概述[​](#overview)

Claudia为Claude Code提供图形界面，非常适合偏好可视化工具而非终端工作流的开发者。通过会话时间线、自定义AI代理和现代桌面应用程序中的全面使用分析，改变您的Claude Code体验。

* * *

* * *

### 功能特性[​](#features)

-   **可视化项目浏览器** - 使用丰富的元数据和缩略图导航项目和会话
-   **会话时间线** - 带有检查点、分支和一键恢复的可视化历史
-   **自定义AI代理** - 创建具有定制系统提示的专门助手
-   **使用分析仪表板** - 实时跟踪令牌消耗和成本
-   **MCP服务器管理** - 集中管理所有模型上下文协议服务器
-   **跨平台支持** - 兼容Windows、macOS和Linux

* * *

* * *

### 安装[​](#installation)

**系统要求**

-   **内存**: 最少4GB（推荐8GB）
-   **存储**: 1GB可用空间
-   **操作系统**: Windows 10/11、macOS 11+或Linux（Ubuntu 20.04+）

**前置条件**

-   已安装Claude Code CLI
-   Rust (1.70+)和Bun（最新版）
-   Git

**特定平台设置：**

**Linux (Ubuntu/Debian):**

```bash
sudo apt update && sudo apt install -y libwebkit2gtk-4.0-dev build-essential curl wget libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
```

**macOS:**

```bash
xcode-select --install
brew install bun rust
```

**快速设置**

```bash
git clone https://github.com/getAsterisk/claudia.git
cd claudia
bun install
bun run tauri dev
```

* * *

* * *

### 使用[​](#usage)

**启动应用程序**

```bash
claudia start
```

**创建自定义代理**

1.  启动Claudia: `claudia start`
2.  导航至"CC Agents"→"Create New Agent"
3.  配置：名称、系统提示、模型、权限
4.  使用您的自定义代理执行专门任务

有关完整文档、高级功能和故障排除，请查看[官方仓库](https://github.com/getAsterisk/claudia)。

虽然我个人不使用Claudia，但我能理解DX如何吸引不同个人的偏好。它经常在[Claude subreddit](https://reddit.com/r/ClaudeAI)上被提及。完美的开发者体验仍然是一个持续的探索，创新应该继续蓬勃发展。

##### 图形界面

Claudia为Claude Code提供GUI界面，为那些偏好可视化工具而非基于终端工作流的用户提供更舒适的开发体验。图形化方式使会话管理、代理配置和使用分析更加易于访问。


* * *

*Claudia由getAsterisk团队开发，是AGPL-3.0许可证下的开源项目。如需技术支持和更新，请参考官方GitHub仓库。*
