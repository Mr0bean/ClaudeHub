#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix mixed Chinese-English translation in claude-code-changelog.md
"""

import re

def fix_changelog_translation():
    """Fix the mixed translation in changelog"""
    
    with open('final-site/docs/claude-code-changelog.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix mixed language entries
    translations = {
        # Technical terms
        '现在 验证': '现在验证',
        '现在 supports': '现在支持',
        '现在 proactively': '现在主动',
        '现在 validates': '现在验证',
        '现在 允许': '现在允许',
        '命令 现在': '命令现在',
        'tool 由': 'tool 由',
        'issues 后台': '问题与后台',
        'tokens 现在': 'tokens 现在',
        'Bash 进程': 'Bash 进程',
        
        # Common English words that should be translated
        'supports WezTerm': '支持 WezTerm',
        'OAuth tokens': 'OAuth 令牌',
        'proactively refresh before expiration': '主动在过期前刷新',
        'reliability issues': '可靠性问题',
        'permission rule syntax and suggests corrections': '权限规则语法并建议修正',
        'global endpoint support': '全局端点支持',
        'custom tools': '自定义工具',
        'as callbacks': '作为回调',
        'from clipboard': '从剪贴板',
        'shortcut': '快捷方式',
        'bypass proxy for specified hostnames and IPs': '绕过指定主机名和IP的代理',
        'take effect immediately': '立即生效',
        'no restart needed': '无需重启',
        'causing': '导致',
        'now includes': '现在包括',
        'incorrect usage tracking': '不正确的使用跟踪',
        'for controlling model aliases': '用于控制模型别名',
        'updated default': '更新了默认',
        'help users self-debug context issues': '帮助用户自助调试上下文问题',
        
        # Version-specific fixes
        'SDK: 添加了 通过以下方式支持部分消息流 --include-partial-messages CLI 标志':
            'SDK: 添加了通过 --include-partial-messages CLI 标志支持部分消息流',
        'Windows: 修复了 路径权限匹配以一致使用 POSIX 格式':
            'Windows: 修复了路径权限匹配以一致使用 POSIX 格式',
        'Settings: `/doctor` 现在 validates permission rule syntax and suggests corrections':
            'Settings: `/doctor` 现在验证权限规则语法并建议修正',
        'Vertex: 为支持的模型添加全局端点支持':
            'Vertex: 为支持的模型添加了全局端点支持',
        'SDK: Add custom tools 作为回调':
            'SDK: 添加了自定义工具作为回调',
        'Windows: Add alt + v 从剪贴板粘贴图像的快捷方式':
            'Windows: 添加了 alt + v 从剪贴板粘贴图像的快捷方式',
        '设置文件更改立即生效 - 无需重启':
            '设置文件更改立即生效 - 无需重启',
        'Status line input 现在 includes `exceeds_200k_tokens`':
            'Status line 输入现在包括 `exceeds_200k_tokens`',
        '修复了 不正确的使用跟踪在 /cost.':
            '修复了 /cost 中不正确的使用跟踪',
        '引入了 `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_OPUS_MODEL` 用于控制模型别名 opusplan, opus, and sonnet.':
            '引入了 `ANTHROPIC_DEFAULT_SONNET_MODEL` 和 `ANTHROPIC_DEFAULT_OPUS_MODEL` 用于控制模型别名 opusplan、opus 和 sonnet',
        'Bedrock: 更新了 默认 Sonnet 模型为 Sonnet 4':
            'Bedrock: 更新了默认 Sonnet 模型为 Sonnet 4',
        '添加了 /context 帮助用户自助调试上下文问题':
            '添加了 /context 帮助用户自助调试上下文问题',
        
        # Fix spacing issues
        'MCP: OAuth tokens 现在 proactively refresh before expiration':
            'MCP: OAuth 令牌现在主动在过期前刷新',
        '修复了 reliability issues 后台 Bash 进程':
            '修复了后台 Bash 进程的可靠性问题',
        '支持 NO\_PROXY 环境变量以绕过指定主机名和 IP 的代理':
            '支持 NO_PROXY 环境变量以绕过指定主机名和 IP 的代理',
        '修复了 issue 导致 "OAuth 身份验证当前不受支持"':
            '修复了导致 "OAuth 身份验证当前不受支持" 的问题',
            
        # Fix common patterns
        'now ': '现在',
        'add ': '添加了',
        'added ': '添加了',
        'fix ': '修复了',
        'fixed ': '修复了',
        'update ': '更新了',
        'updated ': '更新了',
        'improve ': '改进了',
        'improved ': '改进了',
        'support ': '支持',
        'include ': '包括',
        'includes ': '包括',
        'allow ': '允许',
        'allows ': '允许',
        'enable ': '启用',
        'enables ': '启用',
        
        # Technical improvements
        'performance improvements': '性能改进',
        'bug fixes': '错误修复',
        'stability improvements': '稳定性改进',
        'security enhancements': '安全增强',
        'compatibility updates': '兼容性更新',
        'feature additions': '功能添加',
        'usability improvements': '可用性改进',
        'error handling': '错误处理',
        'memory optimization': '内存优化',
        'speed optimization': '速度优化'
    }
    
    # Apply translations
    for en_text, zh_text in translations.items():
        content = content.replace(en_text, zh_text)
    
    # Clean up spacing issues
    content = re.sub(r'(\w) 现在 (\w)', r'\1现在\2', content)
    content = re.sub(r'现在 (\w)', r'现在\1', content)
    content = re.sub(r'添加了 (\w)', r'添加了\1', content)
    content = re.sub(r'修复了 (\w)', r'修复了\1', content)
    
    # Fix specific patterns
    content = re.sub(r'/(\w+) 现在', r'/\1 现在', content)
    content = re.sub(r'`(\w+)` 现在', r'`\1` 现在', content)
    
    with open('final-site/docs/claude-code-changelog.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed changelog translation issues")
    print("📄 File saved: final-site/docs/claude-code-changelog.md")

if __name__ == "__main__":
    fix_changelog_translation()