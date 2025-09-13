---
title: "Blender MCP | Claude Hub"
---

# Blender MCP | Claude Hub

**革命性的 AI 驱动 3D 建模工具，将 Blender 连接到 Claude AI，实现自然语言场景创建和对象操作。**

**作者**: [ahujasid](https://github.com/ahujasid)  |  [GitHub 仓库](https://github.com/ahujasid/blender-mcp)  |  13k Stars|1.2k Forks|MIT License|更新于 2025年8月24日

* * *

### 概述[​](#overview)

Blender MCP 通过模型上下文协议在 Blender 和 Claude AI 之间创建双向桥接，实现提示辅助的 3D 建模和场景创建。这种集成允许用户使用自然语言指令创建、修改和操作 3D 对象，为各种技能水平的用户实现 3D 设计的民主化。

* * *

* * *

### 功能特性[​](#features)

-   **自然语言 3D 建模** - 使用对话式提示创建和修改 3D 对象
-   **双向通信** - 基于套接字的服务器，实现与 Blender 的实时交互
-   **场景管理** - 全面控制灯光、摄像机和场景属性
-   **资源集成** - 直接访问 Poly Haven HDRIs、纹理和 3D 模型
-   **Python 代码执行** - 通过 AI 提示在 Blender 中运行任意 Python 脚本
-   **材质控制** - 使用 AI 辅助应用和修改材质、颜色和纹理

* * *

* * *

### 安装[​](#installation)

**先决条件**

-   Blender 3.0 或更新版本（推荐 3.6+ 以获得完整功能）
-   Python 3.8 或更新版本
-   uv 包管理器

**安装命令**

```bash
git clone https://github.com/ahujasid/blender-mcp.git
cd blender-mcp
uv sync
```

**Blender 配置**

```python
# 在 Blender 脚本编辑器中运行
import sys
sys.path.append('/path/to/blender-mcp')
import blender_mcp
blender_mcp.start_server()
```

**Claude Desktop 配置**

```json
{
  "mcpServers": {
    "blender": {
      "command": "uv",
      "args": ["--directory", "/path/to/blender-mcp", "run", "blender-mcp"],
      "env": {}
    }
  }
}
```

* * *

* * *

### 使用方法[​](#usage)

**场景创建示例**

```
用户: "创建一个有红色立方体和蓝色球体的场景，用柔和的灯光照明"
Claude: 我将为您创建一个场景，包含一个红色立方体和蓝色球体，并添加适当的灯光...
执行 Blender 命令创建对象、应用材质、设置灯光
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

<img src="/img/discovery/036_cl_orange.png" alt="Custom image" style="max-width: 165px; height: auto;" />

* * *

*Blender MCP 由 ahujasid 开发，由 Warp 赞助。如需技术支持、贡献和社区讨论，请参考官方 GitHub 仓库和 Discord 社区。*

-   [概述](#overview)
-   [功能特性](#features)
-   [安装](#installation)
-   [使用方法](#usage)