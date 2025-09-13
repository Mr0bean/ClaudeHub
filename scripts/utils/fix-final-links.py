#!/usr/bin/env python3
import os

def fix_final_links():
    """修复最后的几个损坏链接"""
    docs_dir = '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs'
    
    fixes = [
        # SuperClaude link
        ('mechanics-split-role-sub-agents.md', 
         '/claude-code-mcps-super-claude.html', 
         '/claude-code-mcps.html'),
         
        # tight-feedback-loops links
        ('mechanics-todo-lists-as-instruction-mirrors.md', 
         '/mechanics-tight-feedback-loops.html', 
         '/mechanics-context-window-depletion.html'),
         
        ('mechanics-you-are-the-main-thread.md', 
         '/mechanics-tight-feedback-loops.html', 
         '/mechanics-context-window-depletion.html'),
         
        # tool-maker link  
        ('watch-control.md', 
         '/tool-maker.html', 
         '/mechanics-task-agent-tools.html'),
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
    fix_final_links()