#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin, urlparse
from collections import defaultdict

def scan_vuepress_site(base_url="http://localhost:8081"):
    """Scan all links in the VuePress site"""
    
    # Read sidebar config to get all pages
    with open('final-site/docs/.vuepress/config.js', 'r', encoding='utf-8') as f:
        config_content = f.read()
    
    visited = set()
    to_visit = {base_url}
    broken_links = []
    redirects = []
    all_links = defaultdict(list)
    
    session = requests.Session()
    
    while to_visit:
        current_url = to_visit.pop()
        
        if current_url in visited:
            continue
            
        visited.add(current_url)
        
        try:
            print(f"Checking: {current_url}")
            response = session.get(current_url, timeout=5, allow_redirects=False)
            
            if response.status_code == 301 or response.status_code == 302:
                redirect_to = response.headers.get('Location')
                redirects.append({
                    'from': current_url,
                    'to': redirect_to,
                    'status': response.status_code
                })
                # Follow redirect
                if redirect_to:
                    absolute_redirect = urljoin(current_url, redirect_to)
                    if absolute_redirect not in visited and absolute_redirect.startswith(base_url):
                        to_visit.add(absolute_redirect)
                        
            elif response.status_code == 404:
                broken_links.append({
                    'url': current_url,
                    'status': 404
                })
                
            elif response.status_code == 200:
                # Parse HTML to find more links
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all links
                for tag in soup.find_all(['a']):
                    href = tag.get('href')
                    if href:
                        # Skip external links and anchors
                        if href.startswith('#') or href.startswith('http') and not href.startswith(base_url):
                            continue
                            
                        absolute_url = urljoin(current_url, href)
                        
                        # Only check URLs within our site
                        if absolute_url.startswith(base_url):
                            all_links[current_url].append(absolute_url)
                            
                            if absolute_url not in visited:
                                to_visit.add(absolute_url)
                                
            else:
                broken_links.append({
                    'url': current_url,
                    'status': response.status_code
                })
                
        except requests.RequestException as e:
            broken_links.append({
                'url': current_url,
                'error': str(e)
            })
            
        # Rate limiting
        time.sleep(0.1)
    
    # Generate report
    report = {
        'total_pages_scanned': len(visited),
        'broken_links': broken_links,
        'redirects': redirects,
        'pages_with_links': len(all_links),
        'summary': {
            'broken_count': len(broken_links),
            'redirect_count': len(redirects),
            'success_count': len(visited) - len(broken_links)
        }
    }
    
    return report

def check_specific_pages():
    """Check specific important pages"""
    base_url = "http://localhost:8081"
    important_pages = [
        "/",
        "/install-claude-code.html",
        "/claude-code-tutorial.html",
        "/claude-code-pricing.html",
        "/claude-code-changelog.html",
        "/claude-code-mcps.html",
        "/mechanics-plan-mode.html",
        "/mechanics-auto-plan-mode.html",
        "/mechanics-todo-lists-as-instruction-mirrors.html",
        "/mechanics-sub-agents.html",
        "/mechanics-hooks.html",
        "/configuration.html",
        "/faq.html",
        "/contact.html",
        "/support-claudelog.html",
        "/sponsor.html",
        "/terms-of-service.html",
        "/watch-control.html",
        # MCP pages
        "/claude-code-mcps-awesome-claude-code.html",
        "/claude-code-mcps-awesome-claude-prompts.html",
        "/claude-code-mcps-awesome-mcp-servers.html",
        "/claude-code-mcps-blender-mcp.html",
        "/claude-code-mcps-browser-tools-mcp.html",
        "/claude-code-mcps-cc-usage.html",
        "/claude-code-mcps-claude-code-router.html",
        "/claude-code-mcps-claudia.html",
        "/claude-code-mcps-desktop-commander-mcp.html",
        "/claude-code-mcps-github-mcp-server.html",
        "/claude-code-mcps-puppeteer-mcp.html",
        "/claude-code-mcps-reddit-mcp.html",
        "/claude-code-mcps-serena.html",
        "/claude-code-mcps-tdd-guard.html",
        "/claude-code-mcps-tweakcc.html",
        "/claude-code-mcps-whatsapp-mcp.html",
        "/claude-code-mcps-zen-mcp-server.html",
    ]
    
    results = []
    session = requests.Session()
    
    for page in important_pages:
        url = base_url + page
        try:
            response = session.get(url, timeout=5)
            results.append({
                'url': page,
                'status': response.status_code,
                'ok': response.status_code == 200
            })
            print(f"✓ {page}: {response.status_code}" if response.status_code == 200 else f"✗ {page}: {response.status_code}")
        except Exception as e:
            results.append({
                'url': page,
                'error': str(e),
                'ok': False
            })
            print(f"✗ {page}: ERROR - {e}")
    
    # Summary
    success_count = sum(1 for r in results if r.get('ok'))
    print(f"\n总结: {success_count}/{len(results)} 页面正常访问")
    
    return results

if __name__ == "__main__":
    print("检查重要页面链接...")
    print("=" * 50)
    
    # First check important pages
    results = check_specific_pages()
    
    print("\n" + "=" * 50)
    print("开始全站扫描...")
    print("=" * 50)
    
    # Full site scan
    report = scan_vuepress_site()
    
    print("\n" + "=" * 50)
    print("扫描报告:")
    print(f"- 总页面数: {report['summary']['success_count']}")
    print(f"- 损坏链接: {report['summary']['broken_count']}")
    print(f"- 重定向: {report['summary']['redirect_count']}")
    
    if report['broken_links']:
        print("\n损坏的链接:")
        for link in report['broken_links']:
            print(f"  ✗ {link['url']} - {link.get('status', link.get('error'))}")
    
    if report['redirects']:
        print("\n重定向:")
        for redirect in report['redirects']:
            print(f"  → {redirect['from']} -> {redirect['to']}")
    
    # Save full report
    with open('link_scan_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print("\n完整报告已保存到 link_scan_report.json")