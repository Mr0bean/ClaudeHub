#!/usr/bin/env python3

"""
高并发文档翻译工具 - 使用 Claude Code CLI
支持多种翻译策略，指定使用 Sonnet 模型
"""

import os
import sys
import json
import asyncio
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import re
from datetime import datetime

# 配置
@dataclass
class TranslatorConfig:
    """翻译器配置"""
    model: str = "claude-3-5-sonnet-20241022"  # 指定 Sonnet 模型
    max_concurrency: int = 5  # 最大并发数
    retry_attempts: int = 3  # 重试次数
    retry_delay: float = 2.0  # 重试延迟（秒）
    timeout: int = 60  # 命令超时（秒）
    chunk_size: int = 3000  # 分块大小（字符）
    
    # 不翻译的术语
    preserve_terms: List[str] = None
    
    # 常用翻译映射
    translation_map: Dict[str, str] = None
    
    def __post_init__(self):
        if self.preserve_terms is None:
            self.preserve_terms = [
                'Claude Code', 'Claude', 'Anthropic', 'API', 'MCP', 'CLI',
                'GitHub', 'npm', 'VS Code', 'Git', 'Bash', 'Python', 'JavaScript',
                'TypeScript', 'React', 'Vue', 'VuePress', 'Markdown', 'YAML',
                'JSON', 'XML', 'HTML', 'CSS', 'SQL', 'GraphQL', 'REST', 'WebSocket',
                'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'Linux', 'macOS', 'Windows',
                'Sonnet', 'Opus', 'Haiku', 'token', 'prompt', 'context window'
            ]
        
        if self.translation_map is None:
            self.translation_map = {
                'Installation': '安装',
                'Configuration': '配置',
                'Tutorial': '教程',
                'Overview': '概述',
                'Features': '功能特性',
                'Requirements': '要求',
                'Setup': '设置',
                'Usage': '使用方法',
                'Examples': '示例',
                'Documentation': '文档',
                'Support': '支持',
                'FAQ': '常见问题',
                'Changelog': '更新日志',
                'Getting Started': '快速开始',
                'Advanced': '高级',
                'Troubleshooting': '故障排除',
                'Best Practices': '最佳实践',
                'Performance': '性能',
                'Security': '安全',
                'Testing': '测试',
                'Deployment': '部署',
                'See Also': '另见',
                'Author': '作者',
                'References': '参考',
                'Prerequisites': '前置要求',
                'Monitor': '监控',
                'Debug': '调试',
                'Optimize': '优化',
                'Scale': '扩展',
                'Maintain': '维护'
            }


class ClaudeTranslator:
    """使用 Claude Code CLI 的翻译器"""
    
    def __init__(self, config: TranslatorConfig = None):
        self.config = config or TranslatorConfig()
        self.stats = {
            'total': 0,
            'completed': 0,
            'failed': 0,
            'skipped': 0,
            'start_time': time.time()
        }
        self.failed_files = {}
        
    def translate_with_claude(self, text: str, context: Dict = None) -> str:
        """使用 Claude Code CLI 翻译文本"""
        context = context or {}
        prompt = self._build_prompt(text, context)
        
        # 构建 Claude Code 命令
        cmd = [
            'claude',
            '--model', self.config.model,
            '--no-cache'
        ]
        
        try:
            # 执行命令
            result = subprocess.run(
                cmd,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=self.config.timeout
            )
            
            if result.returncode != 0:
                raise Exception(f"Claude CLI 返回错误: {result.stderr}")
            
            return self._extract_translation(result.stdout)
            
        except subprocess.TimeoutExpired:
            raise Exception(f"翻译超时 ({self.config.timeout}秒)")
        except Exception as e:
            raise Exception(f"翻译失败: {str(e)}")
    
    def _build_prompt(self, text: str, context: Dict) -> str:
        """构建翻译提示词"""
        file_type = context.get('file_type', 'markdown')
        strategy = context.get('strategy', 'smart')
        include_glossary = context.get('include_glossary', True)
        
        prompt = f"""请将以下{file_type}文档从英文翻译成中文。

重要规则：
1. 保留所有markdown格式，包括：
   - 标题格式 (#, ##, ###)
   - 列表格式 (-, *, 1.)
   - 代码块 (```)
   - 行内代码 (`)
   - 链接 [text](url)
   - 图片 ![alt](url)
   - 表格
   - 引用 (>)
   - 分割线 (---)
   - HTML标签和内联样式

2. 不要翻译以下内容：
   - 代码块中的所有代码
   - 行内代码
   - 技术术语：{', '.join(self.config.preserve_terms[:20])}
   - 产品名称和品牌
   - 文件路径和URL
   - 作者名字和GitHub用户名
   
3. 使用自然流畅的中文，适合程序员阅读

4. 保持原文的语气和风格

5. 只返回翻译后的内容，不要添加任何额外的解释或说明
"""

        if include_glossary and self.config.translation_map:
            prompt += "\n常用翻译参考：\n"
            for en, zh in list(self.config.translation_map.items())[:20]:
                prompt += f'- "{en}" → "{zh}"\n'
        
        prompt += f"""
原文：
---
{text}
---

翻译后的中文："""
        
        return prompt
    
    def _extract_translation(self, response: str) -> str:
        """从响应中提取翻译内容"""
        translation = response.strip()
        
        # 移除可能的额外标记
        markers = ['翻译：', '译文：', '翻译后的中文：', 'Translation:', '---']
        for marker in markers:
            if marker in translation:
                parts = translation.split(marker)
                if len(parts) > 1:
                    translation = parts[-1].strip()
        
        return translation
    
    def translate_file(self, file_path: Path, output_path: Path = None, 
                      strategy: str = 'smart', overwrite: bool = False) -> bool:
        """翻译单个文件"""
        try:
            # 读取文件
            content = file_path.read_text(encoding='utf-8')
            
            # 检查是否已经是中文
            if not overwrite and self._is_chinese(content):
                print(f"⏭️  跳过已翻译: {file_path.name}")
                self.stats['skipped'] += 1
                return True
            
            # 根据策略选择翻译方法
            if strategy == 'full':
                translated = self._translate_full(content, file_path)
            elif strategy == 'chunked':
                translated = self._translate_chunked(content, file_path)
            elif strategy == 'smart':
                translated = self._translate_smart(content, file_path)
            elif strategy == 'incremental':
                translated = self._translate_incremental(content, file_path)
            else:
                raise ValueError(f"未知策略: {strategy}")
            
            # 保存翻译结果
            output = output_path or file_path
            output.write_text(translated, encoding='utf-8')
            
            return True
            
        except Exception as e:
            self.failed_files[str(file_path)] = str(e)
            return False
    
    def _translate_full(self, content: str, file_path: Path) -> str:
        """完整文档翻译"""
        return self.translate_with_claude(content, {
            'file_type': 'markdown',
            'strategy': 'full',
            'include_glossary': True
        })
    
    def _translate_chunked(self, content: str, file_path: Path) -> str:
        """分块翻译"""
        chunks = self._split_into_chunks(content)
        translated_chunks = []
        
        for i, chunk in enumerate(chunks, 1):
            print(f"  翻译块 {i}/{len(chunks)}...")
            translated = self.translate_with_claude(chunk, {
                'file_type': 'markdown',
                'strategy': 'chunked',
                'include_glossary': i == 1  # 只在第一块包含词汇表
            })
            translated_chunks.append(translated)
        
        return '\n\n'.join(translated_chunks)
    
    def _translate_smart(self, content: str, file_path: Path) -> str:
        """智能翻译 - 保护特定内容"""
        # 提取需要保护的内容
        protected_content = self._extract_protected_content(content)
        
        # 替换为占位符
        processed = content
        placeholders = {}
        for i, (pattern, match) in enumerate(protected_content):
            placeholder = f"__PROTECTED_{i}__"
            placeholders[placeholder] = match
            processed = processed.replace(match, placeholder)
        
        # 翻译处理后的内容
        translated = self.translate_with_claude(processed, {
            'file_type': 'markdown',
            'strategy': 'smart',
            'include_glossary': True
        })
        
        # 恢复保护的内容
        for placeholder, original in placeholders.items():
            translated = translated.replace(placeholder, original)
        
        return translated
    
    def _translate_incremental(self, content: str, file_path: Path) -> str:
        """增量翻译 - 只翻译英文部分"""
        lines = content.split('\n')
        translated_lines = []
        
        current_block = []
        is_code_block = False
        
        for line in lines:
            # 检测代码块
            if line.strip().startswith('```'):
                if current_block and not is_code_block:
                    # 翻译累积的非代码内容
                    block_text = '\n'.join(current_block)
                    if not self._is_chinese(block_text):
                        block_text = self.translate_with_claude(block_text, {
                            'file_type': 'markdown',
                            'strategy': 'incremental'
                        })
                    translated_lines.append(block_text)
                    current_block = []
                
                is_code_block = not is_code_block
                translated_lines.append(line)
            elif is_code_block:
                # 代码块内容不翻译
                translated_lines.append(line)
            else:
                current_block.append(line)
        
        # 处理最后的块
        if current_block:
            block_text = '\n'.join(current_block)
            if not self._is_chinese(block_text):
                block_text = self.translate_with_claude(block_text, {
                    'file_type': 'markdown',
                    'strategy': 'incremental'
                })
            translated_lines.append(block_text)
        
        return '\n'.join(translated_lines)
    
    def _split_into_chunks(self, content: str) -> List[str]:
        """将内容分成块"""
        chunks = []
        lines = content.split('\n')
        current_chunk = []
        current_size = 0
        
        for line in lines:
            line_size = len(line)
            
            # 如果添加这行会超过块大小，先保存当前块
            if current_size + line_size > self.config.chunk_size and current_chunk:
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
            
            current_chunk.append(line)
            current_size += line_size
        
        # 保存最后一块
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def _extract_protected_content(self, content: str) -> List[Tuple[str, str]]:
        """提取需要保护的内容"""
        protected = []
        
        # 保护代码块
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        for block in code_blocks:
            protected.append(('code_block', block))
        
        # 保护行内代码
        inline_code = re.findall(r'`[^`]+`', content)
        for code in inline_code:
            protected.append(('inline_code', code))
        
        # 保护 frontmatter
        frontmatter = re.findall(r'^---[\s\S]*?^---', content, re.MULTILINE)
        for fm in frontmatter:
            protected.append(('frontmatter', fm))
        
        return protected
    
    def _is_chinese(self, text: str) -> bool:
        """检测文本是否主要是中文"""
        chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', text))
        total_chars = len(re.sub(r'\s', '', text))
        
        if total_chars == 0:
            return False
        
        return (chinese_chars / total_chars) > 0.3
    
    def translate_files_parallel(self, files: List[Path], 
                                strategy: str = 'smart',
                                output_dir: Path = None,
                                overwrite: bool = False) -> None:
        """并发翻译多个文件"""
        self.stats['total'] = len(files)
        self.stats['start_time'] = time.time()
        
        print(f"\n🚀 开始翻译 {len(files)} 个文件")
        print(f"📋 策略: {strategy}")
        print(f"⚡ 并发数: {self.config.max_concurrency}")
        print(f"🤖 模型: {self.config.model}")
        print("")
        
        with ThreadPoolExecutor(max_workers=self.config.max_concurrency) as executor:
            # 提交所有任务
            future_to_file = {}
            for file_path in files:
                output_path = None
                if output_dir:
                    output_path = output_dir / file_path.name
                
                future = executor.submit(
                    self.translate_file,
                    file_path,
                    output_path,
                    strategy,
                    overwrite
                )
                future_to_file[future] = file_path
            
            # 处理完成的任务
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    success = future.result()
                    if success:
                        self.stats['completed'] += 1
                        print(f"✅ [{self.stats['completed']}/{self.stats['total']}] {file_path.name}")
                    else:
                        self.stats['failed'] += 1
                        error = self.failed_files.get(str(file_path), "未知错误")
                        print(f"❌ [{self.stats['completed'] + self.stats['failed']}/{self.stats['total']}] {file_path.name}: {error}")
                except Exception as e:
                    self.stats['failed'] += 1
                    print(f"❌ {file_path.name}: {str(e)}")
        
        self._print_stats()
    
    def _print_stats(self):
        """打印统计信息"""
        duration = time.time() - self.stats['start_time']
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        
        print("\n" + "=" * 50)
        print("📊 翻译统计")
        print("=" * 50)
        print(f"✅ 成功: {self.stats['completed']}")
        print(f"❌ 失败: {self.stats['failed']}")
        print(f"⏭️  跳过: {self.stats['skipped']}")
        print(f"⏱️  耗时: {minutes}分{seconds}秒")
        
        if self.stats['completed'] > 0:
            avg_time = duration / self.stats['completed']
            print(f"⚡ 平均: {avg_time:.2f}秒/文件")
        
        if self.failed_files:
            print("\n❌ 失败详情:")
            for file_path, error in self.failed_files.items():
                print(f"  - {Path(file_path).name}: {error}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='高并发文档翻译工具 - 使用 Claude Code CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
策略说明:
  full        - 完整文档翻译，适合小文件
  chunked     - 分块翻译，适合大文件
  smart       - 智能翻译，自动保护代码块等内容
  incremental - 增量翻译，只翻译英文部分

示例:
  # 翻译单个文件
  python claude-translator.py README.md
  
  # 并发翻译目录中的所有markdown文件
  python claude-translator.py ./docs --pattern "*.md" --concurrency 10
  
  # 使用智能翻译策略，输出到新目录
  python claude-translator.py ./docs --strategy smart --output ./docs_zh
  
  # 覆盖已有翻译
  python claude-translator.py ./docs --overwrite --strategy incremental
        """
    )
    
    parser.add_argument('path', help='要翻译的文件或目录')
    parser.add_argument('--strategy', choices=['full', 'chunked', 'smart', 'incremental'],
                       default='smart', help='翻译策略 (默认: smart)')
    parser.add_argument('--concurrency', type=int, default=5,
                       help='最大并发数 (默认: 5)')
    parser.add_argument('--output', type=str, help='输出目录')
    parser.add_argument('--overwrite', action='store_true',
                       help='覆盖已翻译的文件')
    parser.add_argument('--pattern', default='*.md',
                       help='文件匹配模式 (默认: *.md)')
    parser.add_argument('--model', default='claude-3-5-sonnet-20241022',
                       help='Claude 模型 (默认: claude-3-5-sonnet-20241022)')
    parser.add_argument('--chunk-size', type=int, default=3000,
                       help='分块大小 (默认: 3000字符)')
    parser.add_argument('--timeout', type=int, default=60,
                       help='命令超时秒数 (默认: 60)')
    
    args = parser.parse_args()
    
    # 创建配置
    config = TranslatorConfig(
        model=args.model,
        max_concurrency=args.concurrency,
        chunk_size=args.chunk_size,
        timeout=args.timeout
    )
    
    # 创建翻译器
    translator = ClaudeTranslator(config)
    
    # 处理路径
    target_path = Path(args.path)
    if not target_path.exists():
        print(f"❌ 路径不存在: {target_path}")
        sys.exit(1)
    
    # 收集文件
    files = []
    if target_path.is_file():
        files = [target_path]
    else:
        files = list(target_path.glob(args.pattern))
    
    if not files:
        print(f"⚠️  没有找到匹配的文件: {args.pattern}")
        sys.exit(0)
    
    # 处理输出目录
    output_dir = None
    if args.output:
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # 开始翻译
    try:
        translator.translate_files_parallel(
            files,
            strategy=args.strategy,
            output_dir=output_dir,
            overwrite=args.overwrite
        )
        print("\n✨ 翻译完成!")
    except KeyboardInterrupt:
        print("\n⚠️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()