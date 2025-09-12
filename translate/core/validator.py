"""
翻译验证器 - 验证翻译质量和格式完整性
"""

import re
import logging
from typing import Dict, List, Tuple, Optional


class TranslationValidator:
    """翻译验证器"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def validate_translation(self, 
                           original: str, 
                           translated: str) -> Tuple[bool, List[str]]:
        """
        验证翻译质量
        
        Args:
            original: 原始内容
            translated: 翻译后内容
            
        Returns:
            (是否通过验证, 错误信息列表)
        """
        errors = []
        
        # 1. 基本结构验证
        structure_errors = self._validate_structure(original, translated)
        errors.extend(structure_errors)
        
        # 2. Markdown格式验证
        markdown_errors = self._validate_markdown(original, translated)
        errors.extend(markdown_errors)
        
        # 3. 链接验证
        link_errors = self._validate_links(original, translated)
        errors.extend(link_errors)
        
        # 4. 代码块验证
        code_errors = self._validate_code_blocks(original, translated)
        errors.extend(code_errors)
        
        # 5. HTML标签验证
        html_errors = self._validate_html_tags(original, translated)
        errors.extend(html_errors)
        
        # 6. 内容完整性验证
        content_errors = self._validate_content_completeness(original, translated)
        errors.extend(content_errors)
        
        is_valid = len(errors) == 0
        
        if is_valid:
            self.logger.info("翻译验证通过")
        else:
            self.logger.warning(f"翻译验证失败，发现 {len(errors)} 个问题")
            
        return is_valid, errors
    
    def _validate_structure(self, original: str, translated: str) -> List[str]:
        """验证基本结构"""
        errors = []
        
        # 检查是否为空
        if not translated.strip():
            errors.append("翻译结果为空")
            return errors
        
        # 检查长度是否合理（翻译后应该有一定长度变化）
        orig_len = len(original.strip())
        trans_len = len(translated.strip())
        
        if trans_len < orig_len * 0.3:
            errors.append(f"翻译长度过短: {trans_len}/{orig_len}")
        elif trans_len > orig_len * 3:
            errors.append(f"翻译长度过长: {trans_len}/{orig_len}")
        
        return errors
    
    def _validate_markdown(self, original: str, translated: str) -> List[str]:
        """验证Markdown格式"""
        errors = []
        
        # 检查标题数量
        orig_headers = re.findall(r'^#+\s+', original, re.MULTILINE)
        trans_headers = re.findall(r'^#+\s+', translated, re.MULTILINE)
        
        if len(orig_headers) != len(trans_headers):
            errors.append(f"标题数量不匹配: {len(orig_headers)} vs {len(trans_headers)}")
        
        # 检查列表项数量
        orig_lists = re.findall(r'^\s*[-*+]\s+', original, re.MULTILINE)
        trans_lists = re.findall(r'^\s*[-*+]\s+', translated, re.MULTILINE)
        
        if len(orig_lists) != len(trans_lists):
            errors.append(f"列表项数量不匹配: {len(orig_lists)} vs {len(trans_lists)}")
        
        # 检查编号列表
        orig_numbered = re.findall(r'^\s*\d+\.\s+', original, re.MULTILINE)
        trans_numbered = re.findall(r'^\s*\d+\.\s+', translated, re.MULTILINE)
        
        if len(orig_numbered) != len(trans_numbered):
            errors.append(f"编号列表项数量不匹配: {len(orig_numbered)} vs {len(trans_numbered)}")
        
        # 检查表格
        orig_tables = original.count('|')
        trans_tables = translated.count('|')
        
        if orig_tables > 0 and abs(orig_tables - trans_tables) > 2:
            errors.append(f"表格结构不匹配: {orig_tables} vs {trans_tables} 个'|'符号")
        
        return errors
    
    def _validate_links(self, original: str, translated: str) -> List[str]:
        """验证链接"""
        errors = []
        
        # 检查Markdown链接数量
        orig_md_links = len(re.findall(r'\[.*?\]\([^)]+\)', original))
        trans_md_links = len(re.findall(r'\[.*?\]\([^)]+\)', translated))
        
        if orig_md_links != trans_md_links:
            errors.append(f"Markdown链接数量不匹配: {orig_md_links} vs {trans_md_links}")
        
        # 检查URL数量
        url_pattern = r'https?://[^\s)]+[^\s.,)]'
        orig_urls = len(re.findall(url_pattern, original))
        trans_urls = len(re.findall(url_pattern, translated))
        
        if orig_urls != trans_urls:
            errors.append(f"URL数量不匹配: {orig_urls} vs {trans_urls}")
        
        # 检查链接的URL部分是否被翻译（不应该被翻译）
        trans_md_links_full = re.findall(r'\[.*?\]\(([^)]+)\)', translated)
        for url in trans_md_links_full:
            if self._contains_chinese(url) and not url.startswith('#'):
                errors.append(f"URL被错误翻译: {url}")
        
        return errors
    
    def _validate_code_blocks(self, original: str, translated: str) -> List[str]:
        """验证代码块"""
        errors = []
        
        # 检查代码块数量
        orig_code_blocks = len(re.findall(r'```[\s\S]*?```', original))
        trans_code_blocks = len(re.findall(r'```[\s\S]*?```', translated))
        
        if orig_code_blocks != trans_code_blocks:
            errors.append(f"代码块数量不匹配: {orig_code_blocks} vs {trans_code_blocks}")
        
        # 检查内联代码
        orig_inline_code = len(re.findall(r'`[^`]+`', original))
        trans_inline_code = len(re.findall(r'`[^`]+`', translated))
        
        if abs(orig_inline_code - trans_inline_code) > 2:  # 允许少量差异
            errors.append(f"内联代码数量差异过大: {orig_inline_code} vs {trans_inline_code}")
        
        return errors
    
    def _validate_html_tags(self, original: str, translated: str) -> List[str]:
        """验证HTML标签"""
        errors = []
        
        # 检查HTML标签数量
        orig_tags = len(re.findall(r'<[^>]+>', original))
        trans_tags = len(re.findall(r'<[^>]+>', translated))
        
        if orig_tags != trans_tags:
            errors.append(f"HTML标签数量不匹配: {orig_tags} vs {trans_tags}")
        
        # 检查特定标签的配对
        tag_patterns = [
            r'<img[^>]*>',
            r'<a[^>]*>.*?</a>',
            r'<strong>.*?</strong>',
            r'<em>.*?</em>'
        ]
        
        for pattern in tag_patterns:
            orig_count = len(re.findall(pattern, original, re.DOTALL))
            trans_count = len(re.findall(pattern, translated, re.DOTALL))
            
            if orig_count != trans_count:
                tag_name = pattern.split('[<>]')[1] if '[<>]' in pattern else pattern
                errors.append(f"标签 {tag_name} 数量不匹配: {orig_count} vs {trans_count}")
        
        return errors
    
    def _validate_content_completeness(self, original: str, translated: str) -> List[str]:
        """验证内容完整性"""
        errors = []
        
        # 检查frontmatter
        orig_frontmatter = re.match(r'^---\n.*?\n---\n', original, re.DOTALL)
        trans_frontmatter = re.match(r'^---\n.*?\n---\n', translated, re.DOTALL)
        
        if orig_frontmatter and not trans_frontmatter:
            errors.append("缺少frontmatter")
        elif not orig_frontmatter and trans_frontmatter:
            errors.append("意外添加了frontmatter")
        
        # 检查是否包含原文（可能翻译不完整）
        if self._contains_substantial_english(translated):
            errors.append("翻译结果包含大量英文，可能翻译不完整")
        
        # 检查占位符是否被恢复
        placeholder_patterns = [
            r'__PROTECTED_\w+_\d+__',
            r'__\w+_\d+__'
        ]
        
        for pattern in placeholder_patterns:
            placeholders = re.findall(pattern, translated)
            if placeholders:
                errors.append(f"发现未恢复的占位符: {placeholders[:3]}")  # 只显示前3个
        
        return errors
    
    def _contains_chinese(self, text: str) -> bool:
        """检查文本是否包含中文"""
        return bool(re.search(r'[\u4e00-\u9fff]', text))
    
    def _contains_substantial_english(self, text: str) -> bool:
        """检查是否包含大量英文"""
        # 移除代码块和链接
        clean_text = re.sub(r'```[\s\S]*?```', '', text)
        clean_text = re.sub(r'`[^`]+`', '', clean_text)
        clean_text = re.sub(r'https?://[^\s)]+', '', clean_text)
        
        # 统计英文单词
        english_words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text)
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', clean_text))
        
        # 如果英文单词数量超过中文字符数量的30%，认为包含大量英文
        if len(english_words) > max(chinese_chars * 0.3, 10):
            return True
            
        return False
    
    def get_translation_score(self, original: str, translated: str) -> float:
        """
        计算翻译质量评分
        
        Returns:
            评分 (0-100)
        """
        is_valid, errors = self.validate_translation(original, translated)
        
        if is_valid:
            return 100.0
        
        # 根据错误数量和严重程度计算扣分
        score = 100.0
        
        for error in errors:
            if "为空" in error:
                score -= 50
            elif "长度" in error:
                score -= 10
            elif "数量不匹配" in error:
                score -= 15
            elif "占位符" in error:
                score -= 20
            elif "翻译不完整" in error:
                score -= 25
            else:
                score -= 5
        
        return max(0.0, score)