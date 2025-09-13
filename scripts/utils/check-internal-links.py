#!/usr/bin/env python3
import os
import re
import glob
from urllib.parse import urlparse

def get_all_md_files(docs_dir):
    """获取所有 markdown 文件"""
    return glob.glob(os.path.join(docs_dir, "*.md"))

def get_existing_pages(docs_dir):
    """获取所有存在的页面（不包括扩展名）"""
    md_files = get_all_md_files(docs_dir)
    pages = set()
    
    for file_path in md_files:
        filename = os.path.basename(file_path)
        if filename.endswith('.md'):
            page_name = filename[:-3]  # 移除 .md 扩展名
            pages.add(page_name)
    
    # 添加一些特殊页面
    pages.add('index')  # README.md 对应 index
    pages.add('')  # 首页
    
    return pages

def extract_internal_links(content):
    """提取内容中的内部链接"""
    # 匹配 markdown 链接 [text](url) 和 [text](/url)
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    links = re.findall(link_pattern, content)
    
    internal_links = []
    for text, url in links:
        # 跳过外部链接
        if url.startswith('http://') or url.startswith('https://'):
            continue
        
        # 跳过锚点链接
        if url.startswith('#'):
            continue
            
        # 跳过 mailto 链接
        if url.startswith('mailto:'):
            continue
            
        internal_links.append((text, url))
    
    return internal_links

def normalize_url(url):
    """标准化 URL"""
    # 移除开头的 /
    if url.startswith('/'):
        url = url[1:]
    
    # 移除锚点
    if '#' in url:
        url = url.split('#')[0]
    
    # 移除 .html 扩展名
    if url.endswith('.html'):
        url = url[:-5]
    
    return url

def check_file_links(file_path, existing_pages):
    """检查单个文件中的链接"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    internal_links = extract_internal_links(content)
    broken_links = []
    
    for text, url in internal_links:
        normalized_url = normalize_url(url)
        
        # 特殊处理：空字符串指向首页
        if normalized_url == '' or normalized_url == 'index':
            continue
            
        if normalized_url not in existing_pages:
            broken_links.append((text, url, normalized_url))
    
    return broken_links

def suggest_fix(broken_url, existing_pages):
    """为损坏的链接建议修复方案"""
    # 尝试找到相似的页面
    suggestions = []
    
    for page in existing_pages:
        if page == '':
            continue
            
        # 检查是否是部分匹配
        if broken_url in page or page in broken_url:
            suggestions.append(page)
        
        # 检查是否是相似的名称
        broken_words = set(broken_url.replace('-', ' ').split())
        page_words = set(page.replace('-', ' ').split())
        
        # 如果有共同词汇，可能是相关页面
        if broken_words & page_words:
            suggestions.append(page)
    
    return suggestions[:3]  # 返回最多3个建议

def main():
    docs_dir = '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs'
    
    print("🔍 检查站内链接...")
    
    # 获取所有存在的页面
    existing_pages = get_existing_pages(docs_dir)
    print(f"📄 发现 {len(existing_pages)} 个页面")
    
    # 检查所有文件的链接
    md_files = get_all_md_files(docs_dir)
    total_broken = 0
    files_with_broken_links = 0
    
    for file_path in sorted(md_files):
        filename = os.path.basename(file_path)
        broken_links = check_file_links(file_path, existing_pages)
        
        if broken_links:
            files_with_broken_links += 1
            print(f"\n❌ {filename}:")
            
            for text, original_url, normalized_url in broken_links:
                total_broken += 1
                print(f"   🔗 [{text}]({original_url})")
                print(f"      ➜ 标准化后: {normalized_url}")
                
                # 建议修复方案
                suggestions = suggest_fix(normalized_url, existing_pages)
                if suggestions:
                    print(f"      💡 建议修复为: {', '.join(suggestions)}")
                else:
                    print(f"      ⚠️  未找到相似页面")
    
    print(f"\n📊 检查完成:")
    print(f"   • 总文件数: {len(md_files)}")
    print(f"   • 有问题的文件: {files_with_broken_links}")
    print(f"   • 损坏的链接总数: {total_broken}")
    
    if total_broken == 0:
        print("✅ 所有站内链接都是有效的！")
    else:
        print(f"❌ 发现 {total_broken} 个损坏的站内链接需要修复")

if __name__ == "__main__":
    main()