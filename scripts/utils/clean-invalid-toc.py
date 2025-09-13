#!/usr/bin/env python3
import os
import re

def clean_invalid_toc(file_path):
    """清理文件末尾的无效目录和乱码文本"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 移除文档末尾的目录结构（通常在最后出现）
        # 匹配从 "- [" 开始的目录列表，直到文件末尾
        content = re.sub(r'\n-   \[.*?\]\(#.*?\)(?:\n    -   \[.*?\]\(#.*?\))*(?:\n-   \[.*?\]\(#.*?\)(?:\n    -   \[.*?\]\(#.*?\))*)*(?:\n.*?\]\(#.*?\))*$', '', content, flags=re.DOTALL)
        
        # 移除乱码文本，特别是包含 "这不是实际的英文文档内容" 之类的内容
        content = re.sub(r'````.*?这不是实际的英文文档内容.*?```\n*$', '', content, flags=re.DOTALL)
        
        # 移除其他可能的乱码或错误文本
        content = re.sub(r'，我会立即进行翻译。\n*$', '', content)
        
        # 移除文件末尾多余的空行，但保留一个换行符
        content = content.rstrip() + '\n'
        
        # 如果内容有改变，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 清理了 {file_path}")
            return True
        else:
            print(f"⏭️  跳过 {file_path} (无需清理)")
            return False
            
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    docs_dir = '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs'
    
    # 获取所有 .md 文件
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"发现 {len(md_files)} 个 Markdown 文件")
    
    cleaned_count = 0
    for file_path in sorted(md_files):
        if clean_invalid_toc(file_path):
            cleaned_count += 1
    
    print(f"\n清理完成！共处理了 {cleaned_count} 个文件")

if __name__ == "__main__":
    main()