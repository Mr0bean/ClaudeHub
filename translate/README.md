# Claude Code 智能翻译系统

这是一个基于 Claude Code 的智能翻译系统，专门设计用于翻译技术文档，特别是 Markdown 文件。该系统具有专有名词保护、格式验证、质量检查等高级功能。

## 功能特性

### 🚀 核心功能
- **智能翻译**: 使用 Claude Code 进行高质量翻译
- **内容保护**: 自动保护专有名词、URL、代码块等不应翻译的内容
- **格式保持**: 完美保持 Markdown 格式、HTML 标签和文档结构
- **质量验证**: 内置翻译质量检查和评分系统
- **批量处理**: 支持目录级别的批量翻译

### 🛡️ 内容保护
- **专有名词**: Claude、VuePress、GitHub、API 等技术术语
- **代码内容**: 代码块、内联代码、命令行
- **链接和URL**: 完整保留所有链接
- **HTML标签**: 保持HTML结构不变
- **文件路径**: 保护文件名和路径

### ✅ 质量保证
- **结构验证**: 检查标题、列表、表格结构完整性
- **链接验证**: 确保链接数量和格式正确
- **评分系统**: 自动评估翻译质量（0-100分）
- **错误报告**: 详细的错误信息和建议

## 项目结构

```
claude-translator/
├── claude-translator.py    # 主翻译脚本
├── translate-file.py      # 单文件翻译
├── translate-all.sh       # 批量翻译脚本
├── config.json           # 配置文件
├── logs/                 # 日志目录
└── translation-backups/  # 备份目录
```

## 安装和配置

### 前置要求
1. **Python 3.7+**
2. **Claude Code**: 确保已安装并配置 `claude` 命令
   ```bash
   which claude  # 确认命令可用
   claude --help # 测试连接
   ```

### 快速开始

1. **翻译单个文件**:
   ```bash
   python translate-file.py input.md
   ```

2. **翻译整个目录**:
   ```bash
   python claude-translator.py directory docs/
   ```

3. **强制翻译（覆盖已有中文）**:
   ```bash
   python claude-translator.py directory docs/ --force
   ```

4. **调整并发数**:
   ```bash
   python claude-translator.py directory docs/ --max-workers 3
   ```

## 配置选项

编辑 `config.json` 来自定义翻译行为：

### 翻译设置
```json
{
  "translation": {
    "timeout": 300,
    "max_retries": 3,
    "retry_delay": 5
  }
}
```

### 内容保护
```json
{
  "protection": {
    "protected_terms": ["Claude", "VuePress", "GitHub", "API"],
    "protect_code_blocks": true,
    "protect_urls": true,
    "protect_html": true
  }
}
```

### 质量验证
```json
{
  "validation": {
    "min_quality_score": 70,
    "check_structure": true,
    "check_links": true,
    "check_formatting": true
  }
}
```

## 高级功能

### 1. 自定义保护规则
可以通过配置文件添加自定义的保护模式：
```json
{
  "custom_patterns": [
    "\\b[A-Z]{2,}\\b",
    "\\$\\{[^}]+\\}",
    "@[a-zA-Z0-9_]+"
  ]
}
```

### 2. 质量评分系统
系统会自动评估翻译质量：
- **结构完整性** (30分): 标题、列表、表格结构
- **链接正确性** (25分): URL和Markdown链接
- **格式保持** (25分): 代码块、HTML标签
- **内容完整性** (20分): 是否遗漏内容

### 3. 日志和监控
所有操作都会记录详细日志：
```bash
tail -f logs/translation.log  # 实时查看日志
```

## 使用示例

### 基础使用
```bash
# 翻译单个文件
python translate-file.py README.md

# 翻译目录下所有 .md 文件
python claude-translator.py directory docs/
```

### 高级使用
```bash
# 使用自定义配置文件
python claude-translator.py directory docs/ --config custom-config.json

# 指定文件匹配模式
python claude-translator.py directory docs/ --pattern "*.md"

# 设置并发数和强制模式
python claude-translator.py directory docs/ --max-workers 2 --force
```

## 命令行参数

| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `mode` | 必需 | 翻译模式: `file` 或 `directory` | `file` |
| `path` | 必需 | 文件或目录路径 | `docs/README.md` |
| `--pattern` | 可选 | 文件匹配模式 | `"*.md"` |
| `--force` | 可选 | 强制翻译已有中文文件 | - |
| `--max-workers` | 可选 | 并发工作线程数 | `3` |
| `--config` | 可选 | 自定义配置文件路径 | `my-config.json` |

## 最佳实践

### 1. 翻译前准备
- 确保 Claude Code 已正确配置并可用
- 备份重要文件（系统会自动创建备份）
- 检查配置文件中的专有名词列表

### 2. 批量翻译建议
- 先用少量文件测试配置是否正确
- 根据系统性能调整 `max_workers` 参数
- 对于大型项目，建议分批处理

### 3. 质量检查
- 检查日志中的验证结果
- 对评分较低的文件进行人工检查
- 根据实际需要调整 `validation` 配置

### 4. 错误处理
- 查看详细错误日志定位问题
- 对失败的文件可以单独重试
- 必要时调整超时时间和重试次数

## 故障排除

### 常见问题

1. **"Claude Code not found"**
   - 确保已安装 Claude Code
   - 检查 `claude` 命令是否在 PATH 中

2. **翻译超时**
   - 增加配置中的 `timeout` 值
   - 检查网络连接
   - 考虑分段处理大文件

3. **质量评分过低**
   - 检查原文件格式是否正确
   - 调整 `validation` 设置
   - 增加必要的专有名词到保护列表

4. **内容被错误保护**
   - 检查 `protection` 配置
   - 调整自定义保护模式
   - 使用 `--force` 强制翻译

## 贡献和反馈

如果您在使用过程中遇到问题或有改进建议，欢迎：
1. 查看日志文件获取详细信息
2. 检查配置文件是否正确
3. 提供具体的错误信息和使用场景

---

**注意**: 此系统专门针对技术文档翻译进行优化，特别适合处理包含大量代码、链接和专业术语的 Markdown 文档。