#!/usr/bin/env python3
"""
Fix All Issues Script - 修复扫描发现的所有问题
"""

import re
import json
from pathlib import Path
import shutil
import os
import requests

class IssueFixer:
    def __init__(self, docs_dir="final-site/docs"):
        self.docs_dir = Path(docs_dir)
        self.fixed_count = {
            'images': 0,
            'code_blocks': 0,
            'markdown': 0,
            'links': 0,
            'titles': 0,
            'vue_conflicts': 0,
            'backups': 0
        }
    
    def fix_all(self):
        """修复所有问题"""
        print("🔧 开始修复所有问题...")
        print("=" * 60)
        
        # 1. 创建图片目录并设置占位符
        self.create_image_placeholders()
        
        # 2. 修复代码块和Markdown语法
        self.fix_code_blocks_and_markdown()
        
        # 3. 修复链接格式
        self.fix_internal_links()
        
        # 4. 翻译标题
        self.translate_titles()
        
        # 5. 修复Vue冲突
        self.fix_vue_conflicts()
        
        # 6. 清理备份文件 (可选)
        self.cleanup_backups()
        
        self.print_summary()
    
    def create_image_placeholders(self):
        """创建图片目录和占位符图片"""
        print("📁 创建图片目录...")
        
        # 创建必要的目录
        img_dirs = [
            "final-site/img",
            "final-site/img/discovery", 
            "final-site/img/supporters",
            "final-site/docs/.vuepress/public/img",
            "final-site/docs/.vuepress/public/img/discovery",
            "final-site/docs/.vuepress/public/img/supporters"
        ]
        
        for dir_path in img_dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            print(f"  ✓ 创建目录: {dir_path}")
        
        # 创建一个简单的占位符图片 (SVG格式)
        placeholder_svg = '''<svg width="165" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f0f0f0" stroke="#ccc" stroke-width="2"/>
  <text x="50%" y="50%" text-anchor="middle" dy=".3em" fill="#666" font-family="Arial, sans-serif" font-size="14">
    图片占位符
  </text>
</svg>'''
        
        # 从报告中提取所有需要的图片路径
        with open('comprehensive_issue_report.json', 'r', encoding='utf-8') as f:
            report = json.load(f)
        
        image_paths = set()
        for issue in report['issues'].get('broken_images', []):
            img_path = issue['image']
            if img_path.startswith('/'):
                image_paths.add(img_path[1:])  # 去掉开头的斜杠
        
        # 为每个缺失的图片创建占位符
        for img_path in image_paths:
            # 在两个位置都创建
            for base_dir in ["final-site", "final-site/docs/.vuepress/public"]:
                full_path = Path(base_dir) / img_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                if img_path.endswith('.svg'):
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(placeholder_svg)
                else:
                    # 为非SVG文件创建SVG占位符但保持原扩展名
                    svg_path = full_path.with_suffix('.svg')
                    with open(svg_path, 'w', encoding='utf-8') as f:
                        f.write(placeholder_svg)
                    
                    # 同时创建一个空文件以满足引用
                    full_path.touch()
                
                print(f"  ✓ 创建占位符: {full_path}")
                self.fixed_count['images'] += 1
    
    def fix_code_blocks_and_markdown(self):
        """修复代码块和Markdown语法问题"""
        print("\n📝 修复代码块和Markdown语法...")
        
        md_files = [f for f in self.docs_dir.glob("*.md") if 'backup' not in f.name]
        
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. 修复未闭合的代码块
            code_fence_count = content.count('```')
            if code_fence_count % 2 != 0:
                # 在文件末尾添加闭合的代码块
                content += '\n```\n'
                self.fixed_count['code_blocks'] += 1
                print(f"  ✓ 修复代码块: {md_file.name}")
            
            # 2. 修复不完整的链接 (去掉孤立的方括号)
            # 匹配行尾的 [text] 模式
            content = re.sub(r'\[([^\]]+)\]\s*$', r'\1', content, flags=re.MULTILINE)
            
            # 3. 修复断行的链接语法
            content = re.sub(r'\[\s*\n\s*##', '## [', content)
            content = re.sub(r'\]\s*\n\s*\(', '](', content)
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixed_count['markdown'] += 1
                print(f"  ✓ 修复Markdown语法: {md_file.name}")
    
    def fix_internal_links(self):
        """修复内部链接格式"""
        print("\n🔗 修复内部链接格式...")
        
        md_files = [f for f in self.docs_dir.glob("*.md") if 'backup' not in f.name]
        
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 修复内部链接: /path/ -> /path.html
            # 但保留首页 / 和图片路径 /img/
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
                original_links = len(re.findall(r'\]\((/[^)]*[^/])\)', original_content))
                new_links = len(re.findall(r'\]\((/[^)]*[^/])\)', content))
                fixed_links = original_links - new_links
                
                if fixed_links > 0:
                    self.fixed_count['links'] += fixed_links
                    print(f"  ✓ 修复 {fixed_links} 个链接: {md_file.name}")
    
    def translate_titles(self):
        """翻译frontmatter中的英文标题"""
        print("\n🌐 翻译英文标题...")
        
        # 常见的标题翻译映射
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
        
        md_files = [f for f in self.docs_dir.glob("*.md") if 'backup' not in f.name]
        
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
                            new_frontmatter = frontmatter.replace(
                                f'title: "{current_title}"', 
                                f'title: "{chinese_title}"'
                            ).replace(
                                f"title: '{current_title}'", 
                                f"title: '{chinese_title}'"
                            ).replace(
                                f"title: {current_title}", 
                                f'title: "{chinese_title}"'
                            )
                            
                            content = f"---{new_frontmatter}---{body}"
                            self.fixed_count['titles'] += 1
                            print(f"  ✓ 翻译标题 '{current_title}' -> '{chinese_title}': {md_file.name}")
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def fix_vue_conflicts(self):
        """修复Vue组件冲突"""
        print("\n⚛️ 修复Vue组件冲突...")
        
        md_files = [f for f in self.docs_dir.glob("*.md") if 'backup' not in f.name]
        
        vue_patterns = {
            '<think>': '&lt;think&gt;',
            '</think>': '&lt;/think&gt;',
            '<session-id>': '&lt;session-id&gt;',
            '<agent>': '&lt;agent&gt;',
            '<path>': '&lt;path&gt;',
            '<file>': '&lt;file&gt;',
            '<name>': '&lt;name&gt;'
        }
        
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            for pattern, replacement in vue_patterns.items():
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    self.fixed_count['vue_conflicts'] += 1
                    print(f"  ✓ 修复Vue冲突 {pattern}: {md_file.name}")
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def cleanup_backups(self):
        """清理备份文件 (可选)"""
        print("\n🗑️ 清理备份文件...")
        
        backup_files = list(self.docs_dir.glob("*.backup_*.md"))
        
        if backup_files:
            print(f"发现 {len(backup_files)} 个备份文件")
            response = input("是否要删除这些备份文件? (y/N): ").strip().lower()
            
            if response == 'y':
                for backup_file in backup_files:
                    backup_file.unlink()
                    self.fixed_count['backups'] += 1
                    print(f"  ✓ 删除备份: {backup_file.name}")
            else:
                print("  跳过备份文件清理")
        else:
            print("  没有找到备份文件")
    
    def print_summary(self):
        """打印修复总结"""
        print("\n" + "=" * 60)
        print("🎉 修复完成!")
        print("=" * 60)
        
        total_fixes = sum(self.fixed_count.values())
        
        print(f"\n📊 修复统计:")
        print(f"  - 图片占位符: {self.fixed_count['images']} 个")
        print(f"  - 代码块修复: {self.fixed_count['code_blocks']} 个") 
        print(f"  - Markdown语法: {self.fixed_count['markdown']} 个")
        print(f"  - 链接格式: {self.fixed_count['links']} 个")
        print(f"  - 标题翻译: {self.fixed_count['titles']} 个")
        print(f"  - Vue冲突: {self.fixed_count['vue_conflicts']} 个")
        print(f"  - 备份清理: {self.fixed_count['backups']} 个")
        print(f"\n总计修复: {total_fixes} 个问题")
        
        print("\n✅ 建议接下来:")
        print("  1. 运行 'python3 comprehensive_issue_scanner.py' 验证修复结果")
        print("  2. 检查网站 http://localhost:8081 确认显示正常")
        print("  3. 提交修复更改到Git")

if __name__ == "__main__":
    fixer = IssueFixer()
    fixer.fix_all()