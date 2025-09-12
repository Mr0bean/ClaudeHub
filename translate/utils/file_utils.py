"""
文件工具模块
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional, Dict, Any
import time
import hashlib


class FileUtils:
    """文件操作工具类"""
    
    @staticmethod
    def find_markdown_files(directory: str, 
                          exclude_patterns: List[str] = None) -> List[Path]:
        """
        查找目录下的Markdown文件
        
        Args:
            directory: 目录路径
            exclude_patterns: 排除模式列表
            
        Returns:
            Markdown文件路径列表
        """
        directory = Path(directory)
        if not directory.exists():
            return []
            
        exclude_patterns = exclude_patterns or [
            '**/node_modules/**',
            '**/.git/**',
            '**/.*/**'
        ]
        
        markdown_files = []
        for pattern in ['**/*.md', '**/*.markdown']:
            files = directory.glob(pattern)
            for file_path in files:
                # 检查是否应该排除
                should_exclude = False
                for exclude in exclude_patterns:
                    if file_path.match(exclude):
                        should_exclude = True
                        break
                        
                if not should_exclude:
                    markdown_files.append(file_path)
        
        return sorted(markdown_files)
    
    @staticmethod
    def read_file_safe(file_path: str, encoding: str = 'utf-8') -> Optional[str]:
        """
        安全读取文件
        
        Args:
            file_path: 文件路径
            encoding: 编码格式
            
        Returns:
            文件内容，失败时返回None
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except Exception as e:
            print(f"读取文件失败 {file_path}: {e}")
            return None
    
    @staticmethod
    def write_file_safe(file_path: str, 
                       content: str, 
                       encoding: str = 'utf-8',
                       backup: bool = True) -> bool:
        """
        安全写入文件
        
        Args:
            file_path: 文件路径
            content: 文件内容
            encoding: 编码格式
            backup: 是否创建备份
            
        Returns:
            是否成功
        """
        try:
            file_path = Path(file_path)
            
            # 创建备份
            if backup and file_path.exists():
                backup_path = file_path.with_suffix(f'.backup_{int(time.time())}')
                shutil.copy2(file_path, backup_path)
            
            # 确保目录存在
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入文件
            with open(file_path, 'w', encoding=encoding) as f:
                f.write(content)
                
            return True
        except Exception as e:
            print(f"写入文件失败 {file_path}: {e}")
            return False
    
    @staticmethod
    def get_file_info(file_path: str) -> Dict[str, Any]:
        """
        获取文件信息
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件信息字典
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            return {}
        
        stat = file_path.stat()
        
        return {
            'path': str(file_path),
            'name': file_path.name,
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'created': stat.st_ctime,
            'is_file': file_path.is_file(),
            'is_dir': file_path.is_dir(),
            'extension': file_path.suffix
        }
    
    @staticmethod
    def calculate_file_hash(file_path: str) -> Optional[str]:
        """
        计算文件哈希值
        
        Args:
            file_path: 文件路径
            
        Returns:
            MD5哈希值
        """
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                return hashlib.md5(content).hexdigest()
        except Exception:
            return None
    
    @staticmethod
    def is_file_modified(file_path: str, 
                        reference_time: float) -> bool:
        """
        检查文件是否在指定时间后被修改
        
        Args:
            file_path: 文件路径
            reference_time: 参考时间戳
            
        Returns:
            是否被修改
        """
        try:
            stat = Path(file_path).stat()
            return stat.st_mtime > reference_time
        except Exception:
            return False
    
    @staticmethod
    def create_backup(file_path: str, 
                     backup_dir: Optional[str] = None) -> Optional[str]:
        """
        创建文件备份
        
        Args:
            file_path: 源文件路径
            backup_dir: 备份目录，默认在同目录下
            
        Returns:
            备份文件路径
        """
        try:
            source = Path(file_path)
            if not source.exists():
                return None
            
            if backup_dir:
                backup_path = Path(backup_dir) / f"{source.stem}.backup_{int(time.time())}{source.suffix}"
            else:
                backup_path = source.with_suffix(f'.backup_{int(time.time())}{source.suffix}')
            
            # 确保备份目录存在
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(source, backup_path)
            return str(backup_path)
            
        except Exception as e:
            print(f"创建备份失败 {file_path}: {e}")
            return None
    
    @staticmethod
    def clean_old_backups(directory: str, 
                         max_age_days: int = 7,
                         pattern: str = "*.backup_*") -> int:
        """
        清理旧备份文件
        
        Args:
            directory: 目录路径
            max_age_days: 最大保留天数
            pattern: 备份文件模式
            
        Returns:
            删除的文件数量
        """
        try:
            directory = Path(directory)
            current_time = time.time()
            max_age_seconds = max_age_days * 24 * 3600
            
            deleted_count = 0
            for backup_file in directory.glob(pattern):
                if backup_file.is_file():
                    file_age = current_time - backup_file.stat().st_mtime
                    if file_age > max_age_seconds:
                        backup_file.unlink()
                        deleted_count += 1
                        
            return deleted_count
        except Exception:
            return 0
    
    @staticmethod 
    def ensure_directory(directory: str) -> bool:
        """
        确保目录存在
        
        Args:
            directory: 目录路径
            
        Returns:
            是否成功
        """
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_relative_path(file_path: str, base_path: str) -> str:
        """
        获取相对路径
        
        Args:
            file_path: 文件路径
            base_path: 基准路径
            
        Returns:
            相对路径
        """
        try:
            return str(Path(file_path).relative_to(Path(base_path)))
        except Exception:
            return str(Path(file_path))
    
    @staticmethod
    def filter_files_by_size(file_list: List[str], 
                           min_size: int = 0,
                           max_size: int = None) -> List[str]:
        """
        按文件大小过滤文件
        
        Args:
            file_list: 文件列表
            min_size: 最小大小(字节)
            max_size: 最大大小(字节)
            
        Returns:
            过滤后的文件列表
        """
        filtered = []
        for file_path in file_list:
            try:
                size = Path(file_path).stat().st_size
                if size >= min_size and (max_size is None or size <= max_size):
                    filtered.append(file_path)
            except Exception:
                continue
                
        return filtered