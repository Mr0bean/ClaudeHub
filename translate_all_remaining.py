#!/usr/bin/env python3
"""
翻译所有剩余的未翻译页面
"""

import os
import time
from pathlib import Path
from claude_translator import ClaudeTranslator

def translate_remaining_pages():
    """翻译所有剩余的页面"""
    
    translator = ClaudeTranslator()
    
    # 需要翻译的页面列表（按优先级排序）
    pages_to_translate = [
        # 最高优先级 - 完全未翻译
        'final-site/docs/faq.md',
        'final-site/docs/claude-code-changelog.md', 
        'final-site/docs/claude-news.md',
        'final-site/docs/mechanics-agent-first-design.md',
        'final-site/docs/claude-code-mcps-context7-mcp.md',
        
        # 需要完成翻译的页面
        'final-site/docs/privacy-policy.md',  # 10.5% 已翻译
        'final-site/docs/mechanics-rev-the-engine.md',  # 51.1% 已翻译
    ]
    
    successful = []
    failed = []
    
    for i, file_path in enumerate(pages_to_translate, 1):
        try:
            print(f"\n[{i}/{len(pages_to_translate)}] 正在翻译: {file_path}")
            print("=" * 60)
            
            # 读取原文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 特殊处理：对于部分翻译的文件，只翻译英文部分
            if 'privacy-policy.md' in file_path or 'mechanics-rev-the-engine.md' in file_path:
                print(f"  注意：{os.path.basename(file_path)} 已部分翻译，将保留现有中文内容")
            
            # 翻译
            translated = translator.translate_content(content)
            
            # 创建备份
            backup_path = f"{file_path}.backup_{int(time.time())}"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ 已创建备份: {backup_path}")
            
            # 保存翻译
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            print(f"  ✓ 翻译完成: {file_path}")
            successful.append(file_path)
            
            # 避免API限制
            time.sleep(2)
            
        except Exception as e:
            print(f"  ✗ 翻译失败: {e}")
            failed.append((file_path, str(e)))
    
    # 打印总结
    print("\n" + "=" * 60)
    print("翻译总结")
    print("=" * 60)
    print(f"✓ 成功: {len(successful)}/{len(pages_to_translate)}")
    print(f"✗ 失败: {len(failed)}/{len(pages_to_translate)}")
    
    if successful:
        print("\n成功翻译的文件:")
        for path in successful:
            print(f"  ✓ {os.path.basename(path)}")
    
    if failed:
        print("\n翻译失败的文件:")
        for path, error in failed:
            print(f"  ✗ {os.path.basename(path)}: {error}")
    
    return successful, failed

if __name__ == "__main__":
    print("开始批量翻译剩余页面...")
    translate_remaining_pages()