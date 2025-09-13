#!/usr/bin/env python3
"""单文件翻译工具"""

import sys
import subprocess
import os

def translate_file(file_path):
    """翻译markdown文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return False
    
    # 检查是否已翻译
    chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
    if len(content) > 0 and chinese_chars / len(content) > 0.3:
        print(f"⏭️  已翻译，跳过")
        return True
    
    print(f"🔄 翻译中...")
    
    prompt = f"""请将markdown文档从英文翻译成中文。

规则：
1. 翻译所有英文内容
2. 保留markdown格式、URL、代码块
3. frontmatter中的title翻译成中文
4. 保留HTML标签
5. 使用标准技术术语

{content}

输出完整翻译："""
    
    try:
        result = subprocess.run(
            ['claude', prompt],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0 and result.stdout:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout.strip())
            print(f"✅ 翻译完成")
            return True
        else:
            print(f"❌ 翻译失败")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("使用方法: python translate-file.py <文件路径>")
        print("示例: python translate-file.py final-site/docs/mechanics-plan-mode.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        sys.exit(1)
    
    # 检查是否为 markdown 文件
    if not file_path.endswith('.md'):
        print(f"⚠️  警告: 不是 markdown 文件")
    
    # 执行翻译
    success = translate_file(file_path)
    
    if success:
        print(f"🎉 翻译完成！")
    else:
        print(f"💔 翻译失败")
        sys.exit(1)

if __name__ == "__main__":
    main()