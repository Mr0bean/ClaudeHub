#!/usr/bin/env python3
import os
import re

def fix_remaining_links():
    """修复剩余的损坏链接"""
    docs_dir = '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs'
    
    fixes = [
        # claude-code-mcps.md
        ('claude-code-mcps.md', 
         'claude-code-mcps-browser-tools-mcp.html', 
         'claude-code-mcps-puppeteer-mcp.html'),
        
        # mechanics-dangerous-skip-permissions.md
        ('mechanics-dangerous-skip-permissions.md', 
         'mechanics-auto-accept-permissions.html', 
         'configuration.html'),
        ('mechanics-dangerous-skip-permissions.md', 
         'support-.html', 
         'contact.html'),
        
        # mechanics-git-clone-is-just-the-beginning.md
        ('mechanics-git-clone-is-just-the-beginning.md', 
         'mechanics-tight-feedback-loops.html', 
         'mechanics-context-window-depletion.html'),
        
        # mechanics-permutation-frameworks.md
        ('mechanics-permutation-frameworks.md', 
         'tool-maker.html', 
         'mechanics-task-agent-tools.html'),
    ]
    
    for filename, old_link, new_link in fixes:
        file_path = os.path.join(docs_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            content = content.replace(old_link, new_link)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 修复了 {filename} 中的链接: {old_link} -> {new_link}")
            else:
                print(f"⚪ {filename} 中未找到链接: {old_link}")

if __name__ == "__main__":
    fix_remaining_links()