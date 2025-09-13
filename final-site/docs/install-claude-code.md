---
title: "安装 Claude Code | Claude Hub"
---

# 安装 Claude Code | Claude Hub

只需几步即可在您的系统上启动并运行 Claude Code。这份完整的 Claude Code 安装和设置指南涵盖了 Windows、Mac 和 Linux 系统的下载、安装、配置和模型选择。

**注意：** 如需最新的安装说明，请访问[官方 Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)。

* * *

* * *

## Claude Code 系统要求和先决条件[​](#claude-code-system-requirements-and-prerequisites)

Claude Code 支持以下操作系统：

-   **macOS** 10.15 (Catalina) 或更高版本
-   **Windows** 10 或更高版本
-   **Linux** (Ubuntu 18.04+、CentOS 7+ 或同等版本)

**硬件要求：**

-   最低 4GB RAM（我建议 16GB）
-   500MB 可用磁盘空间
-   用于 API 通信的互联网连接

## 先决条件[​](#prerequisites)

在安装 Claude Code 之前，请确保您拥有：

-   **Node.js** 18.0 或更高版本
-   **Anthropic API 密钥**（从 [console.anthropic.com](https://console.anthropic.com) 获取）
-   终端或命令提示符

* * *

* * *

## 如何安装 Claude Code：分步方法[​](#how-to-install-claude-code-step-by-step-approach)

### 选项 1：npm（推荐）[​](#option-1-npm-recommended)

```bash
npm install -g @anthropic-ai/claude
```

* * *

* * *

## Claude Code 设置和配置指南[​](#claude-code-setup-and-configuration-guide)

### API 密钥配置[​](#api-key-configuration)

安装后，使用您的 API 密钥配置 Claude Code：

```bash
claude auth
```

您将完成与 Claude Pro 或 Anthropic Console 账户的一次性 OAuth 流程。

### 替代方案：环境变量[​](#alternative-environment-variable)

您也可以使用环境变量设置 API 密钥：

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

将此添加到您的 shell 配置文件（`.bashrc`、`.zshrc` 等）以使其持久化。

* * *

### Claude Pro 订阅[​](#claude-pro-subscription)

**重要提示：** Anthropic API 按使用付费，频繁使用可能会变得昂贵。对于经常使用 Claude Code 的用户，[Claude Pro 订阅](https://claude.ai/upgrade)可能是更经济的选择。Claude Pro 以固定的月费提供更高的使用限制，非常适合大量使用 Claude Code 的开发者。

如果您计划以下情况，请考虑 Claude Pro：

-   每天使用 Claude Code 多个小时
-   处理大型代码库
-   定期执行复杂的多文件操作

**入门建议：** 如果您不确定自己的使用模式，可以考虑先购买约 20 美元的 API 额度，用您的典型工作流程测试 Claude Code。这将帮助您确定 Claude Pro 订阅对于您的特定用例是否值得投资。

有关完整的定价细分和计划比较，请参阅我们的 [Claude AI 定价指南](/claude-code-pricing.html)。

*免责声明：作者使用 Claude Pro。*

* * *

* * *

### Claude Code 模型选择和配置[​](#claude-code-model-selection-and-configuration)

Claude Code 支持多个模型。您可以指定使用哪个模型以获得最佳性能：

**Claude 3.5 Sonnet：** 最新的平衡性能和速度

```bash
claude --model claude-3-5-sonnet-20241022
```

**Claude 3 Opus：** 复杂任务的最大能力

```bash
claude --model claude-3-opus-20240229
```

**Claude 3 Haiku：** 最快且最具成本效益

```bash
claude --model claude-3-haiku-20240307
```

重要限制：Claude 3 Haiku

虽然 Haiku 具有成本效益，但它在 Claude Code 使用方面有重大限制：

-   **推理能力降低** - 在复杂的多步骤规划和架构决策方面有困难
-   **有限的上下文理解** - 在分析大型代码库和跨多个文件维护上下文方面效果较差
-   **简化的代码分析** - 可能会错过现代模型能够捕获的细微错误、依赖关系或复杂模式
-   **仅基本重构** - 不适合复杂的重构或功能实现
-   **有限的框架知识** - 对复杂框架或新颖编码模式的效果较差

**Haiku 的推荐用例：**

-   简单的单文件编辑
-   基本语法更正
-   快速代码问题
-   升级前学习 Claude Code 基础知识

对于严肃的开发工作，Claude 3.5 Sonnet 或 Opus 提供显著更好的结果，值得额外的成本。

**替代方法：** 您也可以在启动 Claude Code 时直接指定模型：

```bash
claude --model claude-3-5-sonnet-20241022 "Explain this function"
```

要监控您的使用情况和成本，请考虑 [cc-usage 插件](/claude-code-mcps-cc-usage.html)。

有关详细的模型比较和选择指南，请参阅我们的[完整模型比较指南](/mechanics-tactical-model-selection.html)。

* * *

* * *

## 特定平台的 Claude Code 设置：Windows、Mac 和 Linux[​](#platform-specific-claude-code-setup-windows-mac-and-linux)

### Claude Code Windows 设置[​](#claude-code-windows-setup)

为了在 Windows 上获得最佳的 Claude Code 体验，请遵循以下优化步骤：

#### WSL2 安装和配置[​](#wsl2-installation-and-configuration)

**1\. 安装 WSL2**（如果尚未安装）：

```powershell
wsl --install
```

**2\. 安装 Linux 发行版**（推荐 Ubuntu）：

```powershell
wsl --install -d Ubuntu
```

**3\. WSL2 性能优化：**

通过在 Windows 用户目录中创建 `.wslconfig` 来设置 WSL2 内存限制：

```ini
wsl2
memory=8GB
processors=4
```

**4\. 将 WSL2 更新到最新版本：**

```powershell
wsl --update
```

#### 终端推荐[​](#terminal-recommendations)

我个人使用 Windows Terminal 应用进行 Claude Code 开发。您可以从 [Microsoft Store](https://www.microsoft.com/store/productId/9N0DX20HK701) 或 [GitHub releases](https://github.com/microsoft/terminal/releases) 下载。

#### Claude Code VS Code 集成[​](#claude-code-vs-code-integration)

**1\. 安装 VS Code 扩展：**

-   **WSL 扩展：** `ms-vscode-remote.remote-wsl`
-   **远程开发扩展包：** `ms-vscode-remote.vscode-remote-extensionpack`

**2\. 将 VS Code 连接到 WSL：**

```bash
code .
```

**3\. 安装 Claude Code VS Code 扩展：** 从 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) 安装官方 Claude Code 扩展，或在 VS Code 的扩展面板中搜索"Claude Code"。

**4\. 完全重启 VS Code** 以使扩展生效。

**5\. 在 VS Code 中使用 Claude Code：**

```
Cmd+Shift+P > Claude: Start Chat
```

**6\. VS Code 集成功能：**

-   使用 `Cmd+Shift+/` (Mac) 或 `Ctrl+Shift+/` (Windows/Linux) 直接打开 Claude Code
-   文件引用：`Cmd+Shift+@` (Mac) 或 `Ctrl+Shift+@` (Windows/Linux) 插入文件引用
-   在 VS Code 的差异查看器中查看建议的更改

* * *

* * *

## 验证 Claude Code 安装：测试您的设置[​](#verifying-claude-code-installation-testing-your-setup)

通过运行以下命令验证您的 Claude Code 安装：

```bash
claude --version
```

您应该看到 Claude Code 的当前版本打印到终端。

##### 安装完成

成功安装 Claude Code 后，您现在可以访问最强大的 AI 开发工具之一。每一段伟大的开发旅程都始于坚实的基础。


* * *

**另请参阅**: [定价计划](/claude-code-pricing.html)|[常见问题](/contact.html)|[MCPs 和插件](/claude-code-mcps.html)|[计划模式](/mechanics-agent-engineering.html)
