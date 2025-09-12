#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终修复所有翻译问题的脚本
"""

import os
import re
from pathlib import Path

def fix_all_issues(content):
    """修复所有已知的翻译问题"""
    
    # 1. 移除markdown代码块包装
    if content.startswith('```markdown\n'):
        content = content[12:]
    if content.rstrip().endswith('```'):
        lines = content.rstrip().rsplit('\n', 1)
        if len(lines) == 2 and lines[1] == '```':
            content = lines[0] + '\n'
    
    # 2. 修复分行的markdown链接
    # 修复图片链接分行问题
    content = re.sub(r'\[\s*\n\s*(<img[^>]+>)\s*\n\s*\]', r'[\1]', content, flags=re.MULTILINE)
    
    # 3. 修复链接路径
    # 确保内部链接使用.html扩展名
    content = re.sub(r'\]\((/[^)#]+?)(?<!\.html)(?<!/)(\)|#)', r'](\1.html\2', content)
    # 修复根路径
    content = content.replace('](/README.html)', '](/)')
    
    # 4. 修复路径问题
    content = content.replace('/mechanics/', '/mechanics-')
    content = content.replace('/claude-code/', '/claude-code-')
    
    # 5. 移除Claude的多余回复
    patterns_to_remove = [
        r'我需要看到实际的英文文档内容才能进行翻译.*?请提供具体的英文文档内容。\s*',
        r'您提到的.*?是一个占位符.*?\s*',
        r'您提供的内容.*?占位符.*?\s*',
        r'这是翻译后的中文版本：\s*',
        r'以下是翻译后的内容：\s*',
        r'好的，我来翻译这个文档：\s*',
        r'我注意到您提供的内容是.*?\s*',
        r'请提供.*?英文文档内容.*?\s*',
        r'请粘贴实际的英文文档内容.*?\s*',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # 6. 清理开头的Claude回复
    lines = content.split('\n')
    clean_lines = []
    skip_until_frontmatter = False
    
    for i, line in enumerate(lines):
        # 如果找到frontmatter开始，从这里开始保留
        if line.strip() == '---' and i < 10:
            clean_lines = lines[i:]
            break
        # 如果包含Claude的常见回复模式，跳过
        if any(phrase in line for phrase in ['我无法看到', '请提供', '占位符', '实际内容']):
            continue
        clean_lines.append(line)
    
    if clean_lines:
        content = '\n'.join(clean_lines)
    
    # 7. 确保有正确的标题
    # 检查是否有frontmatter
    if content.startswith('---'):
        # 查找frontmatter结束位置
        end_idx = content.find('\n---\n', 4)
        if end_idx > 0:
            frontmatter = content[:end_idx + 5]
            body = content[end_idx + 5:]
            
            # 从frontmatter提取标题
            title_match = re.search(r'title:\s*"([^"]+)"', frontmatter)
            if title_match:
                title = title_match.group(1)
                # 确保body有H1标题
                if not body.strip().startswith('#'):
                    body = f"\n# {title}\n{body}"
                content = frontmatter + body
    
    return content

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = fix_all_issues(content)
        
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
    
    # 获取所有markdown文件（排除backup文件）
    md_files = [f for f in docs_dir.glob('*.md') if 'backup' not in str(f)]
    
    print(f"🔍 找到 {len(md_files)} 个markdown文件")
    print("=" * 50)
    
    fixed_count = 0
    for file_path in sorted(md_files):
        if process_file(file_path):
            fixed_count += 1
    
    print("=" * 50)
    print(f"✨ 完成！修复了 {fixed_count} 个文件")
    
    # 显示修复统计
    print("\n📊 修复统计:")
    print(f"  - 总文件数: {len(md_files)}")
    print(f"  - 已修复: {fixed_count}")
    print(f"  - 无需修复: {len(md_files) - fixed_count}")

if __name__ == '__main__':
    main()