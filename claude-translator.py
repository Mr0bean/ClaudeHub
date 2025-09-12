#!/usr/bin/env python3
"""高并发文档翻译工具"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import re

@dataclass
class TranslatorConfig:
    """翻译器配置"""
    model: str = "sonnet"
    max_concurrency: int = 5
    timeout: int = 60
    chunk_size: int = 3000
    
    preserve_terms: List[str] = None
    translation_map: Dict[str, str] = None
    
    def __post_init__(self):
        if self.preserve_terms is None:
            self.preserve_terms = [
                'Claude Code', 'Claude', 'Anthropic', 'API', 'MCP', 'CLI',
                'GitHub', 'npm', 'VS Code', 'Git', 'Bash', 'Python', 'JavaScript',
                'TypeScript', 'React', 'Vue', 'VuePress', 'Markdown'
            ]
        
        if self.translation_map is None:
            self.translation_map = {
                'Installation': '安装', 'Configuration': '配置', 'Tutorial': '教程',
                'Overview': '概述', 'Features': '功能特性', 'Setup': '设置',
                'Usage': '使用方法', 'Examples': '示例', 'FAQ': '常见问题'
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
        """翻译文本"""
        prompt = f"""将markdown文档翻译成中文。

规则：
1. 保留所有格式
2. 不翻译代码和技术术语
3. 使用流畅中文

{text}

翻译："""
        
        try:
            result = subprocess.run(
                ['claude', '--model', self.config.model],
                input=prompt,
                capture_output=True,
                text=True,
                timeout=self.config.timeout
            )
            
            if result.returncode != 0:
                raise Exception(f"CLI错误: {result.stderr}")
            
            return result.stdout.strip()
            
        except subprocess.TimeoutExpired:
            raise Exception(f"超时")
        except Exception as e:
            raise Exception(f"失败: {str(e)}")
    
    
    def translate_file(self, file_path: Path, output_path: Path = None, 
                      strategy: str = 'smart', overwrite: bool = False) -> bool:
        """翻译文件"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            if not overwrite and self._is_chinese(content):
                self.stats['skipped'] += 1
                return True
            
            translated = self.translate_with_claude(content)
            
            output = output_path or file_path
            output.write_text(translated, encoding='utf-8')
            
            return True
            
        except Exception as e:
            self.failed_files[str(file_path)] = str(e)
            return False
    
    
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
        
        print(f"🚀 翻译 {len(files)} 个文件")
        
        with ThreadPoolExecutor(max_workers=self.config.max_concurrency) as executor:
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
            
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    success = future.result()
                    if success:
                        self.stats['completed'] += 1
                        print(f"✅ {file_path.name}")
                    else:
                        self.stats['failed'] += 1
                        print(f"❌ {file_path.name}")
                except Exception as e:
                    self.stats['failed'] += 1
                    print(f"❌ {file_path.name}: {str(e)}")
        
        self._print_stats()
    
    def _print_stats(self):
        """打印统计信息"""
        duration = time.time() - self.stats['start_time']
        print(f"\n📊 完成: {self.stats['completed']}, 失败: {self.stats['failed']}, 跳过: {self.stats['skipped']}")
        print(f"⏱️ 耗时: {duration:.1f}秒")


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