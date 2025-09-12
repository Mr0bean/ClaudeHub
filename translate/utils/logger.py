"""
日志配置模块
"""

import logging
import sys
from datetime import datetime
from pathlib import Path


def setup_logger(name: str = "translator", 
                log_level: str = "INFO",
                log_file: str = None,
                console_output: bool = True) -> logging.Logger:
    """
    设置日志记录器
    
    Args:
        name: 日志器名称
        log_level: 日志级别
        log_file: 日志文件路径
        console_output: 是否输出到控制台
        
    Returns:
        配置好的日志器
    """
    # 创建日志器
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # 清除已有处理器
    logger.handlers.clear()
    
    # 格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 控制台处理器
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # 文件处理器
    if log_file:
        # 确保日志目录存在
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        # 默认日志文件
        default_log = Path("translate/logs") / f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        default_log.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(default_log, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


class TranslationLogger:
    """翻译日志记录器"""
    
    def __init__(self, log_file: str = None):
        self.logger = setup_logger("translator", log_file=log_file)
        
    def info(self, message: str):
        """记录信息"""
        self.logger.info(message)
        
    def warning(self, message: str):
        """记录警告"""
        self.logger.warning(message)
        
    def error(self, message: str):
        """记录错误"""
        self.logger.error(message)
        
    def debug(self, message: str):
        """记录调试信息"""
        self.logger.debug(message)
        
    def translation_start(self, file_path: str):
        """记录翻译开始"""
        self.logger.info(f"🔄 开始翻译: {file_path}")
        
    def translation_success(self, file_path: str, duration: float = None):
        """记录翻译成功"""
        duration_str = f" ({duration:.2f}秒)" if duration else ""
        self.logger.info(f"✅ 翻译成功: {file_path}{duration_str}")
        
    def translation_failure(self, file_path: str, error: str):
        """记录翻译失败"""
        self.logger.error(f"❌ 翻译失败: {file_path} - {error}")
        
    def translation_skip(self, file_path: str, reason: str):
        """记录跳过翻译"""
        self.logger.info(f"⏭️  跳过翻译: {file_path} - {reason}")
        
    def batch_start(self, total_files: int):
        """记录批量翻译开始"""
        self.logger.info(f"🚀 开始批量翻译，共 {total_files} 个文件")
        
    def batch_complete(self, success_count: int, total_count: int, duration: float):
        """记录批量翻译完成"""
        success_rate = (success_count / total_count) * 100 if total_count > 0 else 0
        self.logger.info(f"🎉 批量翻译完成: {success_count}/{total_count} ({success_rate:.1f}%) 用时 {duration:.2f}秒")
        
    def protection_stats(self, stats: dict):
        """记录保护统计"""
        stats_str = ", ".join([f"{k}: {v}" for k, v in stats.items()])
        self.logger.debug(f"🛡️  内容保护统计: {stats_str}")
        
    def validation_result(self, file_path: str, is_valid: bool, score: float, errors: list):
        """记录验证结果"""
        if is_valid:
            self.logger.info(f"✅ 验证通过: {file_path} (评分: {score:.1f})")
        else:
            self.logger.warning(f"⚠️  验证失败: {file_path} (评分: {score:.1f}) - 错误: {len(errors)}个")