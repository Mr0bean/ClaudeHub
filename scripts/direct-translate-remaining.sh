#!/bin/bash
# 直接翻译剩余的13个文件

FILES=(
  "claude-code-changelog.md"
  "claude-code-mcps-claudia.md"
  "claude-code-mcps-context7-mcp.md"
  "claude-news.md"
  "configuration.md"
  "disclaimer.md"
  "faq.md"
  "install-claude-code.md"
  "mechanics-agent-engineering.md"
  "mechanics-agent-first-design.md"
  "mechanics-context-window-constraints-as-training.md"
  "mechanics-rev-the-engine.md"
  "privacy-policy.md"
)

cd /Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate

for file in "${FILES[@]}"; do
  echo "==============================================="
  echo "翻译: $file"
  echo "==============================================="
  
  # 读取文件内容
  if [ -f "final-site/docs/$file" ]; then
    content=$(cat "final-site/docs/$file")
    
    # 创建临时翻译提示文件
    cat > temp_prompt.txt << 'EOF'
请将以下markdown文档从英文翻译成中文。要求：
1. 保持markdown格式不变
2. 保留所有URL链接不翻译
3. 保留专有名词如Claude, API, GitHub等不翻译
4. 保留代码块不翻译
5. 翻译frontmatter中的title
6. 确保翻译自然流畅

直接返回翻译后的完整markdown文档，不要添加任何额外说明。

文档内容：
EOF
    
    echo "$content" >> temp_prompt.txt
    
    # 使用claude命令翻译
    translated=$(claude < temp_prompt.txt 2>/dev/null)
    
    if [ ! -z "$translated" ]; then
      # 保存翻译结果
      echo "$translated" > "final-site/docs/$file"
      echo "✅ 完成: $file"
    else
      echo "❌ 失败: $file"
    fi
    
    # 清理临时文件
    rm -f temp_prompt.txt
    
    # 延迟避免请求过快
    sleep 3
  else
    echo "⚠️  文件不存在: $file"
  fi
done

echo "==============================================="
echo "✨ 翻译任务完成！"
echo "==============================================="