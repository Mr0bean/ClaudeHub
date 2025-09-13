#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面的最终清理脚本 - 修复所有剩余的英文内容
"""

import re

def comprehensive_cleanup():
    # 读取文件
    with open('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs/faq.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 全面的修复映射
    fixes = {
        # 常见英文单词
        " for ": " 用于 ",
        " to ": " 到 ",
        " and ": " 和 ",
        " or ": " 或 ",
        " with ": " 与 ",
        " from ": " 从 ",
        " by ": " 通过 ",
        " in ": " 在 ",
        " on ": " 在 ",
        " at ": " 在 ",
        " of ": " 的 ",
        " that ": " 那 ",
        " this ": " 这 ",
        " the ": " ",
        " a ": " 一个 ",
        " an ": " 一个 ",
        " can ": " 可以 ",
        " are ": " 是 ",
        " use ": " 使用 ",
        " you ": " 您 ",
        " all ": " 所有 ",
        " will ": " 将 ",
        " may ": " 可能 ",
        " down to ": " 归结为 ",
        " comes down to ": " 归结为 ",

        # 常见短语
        "for complex operations": "用于复杂操作",
        "for planning": "用于规划",
        "for execution": "用于执行",
        "for detailed": "详细的",
        "with Max": "使用 Max",
        "with Pro": "使用 Pro",
        "with Claude": "使用 Claude",
        "to the": "到",
        "in the": "在",
        "at the": "在",
        "from the": "从",
        "on the": "在",
        "of the": "的",
        "that the": "那",
        "can use": "可以使用",
        "are available": "可用",
        "you can": "您可以",
        "all the": "所有",
        "will be": "将被",
        "may be": "可能",
        "should use": "应该使用",
        "can help": "可以帮助",
        "allows you to": "允许您",
        "enables you to": "使您能够",
        "helps you": "帮助您",

        # 技术词汇
        "toextend": "来延长",
        "torun": "来运行",
        "tosummarize": "来总结",
        "tomanage": "来管理",
        "toconfigure": "来配置",
        "tohandle": "来处理",
        "tocheck": "来检查",
        "toavoid": "来避免",
        "tospawn": "来生成",
        "towrite": "来编写",
        "toanalyze": "来分析",

        # 连词和介词清理
        "withtheir": "拥有自己的",
        "withexact": "具有确切的",
        "withdifferent": "具有不同的",
        "withproper": "通过适当的",
        "formultiple": "用于多个",
        "forcomplex": "用于复杂的",
        "forsafe": "用于安全的",
        "forefficiency": "为了效率",
        "indifferent": "在不同的",
        "inClaude": "在 Claude",
        "involuntary": "非自愿的",

        # 时间和频率
        "per月": "每月",
        "per周": "每周",
        "per 5 小时": "每 5 小时",
        "per百万": "每百万",
        "per...重置": "每隔...重置",

        # 技术术语
        "thatrun": "运行的",
        "thathandle": "处理的",
        "thatdisplay": "显示的",
        "thatcontain": "包含的",
        "thattrack": "跟踪的",
        "thatmonitor": "监控的",
        "thatadd": "添加的",
        "thathelp": "帮助的",
        "thatturns": "变成",
        "thatlook": "看起来",
        "thatwork": "工作的",
        "thatsupport": "支持的",

        # 修复特定问题
        "Claude Code for什么": "Claude Code 用于什么",
        "This helps you work longer without needingtorun": "这帮助您在不需要运行的情况下工作更长时间",
        "foreach": "每个",
        "withoutneedingtorun": "而不需要运行",
        "These are temporary server-side issuesthatusually resolvein2-5 minutes": "这些是临时的服务器端问题，通常在 2-5 分钟内自动解决",
        "issuesthatusually": "问题通常",
        "resolvein2-5": "在 2-5 分钟内解决",
        "basedin当前": "基于当前",
        "I observethatsophisticated": "我观察到复杂的",
        "I findthatiterative": "我发现迭代的",
        "I观察to": "我观察到",
        "通过whetherresult": "通过结果是否",
        "通过code": "通过代码",
        "builthatwork": "但工作",
        "tofix": "来修复",
        "withproper": "通过适当的",

        # 更多混合词修复
        "ooperations": "操作",
        "ooperation": "操作",
        "orspecific": "或特定的",
        "orask": "或询问",
        "orcontinue": "或继续",
        "orexperiencing": "或遇到",
        "anwrite": "并编写",
        "andcost": "和成本",
        "andcode": "和代码",
        "showninClaude": "在 Claude 中显示",
        "accesstoClaude": "访问 Claude",
        "comparedtoClaude": "与 Claude 相比",
        "usingClaude": "使用 Claude",
        "aboutyour": "关于您的",
        "inyour": "在您的",
        "directlytoconfigure": "直接配置",
        "automatically处理": "自动处理",
        "settings和enabling": "设置并启用",
        "information,和custom": "信息和自定义",
        "setting和enabling": "设置并启用",
        "时间、会话持续时间, git": "时间、会话持续时间、git",

        # 修复链接和标题
        "Direct link to入门指南": "直接链接到入门指南",
        "Direct link to定价": "直接链接到定价",
        "Direct link toConfiguration": "直接链接到配置",
        "Direct link toCore Features": "直接链接到核心功能",
        "Direct link toPlans & Pricing": "直接链接到计划和定价",
        "Direct link toBest Practices": "直接链接到最佳实践",
        "Direct link toTroubleshooting": "直接链接到故障排除",

        # 特殊修复
        "withClaudeMax": "使用 Claude Max",
        "andGit": "和 Git",
        "andconfigure": "并配置",
        "forlinux": "用于 Linux",
        "toolfortracking": "跟踪工具",
        "usefulthat": "有用的",

        # 保持一些必要的英文内容
        "Claude Code": "Claude Code",
        "Claude": "Claude",
        "API": "API",
        "MCP": "MCP",
        "WSL": "WSL",
        "Linux": "Linux",
        "Windows": "Windows",
        "macOS": "macOS",
        "GitHub": "GitHub",
        "VS Code": "VS Code",
        "npm": "npm",
        "Node.js": "Node.js",
        "Git": "Git",
        "SSH": "SSH",
        "CI/CD": "CI/CD",
        "JSON": "JSON",
        "HTML": "HTML",
        "CSS": "CSS",
        "JavaScript": "JavaScript",
        "TypeScript": "TypeScript",
        "Python": "Python",
        "Java": "Java",
        "C++": "C++",
        "Chrome": "Chrome",
        "Sonnet": "Sonnet",
        "Opus": "Opus",
        "Haiku": "Haiku",
        "Pro": "Pro",
        "Max": "Max",
        "WSL2": "WSL2",
        "Anthropic": "Anthropic",
        "SuperClaude": "SuperClaude",
        "UltraThink": "UltraThink",
        "VPS": "VPS",
        "UI": "UI",
    }

    # 应用修复
    for wrong, correct in fixes.items():
        content = content.replace(wrong, correct)

    # 更多针对性的正则表达式修复
    # 修复连在一起的单词
    content = re.sub(r'([a-z])([A-Z])', r'\1 \2', content)

    # 修复 forXX 模式
    content = re.sub(r'\bfor([A-Z][a-z]+)', r'用于\1', content)

    # 修复 toXX 模式
    content = re.sub(r'\bto([A-Z][a-z]+)', r'到\1', content)

    # 修复 withXX 模式
    content = re.sub(r'\bwith([A-Z][a-z]+)', r'使用\1', content)

    # 修复 andXX 模式
    content = re.sub(r'\band([A-Z][a-z]+)', r'和\1', content)

    # 修复多余的空格
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r' ,', ',', content)
    content = re.sub(r' \.', '.', content)
    content = re.sub(r' ;', ';', content)
    content = re.sub(r' :', ':', content)

    # 保存修复后的文件
    with open('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs/faq.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("FAQ文档全面清理完成!")

if __name__ == "__main__":
    comprehensive_cleanup()