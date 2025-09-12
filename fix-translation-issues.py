#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复翻译文件中的常见问题
"""

import os
import re
from pathlib import Path

def fix_markdown_wrapper(content):
    """移除多余的markdown代码块包装"""
    # 检查是否以```markdown开头
    if content.startswith('```markdown\n'):
        content = content[12:]  # 移除开头的```markdown\n
    
    # 检查是否以```结尾
    if content.rstrip().endswith('```'):
        lines = content.rstrip().rsplit('\n', 1)
        if len(lines) == 2 and lines[1] == '```':
            content = lines[0] + '\n'
    
    return content

def fix_broken_links(content):
    """修复损坏的链接格式"""
    # 修复路径问题
    content = content.replace('/mechanics/', '/mechanics-')
    content = content.replace('/claude-code/', '/claude-code-')
    
    # 确保链接使用.html扩展名
    content = re.sub(r'\]\((/[^)]+?)(?<!\.html)(?<!/)(\)|#)', r'](\1.html\2', content)
    
    return content

def remove_claude_artifacts(content):
    """移除Claude的多余回复内容"""
    # 移除常见的Claude多余回复
    patterns = [
        r'我需要看到实际的英文文档内容才能进行翻译.*?请提供具体的英文文档内容。\n*',
        r'您提到的.*?是一个占位符.*?\n*',
        r'这是翻译后的中文版本：\n*',
        r'以下是翻译后的内容：\n*',
        r'好的，我来翻译这个文档：\n*',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    return content

def fix_file(file_path):
    """修复单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用所有修复
        content = fix_markdown_wrapper(content)
        content = fix_broken_links(content)
        content = remove_claude_artifacts(content)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复: {file_path}")
            return True
        else:
            print(f"⏭️  跳过: {file_path} (无需修复)")
            return False
    except Exception as e:
        print(f"❌ 错误: {file_path} - {e}")
        return False

def main():
    """主函数"""
    docs_dir = Path('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs')
    
    # 获取所有markdown文件
    md_files = list(docs_dir.glob('*.md'))
    
    print(f"🔍 找到 {len(md_files)} 个markdown文件")
    print("=" * 50)
    
    fixed_count = 0
    for file_path in md_files:
        if fix_file(file_path):
            fixed_count += 1
    
    print("=" * 50)
    print(f"✨ 完成！修复了 {fixed_count} 个文件")

if __name__ == '__main__':
    main()