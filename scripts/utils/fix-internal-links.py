#!/usr/bin/env python3
import os
import re
import glob

def get_all_md_files(docs_dir):
    """获取所有 markdown 文件"""
    return glob.glob(os.path.join(docs_dir, "*.md"))

def fix_common_links(content):
    """修复常见的链接错误"""
    fixes = [
        # 修复 faqs 目录链接 - 大部分不存在，转换为通用 faq.html
        (r'/faqs/[^)]+\.html', '/faq.html'),
        
        # 修复 model-comparison.html - 替换为 mechanics-tactical-model-selection.html
        (r'/model-comparison\.html', '/mechanics-tactical-model-selection.html'),
        
        # 修复 claude-ai-free.html - 这个文件不存在，替换为 claude-code-pricing.html
        (r'/claude-ai-free\.html', '/claude-code-pricing.html'),
        
        # 修复 troubleshooting.html - 这个文件不存在，替换为 faq.html
        (r'/troubleshooting\.html', '/faq.html'),
        
        # 修复 mechanics-auto-accept-permissions.html - 这个文件不存在
        (r'/mechanics-auto-accept-permissions\.html', '/mechanics-dangerous-skip-permissions.html'),
        
        # 修复 task-agent-工具.html - 中文字符问题
        (r'/mechanics-task-agent-工具\.html', '/mechanics-task-agent-tools.html'),
        
        # 修复 claude-code-mcps/ 子目录链接
        (r'/claude-code-mcps/([^)]+)\.html', r'/claude-code-mcps-\1.html'),
        
        # 修复配置链接中的锚点问题
        (r'/configuration/#[^)]+\.html', '/configuration.html'),
        
        # 修复 changelog 锚点问题
        (r'/claude-code-changelog/#[^)]+\.html', '/claude-code-changelog.html'),
        
        # 修复一些特殊的 FAQ 页面
        (r'/faqs/what-is-dangerously-skip-permissions\.html', '/mechanics-dangerous-skip-permissions.html'),
        (r'/faqs/what-are-role-sub-agents\.html', '/mechanics-split-role-sub-agents.html'),
        (r'/faqs/what-is-plan-mode\.html', '/mechanics-plan-mode.html'),
        (r'/faqs/what-is-auto-plan-mode\.html', '/mechanics-auto-plan-mode.html'),
        (r'/faqs/what-is-ultrathink\.html', '/mechanics-ultrathink-plus-plus.html'),
        (r'/faqs/what-is-cc-usage\.html', '/mechanics-claude-usage.html'),
        (r'/faqs/what-is-model-alias\.html', '/mechanics-tactical-model-selection.html'),
        (r'/faqs/what-is-micro-compact\.html', '/mechanics-context-window-depletion.html'),
        (r'/faqs/what-is-statusline\.html', '/configuration.html'),
        (r'/faqs/--添加-dir\.html', '/configuration.html'),
        (r'/faqs/claude-4-sonnet-vs-opus\.html', '/mechanics-tactical-model-selection.html'),
        
        # 修复 MCPs 相关链接 - 将不存在的 MCP 页面指向主 MCPs 页面
        (r'/claude-code-mcps-browser-tools-mcp\.html', '/claude-code-mcps.html'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_file_links(file_path):
    """修复单个文件中的链接"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    content = fix_common_links(content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    docs_dir = '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs'
    
    print("🔧 修复站内链接...")
    
    md_files = get_all_md_files(docs_dir)
    fixed_count = 0
    total_files = len(md_files)
    
    for file_path in sorted(md_files):
        filename = os.path.basename(file_path)
        if fix_file_links(file_path):
            fixed_count += 1
            print(f"✅ 修复了 {filename}")
        else:
            print(f"⚪ {filename} (无需修复)")
    
    print(f"\n📊 修复完成:")
    print(f"   • 总文件数: {total_files}")
    print(f"   • 修复的文件: {fixed_count}")
    print(f"   • 无需修复: {total_files - fixed_count}")

if __name__ == "__main__":
    main()