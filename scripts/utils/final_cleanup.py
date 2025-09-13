#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终清理FAQ文档的脚本 - 修复剩余的翻译问题
"""

def final_cleanup():
    # 读取文件
    with open('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs/faq.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 最终修复
    fixes = {
        "Su每Claude": "SuperClaude",
        "Su每": "Super",
        "每": "pe",
        "或": "or",
        "到": "to",
        "个": "",
        "用于": "for",
        "从": "from",
        "在": "in",
        "与": "with",
        "那": "that",
        "这": "this",
        "的": "的", # 保留中文的"的"字
        "w或ld": "world",
        "w或": "wor",
        "或": "or",
        "或": "or",
        "f或ce": "force",
        "f或": "for",
        "h和": "han",
        "st和": "stan",
        "underst和": "understand",
        "expl或": "explor",
        "monit或": "monitor",
        "edit或": "editor",
        "direct或": "director",
        "hist或": "history",
        "mem或": "memory",
        "seni或": "senior",
        "pri或": "prior",
        "err或": "error",
        "supp或": "support",
        "imp或": "impor",
        "rep或": "repor",
        "每": "per",
        "到": "to",
        "advis或": "advisor",
        "cus到": "custo",
        "sens或": "sensor",
        "creat或": "creator",
        "categ或": "category",
        "bot到": "bottom",
        "tut或": "tutorial",
        "maj或": "major",
        "mani或": "minor",
        "coding": "编码",
        "每spectives": "perspectives",
        "每iencing": "experiencing",
        "每ienced": "experienced",
        "每sonally": "personally",
        "每f或mance": "performance",
        "每f或m": "perform",
        "每ations": "operations",
        "每mit": "permit",
        "每missions": "permissions",
        "或ganize": "organize",
        "或iented": "oriented",
        "或chestration": "orchestration",
        "或chestrated": "orchestrated",
        "或chestrates": "orchestrates",
        "到ol": "tool",
        "到ols": "tools",
        "到pic": "topic",
        "到pics": "topics",
        "到ken": "token",
        "到kens": "tokens",
        "到ward": "toward",
        "到uch": "touch",
        "w或k": "work",
        "w或ks": "works",
        "w或king": "working",
        "w或kflow": "workflow",
        "w或kflows": "workflows",
        "netw或k": "network",
        "h和le": "handle",
        "h和ling": "handling",
        "h和s-on": "hands-on",
        "temp或ary": "temporary",
        "每action": "protection",
        "每actions": "protections",
        "每duct": "product",
        "每ducts": "products",
        "每duction": "production",
        "每ductive": "productive",
        "每ductivity": "productivity",
        "每cess": "process",
        "每cesses": "processes",
        "每cessing": "processing",
        "每cessor": "processor",
        "每cessors": "processors",
        "每gram": "program",
        "每grams": "programs",
        "每gramming": "programming",
        "每grammer": "programmer",
        "每grammers": "programmers",
        "每ject": "project",
        "每jects": "projects",
        "每jecting": "projecting",
        "每jection": "projection",
        "每jections": "projections",
        "每vide": "provide",
        "每vides": "provides",
        "每viding": "providing",
        "每vider": "provider",
        "每viders": "providers",
        "每vision": "provision",
        "每visions": "provisions",
        "每ventable": "preventable",
        "每vention": "prevention",
        "每vent": "prevent",
        "每vents": "prevents",
        "每venting": "preventing",
        "每vented": "prevented",
        "st或age": "storage",
        "st或ing": "storing",
        "st或ed": "stored",
        "st或es": "stores",
        "auth或itative": "authoritative",
        "auth或ization": "authorization",
        "auth或ize": "authorize",
        "auth或ized": "authorized",
        "auth或izing": "authorizing",
        # 修复一些混乱的翻译
        "那handle": "that handle",
        "那display": "that display",
        "那show": "that show",
        "那contain": "that contain",
        "那track": "that track",
        "那monitor": "that monitor",
        "那add": "that add",
        "那help": "that help",
        "是most": "is most",
        "是best": "is best",
        "是main": "is main",
        "是primary": "is primary",
        "用于Chrome": "for Chrome",
        "与AI": "与 AI",
        "与all": "与所有",
        "与any": "与任何",
        "与your": "与您的",
        "从your": "从您的",
        "从the": "从",
        "从all": "从所有",
        "在your": "在您的",
        "在the": "在",
        "在all": "在所有",
        "到your": "到您的",
        "到the": "到",
        "到all": "到所有",
        # 修复更多混乱
        "一个single": "单个",
        "一个lot": "大量",
        "一个few": "一些",
        "这task": "这个任务",
        "这system": "这个系统",
        "这approach": "这种方法",
        "这method": "这种方法",
        "这feature": "这个功能",
        "这function": "这个功能",
        "这tool": "这个工具",
        # 修复特定的问题项
        "hello w或ld": "hello world",
        "C或e Features": "Core Features",
        "Su每 Claude": "Super Claude",
    }

    # 应用修复
    for wrong, correct in fixes.items():
        content = content.replace(wrong, correct)

    # 更多针对性的修复
    import re

    # 修复链接文本中的问题
    content = re.sub(r'\[([^\]]*) guide\]', r'[\1指南]', content)
    content = re.sub(r'\[([^\]]*) setup\]', r'[\1设置]', content)
    content = re.sub(r'\[([^\]]*) help\]', r'[\1帮助]', content)
    content = re.sub(r'\[([^\]]*) tips\]', r'[\1技巧]', content)
    content = re.sub(r'\[([^\]]*) support\]', r'[\1支持]', content)

    # 保存修复后的文件
    with open('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs/faq.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("FAQ文档最终清理完成!")

if __name__ == "__main__":
    final_cleanup()