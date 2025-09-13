#!/usr/bin/env python3
"""
Comprehensive Issue Scanner for VuePress Site
Scans for all potential problems in the translated documentation
"""

import re
import json
from pathlib import Path
from collections import defaultdict
import os

class ComprehensiveIssueScanner:
    def __init__(self, docs_dir="final-site/docs"):
        self.docs_dir = Path(docs_dir)
        self.issues = defaultdict(list)
        self.stats = {
            'total_files': 0,
            'files_scanned': 0,
            'total_issues': 0
        }
    
    def scan_all(self):
        """Run all scans"""
        print("🔍 开始全面问题扫描...")
        print("=" * 60)
        
        # Get all markdown files (excluding backups)
        md_files = [f for f in self.docs_dir.glob("*.md") 
                   if not 'backup' in f.name]
        self.stats['total_files'] = len(md_files)
        
        for md_file in md_files:
            self.stats['files_scanned'] += 1
            print(f"扫描: {md_file.name}")
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Run all checks
            self.check_broken_images(md_file, content)
            self.check_untranslated_content(md_file, content)
            self.check_code_blocks(md_file, content)
            self.check_malformed_markdown(md_file, content)
            self.check_frontmatter(md_file, content)
            self.check_special_characters(md_file, content)
            self.check_links(md_file, content)
            self.check_translation_quality(md_file, content)
        
        self.check_duplicate_files()
        self.check_missing_images()
        
        return self.generate_report()
    
    def check_broken_images(self, file_path, content):
        """Check for broken image references"""
        # Find all image references
        img_patterns = [
            r'!\[([^\]]*)\]\(([^\)]+)\)',  # Markdown images
            r'<img[^>]+src=["\']([^"\']+)["\']',  # HTML images
        ]
        
        for pattern in img_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                img_path = match[-1] if isinstance(match, tuple) else match
                
                # Check if image file exists
                if img_path.startswith('/'):
                    full_path = self.docs_dir.parent / img_path[1:]
                else:
                    full_path = file_path.parent / img_path
                
                if not full_path.exists() and not img_path.startswith('http'):
                    self.issues['broken_images'].append({
                        'file': file_path.name,
                        'image': img_path,
                        'line': self._find_line_number(content, img_path)
                    })
    
    def check_untranslated_content(self, file_path, content):
        """Check for untranslated English content"""
        # Skip frontmatter
        if '---' in content:
            parts = content.split('---')
            if len(parts) >= 3:
                content = '---'.join(parts[2:])
        
        # Common English phrases that might be missed
        english_patterns = [
            r'\b(The|This|That|These|Those|What|Where|When|Why|How)\b',
            r'\b(is|are|was|were|been|being|have|has|had)\b',
            r'\b(will|would|could|should|shall|might|may)\b',
            r'\b(for|and|but|or|nor|yet|so)\b',
            r'\b(with|without|through|during|before|after)\b',
        ]
        
        # Check for significant English content (more than 20% English words)
        english_word_count = 0
        total_words = len(re.findall(r'\b\w+\b', content))
        
        for pattern in english_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            english_word_count += len(matches)
        
        if total_words > 0:
            english_ratio = english_word_count / total_words
            if english_ratio > 0.2:  # More than 20% English
                self.issues['untranslated_content'].append({
                    'file': file_path.name,
                    'english_ratio': f"{english_ratio:.1%}",
                    'sample': content[:200] + '...' if len(content) > 200 else content
                })
    
    def check_code_blocks(self, file_path, content):
        """Check for malformed code blocks"""
        # Check for unclosed code blocks
        code_fence_count = content.count('```')
        if code_fence_count % 2 != 0:
            self.issues['code_blocks'].append({
                'file': file_path.name,
                'issue': '未闭合的代码块',
                'fence_count': code_fence_count
            })
        
        # Check for code blocks with broken line breaks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        for block in code_blocks:
            if '<br>' in block or '<br/>' in block:
                self.issues['code_blocks'].append({
                    'file': file_path.name,
                    'issue': '代码块中包含 HTML 换行标签',
                    'sample': block[:100] + '...' if len(block) > 100 else block
                })
    
    def check_malformed_markdown(self, file_path, content):
        """Check for malformed markdown syntax"""
        # Check for broken link syntax
        if re.search(r'\[\s*\n\s*##', content):
            self.issues['malformed_markdown'].append({
                'file': file_path.name,
                'issue': '链接语法断行',
                'pattern': '[换行## 标题]'
            })
        
        # Check for incomplete links
        incomplete_links = re.findall(r'\[([^\]]+)\]\s*$', content, re.MULTILINE)
        if incomplete_links:
            self.issues['malformed_markdown'].append({
                'file': file_path.name,
                'issue': '不完整的链接',
                'count': len(incomplete_links)
            })
        
        # Check for escaped characters that shouldn't be escaped
        over_escaped = re.findall(r'\\([#\*\+\-\.])', content)
        if len(over_escaped) > 10:  # Too many escaped characters
            self.issues['malformed_markdown'].append({
                'file': file_path.name,
                'issue': '过度转义的字符',
                'count': len(over_escaped)
            })
    
    def check_frontmatter(self, file_path, content):
        """Check frontmatter validity"""
        if not content.startswith('---'):
            self.issues['frontmatter'].append({
                'file': file_path.name,
                'issue': '缺少 frontmatter'
            })
        else:
            # Extract frontmatter
            parts = content.split('---')
            if len(parts) >= 3:
                frontmatter = parts[1]
                
                # Check for required fields
                if 'title:' not in frontmatter:
                    self.issues['frontmatter'].append({
                        'file': file_path.name,
                        'issue': '缺少 title 字段'
                    })
                
                # Check for untranslated title
                if re.search(r'title:\s*["\']?[A-Za-z\s]+["\']?', frontmatter):
                    if not any(chinese in frontmatter for chinese in ['中文', '配置', '安装', '教程']):
                        self.issues['frontmatter'].append({
                            'file': file_path.name,
                            'issue': 'Title 可能未翻译'
                        })
    
    def check_special_characters(self, file_path, content):
        """Check for problematic special characters"""
        # Check for unescaped angle brackets that might break Vue
        vue_like_patterns = re.findall(r'<([a-z-]+)>', content)
        for pattern in vue_like_patterns:
            if pattern not in ['img', 'div', 'span', 'p', 'a', 'br', 'hr']:
                self.issues['special_characters'].append({
                    'file': file_path.name,
                    'issue': f'可能被误认为 Vue 组件: <{pattern}>',
                    'pattern': f'<{pattern}>'
                })
        
        # Check for control characters
        control_chars = re.findall(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', content)
        if control_chars:
            self.issues['special_characters'].append({
                'file': file_path.name,
                'issue': '包含控制字符',
                'count': len(control_chars)
            })
    
    def check_links(self, file_path, content):
        """Check internal links"""
        # Find all internal links
        internal_links = re.findall(r'\]\((/[^\)]+)\)', content)
        
        for link in internal_links:
            # Check if link uses correct format
            if not link.endswith('.html') and link != '/' and not link.startswith('/img/'):
                if not link.startswith('http'):
                    self.issues['links'].append({
                        'file': file_path.name,
                        'link': link,
                        'issue': '内部链接应使用 .html 扩展名'
                    })
    
    def check_translation_quality(self, file_path, content):
        """Check translation quality issues"""
        # Check for machine translation artifacts
        machine_patterns = [
            r'Claude\s+Code',  # Should be translated or kept consistent
            r'npm\s+install',  # Commands should remain in English
            r'[A-Z]{2,}',  # All caps words (might be untranslated)
        ]
        
        # Check for inconsistent terminology
        terminology_issues = []
        
        # Check if mixing simplified and traditional Chinese
        simplified = re.findall(r'[个这那没]', content)
        traditional = re.findall(r'[個這那沒]', content)
        
        if simplified and traditional:
            self.issues['translation_quality'].append({
                'file': file_path.name,
                'issue': '混用简体和繁体中文'
            })
    
    def check_duplicate_files(self):
        """Check for duplicate or backup files"""
        all_files = list(self.docs_dir.glob("*.md"))
        
        # Group files by base name
        file_groups = defaultdict(list)
        for f in all_files:
            base_name = re.sub(r'\.backup_\d+', '', f.stem)
            file_groups[base_name].append(f.name)
        
        for base_name, files in file_groups.items():
            if len(files) > 1:
                self.issues['duplicate_files'].append({
                    'base_name': base_name,
                    'files': files,
                    'count': len(files)
                })
    
    def check_missing_images(self):
        """Check for missing images in img directory"""
        img_dir = self.docs_dir.parent / 'img'
        if not img_dir.exists():
            self.issues['missing_images'].append({
                'issue': 'img 目录不存在'
            })
        else:
            # Check if common images exist
            expected_images = [
                'img/discovery',
                'img/supporters'
            ]
            
            for img_path in expected_images:
                full_path = self.docs_dir.parent / img_path
                if not full_path.exists():
                    self.issues['missing_images'].append({
                        'path': img_path,
                        'issue': '预期的图片目录不存在'
                    })
    
    def _find_line_number(self, content, search_text):
        """Find line number of text in content"""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if search_text in line:
                return i
        return 0
    
    def generate_report(self):
        """Generate comprehensive report"""
        self.stats['total_issues'] = sum(len(issues) for issues in self.issues.values())
        
        report = {
            'summary': self.stats,
            'issues': dict(self.issues),
            'severity_count': {
                'critical': 0,
                'warning': 0,
                'info': 0
            }
        }
        
        # Categorize by severity
        critical_types = ['broken_images', 'code_blocks', 'malformed_markdown', 'missing_images']
        warning_types = ['untranslated_content', 'frontmatter', 'special_characters', 'links']
        
        for issue_type, issues in self.issues.items():
            if issue_type in critical_types:
                report['severity_count']['critical'] += len(issues)
            elif issue_type in warning_types:
                report['severity_count']['warning'] += len(issues)
            else:
                report['severity_count']['info'] += len(issues)
        
        return report

def main():
    scanner = ComprehensiveIssueScanner()
    report = scanner.scan_all()
    
    print("\n" + "=" * 60)
    print("📊 扫描报告总结")
    print("=" * 60)
    
    print(f"\n📁 文件统计:")
    print(f"  - 总文件数: {report['summary']['total_files']}")
    print(f"  - 已扫描: {report['summary']['files_scanned']}")
    print(f"  - 发现问题: {report['summary']['total_issues']}")
    
    print(f"\n⚠️ 问题严重性:")
    print(f"  - 🔴 严重: {report['severity_count']['critical']}")
    print(f"  - 🟡 警告: {report['severity_count']['warning']}")
    print(f"  - 🔵 信息: {report['severity_count']['info']}")
    
    if report['issues']:
        print("\n📋 问题详情:")
        
        for issue_type, issues in report['issues'].items():
            if issues:
                print(f"\n### {issue_type.replace('_', ' ').title()} ({len(issues)} 个)")
                
                # Show first 3 issues as examples
                for issue in issues[:3]:
                    print(f"  - {json.dumps(issue, ensure_ascii=False, indent=4)}")
                
                if len(issues) > 3:
                    print(f"  ... 还有 {len(issues) - 3} 个问题")
    
    # Save full report
    with open('comprehensive_issue_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 完整报告已保存到: comprehensive_issue_report.json")
    
    # Generate actionable summary
    print("\n" + "=" * 60)
    print("🎯 建议的修复优先级:")
    print("=" * 60)
    
    if report['severity_count']['critical'] > 0:
        print("\n1. 🔴 立即修复 (影响功能):")
        if 'broken_images' in report['issues'] and report['issues']['broken_images']:
            print(f"   - 修复 {len(report['issues']['broken_images'])} 个损坏的图片引用")
        if 'code_blocks' in report['issues'] and report['issues']['code_blocks']:
            print(f"   - 修复 {len(report['issues']['code_blocks'])} 个代码块问题")
        if 'malformed_markdown' in report['issues'] and report['issues']['malformed_markdown']:
            print(f"   - 修复 {len(report['issues']['malformed_markdown'])} 个 Markdown 语法问题")
    
    if report['severity_count']['warning'] > 0:
        print("\n2. 🟡 建议修复 (影响质量):")
        if 'untranslated_content' in report['issues'] and report['issues']['untranslated_content']:
            print(f"   - 翻译 {len(report['issues']['untranslated_content'])} 个页面的剩余英文内容")
        if 'links' in report['issues'] and report['issues']['links']:
            print(f"   - 修正 {len(report['issues']['links'])} 个链接格式")
    
    print("\n✅ 扫描完成!")

if __name__ == "__main__":
    main()