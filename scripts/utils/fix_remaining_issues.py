#!/usr/bin/env python3
"""
Fix remaining issues - 修复剩余问题 (无交互式输入)
"""

import re
import json
from pathlib import Path

def fix_internal_links():
    """修复内部链接格式"""
    print("🔗 修复内部链接格式...")
    docs_dir = Path("final-site/docs")
    
    md_files = [f for f in docs_dir.glob("*.md") if 'backup' not in f.name]
    total_fixed = 0
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 修复内部链接: /path/ -> /path.html
        def fix_link(match):
            link = match.group(1)
            if link == '/' or link.startswith('/img/') or link.startswith('http'):
                return match.group(0)  # 保持不变
            elif link.endswith('/'):
                return f']({link[:-1]}.html)'
            else:
                return match.group(0)  # 已经是正确格式
        
        content = re.sub(r'\]\((/[^)]+)\)', fix_link, content)
        
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # 计算修复的链接数量
            fixed_count = len(re.findall(r'/[^/)]+/', original_content)) - len(re.findall(r'/[^/)]+/', content))
            if fixed_count > 0:
                total_fixed += fixed_count
                print(f"  ✓ 修复 {fixed_count} 个链接: {md_file.name}")
    
    print(f"总计修复了 {total_fixed} 个内部链接")
    return total_fixed

def translate_titles():
    """翻译frontmatter中的英文标题"""
    print("🌐 翻译英文标题...")
    docs_dir = Path("final-site/docs")
    
    title_translations = {
        # MCP相关
        "Awesome Claude Code": "强大的 Claude Code",
        "Awesome Claude Prompts": "强大的 Claude 提示词",
        "Awesome MCP Servers": "强大的 MCP 服务器",
        "Blender MCP": "Blender MCP 插件",
        "Browser Tools MCP": "浏览器工具 MCP",
        "CC Usage": "CC 使用指南",
        "Claude Code Router": "Claude Code 路由器",
        "Claudia": "Claudia 助手",
        "Context7 MCP": "Context7 MCP 插件",
        "Desktop Commander MCP": "桌面指挥官 MCP",
        "GitHub MCP Server": "GitHub MCP 服务器",
        "Puppeteer MCP": "Puppeteer MCP 插件",
        "Reddit MCP": "Reddit MCP 插件",
        "Serena": "Serena 助手",
        "TDD Guard": "TDD 守护者",
        "TweakCC": "TweakCC 调优工具",
        "WhatsApp MCP": "WhatsApp MCP 插件",
        "Zen MCP Server": "Zen MCP 服务器",
        "MCPs & Add-ons": "MCP 插件与扩展",
        
        # Mechanics 机制相关
        "Agent Engineering": "智能体工程",
        "Agent-First Design": "智能体优先设计",
        "Always Be Experimenting": "持续实验原则",
        "Auto-Accept Permissions": "自动接受权限",
        "Auto Plan Mode": "自动规划模式",
        "Bash Scripts": "Bash 脚本",
        "Claude.md Supremacy": "Claude.md 至上原则",
        "Claude Usage": "Claude 使用技巧",
        "Context Inspection": "上下文检查",
        "Context Window Constraints as Training": "上下文窗口约束训练",
        "Context Window Depletion": "上下文窗口耗尽",
        "Custom Agents": "自定义智能体",
        "Dangerous Skip Permissions": "危险的跳过权限",
        "Dynamic Memory": "动态内存",
        "Git Clone is Just the Beginning": "Git Clone 只是开始",
        "Hooks": "钩子函数",
        "Humanising Agents": "智能体人性化",
        "Output Styles": "输出样式",
        "Permutation Frameworks": "排列组合框架",
        "Plan Mode": "规划模式",
        "Poison Context Awareness": "毒化上下文感知",
        "Rev the Engine": "启动引擎",
        "Sanity Check": "合理性检查",
        "Skeleton Projects": "骨架项目",
        "Split-Role Sub-Agents": "分角色子智能体",
        "Sub-Agent Tactics": "子智能体战术",
        "Sub-Agents": "子智能体",
        "Tactical Model Selection": "战术模型选择",
        "Task Agent Tools": "任务智能体工具",
        "Tight Feedback Loops": "紧密反馈循环",
        "Todo Lists as Instruction Mirrors": "待办清单作为指令镜像",
        "UltraThink++": "UltraThink++ 超级思考",
        "You Are the Main Thread": "你是主线程",
        
        # 其他页面
        "Claude Code Tutorial": "Claude Code 教程",
        "Claude Code Pricing": "Claude Code 价格",
        "Claude Code Changelog": "Claude Code 更新日志",
        "Install Claude Code": "安装 Claude Code",
        "Configuration": "配置",
        "FAQ": "常见问题",
        "Contact": "联系我们",
        "Support ClaudeLog": "支持 ClaudeLog",
        "Sponsor": "赞助",
        "Terms of Service": "服务条款",
        "Privacy Policy": "隐私政策",
        "Disclaimer": "免责声明",
        "Watch Control": "监控控制",
        "Claude News": "Claude 新闻"
    }
    
    md_files = [f for f in docs_dir.glob("*.md") if 'backup' not in f.name]
    translated_count = 0
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 提取frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # 查找title行
                title_match = re.search(r'title:\s*["\']?([^"\'\\n]+)["\']?', frontmatter)
                if title_match:
                    current_title = title_match.group(1).strip()
                    
                    # 查找对应的中文翻译
                    chinese_title = title_translations.get(current_title)
                    if chinese_title:
                        # 替换所有可能的title格式
                        patterns = [
                            (f'title: "{current_title}"', f'title: "{chinese_title}"'),
                            (f"title: '{current_title}'", f"title: '{chinese_title}'"),
                            (f"title: {current_title}", f'title: "{chinese_title}"')
                        ]
                        
                        new_frontmatter = frontmatter
                        for old_pattern, new_pattern in patterns:
                            if old_pattern in new_frontmatter:
                                new_frontmatter = new_frontmatter.replace(old_pattern, new_pattern)
                                break
                        
                        content = f"---{new_frontmatter}---{body}"
                        translated_count += 1
                        print(f"  ✓ 翻译标题 '{current_title}' -> '{chinese_title}': {md_file.name}")
        
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"总计翻译了 {translated_count} 个标题")
    return translated_count

def clean_backups_auto():
    """自动清理备份文件"""
    print("🗑️ 自动清理备份文件...")
    docs_dir = Path("final-site/docs")
    
    backup_files = list(docs_dir.glob("*.backup_*.md"))
    cleaned_count = 0
    
    if backup_files:
        print(f"发现 {len(backup_files)} 个备份文件，自动清理...")
        for backup_file in backup_files:
            try:
                backup_file.unlink()
                cleaned_count += 1
                print(f"  ✓ 删除备份: {backup_file.name}")
            except Exception as e:
                print(f"  ✗ 删除失败: {backup_file.name} - {e}")
        
        print(f"总计清理了 {cleaned_count} 个备份文件")
    else:
        print("  没有找到备份文件")
    
    return cleaned_count

def main():
    print("🔧 继续修复剩余问题...")
    print("=" * 60)
    
    # 修复链接
    links_fixed = fix_internal_links()
    
    print()
    # 翻译标题
    titles_translated = translate_titles()
    
    print()
    # 清理备份
    backups_cleaned = clean_backups_auto()
    
    print("\n" + "=" * 60)
    print("🎉 修复完成!")
    print("=" * 60)
    
    print(f"\n📊 本次修复统计:")
    print(f"  - 内部链接: {links_fixed} 个")
    print(f"  - 标题翻译: {titles_translated} 个") 
    print(f"  - 备份清理: {backups_cleaned} 个")
    
    total_fixes = links_fixed + titles_translated + backups_cleaned
    print(f"\n总计修复: {total_fixes} 个问题")
    
    print("\n✅ 建议接下来:")
    print("  1. 运行 'python3 comprehensive_issue_scanner.py' 验证修复结果")
    print("  2. 检查网站 http://localhost:8081 确认显示正常") 
    print("  3. 提交修复更改到Git")

if __name__ == "__main__":
    main()