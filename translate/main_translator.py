#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主翻译脚本 - Claude Code CLI智能翻译系统
"""

import argparse
import json
import time
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Optional, Tuple

# 添加模块路径
sys.path.insert(0, str(Path(__file__).parent))

from core.cli_controller import ClaudeController
from core.content_processor import ContentProcessor
from core.validator import TranslationValidator
from utils.logger import TranslationLogger
from utils.file_utils import FileUtils


class SmartTranslator:
    """智能翻译器"""
    
    def __init__(self, config_path: Optional[str] = None):
        """初始化翻译器"""
        self.config = self._load_config(config_path)
        
        # 初始化组件
        self.claude = ClaudeController(
            model=self.config['translation']['model'],
            timeout=self.config['translation']['timeout'],
            max_retries=self.config['translation']['max_retries']
        )
        
        self.processor = ContentProcessor()
        self.validator = TranslationValidator()
        self.logger = TranslationLogger()
        
        # 统计信息
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'start_time': None,
            'end_time': None
        }
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict:
        """加载配置"""
        if config_path is None:
            config_path = Path(__file__).parent / "config" / "translation_config.json"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"加载配置失败: {e}")
            return self._default_config()
    
    def _default_config(self) -> Dict:
        """默认配置"""
        return {
            'translation': {
                'model': 'claude-3-sonnet-20240229',
                'timeout': 300,
                'max_retries': 3,
                'chinese_threshold': 0.3
            },
            'file_processing': {
                'backup_enabled': True,
                'exclude_patterns': ['**/node_modules/**', '**/.git/**']
            },
            'validation': {
                'enabled': True,
                'min_score': 70.0
            },
            'batch_processing': {
                'max_concurrent': 3,
                'stop_on_error': False
            }
        }
    
    def translate_file(self, file_path: str, force: bool = False) -> Tuple[bool, str]:
        """
        翻译单个文件
        
        Args:
            file_path: 文件路径
            force: 是否强制翻译
            
        Returns:
            (成功状态, 错误信息)
        """
        file_path = Path(file_path)
        start_time = time.time()
        
        self.logger.translation_start(str(file_path))
        
        try:
            # 读取文件
            content = FileUtils.read_file_safe(str(file_path))
            if content is None:
                return False, "无法读取文件"
            
            # 检查是否需要翻译
            if not force:
                should_translate, reason = self.processor.should_translate(content)
                if not should_translate:
                    self.logger.translation_skip(str(file_path), reason)
                    return False, reason
            
            # 保护内容
            protected_content = self.processor.protect_content(content)
            stats = self.processor.get_protection_stats()
            self.logger.protection_stats(stats)
            
            # 翻译
            translated = self.claude.translate_text(protected_content)
            if translated is None:
                return False, "翻译失败"
            
            # 恢复内容
            final_content = self.processor.restore_content(translated)
            
            # 验证翻译质量
            if self.config['validation']['enabled']:
                is_valid, errors = self.validator.validate_translation(content, final_content)
                score = self.validator.get_translation_score(content, final_content)
                
                self.logger.validation_result(str(file_path), is_valid, score, errors)
                
                if not is_valid and score < self.config['validation']['min_score']:
                    return False, f"翻译质量不达标 (评分: {score:.1f})"
            
            # 备份和保存
            if self.config['file_processing']['backup_enabled']:
                FileUtils.create_backup(str(file_path))
            
            success = FileUtils.write_file_safe(str(file_path), final_content)
            if not success:
                return False, "保存文件失败"
            
            duration = time.time() - start_time
            self.logger.translation_success(str(file_path), duration)
            
            return True, "翻译成功"
            
        except Exception as e:
            error_msg = f"翻译异常: {e}"
            self.logger.translation_failure(str(file_path), error_msg)
            return False, error_msg
    
    def translate_directory(self, 
                          directory: str, 
                          pattern: str = "**/*.md",
                          force: bool = False,
                          max_workers: int = None) -> Dict:
        """
        翻译目录下的文件
        
        Args:
            directory: 目录路径
            pattern: 文件模式
            force: 是否强制翻译
            max_workers: 最大并发数
            
        Returns:
            翻译结果统计
        """
        directory = Path(directory)
        if not directory.exists():
            raise ValueError(f"目录不存在: {directory}")
        
        # 查找文件
        files = list(directory.glob(pattern))
        exclude_patterns = self.config['file_processing']['exclude_patterns']
        
        # 过滤文件
        filtered_files = []
        for file_path in files:
            should_exclude = False
            for exclude in exclude_patterns:
                if file_path.match(exclude):
                    should_exclude = True
                    break
            if not should_exclude:
                filtered_files.append(file_path)
        
        if not filtered_files:
            self.logger.info("没有找到符合条件的文件")
            return self.stats
        
        # 初始化统计
        self.stats['total'] = len(filtered_files)
        self.stats['start_time'] = time.time()
        
        self.logger.batch_start(len(filtered_files))
        
        # 并发处理
        max_workers = max_workers or self.config['batch_processing']['max_concurrent']
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交任务
            future_to_file = {
                executor.submit(self.translate_file, str(file_path), force): file_path 
                for file_path in filtered_files
            }
            
            # 处理结果
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    success, message = future.result()
                    if success:
                        self.stats['success'] += 1
                    else:
                        if "跳过" in message:
                            self.stats['skipped'] += 1
                        else:
                            self.stats['failed'] += 1
                            
                except Exception as e:
                    self.stats['failed'] += 1
                    self.logger.translation_failure(str(file_path), str(e))
                    
                    if self.config['batch_processing']['stop_on_error']:
                        break
        
        # 完成统计
        self.stats['end_time'] = time.time()
        duration = self.stats['end_time'] - self.stats['start_time']
        
        self.logger.batch_complete(
            self.stats['success'], 
            self.stats['total'], 
            duration
        )
        
        return self.stats
    
    def get_summary(self) -> str:
        """获取翻译摘要"""
        if self.stats['total'] == 0:
            return "未执行翻译任务"
        
        success_rate = (self.stats['success'] / self.stats['total']) * 100
        duration = self.stats.get('end_time', time.time()) - self.stats.get('start_time', time.time())
        
        summary = f"""
翻译摘要：
=========
总文件数: {self.stats['total']}
成功: {self.stats['success']} ({success_rate:.1f}%)
失败: {self.stats['failed']}
跳过: {self.stats['skipped']}
耗时: {duration:.2f}秒
平均每文件: {duration / self.stats['total']:.2f}秒
"""
        return summary.strip()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Claude Code CLI智能翻译系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python main_translator.py file final-site/docs/README.md
  python main_translator.py dir final-site/docs --pattern "**/*.md"
  python main_translator.py dir final-site/docs --force --workers 2
        """
    )
    
    parser.add_argument(
        'mode', 
        choices=['file', 'dir'],
        help='翻译模式: file(单文件) 或 dir(目录)'
    )
    
    parser.add_argument(
        'path',
        help='文件或目录路径'
    )
    
    parser.add_argument(
        '--pattern',
        default='**/*.md',
        help='文件匹配模式 (默认: **/*.md)'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='强制翻译已有中文的文件'
    )
    
    parser.add_argument(
        '--workers',
        type=int,
        default=None,
        help='并发工作线程数'
    )
    
    parser.add_argument(
        '--config',
        help='配置文件路径'
    )
    
    args = parser.parse_args()
    
    try:
        # 初始化翻译器
        translator = SmartTranslator(args.config)
        
        if args.mode == 'file':
            # 单文件翻译
            success, message = translator.translate_file(args.path, args.force)
            print(f"{'✅' if success else '❌'} {message}")
            sys.exit(0 if success else 1)
            
        elif args.mode == 'dir':
            # 目录翻译
            stats = translator.translate_directory(
                args.path, 
                args.pattern, 
                args.force,
                args.workers
            )
            
            print(translator.get_summary())
            sys.exit(0 if stats['failed'] == 0 else 1)
            
    except KeyboardInterrupt:
        print("\n用户中断翻译")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()