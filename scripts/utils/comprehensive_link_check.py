#!/usr/bin/env python3
import requests
import json
import re
from pathlib import Path

def extract_sidebar_links_from_config():
    """Extract all sidebar links from VuePress config"""
    
    config_path = Path('final-site/docs/.vuepress/config.js')
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all links from the sidebar configuration
    # Look for patterns like '/path.html' or '/'
    link_pattern = r'["\'](/[^"\']*)["\']'
    links = re.findall(link_pattern, content)
    
    # Clean and deduplicate
    unique_links = set()
    for link in links:
        # Skip non-page links
        if link.startswith('/img/') or link.startswith('/css/') or link.startswith('/js/'):
            continue
        # Add to set
        unique_links.add(link)
    
    return sorted(list(unique_links))

def check_all_pages():
    """Check all pages found in config"""
    
    base_url = "http://localhost:8081"
    sidebar_links = extract_sidebar_links_from_config()
    
    print(f"找到 {len(sidebar_links)} 个页面链接")
    print("=" * 50)
    
    results = {
        'success': [],
        'failed': [],
        'total': len(sidebar_links)
    }
    
    session = requests.Session()
    
    for link in sidebar_links:
        url = base_url + link
        
        try:
            response = session.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✓ {link}")
                results['success'].append(link)
            else:
                print(f"✗ {link} - Status: {response.status_code}")
                results['failed'].append({
                    'link': link,
                    'status': response.status_code
                })
        except Exception as e:
            print(f"✗ {link} - Error: {str(e)}")
            results['failed'].append({
                'link': link,
                'error': str(e)
            })
    
    # Print summary
    print("\n" + "=" * 50)
    print("链接检查总结:")
    print(f"✓ 成功: {len(results['success'])} / {results['total']}")
    print(f"✗ 失败: {len(results['failed'])} / {results['total']}")
    
    if results['failed']:
        print("\n失败的链接:")
        for item in results['failed']:
            if 'status' in item:
                print(f"  - {item['link']}: HTTP {item['status']}")
            else:
                print(f"  - {item['link']}: {item['error']}")
    
    # Check if all Markdown files have corresponding routes
    print("\n" + "=" * 50)
    print("检查 Markdown 文件与路由映射:")
    
    docs_dir = Path('final-site/docs')
    md_files = list(docs_dir.glob('*.md'))
    
    print(f"找到 {len(md_files)} 个 Markdown 文件")
    
    # Check each markdown file has a route
    unmapped_files = []
    for md_file in md_files:
        # Convert file name to expected URL
        if md_file.name == 'README.md':
            expected_url = '/'
        else:
            expected_url = '/' + md_file.stem + '.html'
        
        # Check if this URL is in our sidebar links
        if expected_url not in sidebar_links:
            unmapped_files.append({
                'file': md_file.name,
                'expected_url': expected_url
            })
    
    if unmapped_files:
        print(f"\n⚠️ 发现 {len(unmapped_files)} 个未映射到路由的文件:")
        for item in unmapped_files:
            print(f"  - {item['file']} -> {item['expected_url']}")
    else:
        print("✓ 所有 Markdown 文件都已正确映射到路由")
    
    # Save detailed report
    report = {
        'sidebar_links': sidebar_links,
        'check_results': results,
        'unmapped_files': unmapped_files,
        'summary': {
            'total_links': len(sidebar_links),
            'successful': len(results['success']),
            'failed': len(results['failed']),
            'markdown_files': len(md_files),
            'unmapped_files': len(unmapped_files)
        }
    }
    
    with open('comprehensive_link_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n详细报告已保存到 comprehensive_link_report.json")
    
    return report

if __name__ == "__main__":
    print("开始全面链接检查...")
    print("=" * 50)
    check_all_pages()