#!/usr/bin/env python3
import re
import sys

def fix_table_in_file(filepath):
    """修复文件中的表格格式"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 第一个表格：生态系统对比
        if '比较：自定义代理 vs. 子代理 vs. 任务工具' in content:
            table1 = """| 方面 | 自定义代理 | 分角色子代理 | 任务/代理工具 |
|------|------------|--------------|---------------|
| **令牌效率** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **激活方式** | 自动委派 | 手动委派 | 手动委派 |
| **共享系统提示** | 否 | 是 | 是 |
| **可移植性** | 高度可移植（单个 .md 文件） | 不实用 | 不实用 |
| **配置** | YAML frontmatter + 系统提示 | 仅任务描述 | 仅任务描述 |
| **系统提示** | 自定义系统提示访问 | 继承系统提示 | 继承系统提示 |
| **自定义工具选择** | 是 | 否 | 否 |
| **Claude.md 继承** | 是 | 是 | 是 |
| **用例** | 专业化可重复任务 | 多视角分析 | 并行任务执行 |"""
            
            # 替换第一个表格
            pattern1 = r'比较：自定义代理 vs\. 子代理 vs\. 任务工具\s*\n\n方面\s*\n\n.*?并行任务执行'
            content = re.sub(pattern1, table1, content, flags=re.DOTALL)
        
        # 第二个表格：性能分析
        if '按工具数量的性能分析' in content:
            table2 = """| 工具数量 | 令牌使用量 | 相对初始化时间 | Claude.md 为空 |
|----------|------------|----------------|----------------|
| 0 | 640 | 2.6s | true |
| 1 | 2.6k | 3.9s | false |
| 2 | 2.9k | 4.3s | false |
| 3 | 3.2k | 6.0s | false |
| 4 | 3.4k | 6.1s | false |
| 5 | 3.9k | 5.1s | false |
| 6 | 4.1k | 7.0s | false |
| 7 | 5.0k | 6.9s | false |
| 8 | 7.1k | 5.6s | false |
| 9 | 7.5k | 5.1s | false |
| 10 | 7.9k | 6.2s | false |
| 15+ | 13.9k - 25k | 6.4s | false |"""
            
            # 替换第二个表格  
            pattern2 = r'工具数量\s*\n\n令牌使用量\s*\n\n.*?false'
            content = re.sub(pattern2, table2, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 修复了 {filepath} 中的表格")
        return True
        
    except Exception as e:
        print(f"❌ 处理 {filepath} 时出错: {e}")
        return False

# 需要修复的文件
files_to_fix = [
    '/Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs/mechanics-agent-engineering.md'
]

for file in files_to_fix:
    fix_table_in_file(file)

print("\n表格修复完成！")