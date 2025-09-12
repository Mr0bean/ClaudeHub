#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查未翻译的文件
"""

import os
import re
from pathlib import Path

def is_translated(file_path):
    """检查文件是否已翻译"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 检查标题是否包含中文
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        if not title_match:
            return True  # 没有标题，跳过
            
        title = title_match.group(1)
        
        # 检查是否包含中文字符
        if re.search(r'[\u4e00-\u9fff]', title):
            return True
            
        # 检查内容中是否有中文（前1000个字符）
        if re.search(r'[\u4e00-\u9fff]', content[:1000]):
            return True
            
        return False
    except Exception:
        return True  # 出错时假设已翻译

def main():
    docs_dir = Path('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs')
    
    # 获取所有markdown文件（排除backup）
    md_files = [f for f in docs_dir.glob('*.md') if 'backup' not in str(f)]
    
    untranslated = []
    translated = []
    
    for file_path in sorted(md_files):
        if is_translated(file_path):
            translated.append(file_path.name)
        else:
            untranslated.append(file_path.name)
    
    print("=" * 60)
    print(f"📊 翻译统计:")
    print(f"  总文件数: {len(md_files)}")
    print(f"  已翻译: {len(translated)}")
    print(f"  未翻译: {len(untranslated)}")
    print("=" * 60)
    
    if untranslated:
        print("\n❌ 未翻译的文件:")
        for i, file in enumerate(untranslated, 1):
            print(f"  {i}. {file}")
    else:
        print("\n✅ 所有文件都已翻译!")
    
    return untranslated

if __name__ == '__main__':
    untranslated_files = main()
    
    # 如果有未翻译的文件，生成翻译脚本
    if untranslated_files:
        print("\n生成翻译脚本: translate-remaining.sh")
        with open('/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/translate-remaining.sh', 'w') as f:
            f.write('#!/bin/bash\n')
            f.write('# 翻译剩余的文件\n\n')
            f.write('cd /Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/translate\n\n')
            
            for file in untranslated_files:
                f.write(f'echo "翻译 {file}..."\n')
                f.write(f'python main_translator.py file ../final-site/docs/{file} --force\n')
                f.write('sleep 3\n\n')
            
            f.write('echo "✅ 所有文件翻译完成!"\n')