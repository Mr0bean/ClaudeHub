#!/bin/bash
# 翻译剩余的文件

cd /Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/translate

echo "翻译 claude-code-changelog.md..."
python main_translator.py file ../final-site/docs/claude-code-changelog.md --force
sleep 3

echo "翻译 claude-code-mcps-claudia.md..."
python main_translator.py file ../final-site/docs/claude-code-mcps-claudia.md --force
sleep 3

echo "翻译 claude-code-mcps-context7-mcp.md..."
python main_translator.py file ../final-site/docs/claude-code-mcps-context7-mcp.md --force
sleep 3

echo "翻译 claude-news.md..."
python main_translator.py file ../final-site/docs/claude-news.md --force
sleep 3

echo "翻译 configuration.md..."
python main_translator.py file ../final-site/docs/configuration.md --force
sleep 3

echo "翻译 disclaimer.md..."
python main_translator.py file ../final-site/docs/disclaimer.md --force
sleep 3

echo "翻译 faq.md..."
python main_translator.py file ../final-site/docs/faq.md --force
sleep 3

echo "翻译 install-claude-code.md..."
python main_translator.py file ../final-site/docs/install-claude-code.md --force
sleep 3

echo "翻译 mechanics-agent-engineering.md..."
python main_translator.py file ../final-site/docs/mechanics-agent-engineering.md --force
sleep 3

echo "翻译 mechanics-agent-first-design.md..."
python main_translator.py file ../final-site/docs/mechanics-agent-first-design.md --force
sleep 3

echo "翻译 mechanics-context-window-constraints-as-training.md..."
python main_translator.py file ../final-site/docs/mechanics-context-window-constraints-as-training.md --force
sleep 3

echo "翻译 mechanics-rev-the-engine.md..."
python main_translator.py file ../final-site/docs/mechanics-rev-the-engine.md --force
sleep 3

echo "翻译 privacy-policy.md..."
python main_translator.py file ../final-site/docs/privacy-policy.md --force
sleep 3

echo "✅ 所有文件翻译完成!"
