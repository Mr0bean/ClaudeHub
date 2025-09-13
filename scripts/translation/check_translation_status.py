#!/usr/bin/env python3
"""
检查所有页面的翻译状态
"""

import os
import re
from pathlib import Path
import json

def analyze_translation_status(file_path):
    """分析单个文件的翻译状态"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 跳过frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]
        else:
            frontmatter = ""
            body = content
    else:
        frontmatter = ""
        body = content
    
    # 统计中英文字符
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', body))
    english_words = len(re.findall(r'\b[a-zA-Z]+\b', body))
    
    # 提取标题
    title_match = re.search(r'title:\s*["\']?([^"\'\\n]+)["\']?', frontmatter)
    title = title_match.group(1) if title_match else "No title"
    
    # 检查是否有中文标题
    has_chinese_title = bool(re.search(r'[\u4e00-\u9fff]', title))
    
    # 检查主要标题（H1, H2）
    headers = re.findall(r'^#{1,2}\s+(.+)$', body, re.MULTILINE)
    chinese_headers = sum(1 for h in headers if re.search(r'[\u4e00-\u9fff]', h))
    
    # 计算翻译比例（粗略估计）
    total_content = chinese_chars + english_words
    if total_content > 0:
        translation_ratio = chinese_chars / total_content
    else:
        translation_ratio = 0
    
    return {
        'title': title,
        'has_chinese_title': has_chinese_title,
        'chinese_chars': chinese_chars,
        'english_words': english_words,
        'translation_ratio': translation_ratio,
        'total_headers': len(headers),
        'chinese_headers': chinese_headers,
        'file_name': os.path.basename(file_path)
    }

def main():
    docs_dir = Path('final-site/docs')
    
    # 获取所有markdown文件（排除备份）
    md_files = [f for f in docs_dir.glob('*.md') 
                if 'backup' not in f.name]
    
    results = []
    
    for file_path in sorted(md_files):
        status = analyze_translation_status(file_path)
        results.append(status)
    
    # 分类文件
    fully_translated = []
    partially_translated = []
    untranslated = []
    
    for result in results:
        if result['translation_ratio'] > 0.7:  # 70%以上认为已翻译
            fully_translated.append(result)
        elif result['translation_ratio'] > 0.1:  # 10%-70%认为部分翻译
            partially_translated.append(result)
        else:  # 10%以下认为未翻译
            untranslated.append(result)
    
    # 打印报告
    print("=" * 80)
    print("📊 翻译状态报告")
    print("=" * 80)
    
    print(f"\n📈 总体统计:")
    print(f"  总文件数: {len(results)}")
    print(f"  ✅ 已翻译: {len(fully_translated)} ({len(fully_translated)/len(results)*100:.1f}%)")
    print(f"  🔶 部分翻译: {len(partially_translated)} ({len(partially_translated)/len(results)*100:.1f}%)")
    print(f"  ❌ 未翻译: {len(untranslated)} ({len(untranslated)/len(results)*100:.1f}%)")
    
    if untranslated:
        print(f"\n❌ 未翻译页面 ({len(untranslated)} 个):")
        for item in sorted(untranslated, key=lambda x: x['file_name']):
            print(f"  - {item['file_name']:<45} | {item['title']}")
    
    if partially_translated:
        print(f"\n🔶 部分翻译页面 ({len(partially_translated)} 个):")
        for item in sorted(partially_translated, key=lambda x: x['translation_ratio']):
            print(f"  - {item['file_name']:<45} | {item['translation_ratio']:.1%} | {item['title']}")
    
    # 特别检查重要页面
    important_pages = [
        'README.md',
        'install-claude-code.md',
        'claude-code-tutorial.md',
        'configuration.md',
        'faq.md',
        'claude-code-pricing.md'
    ]
    
    print(f"\n⭐ 重要页面状态:")
    for page_name in important_pages:
        page_status = next((r for r in results if r['file_name'] == page_name), None)
        if page_status:
            status_icon = "✅" if page_status['translation_ratio'] > 0.7 else "🔶" if page_status['translation_ratio'] > 0.1 else "❌"
            print(f"  {status_icon} {page_name:<30} | {page_status['translation_ratio']:.1%} | {page_status['title']}")
    
    # 保存详细报告
    with open('translation_status_report.json', 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total': len(results),
                'fully_translated': len(fully_translated),
                'partially_translated': len(partially_translated),
                'untranslated': len(untranslated)
            },
            'details': results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 详细报告已保存到: translation_status_report.json")

if __name__ == "__main__":
    main()