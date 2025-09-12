"""
内容处理器 - 保护专有名词、URL和格式结构
"""

import re
import json
import logging
from typing import Dict, List, Tuple, Optional
from pathlib import Path


class ContentProcessor:
    """内容处理器 - 负责内容的保护和恢复"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        初始化处理器
        
        Args:
            config_path: 配置文件路径
        """
        self.logger = logging.getLogger(__name__)
        self.protected_items = {}  # 存储被保护的内容
        self.protection_counter = 0
        
        # 加载配置
        self._load_config(config_path)
        
    def _load_config(self, config_path: Optional[str] = None) -> None:
        """加载配置文件"""
        if config_path and Path(config_path).exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.protected_terms = config.get('protected_terms', [])
                    self.custom_patterns = config.get('custom_patterns', {})
            except Exception as e:
                self.logger.warning(f"加载配置文件失败: {e}")
                self._load_default_config()
        else:
            self._load_default_config()
    
    def _load_default_config(self) -> None:
        """加载默认配置"""
        self.protected_terms = [
            # 基础技术术语
            'Claude', 'ChatGPT', 'GPT', 'API', 'CLI', 'JSON', 'XML', 'HTML', 'CSS', 'JavaScript',
            'TypeScript', 'Python', 'Node.js', 'npm', 'yarn', 'pip', 'git', 'GitHub', 'GitLab',
            
            # 框架和工具
            'VuePress', 'Vue.js', 'React', 'Angular', 'Next.js', 'Nuxt.js', 'Express', 'FastAPI',
            'Django', 'Flask', 'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP',
            
            # Claude Code相关
            'MCP', 'MCPs', 'claude.ai', 'Anthropic', 'Sonnet', 'Haiku', 'Opus',
            
            # 其他常见术语
            'OAuth', 'JWT', 'REST', 'GraphQL', 'WebSocket', 'HTTP', 'HTTPS', 'SSL', 'TLS',
            'SQL', 'NoSQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis'
        ]
        
        self.custom_patterns = {
            # 特殊模式
            'version_numbers': r'\d+\.\d+\.\d+',
            'file_extensions': r'\.\w{2,4}',
            'environment_vars': r'\$\{[^}]+\}|\$\w+'
        }
    
    def _generate_placeholder(self, content_type: str) -> str:
        """生成占位符"""
        self.protection_counter += 1
        return f"__PROTECTED_{content_type}_{self.protection_counter}__"
    
    def protect_content(self, content: str) -> str:
        """
        保护内容中不应翻译的部分
        
        Args:
            content: 原始内容
            
        Returns:
            保护后的内容
        """
        self.protected_items.clear()
        self.protection_counter = 0
        
        # 1. 保护代码块
        content = self._protect_code_blocks(content)
        
        # 2. 保护URLs
        content = self._protect_urls(content)
        
        # 3. 保护HTML标签
        content = self._protect_html_tags(content)
        
        # 4. 保护专有名词
        content = self._protect_terms(content)
        
        # 5. 保护frontmatter
        content = self._protect_frontmatter(content)
        
        # 6. 保护内联代码
        content = self._protect_inline_code(content)
        
        # 7. 保护文件路径和扩展名
        content = self._protect_file_paths(content)
        
        self.logger.info(f"保护了 {len(self.protected_items)} 个内容项")
        return content
    
    def restore_content(self, content: str) -> str:
        """
        恢复被保护的内容
        
        Args:
            content: 处理后的内容
            
        Returns:
            恢复后的内容
        """
        for placeholder, original in self.protected_items.items():
            content = content.replace(placeholder, original)
        
        self.logger.info(f"恢复了 {len(self.protected_items)} 个内容项")
        return content
    
    def _protect_code_blocks(self, content: str) -> str:
        """保护代码块"""
        pattern = r'```[\s\S]*?```'
        
        def replace_code_block(match):
            placeholder = self._generate_placeholder("CODE_BLOCK")
            self.protected_items[placeholder] = match.group(0)
            return placeholder
            
        return re.sub(pattern, replace_code_block, content)
    
    def _protect_urls(self, content: str) -> str:
        """保护URLs"""
        # 匹配http(s)链接
        url_pattern = r'https?://[^\s)]+[^\s.,)]'
        
        def replace_url(match):
            placeholder = self._generate_placeholder("URL")
            self.protected_items[placeholder] = match.group(0)
            return placeholder
            
        content = re.sub(url_pattern, replace_url, content)
        
        # 保护markdown链接中的URL部分
        md_link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_md_link(match):
            text, url = match.groups()
            url_placeholder = self._generate_placeholder("URL")
            self.protected_items[url_placeholder] = url
            return f'[{text}]({url_placeholder})'
            
        return re.sub(md_link_pattern, replace_md_link, content)
    
    def _protect_html_tags(self, content: str) -> str:
        """保护HTML标签"""
        # 匹配完整的HTML标签
        html_pattern = r'<[^>]+>'
        
        def replace_html(match):
            placeholder = self._generate_placeholder("HTML")
            self.protected_items[placeholder] = match.group(0)
            return placeholder
            
        return re.sub(html_pattern, replace_html, content)
    
    def _protect_terms(self, content: str) -> str:
        """保护专有名词"""
        for term in self.protected_terms:
            # 使用单词边界确保精确匹配
            pattern = rf'\b{re.escape(term)}\b'
            
            def replace_term(match):
                placeholder = self._generate_placeholder("TERM")
                self.protected_items[placeholder] = match.group(0)
                return placeholder
                
            content = re.sub(pattern, replace_term, content, flags=re.IGNORECASE)
        
        # 保护自定义模式
        for pattern_name, pattern in self.custom_patterns.items():
            def replace_custom(match):
                placeholder = self._generate_placeholder(f"CUSTOM_{pattern_name.upper()}")
                self.protected_items[placeholder] = match.group(0)
                return placeholder
                
            content = re.sub(pattern, replace_custom, content)
            
        return content
    
    def _protect_frontmatter(self, content: str) -> str:
        """保护frontmatter（除了title字段）"""
        frontmatter_pattern = r'^---\n(.*?)\n---\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)
        
        if match:
            frontmatter_content = match.group(1)
            lines = frontmatter_content.split('\n')
            protected_lines = []
            
            for line in lines:
                # 只保护非title字段
                if line.strip() and not line.strip().startswith('title:'):
                    placeholder = self._generate_placeholder("FRONTMATTER_LINE")
                    self.protected_items[placeholder] = line
                    protected_lines.append(placeholder)
                else:
                    protected_lines.append(line)
            
            protected_frontmatter = '---\n' + '\n'.join(protected_lines) + '\n---\n'
            return content.replace(match.group(0), protected_frontmatter)
            
        return content
    
    def _protect_inline_code(self, content: str) -> str:
        """保护内联代码"""
        # 匹配单个反引号包围的内容
        inline_code_pattern = r'`([^`]+)`'
        
        def replace_inline_code(match):
            placeholder = self._generate_placeholder("INLINE_CODE")
            self.protected_items[placeholder] = match.group(0)
            return placeholder
            
        return re.sub(inline_code_pattern, replace_inline_code, content)
    
    def _protect_file_paths(self, content: str) -> str:
        """保护文件路径"""
        # 匹配类似文件路径的模式
        file_path_patterns = [
            r'/[a-zA-Z0-9._/-]+\.[a-zA-Z0-9]{1,4}',  # Unix路径
            r'[a-zA-Z]:\\[a-zA-Z0-9._\\-]+\.[a-zA-Z0-9]{1,4}',  # Windows路径
            r'\./[a-zA-Z0-9._/-]+',  # 相对路径
            r'[a-zA-Z0-9._-]+\.(js|ts|py|md|json|yml|yaml|xml|html|css)(?!\w)',  # 文件名
        ]
        
        for pattern in file_path_patterns:
            def replace_path(match):
                placeholder = self._generate_placeholder("FILE_PATH")
                self.protected_items[placeholder] = match.group(0)
                return placeholder
                
            content = re.sub(pattern, replace_path, content)
            
        return content
    
    def get_protection_stats(self) -> Dict[str, int]:
        """获取保护统计信息"""
        stats = {}
        for placeholder in self.protected_items.keys():
            content_type = placeholder.split('_')[2]  # 提取类型
            stats[content_type] = stats.get(content_type, 0) + 1
        
        return stats
    
    def should_translate(self, content: str) -> Tuple[bool, str]:
        """
        判断内容是否需要翻译
        
        Returns:
            (需要翻译, 原因)
        """
        # 检查中文比例
        chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
        total_chars = len(content.strip())
        
        if total_chars == 0:
            return False, "内容为空"
            
        chinese_ratio = chinese_chars / total_chars
        
        if chinese_ratio > 0.3:
            return False, f"中文比例过高: {chinese_ratio:.2%}"
        
        # 检查内容长度
        if total_chars > 100000:  # 100KB
            return False, "文件过大，需要分段处理"
            
        if total_chars < 10:
            return False, "内容过短"
        
        return True, "可以翻译"