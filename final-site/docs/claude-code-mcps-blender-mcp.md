---
title: "Blender MCP | ClaudeLog"
---

# Blender MCP | ClaudeLog

**革命性的 AI 驱动 3D 建模工具，将 Blender 连接到 Claude AI，实现自然语言场景创建和对象操作。**

**作者**: [ahujasid](https://github.com/ahujasid)  |  [GitHub 仓库](https://github.com/ahujasid/blender-mcp)  |  13k Stars|1.2k Forks|MIT License|更新于 2025年8月24日

* * *

### 概述[​](#概述 "Direct link to 概述")

Blender MCP 通过模型上下文协议在 Blender 和 Claude AI 之间创建双向桥接，实现提示辅助的 3D 建模和场景创建。这种集成允许用户使用自然语言指令创建、修改和操作 3D 对象，为各种技能水平的用户实现 3D 设计的民主化。

* * *

* * *

### 功能特性[​](#功能特性 "Direct link to 功能特性")

-   **自然语言 3D 建模** - 使用对话式提示创建和修改 3D 对象
-   **双向通信** - 基于套接字的服务器，实现与 Blender 的实时交互
-   **场景管理** - 全面控制灯光、摄像机和场景属性
-   **资源集成** - 直接访问 Poly Haven HDRIs、纹理和 3D 模型
-   **Python 代码执行** - 通过 AI 提示在 Blender 中运行任意 Python 脚本
-   **材质控制** - 使用 AI 辅助应用和修改材质、颜色和纹理

* * *

* * *

### 安装[​](#安装 "Direct link to 安装")

**先决条件**

-   Blender 3.0 或更新版本（推荐 3.6+ 以获得完整功能）
-   Python 3.10 或更新版本
-   uv 包管理器

**安装命令**

```bash
# 安装 uv 包管理器 (macOS)

curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 uv 包管理器 (Windows)

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 安装 uv 包管理器 (Linux)

curl -LsSf https://astral.sh/uv/install.sh | sh

```

**Blender 配置**

```bash
# 1. 从仓库下载 addon.py

# 2. 打开 Blender → 编辑 → 偏好设置 → 插件

# 3. 点击"安装..."并选择 addon.py

# 4. 启用"MCP Blender Bridge"插件

```

**Claude Desktop 配置**

```bash
{

  "mcpServers": {

    "blender": {

      "command": "uvx",

      "args": ["blender-mcp"]

    }

  }

}

```

* * *

* * *

### 使用方法[​](#使用方法 "Direct link to 使用方法")

**场景创建示例**

```bash
# 通过 Claude 的自然语言命令：

# "创建一个有棕榈树和岩石的海滩场景"

# "添加日落 HDRI 并调整照明"

# "生成一个低多边形角色模型"

# "将海洋材质应用到水平面"

```

该集成通过对话式交互支持复杂的 3D 工作流程。用户可以描述场景、修改对象属性、从集成库下载资源，并执行高级建模操作，而无需深入了解 Blender 知识。

**高级功能**

-   **资源下载**：与 Poly Haven 和 Hyper3D 库的自动集成
-   **场景分析**：AI 可以检查和描述当前的 Blender 场景
-   **代码生成**：为复杂操作生成并执行 Python 脚本
-   **基于参考的创建**：从参考图像生成 3D 场景

* * *

##### 社区见解

Blender MCP 被称为"3D 艺术家的游戏规则改变者"，用户报告称"几乎不了解 Blender 的业余用户可以使用自然语言来描述模型。"该集成代表了"实时展现的文本到 3D 工作流程"，类似的服务器也在 Unity 和虚幻引擎中出现。

<img src="/img/discovery/021_happy.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Blender MCP 由 ahujasid 开发，由 Warp 赞助。如需技术支持、贡献和社区讨论，请参考官方 GitHub 仓库和 Discord 社区。*

-   [概述](#概述)
-   [功能特性](#功能特性)
-   [安装](#安装)
-   [使用方法](#使用方法)