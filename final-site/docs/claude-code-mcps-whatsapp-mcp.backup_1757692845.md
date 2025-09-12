---
title: "WhatsApp MCP | ClaudeLog"
---

# WhatsApp MCP | ClaudeLog

**为 Claude Code 提供个人 WhatsApp 消息和搜索功能**

**作者**: [lharries](https://github.com/lharries)  |  [GitHub 仓库](https://github.com/lharries/whatsapp-mcp)  |  4.7k 星标|693 分叉|MIT 许可证|更新于 2025年8月24日

* * *

### 概述[​](#overview "Direct link to 概述")

WhatsApp MCP 使 Claude Code 能够通过模型上下文协议与你的个人 WhatsApp 账户交互。搜索和阅读你的 WhatsApp 消息（包括媒体）、管理联系人，并使用 WhatsApp Web 的多设备 API 向个人或群组发送消息。

* * *

* * *

### 功能特性[​](#features "Direct link to 功能特性")

-   **消息搜索** - 搜索你的个人 WhatsApp 消息历史
-   **媒体支持** - 访问图片、视频、文档和音频消息
-   **联系人管理** - 按姓名或电话号码搜索联系人
-   **群组消息** - 向个人或群组发送消息
-   **本地存储** - 所有消息本地存储在 SQLite 数据库中
-   **隐私优先** - 消息仅在主动访问时发送给 LLM

* * *

* * *

### 安装[​](#installation "Direct link to 安装")

**前置要求**

-   支持多设备的 WhatsApp 账户
-   安装 Go 1.19+ 编程语言
-   安装 Python 3.6+
-   UV 包管理器：`pip install uv`
-   FFmpeg（可选，用于音频消息转换）
-   **Windows 用户**：启用 CGO 并安装 C 编译器

**步骤 1：克隆和构建**

```bash
git clone https://github.com/lharries/whatsapp-mcp.git

cd whatsapp-mcp

go build -o whatsapp-mcp-server

```

**步骤 2：WhatsApp 桥接设置**

```bash
cd whatsapp-bridge

# 启动桥接（按照仓库说明适配你的操作系统）

# 提示时使用 WhatsApp 移动应用扫描二维码

# 等待初始消息历史同步完成

```

**步骤 3：Claude Code 配置**

编辑 `~/.claude.json`：

```bash
{

  "projects": {

    "/path/to/your/project": {

      "mcpServers": {

        "whatsapp": {

          "command": "uv",

          "args": [

            "--directory",

            "/path/to/whatsapp-mcp-server",

            "run",

            "main.py"

          ],

          "env": {}

        }

      }

    }

  }

}

```

**步骤 4：启动服务**

1.  配置后重启 Claude Code
2.  确保 WhatsApp 桥接正在运行
3.  使用简单的联系人搜索命令测试

**故障排除**

-   **二维码问题**：确保手机上启用了 WhatsApp 多设备功能
-   **构建错误**：验证 Go 安装和 GOPATH 配置
-   **Windows 编译**：安装 TDM-GCC 或 Visual Studio 构建工具
-   **桥接连接**：检查防火墙设置和端口可用性

* * *

* * *

### 使用方法[​](#usage "Direct link to 使用方法")

**消息搜索和分析**

```bash
# 搜索你的消息历史

claude "搜索上周关于项目截止日期的消息"

# 分析对话模式

claude "上个月与 John 讨论的主要话题是什么？"

```

有关详细设置说明和高级配置，请参阅[官方文档](https://github.com/lharries/whatsapp-mcp)。

专业提示

设置 Claude Code 以监控发送到你自己 WhatsApp 号码的消息。通过给自己发消息并以"claude"开头，它允许你从任何有 WhatsApp 访问权限的设备远程访问 Claude Code - 包括桌面、移动设备和智能手表。

##### 可扩展性

WhatsApp MCP 为额外功能提供了良好的基础。该仓库可以轻松扩展以适应超出默认消息功能的自定义功能。

<img src="/img/discovery/004.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*WhatsApp MCP 由 lharries 作为社区项目开发。如需技术支持和设置帮助，请参考官方 GitHub 仓库。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)