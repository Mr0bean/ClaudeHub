#!/usr/bin/env python3
import re

def translate_faq():
    file_path = 'final-site/docs/faq.md'
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translation mappings for section headers
    translations = {
        '## Installation & Setup': '## 安装与设置',
        '## Configuration': '## 配置', 
        '## Core Features': '## 核心功能',
        '## Plans & Pricing': '## 计划与定价',
        '## Best Practices': '## 最佳实践',
        '## Troubleshooting': '## 故障排除',
        '## Advanced Usage': '## 高级用法',
        '## Resources': '## 资源',
        '## AI Tools Fundamentals': '## AI 工具基础',
        '## Vibe Coding': '## 氛围编程',
        '## AI & Human-Computer Interface (HCI)': '## AI 与人机界面 (HCI)',
        
        # Installation & Setup section Q&As
        '**Q: Download Claude Code**': '**问：下载 Claude Code**',
        'A: Download Claude Code via npm': '答：通过 npm 下载 Claude Code',
        'Requires Node.js 18+ and Claude subscription or API key for authentication.': '需要 Node.js 18+ 和 Claude 订阅或 API 密钥进行身份验证。',
        
        '**Q: Download Claude Code for Windows**': '**问：为 Windows 下载 Claude Code**',
        'A: Requires WSL2 installation. Claude Code runs within the Linux environment on Windows through WSL2 only - no native Windows installation available.': '答：需要安装 WSL2。Claude Code 仅通过 WSL2 在 Windows 上的 Linux 环境中运行 - 没有原生 Windows 安装。',
        
        '**Q: Download Claude Code for Mac**': '**问：为 Mac 下载 Claude Code**',
        'A: Install via npm in Terminal on macOS 10.15+. Use Homebrew to install Node.js 18+ first for easy setup and version management.': '答：在 macOS 10.15+ 的终端中通过 npm 安装。首先使用 Homebrew 安装 Node.js 18+ 以便于设置和版本管理。',
        
        '**Q: How do I install Claude Code?**': '**问：如何安装 Claude Code？**',
        "A: Install Claude Code using npm: `npm install -g @anthropic-ai/claude-code`. You'll need Node.js 18.0+ and either an Anthropic API key or Claude Max subscription.": '答：使用 npm 安装 Claude Code：`npm install -g @anthropic-ai/claude-code`。您需要 Node.js 18.0+ 以及 Anthropic API 密钥或 Claude Max 订阅。',
        
        '**Q: Does Claude Code work on Windows?**': '**问：Claude Code 在 Windows 上工作吗？**',
        'A: Yes, Claude Code works smoothly on Windows via WSL2': '答：是的，Claude Code 通过 WSL2 在 Windows 上流畅运行',
        
        '**Q: How do I install Claude Code on Windows?**': '**问：如何在 Windows 上安装 Claude Code？**',
        'A: Install WSL2 first, then install Node.js and Claude Code within the Linux environment.': '答：首先安装 WSL2，然后在 Linux 环境中安装 Node.js 和 Claude Code。',
        
        '**Q: Does Claude Code work on Windows 11?**': '**问：Claude Code 在 Windows 11 上工作吗？**',
        'A: Yes, Claude Code works excellently on Windows 11 via WSL2.': '答：是的，Claude Code 通过 WSL2 在 Windows 11 上出色运行。',
        
        '**Q: How do I install Claude Code on Mac?**': '**问：如何在 Mac 上安装 Claude Code？**',
        'A: Install Node.js 18.0+, then run': '答：安装 Node.js 18.0+，然后运行',
        
        '**Q: Does Claude Code work on macOS?**': '**问：Claude Code 在 macOS 上工作吗？**',
        'A: Yes, Claude Code works natively on macOS 10.15+ with excellent performance.': '答：是的，Claude Code 在 macOS 10.15+ 上原生运行，性能出色。',
        
        '**Q: Can you use Claude Code on a VPS/remote server?**': '**问：可以在 VPS/远程服务器上使用 Claude Code 吗？**',
        'A: Yes, Claude Code can be installed and run on VPS with proper security setup.': '答：是的，可以在 VPS 上安装和运行 Claude Code，需要适当的安全设置。',
        
        '**Q: Is Claude Code slower on WSL compared to native Linux?**': '**问：与原生 Linux 相比，Claude Code 在 WSL 上更慢吗？**',
        'A: Yes, Claude Code typically runs more efficiently on native Linux': '答：是的，Claude Code 通常在原生 Linux 上运行更高效',
        
        '**Q: How do I update Claude Code to the latest version?**': '**问：如何将 Claude Code 更新到最新版本？**',
        'A: Run `npm update -g @anthropic-ai/claude-code`': '答：运行 `npm update -g @anthropic-ai/claude-code`',
        
        '**Q: How do I check my Claude Code version?**': '**问：如何检查我的 Claude Code 版本？**',
        'A: Run `claude --version`': '答：运行 `claude --version`',
        
        '**Q: How do I uninstall Claude Code?**': '**问：如何卸载 Claude Code？**',
        'A: See our': '答：请查看我们的',
        'uninstall guide': '卸载指南',
        'for step-by-step removal instructions including configuration cleanup.': '了解逐步删除说明，包括配置清理。',
        
        '**Q: Where is Claude Code installed?**': '**问：Claude Code 安装在哪里？**',
        'A: Claude Code installs globally via npm at': '答：Claude Code 通过 npm 全局安装在',
        'with configuration files in': '配置文件位于',
        
        '**Q: How do I revert Claude Code to a previous version?**': '**问：如何将 Claude Code 恢复到以前的版本？**',
        'A: Navigate to': '答：导航到',
        'and run': '并运行',
        '(replace version as needed). All settings, projects, and configuration data are preserved during version changes.': '（根据需要替换版本）。版本更改期间将保留所有设置、项目和配置数据。',
        
        '**Q: Can I use Visual Studio Code with Claude Code on Windows WSL?**': '**问：可以在 Windows WSL 上将 Visual Studio Code 与 Claude Code 一起使用吗？**',
        'A: Yes, you can edit files in Visual Studio Code while Claude Code runs in the WSL terminal.': '答：是的，您可以在 Visual Studio Code 中编辑文件，同时 Claude Code 在 WSL 终端中运行。',
        
        '**Q: Should I use Claude Code in the terminal or VS Code on Windows?**': '**问：我应该在 Windows 上的终端还是 VS Code 中使用 Claude Code？**',
        'A: For beginners, start with VS Code integration': '答：对于初学者，从 VS Code 集成开始',
        
        # Configuration section
        "**Q: How do you stop Claude Code from asking for permissions every time?**": "**问：如何阻止 Claude Code 每次都要求权限？**",
        "A: Use `Shift+Tab` to enable auto-accept mode": "答：使用 `Shift+Tab` 启用自动接受模式",
        
        "**Q: How do I enable auto-accept mode in Claude Code?**": "**问：如何在 Claude Code 中启用自动接受模式？**",
        "A: Press `Shift+Tab` repeatedly": "答：反复按 `Shift+Tab`",
        
        "**Q: What's the difference between auto-accept mode and plan mode?**": "**问：自动接受模式和计划模式有什么区别？**",
        "A: Auto-accept mode eliminates permission prompts": "答：自动接受模式消除权限提示",
        
        "**Q: What are Allowed Tools in Claude Code?**": "**问：Claude Code 中的允许工具是什么？**",
        "A: Allowed Tools configuration lets you specify": "答：允许工具配置让您指定",
        
        "**Q: Can I customize which tools are auto-accepted in Claude Code?**": "**问：我可以自定义 Claude Code 中哪些工具被自动接受吗？**",
        "A: Yes, configure `allowedTools`": "答：是的，配置 `allowedTools`",
        
        "**Q: What is --dangerously-skip-permissions in Claude Code?**": "**问：Claude Code 中的 --dangerously-skip-permissions 是什么？**",
        "A: A CLI flag that bypasses all safety checks": "答：一个绕过所有安全检查的 CLI 标志",
        
        "**Q: How do I set Claude Code permission mode?**": "**问：如何设置 Claude Code 权限模式？**",
        "A: Configure `defaultMode` in settings.json": "答：在 settings.json 中配置 `defaultMode`",
        
        "**Q: Is --dangerously-skip-permissions safe to use?**": "**问：--dangerously-skip-permissions 安全使用吗？**",
        "A: No, it removes all safety guardrails": "答：不，它移除了所有安全防护",
        
        "**Q: How do I update system prompt in Claude Code?**": "**问：如何在 Claude Code 中更新系统提示？**",
        "A: Use `--append-system-prompt`": "答：使用 `--append-system-prompt`",
        
        "**Q: What is --system-prompt-file flag in Claude Code?**": "**问：Claude Code 中的 --system-prompt-file 标志是什么？**",
        "A: The `--system-prompt-file` flag completely replaces": "答：`--system-prompt-file` 标志完全替换",
        
        "**Q: What is CLAUDE.md and why is it important?**": "**问：什么是 CLAUDE.md，为什么重要？**",
        "A: See our": "答：请查看我们的",
        "for project configuration fundamentals": "了解项目配置基础",
        
        "**Q: How should you structure your CLAUDE.md file?**": "**问：应该如何构建 CLAUDE.md 文件？**",
        "A: Break it into clear sections": "答：将其分成清晰的部分",
        
        "**Q: What is MCP Server in Claude Code?**": "**问：Claude Code 中的 MCP 服务器是什么？**",
        "A: MCP (Model Context Protocol) servers extend": "答：MCP（模型上下文协议）服务器扩展",
        
        "**Q: How do I configure an MCP server with Claude Code?**": "**问：如何配置 Claude Code 的 MCP 服务器？**",
        "A: Configure MCP servers in": "答：在以下位置配置 MCP 服务器",
        
        "**Q: How do I setup Claude Code MCP servers?**": "**问：如何设置 Claude Code MCP 服务器？**",
        "A: Install and configure MCP servers": "答：安装和配置 MCP 服务器",
        
        "**Q: Claude Code best MCP**": "**问：Claude Code 最佳 MCP**",
        "A: Best Claude Code MCP servers include": "答：最佳的 Claude Code MCP 服务器包括",
        
        "**Q: How do you add multiple working directories in Claude Code?**": "**问：如何在 Claude Code 中添加多个工作目录？**",
        "A: Use the `--add-dir` CLI argument": "答：使用 `--add-dir` CLI 参数",
        
        "**Q: How do I resume previous Claude Code conversations?**": "**问：如何恢复以前的 Claude Code 对话？**",
        "A: Use `--continue` to resume": "答：使用 `--continue` 恢复",
        
        "**Q: How do I run Claude Code in automation scripts and CI/CD?**": "**问：如何在自动化脚本和 CI/CD 中运行 Claude Code？**",
        "A: Use the `--print` flag": "答：使用 `--print` 标志",
        
        "**Q: How do I configure granular permissions for Claude Code automation?**": "**问：如何为 Claude Code 自动化配置细粒度权限？**",
        "A: Use the `--allowedTools` flag": "答：使用 `--allowedTools` 标志",
        
        "**Q: What are hooks in Claude Code?**": "**问：Claude Code 中的钩子是什么？**",
        "A: Hooks are user-defined shell commands": "答：钩子是用户定义的 shell 命令",
        
        "**Q: What is Super Claude for Claude Code?**": "**问：什么是 Claude Code 的 Super Claude？**",
        "A: SuperClaude is a configuration framework": "答：SuperClaude 是一个配置框架",
        
        "**Q: How do I switch between different Claude models in Claude Code?**": "**问：如何在 Claude Code 中切换不同的 Claude 模型？**",
        "A: Use the command line flag `--model`": "答：使用命令行标志 `--model`",
        
        "**Q: What are Model Aliases in Claude Code?**": "**问：Claude Code 中的模型别名是什么？**",
        "A: Model aliases are shortcuts": "答：模型别名是快捷方式",
        
        "**Q: Claude 4 Sonnet vs Opus for Claude Code - which should I choose?**": "**问：Claude 4 Sonnet 与 Opus 用于 Claude Code - 我应该选择哪个？**",
        "A: Use Claude 4 Opus for most development work": "答：大多数开发工作使用 Claude 4 Opus",
        
        "**Q: What is Claude 4.1 Opus?**": "**问：什么是 Claude 4.1 Opus？**",
        "A: Claude 4.1 Opus is Anthropic's latest maximum capability model": "答：Claude 4.1 Opus 是 Anthropic 最新的最大能力模型",
        
        "**Q: Which Claude model should I use with Claude Code?**": "**问：我应该在 Claude Code 中使用哪个 Claude 模型？**",
        "A: Claude 4 Sonnet is recommended": "答：推荐使用 Claude 4 Sonnet",
        
        # Core Features section
        "**Q: What is Plan Mode in Claude Code?**": "**问：Claude Code 中的计划模式是什么？**",
        "A: Plan Mode is Claude Code's safety feature": "答：计划模式是 Claude Code 的安全功能",
        
        "**Q: What is Auto Plan Mode in Claude Code?**": "**问：Claude Code 中的自动计划模式是什么？**",
        "A: `Auto Plan Mode` is a defensive system prompt technique": "答：`自动计划模式`是一种防御性系统提示技术",
        
        "**Q: What is Auto-Approve Mode in Claude Code?**": "**问：Claude Code 中的自动批准模式是什么？**",
        "A: Auto-Approve Mode eliminates confirmation prompts": "答：自动批准模式消除确认提示",
        
        "**Q: What is UltraThink in Claude Code?**": "**问：Claude Code 中的 UltraThink 是什么？**",
        "A: UltraThink is a Claude Code magic word": "答：UltraThink 是 Claude Code 的魔法词",
        
        "**Q: What is Output Styles in Claude Code?**": "**问：Claude Code 中的输出样式是什么？**",
        "A: Output Styles enable complete personality transformation": "答：输出样式可以完全改变个性",
        
        "**Q: How do you activate Plan Mode in Claude Code?**": "**问：如何在 Claude Code 中激活计划模式？**",
        "A: Press `Shift+Tab` twice": "答：按两次 `Shift+Tab`",
        
        "**Q: What are Background Commands in Claude Code?**": "**问：Claude Code 中的后台命令是什么？**",
        "A: Background commands allow you to run bash processes": "答：后台命令允许您运行 bash 进程",
        
        "**Q: What is Slash Commands in Claude Code?**": "**问：Claude Code 中的斜杠命令是什么？**",
        "A: Slash commands are built-in Claude Code commands": "答：斜杠命令是内置的 Claude Code 命令",
        
        "**Q: What are the most important Claude Code commands?**": "**问：最重要的 Claude Code 命令有哪些？**",
        "A: Essential commands include": "答：基本命令包括",
        
        "**Q: How do I see all Claude Code commands?**": "**问：如何查看所有 Claude Code 命令？**",
        "A: Type `/help` in Claude Code": "答：在 Claude Code 中输入 `/help`",
        
        "**Q: What is the Task tool in Claude Code and when should you use it?**": "**问：Claude Code 中的任务工具是什么，何时应该使用？**",
        "A: The Task tool launches parallel sub-agents": "答：任务工具启动并行子代理",
        
        "**Q: What are sub-agents in Claude Code?**": "**问：Claude Code 中的子代理是什么？**",
        "A: Sub-agents are specialized AI assistants": "答：子代理是专门的 AI 助手",
        
        '**Q: What does "Auto-Compact" mean in Claude Code?**': '**问：Claude Code 中的"自动压缩"是什么意思？**',
        "A: When context window approaches limit": "答：当上下文窗口接近限制时",
        
        "**Q: What is Micro-Compact in Claude Code?**": "**问：Claude Code 中的微压缩是什么？**",
        "A: Micro-compact automatically clears old tool calls": "答：微压缩自动清除旧的工具调用",
        
        '**Q: What does "context window full" mean in Claude Code?**': '**问：Claude Code 中的"上下文窗口已满"是什么意思？**',
        "A: The context window is Claude's memory limit": "答：上下文窗口是 Claude 的内存限制",
        
        "**Q: How do I manage Claude Code context window efficiently?**": "**问：如何有效管理 Claude Code 上下文窗口？**",
        "A: Use smaller files": "答：使用较小的文件",
        
        "**Q: Should I restart Claude Code or use the /clear command?**": "**问：我应该重启 Claude Code 还是使用 /clear 命令？**",
        "A: Use `/clear` first": "答：首先使用 `/clear`",
        
        "**Q: Can Claude Code analyze images and screenshots from my computer?**": "**问：Claude Code 可以分析我电脑上的图像和截图吗？**",
        "A: Yes, Claude Code can analyze images": "答：是的，Claude Code 可以分析图像",
        
        "**Q: How do I configure terminal setup for Claude Code?**": "**问：如何为 Claude Code 配置终端设置？**",
        "A: Run `/terminal-setup`": "答：运行 `/terminal-setup`",
        
        "**Q: How do I customize the status line in Claude Code?**": "**问：如何自定义 Claude Code 中的状态行？**",
        "A: Use the `/statusline` command": "答：使用 `/statusline` 命令",
        
        "**Q: What is the Status Line in Claude Code?**": "**问：Claude Code 中的状态行是什么？**",
        "A: The status line is a customizable area": "答：状态行是一个可自定义的区域",
        
        "**Q: How do I set up terminal bell notifications on Windows WSL?**": "**问：如何在 Windows WSL 上设置终端铃声通知？**",
        "A: For Windows WSL users": "答：对于 Windows WSL 用户",
        
        "**Q: What is Sub-Agent Delegation in Claude Code?**": "**问：Claude Code 中的子代理委派是什么？**",
        "A: Sub-agent delegation uses the Task tool": "答：子代理委派使用任务工具",
        
        "**Q: How do sub-agents work in Claude Code and when should I use them?**": "**问：子代理在 Claude Code 中如何工作，何时应该使用它们？**",
        "A: Sub-agents are parallel task executors": "答：子代理是并行任务执行器",
        
        "**Q: Do sub-agents consume the main agent's context window?**": "**问：子代理会消耗主代理的上下文窗口吗？**",
        "A: Sub-agents have their own separate context windows": "答：子代理有自己独立的上下文窗口",
        
        "**Q: How do I control how many sub-agents Claude Code uses?**": "**问：如何控制 Claude Code 使用多少个子代理？**",
        "A: You can explicitly request the number": "答：您可以明确请求数量",
        
        "**Q: Can you use Claude Code with multiple codebases simultaneously?**": "**问：可以同时在多个代码库中使用 Claude Code 吗？**",
        "A: Yes, open a separate terminal window": "答：是的，打开一个单独的终端窗口",
        
        "**Q: How should I optimize my Claude Code usage strategy?**": "**问：我应该如何优化我的 Claude Code 使用策略？**",
        "A: Pro users: Focus on Sonnet": "答：Pro 用户：专注于 Sonnet",
        
        # Continue with more sections...
        "##### Community Knowledge": "##### 社区知识",
        "These FAQs represent the collective wisdom of the Claude Code community. The questions answered here come from real developers solving actual problems and sharing their discoveries.": "这些常见问题解答代表了 Claude Code 社区的集体智慧。这里回答的问题来自解决实际问题并分享他们发现的真实开发者。",
        
        "*These FAQs are compiled from community discussions and real user experiences. For official documentation, visit the": "*这些常见问题解答根据社区讨论和真实用户体验编译而成。有关官方文档，请访问",
        "[Claude Code docs]": "[Claude Code 文档]",
        
        # Navigation links at bottom  
        "-   [Getting Started]": "-   [入门指南]",
        "-   [Pricing]": "-   [定价]",
        "-   [Installation & Setup]": "-   [安装与设置]",
        "-   [Configuration]": "-   [配置]",
        "-   [Core Features]": "-   [核心功能]",
        "-   [Plans & Pricing]": "-   [计划与定价]",
        "-   [Best Practices]": "-   [最佳实践]",
        "-   [Troubleshooting]": "-   [故障排除]",
        "-   [Advanced Usage]": "-   [高级用法]",
        "-   [Resources]": "-   [资源]",
        "-   [AI Tools Fundamentals]": "-   [AI 工具基础]",
        "-   [Vibe Coding]": "-   [氛围编程]",
        "-   [AI & Human-Computer Interface (HCI)]": "-   [AI 与人机界面 (HCI)]",
    }
    
    # Apply translations
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated FAQ page: {file_path}")

if __name__ == "__main__":
    translate_faq()