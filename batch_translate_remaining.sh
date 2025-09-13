#!/bin/bash

# 批量翻译剩余页面脚本

echo "开始批量翻译剩余页面..."
echo "================================"

# FAQ页面 - 最重要
echo "[1/7] 翻译 FAQ 页面..."
python3 translate-file.py final-site/docs/faq.md

# Claude Code Changelog
echo "[2/7] 翻译 Claude Code Changelog..."
python3 translate-file.py final-site/docs/claude-code-changelog.md

# Claude News
echo "[3/7] 翻译 Claude News..."
python3 translate-file.py final-site/docs/claude-news.md

# Agent-First Design
echo "[4/7] 翻译 Agent-First Design..."
python3 translate-file.py final-site/docs/mechanics-agent-first-design.md

# Context7 MCP
echo "[5/7] 翻译 Context7 MCP..."
python3 translate-file.py final-site/docs/claude-code-mcps-context7-mcp.md

# 完成 Privacy Policy 翻译
echo "[6/7] 完成 Privacy Policy 翻译..."
python3 translate-file.py final-site/docs/privacy-policy.md

# 完成 Rev the Engine 翻译
echo "[7/7] 完成 Rev the Engine 翻译..."
python3 translate-file.py final-site/docs/mechanics-rev-the-engine.md

echo "================================"
echo "批量翻译完成！"
echo ""
echo "请运行以下命令验证翻译状态："
echo "python3 check_translation_status.py"