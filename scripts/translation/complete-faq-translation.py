#!/usr/bin/env python3
import re

def complete_faq_translation():
    file_path = 'final-site/docs/faq.md'
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Complete remaining translations
    translations = {
        # Plans & Pricing section
        '**Q: How much does Claude Code cost?**': '**问：Claude Code 多少钱？**',
        'A: Claude Pro costs $20/month': '答：Claude Pro 每月 20 美元',
        
        "**Q: What's the difference between Claude Pro and Claude Max for developers?**": "**问：对于开发者来说，Claude Pro 和 Claude Max 有什么区别？**",
        'A: Claude Pro ($20/month) includes Sonnet 4 with limited usage': '答：Claude Pro（每月 20 美元）包括有限使用的 Sonnet 4',
        
        '**Q: Can I use Claude Code with the Pro subscription?**': '**问：我可以使用 Pro 订阅使用 Claude Code 吗？**',
        "A: Yes, Claude Code works with Claude Pro, but you're limited": "答：是的，Claude Code 可以与 Claude Pro 一起使用，但您仅限于",
        
        "**Q: What's the difference between Claude Max 5X and regular Pro for Claude Code?**": "**问：Claude Max 5X 与常规 Pro 对于 Claude Code 有什么区别？**",
        'A: Claude Max 5X provides 5x higher usage limits': '答：Claude Max 5X 提供 5 倍更高的使用限制',
        
        '**Q: What are the real-world Claude Code Max usage limits?**': '**问：实际的 Claude Code Max 使用限制是什么？**',
        'A: Claude Max 5x supports all-day Sonnet coding': '答：Claude Max 5x 支持全天 Sonnet 编码',
        
        "**Q: What's the difference between Claude API and subscription for Claude Code?**": "**问：Claude API 和订阅对于 Claude Code 有什么区别？**",
        'A: API offers pay-per-use pricing': '答：API 提供按使用付费定价',
        
        '**Q: Can I use both API keys and subscription plans with Claude Code?**': '**问：我可以同时使用 API 密钥和订阅计划与 Claude Code 吗？**',
        'A: Yes, Claude Code supports both Anthropic API keys': '答：是的，Claude Code 支持 Anthropic API 密钥',
        
        '**Q: How do I check my Claude Code usage to avoid unexpected API costs?**': '**问：如何检查我的 Claude Code 使用情况以避免意外的 API 成本？**',
        'A: API users can check usage': '答：API 用户可以检查使用情况',
        
        '**Q: What is CC Usage for Claude Code?**': '**问：什么是 Claude Code 的 CC Usage？**',
        'A: CC Usage is a command-line tool': '答：CC Usage 是一个命令行工具',
        
        '**Q: What are the real Claude Code usage limits by plan?**': '**问：按计划的实际 Claude Code 使用限制是什么？**',
        'A: Pro tier: 10-40 prompts every 5 hours': '答：Pro 层级：每 5 小时 10-40 个提示',
        
        '**Q: How often do Claude Code limits reset?**': '**问：Claude Code 限制多久重置一次？**',
        'A: Limits reset every 5 hours': '答：限制每 5 小时重置',
        
        '**Q: What happens when I hit Claude Code limits?**': '**问：当我达到 Claude Code 限制时会发生什么？**',
        'A: New prompts are rejected until reset': '答：新提示将被拒绝，直到重置',
        
        # Best Practices section
        '**Q: What are Claude Code best practices?**': '**问：Claude Code 最佳实践是什么？**',
        'A: Essential Claude Code best practices include': '答：基本的 Claude Code 最佳实践包括',
        
        '**Q: What are Role Sub-Agents in Claude Code?**': '**问：Claude Code 中的角色子代理是什么？**',
        'A: Role Sub-Agents use multiple sub-agents': '答：角色子代理使用多个子代理',
        
        '**Q: How do I write better prompts for Claude Code?**': '**问：如何为 Claude Code 编写更好的提示？**',
        'A: Be specific about what you want': '答：明确说明您想要什么',
        
        '**Q: Should you use many small files or few large files with Claude Code?**': '**问：使用 Claude Code 时应该使用许多小文件还是少数大文件？**',
        'A: Use many small files organized by logical boundaries': '答：使用按逻辑边界组织的许多小文件',
        
        '**Q: How do I optimize Claude Code token usage?**': '**问：如何优化 Claude Code 令牌使用？**',
        'A: Use lean file structures': '答：使用精简的文件结构',
        
        '**Q: How do I speed up Claude Code performance?**': '**问：如何加快 Claude Code 性能？**',
        'A: Use Claude 4 Sonnet for balanced speed': '答：使用 Claude 4 Sonnet 以获得平衡的速度',
        
        '**Q: Does Claude Code store my data?**': '**问：Claude Code 是否存储我的数据？**',
        'A: Claude Code sends your code': '答：Claude Code 将您的代码发送',
        
        # Troubleshooting section
        '**Q: Why is Claude Code not working?**': '**问：为什么 Claude Code 不工作？**',
        'A: Common issues include authentication problems': '答：常见问题包括身份验证问题',
        
        '**Q: Is Claude down right now?**': '**问：Claude 现在宕机了吗？**',
        'A: Check the official status page': '答：检查官方状态页面',
        
        '**Q: How do I fix Claude Code not responding?**': '**问：如何修复 Claude Code 无响应？**',
        'A: First restart Claude Code': '答：首先重启 Claude Code',
        
        '**Q: How do I fix Claude Code installation errors?**': '**问：如何修复 Claude Code 安装错误？**',
        'A: Common solutions: verify Node.js': '答：常见解决方案：验证 Node.js',
        
        '**Q: Why is Claude Code showing 503 error? Is my Claude Code broken?**': '**问：为什么 Claude Code 显示 503 错误？我的 Claude Code 坏了吗？**',
        'A: No, a 503 error indicates server issues': '答：不，503 错误表示服务器问题',
        
        '**Q: Is Claude Code down for everyone right now? How do I check if Claude Code is just me?**': '**问：Claude Code 现在对所有人都宕机了吗？如何检查是否只是我的问题？**',
        'A: Check the official status page at status.anthropic.com': '答：在 status.anthropic.com 检查官方状态页面',
        
        '**Q: Why am I getting Claude Code API errors? Is there a Claude Code API outage?**': '**问：为什么我收到 Claude Code API 错误？Claude Code API 有故障吗？**',
        'A: Claude Code API errors are usually temporary': '答：Claude Code API 错误通常是暂时的',
        
        '**Q: What does "Claude Code internal server error" mean? How do I fix it?**': '**问："Claude Code 内部服务器错误"是什么意思？如何修复？**',
        'A: Claude Code internal server errors are temporary': '答：Claude Code 内部服务器错误是暂时的',
        
        '**Q: What does "Claude Code overloaded" mean?**': '**问："Claude Code 过载"是什么意思？**',
        'A: Claude Code "overloaded" errors indicate Anthropic\'s servers': '答：Claude Code "过载"错误表示 Anthropic 的服务器',
        
        '**Q: What is Todo List in Claude Code?**': '**问：Claude Code 中的待办事项列表是什么？**',
        'A: Claude Code includes a built-in todo list system': '答：Claude Code 包含一个内置的待办事项列表系统',
        
        '**Q: Why is Claude Code running slowly?**': '**问：为什么 Claude Code 运行缓慢？**',
        'A: Performance varies based on server demand': '答：性能因服务器需求而异',
        
        '**Q: How do I optimize Claude Code performance?**': '**问：如何优化 Claude Code 性能？**',
        'A: Use Sonnet for balanced performance': '答：使用 Sonnet 以获得平衡的性能',
        
        '**Q: How do I manage Claude Code context window efficiently?**': '**问：如何有效管理 Claude Code 上下文窗口？**',
        'A: Use `/compact` to summarize conversation history': '答：使用 `/compact` 来总结对话历史',
        
        # Advanced Usage section
        '**Q: How do I automate workflows with Claude Code hooks?**': '**问：如何使用 Claude Code 钩子自动化工作流程？**',
        'A: Use hooks to execute shell commands automatically': '答：使用钩子自动执行 shell 命令',
        
        '**Q: How do I use Claude Code for debugging?**': '**问：如何使用 Claude Code 进行调试？**',
        'A: Claude Code excels at error analysis': '答：Claude Code 擅长错误分析',
        
        '**Q: How do I use Claude Code for code review?**': '**问：如何使用 Claude Code 进行代码审查？**',
        'A: Claude Code provides comprehensive code reviews': '答：Claude Code 提供全面的代码审查',
        
        '**Q: What programming languages work best with Claude Code?**': '**问：哪些编程语言最适合与 Claude Code 一起使用？**',
        'A: JavaScript/TypeScript, Python, and Java have excellent support': '答：JavaScript/TypeScript、Python 和 Java 具有出色的支持',
        
        '**Q: How do I suspend and resume Claude Code?**': '**问：如何暂停和恢复 Claude Code？**',
        'A: Press `Ctrl+Z` to suspend Claude Code': '答：按 `Ctrl+Z` 暂停 Claude Code',
        
        # Resources section
        '**Q: Where can I find additional tools, extensions, and community projects for Claude Code?**': '**问：在哪里可以找到 Claude Code 的其他工具、扩展和社区项目？**',
        'A: Check out [Awesome Claude Code]': '答：查看 [Awesome Claude Code]',
        
        '**Q: Where can I ask questions about Claude Code?**': '**问：在哪里可以询问有关 Claude Code 的问题？**',
        'A: The [r/ClaudeAI]': '答：[r/ClaudeAI]',
        
        '**Q: Is there a Claude Code community forum or discussion board?**': '**问：有 Claude Code 社区论坛或讨论板吗？**',
        "A: While there's no official forum": '答：虽然没有官方论坛',
        
        '**Q: Where can I find MCP servers to extend Claude Code functionality?**': '**问：在哪里可以找到 MCP 服务器来扩展 Claude Code 功能？**',
        'A: [Awesome MCP Servers]': '答：[Awesome MCP Servers]',
        
        # Claude AI section
        '**Q: What is Claude AI?**': '**问：什么是 Claude AI？**',
        "A: Claude AI is Anthropic's conversational AI assistant": "答：Claude AI 是 Anthropic 的对话式 AI 助手",
        
        '**Q: Is Claude AI free?**': '**问：Claude AI 免费吗？**',
        'A: Claude AI offers a free tier': '答：Claude AI 提供免费层级',
        
        '**Q: How much does Claude AI cost?**': '**问：Claude AI 多少钱？**',
        'A: Claude AI costs $20/month for Pro': '答：Claude AI Pro 每月 20 美元',
        
        '**Q: Is Claude AI safe?**': '**问：Claude AI 安全吗？**',
        'A: Claude AI is designed with safety': '答：Claude AI 的设计以安全为核心',
        
        '**Q: How to use Claude AI?**': '**问：如何使用 Claude AI？**',
        'A: Start at claude.ai with email signup': '答：在 claude.ai 使用电子邮件注册开始',
        
        # AI Tools Fundamentals section
        '**Q: What is an AI tool?**': '**问：什么是 AI 工具？**',
        'A: AI tools are software that uses artificial intelligence': '答：AI 工具是使用人工智能的软件',
        
        '**Q: How do I use AI tools effectively?**': '**问：如何有效使用 AI 工具？**',
        'A: Getting great results from AI tools': '答：从 AI 工具获得出色的结果',
        
        '**Q: How do I use AI tools responsibly?**': '**问：如何负责任地使用 AI 工具？**',
        'A: Claude Code exemplifies responsible AI design': '答：Claude Code 体现了负责任的 AI 设计',
        
        '**Q: What AI tools are available?**': '**问：有哪些 AI 工具可用？**',
        'A: AI tools in 2025 have matured': '答：2025 年的 AI 工具已经成熟',
        
        '**Q: What AI tools should I be using?**': '**问：我应该使用哪些 AI 工具？**',
        'A: Choose AI tools strategically': '答：战略性地选择 AI 工具',
        
        '**Q: Why should I learn AI tools?**': '**问：为什么我应该学习 AI 工具？**',
        'A: I observe AI tools creating': '答：我观察到 AI 工具创造',
        
        '**Q: Where to learn AI tools?**': '**问：在哪里学习 AI 工具？**',
        'A: For technical professionals': '答：对于技术专业人员',
        
        '**Q: How to use AI tools in daily life?**': '**问：如何在日常生活中使用 AI 工具？**',
        'A: I observe that AI tools transform': '答：我观察到 AI 工具改变',
        
        '**Q: AI tools learning resources: free vs paid courses?**': '**问：AI 工具学习资源：免费还是付费课程？**',
        'A: I find that free resources': '答：我发现免费资源',
        
        '**Q: What is an AI agent?**': '**问：什么是 AI 代理？**',
        'A: AI agents are autonomous AI systems': '答：AI 代理是自主的 AI 系统',
        
        '**Q: What is the role of an orchestrator agent?**': '**问：编排代理的作用是什么？**',
        'A: Orchestrator agents coordinate': '答：编排代理协调',
        
        # Vibe Coding section
        '**Q: What is vibe coding?**': '**问：什么是氛围编程？**',
        'A: Vibe coding is a development tactic': '答：氛围编程是一种开发策略',
        
        '**Q: How is vibe coding different from traditional coding?**': '**问：氛围编程与传统编程有何不同？**',
        'A: Vibe coding prioritizes outcomes': '答：氛围编程优先考虑结果',
        
        '**Q: What are common vibe coding issues?**': '**问：常见的氛围编程问题是什么？**',
        'A: Common vibe coding problems include': '答：常见的氛围编程问题包括',
        
        '**Q: What are vibe coding security vulnerabilities?**': '**问：氛围编程的安全漏洞是什么？**',
        'A: Vibe coding can create security problems': '答：氛围编程可能造成安全问题',
        
        # AI & HCI section
        '**Q: How does AI integrate with physical user interfaces like smartwatches?**': '**问：AI 如何与智能手表等物理用户界面集成？**',
        'A: AI integrates into wearables primarily': '答：AI 主要通过以下方式集成到可穿戴设备',
        
        '**Q: What are the current challenges in accessing AI on wearable devices?**': '**问：在可穿戴设备上访问 AI 的当前挑战是什么？**',
        'A: A primary challenge is that hardware design': '答：主要挑战是硬件设计',
        
        '**Q: How do different HCI methods (e.g., Touch Bezel, buttons) affect AI interaction?**': '**问：不同的 HCI 方法（如触摸表圈、按钮）如何影响 AI 交互？**',
        'A: Each HCI method serves a different purpose': '答：每种 HCI 方法都有不同的用途',
        
        '**Q: How could we monitor complex AI tasks, like those using sub-agents, from a watch?**': '**问：我们如何从手表监控使用子代理的复杂 AI 任务？**',
        'A: Monitoring advanced AI on a small screen': '答：在小屏幕上监控高级 AI',
        
        '**Q: What is the role of haptic feedback in AI-powered interfaces?**': '**问：触觉反馈在 AI 驱动界面中的作用是什么？**',
        'A: Haptic feedback is crucial': '答：触觉反馈至关重要',
        
        '**Q: How does the concept of "context awareness" in AI apply to wearables?**': '**问：AI 中的"上下文感知"概念如何应用于可穿戴设备？**',
        'A: Context awareness is the ability': '答：上下文感知是能力',
        
        '**Q: How will wearable interfaces need to evolve for an AI-first future?**': '**问：可穿戴界面需要如何发展才能适应 AI 优先的未来？**',
        'A: The current app-centric and tile-based model': '答：当前以应用程序为中心和基于磁贴的模型',
        
        '**Q: How could an AI like Claude influence future wearable interfaces?**': '**问：像 Claude 这样的 AI 如何影响未来的可穿戴界面？**',
        'A: While current assistants like Gemini': '答：虽然当前的助手如 Gemini',
        
        '**Q: How could AI make battery warnings smarter and more useful?**': '**问：AI 如何使电池警告更智能、更有用？**',
        'A: Traditional battery warnings are reactive': '答：传统的电池警告是被动的',
        
        '**Q: What are the most powerful devices that can handle AI on WearOS?**': '**问：哪些最强大的设备可以在 WearOS 上处理 AI？**',
        "A: Any of Samsung's modern": "答：三星的任何现代",
        
        # Fix HCI section translation
        'This section explores the fascinating intersection': '本节探讨了迷人的交叉点',
        'Drawing from insights on my': '借鉴我的见解',
        'these FAQs use modern smartwatches': '这些常见问题解答使用现代智能手表',
    }
    
    # Apply translations
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Completed FAQ translation: {file_path}")

if __name__ == "__main__":
    complete_faq_translation()