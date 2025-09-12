#!/usr/bin/env python3
"""
测试翻译10个网站文件的脚本
"""

import subprocess
import sys
from pathlib import Path
import time

# 要翻译的10个文件（选择一些有代表性的文件）
test_files = [
    "../final-site/docs/mechanics-humanising-agents.md",
    "../final-site/docs/claude-code-pricing.md",
    "../final-site/docs/privacy-policy.md", 
    "../final-site/docs/mechanics-todo-lists-as-instruction-mirrors.md",
    "../final-site/docs/mechanics-sanity-check.md",
    "../final-site/docs/claude-code-mcps-tdd-guard.md",
    "../final-site/docs/mechanics-poison-context-awareness.md",
    "../final-site/docs/mechanics-claude-usage.md",
    "../final-site/docs/claude-code-mcps-awesome-claude-code.md",
    "../final-site/docs/mechanics-context-window-constraints-as-training.md"
]

print("🚀 开始批量翻译测试...")
print(f"📋 计划翻译 {len(test_files)} 个文件\n")

success_count = 0
failed_count = 0
start_time = time.time()

for i, file_path in enumerate(test_files, 1):
    file_name = Path(file_path).name
    print(f"[{i}/{len(test_files)}] 正在翻译: {file_name}")
    
    try:
        # 使用我们的翻译系统
        result = subprocess.run(
            ["python", "main_translator.py", "file", file_path],
            capture_output=True,
            text=True,
            timeout=180  # 3分钟超时
        )
        
        if result.returncode == 0:
            print(f"✅ 成功: {file_name}")
            success_count += 1
        else:
            print(f"❌ 失败: {file_name} - {result.stderr.strip()}")
            failed_count += 1
            
    except subprocess.TimeoutExpired:
        print(f"⏰ 超时: {file_name}")
        failed_count += 1
    except Exception as e:
        print(f"❌ 异常: {file_name} - {e}")
        failed_count += 1
    
    print()  # 空行分隔

# 统计结果
end_time = time.time()
duration = end_time - start_time

print("=" * 50)
print("📊 翻译结果统计:")
print(f"✅ 成功: {success_count}")
print(f"❌ 失败: {failed_count}")
print(f"📈 成功率: {(success_count / len(test_files) * 100):.1f}%")
print(f"⏱️ 总耗时: {duration:.1f}秒")
print(f"⚡ 平均每文件: {duration / len(test_files):.1f}秒")