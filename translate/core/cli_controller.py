"""
Claude Code CLI控制器 - 智能管理Claude CLI调用
"""

import subprocess
import time
import os
import logging
from typing import Optional, Dict, Any


class ClaudeController:
    """Claude Code CLI控制器"""
    
    def __init__(self, 
                 model: str = "claude-3-sonnet-20240229",
                 timeout: int = 300,
                 max_retries: int = 3):
        """
        初始化控制器
        
        Args:
            model: Claude模型名称
            timeout: 超时时间(秒)
            max_retries: 最大重试次数
        """
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries
        self.logger = logging.getLogger(__name__)
        
        # 验证Claude CLI是否可用
        self._verify_cli()
    
    def _verify_cli(self) -> None:
        """验证Claude CLI是否安装和可用"""
        try:
            result = subprocess.run(['which', 'claude'], 
                                 capture_output=True, 
                                 text=True, 
                                 timeout=5)
            if result.returncode != 0:
                raise RuntimeError("Claude CLI未安装或不在PATH中")
                
            # 测试CLI是否工作
            test_result = subprocess.run(['claude', '--version'], 
                                       capture_output=True, 
                                       text=True, 
                                       timeout=5)
            if test_result.returncode != 0:
                raise RuntimeError("Claude CLI无法正常工作")
                
            self.logger.info("Claude CLI验证成功")
            
        except subprocess.TimeoutExpired:
            raise RuntimeError("Claude CLI验证超时")
        except Exception as e:
            raise RuntimeError(f"Claude CLI验证失败: {e}")
    
    def call_claude(self, 
                   prompt: str, 
                   model: Optional[str] = None,
                   timeout: Optional[int] = None) -> Optional[str]:
        """
        调用Claude CLI
        
        Args:
            prompt: 输入提示
            model: 可选的模型覆盖
            timeout: 可选的超时覆盖
            
        Returns:
            Claude的响应文本，失败时返回None
        """
        use_model = model or self.model
        use_timeout = timeout or self.timeout
        
        for attempt in range(self.max_retries):
            try:
                self.logger.info(f"调用Claude CLI (尝试 {attempt + 1}/{self.max_retries})")
                
                # 构建命令
                cmd = ['claude']
                if use_model:
                    cmd.extend(['--model', use_model])
                
                # 执行命令
                result = subprocess.run(
                    cmd,
                    input=prompt,
                    text=True,
                    capture_output=True,
                    timeout=use_timeout
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    self.logger.info("Claude CLI调用成功")
                    return result.stdout.strip()
                else:
                    error_msg = result.stderr.strip() if result.stderr else "无错误信息"
                    self.logger.warning(f"Claude CLI返回错误: {error_msg}")
                    
            except subprocess.TimeoutExpired:
                self.logger.warning(f"Claude CLI调用超时 ({use_timeout}秒)")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # 指数退避
                    continue
                    
            except Exception as e:
                self.logger.error(f"Claude CLI调用异常: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                    
        self.logger.error("Claude CLI调用最终失败")
        return None
    
    def translate_text(self, 
                      content: str, 
                      source_lang: str = "English",
                      target_lang: str = "Chinese") -> Optional[str]:
        """
        翻译文本
        
        Args:
            content: 要翻译的内容
            source_lang: 源语言
            target_lang: 目标语言
            
        Returns:
            翻译结果
        """
        prompt = f"""请将以下{source_lang}文档翻译成{target_lang}。

**严格遵循规则:**
1. 保持所有markdown格式不变
2. 保留所有URL链接
3. 保留专有名词: Claude, VuePress, GitHub, API, CLI, JSON, MCP等
4. 保留代码块和命令行内容
5. frontmatter中的title翻译，其他字段保持原文
6. HTML标签和属性保持不变
7. 使用准确的技术术语

**内容:**
{content}

**直接输出翻译结果，不要解释:**"""
        
        return self.call_claude(prompt)
    
    def get_model_info(self) -> Dict[str, Any]:
        """获取当前配置信息"""
        return {
            "model": self.model,
            "timeout": self.timeout,
            "max_retries": self.max_retries
        }
    
    def set_model(self, model: str) -> None:
        """设置模型"""
        self.model = model
        self.logger.info(f"切换模型到: {model}")
    
    def set_timeout(self, timeout: int) -> None:
        """设置超时时间"""
        self.timeout = timeout
        self.logger.info(f"设置超时时间: {timeout}秒")