#!/usr/bin/env node

/**
 * 高并发文档翻译工具
 * 支持多种翻译策略，使用 Claude Sonnet 模型
 */

const fs = require('fs').promises;
const path = require('path');
const { exec } = require('child_process');
const { promisify } = require('util');
const execPromise = promisify(exec);

// 配置
const CONFIG = {
  // Claude Code 配置
  claudeCode: {
    model: 'claude-3-5-sonnet-20241022', // 指定使用 Sonnet
    maxConcurrency: 5, // 最大并发数
    retryAttempts: 3, // 重试次数
    retryDelay: 2000, // 重试延迟（毫秒）
  },
  
  // 翻译策略
  strategies: {
    // 策略1：完整文档翻译
    full: {
      name: '完整文档翻译',
      description: '翻译整个文档，保留格式',
      batchSize: 1,
    },
    
    // 策略2：分段翻译
    chunked: {
      name: '分段翻译',
      description: '将文档分成小段进行翻译',
      chunkSize: 500, // 每段字符数
      batchSize: 3,
    },
    
    // 策略3：智能翻译
    smart: {
      name: '智能翻译',
      description: '根据内容类型智能选择翻译方式',
      batchSize: 2,
    },
    
    // 策略4：增量翻译
    incremental: {
      name: '增量翻译',
      description: '只翻译未翻译的部分',
      batchSize: 5,
    }
  },
  
  // 文件类型配置
  fileTypes: {
    markdown: {
      extensions: ['.md'],
      preservePatterns: [
        /```[\s\S]*?```/g, // 代码块
        /`[^`]+`/g, // 行内代码
        /\[([^\]]+)\]\(([^)]+)\)/g, // 链接
        /^---[\s\S]*?^---/gm, // frontmatter
      ]
    }
  },
  
  // 翻译规则
  translationRules: {
    // 不翻译的术语
    preserveTerms: [
      'Claude Code', 'Claude', 'Anthropic', 'API', 'MCP', 'CLI',
      'GitHub', 'npm', 'VS Code', 'Git', 'Bash', 'Python', 'JavaScript',
      'TypeScript', 'React', 'Vue', 'VuePress', 'Markdown', 'YAML',
      'JSON', 'XML', 'HTML', 'CSS', 'SQL', 'GraphQL', 'REST', 'WebSocket',
      'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'Linux', 'macOS', 'Windows'
    ],
    
    // 常用翻译映射
    commonTranslations: {
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
      'License': '许可证',
      'Contributing': '贡献',
      'See Also': '另见',
      'Author': '作者',
      'References': '参考',
      'Related': '相关',
      'Prerequisites': '前置要求',
      'Getting Started': '快速开始',
      'Advanced': '高级',
      'Troubleshooting': '故障排除',
      'Best Practices': '最佳实践',
      'Performance': '性能',
      'Security': '安全',
      'Testing': '测试',
      'Deployment': '部署',
      'Architecture': '架构',
      'Design': '设计',
      'Implementation': '实现',
      'Integration': '集成',
      'Migration': '迁移',
      'Upgrade': '升级',
      'Downgrade': '降级',
      'Rollback': '回滚',
      'Backup': '备份',
      'Restore': '恢复',
      'Monitor': '监控',
      'Debug': '调试',
      'Optimize': '优化',
      'Scale': '扩展',
      'Maintain': '维护'
    }
  }
};

// 翻译器类
class DocumentTranslator {
  constructor(options = {}) {
    this.config = { ...CONFIG, ...options };
    this.queue = [];
    this.processing = new Set();
    this.completed = new Set();
    this.failed = new Map();
    this.stats = {
      total: 0,
      completed: 0,
      failed: 0,
      skipped: 0,
      startTime: Date.now()
    };
  }

  /**
   * 使用 Claude Code 翻译文本
   */
  async translateWithClaude(text, context = {}) {
    const prompt = this.buildTranslationPrompt(text, context);
    
    // 构建 Claude Code 命令
    const command = `echo '${this.escapeForShell(prompt)}' | claude --model ${this.config.claudeCode.model} --no-cache`;
    
    try {
      const { stdout, stderr } = await execPromise(command, {
        maxBuffer: 10 * 1024 * 1024, // 10MB buffer
        timeout: 60000 // 60秒超时
      });
      
      if (stderr && !stderr.includes('Warning')) {
        console.warn(`警告: ${stderr}`);
      }
      
      return this.extractTranslation(stdout);
    } catch (error) {
      throw new Error(`翻译失败: ${error.message}`);
    }
  }

  /**
   * 构建翻译提示词
   */
  buildTranslationPrompt(text, context) {
    const { fileType = 'markdown', strategy = 'smart' } = context;
    
    let prompt = `请将以下${fileType}文档从英文翻译成中文。

重要规则：
1. 保留所有markdown格式、代码块、链接
2. 不要翻译以下内容：
   - 代码块中的代码
   - 技术术语：${this.config.translationRules.preserveTerms.join(', ')}
   - 产品名称和品牌
   - 文件路径和URL
3. 使用自然流畅的中文，适合程序员阅读
4. 保持原文的语气和风格
5. 只返回翻译后的内容，不要添加任何解释

`;

    // 添加常用翻译参考
    if (context.includeGlossary) {
      prompt += '\n常用翻译参考：\n';
      for (const [en, zh] of Object.entries(this.config.translationRules.commonTranslations)) {
        prompt += `- "${en}" → "${zh}"\n`;
      }
      prompt += '\n';
    }

    prompt += `原文：
---
${text}
---

翻译：`;

    return prompt;
  }

  /**
   * 转义shell特殊字符
   */
  escapeForShell(text) {
    return text.replace(/'/g, "'\\''");
  }

  /**
   * 从Claude响应中提取翻译
   */
  extractTranslation(response) {
    // 移除可能的额外说明文字
    let translation = response.trim();
    
    // 如果响应包含"翻译："或类似标记，提取其后的内容
    const markers = ['翻译：', '译文：', 'Translation:', '---'];
    for (const marker of markers) {
      const index = translation.lastIndexOf(marker);
      if (index !== -1) {
        translation = translation.substring(index + marker.length).trim();
      }
    }
    
    return translation;
  }

  /**
   * 并发翻译多个文件
   */
  async translateFiles(files, options = {}) {
    const {
      strategy = 'smart',
      concurrency = this.config.claudeCode.maxConcurrency,
      outputDir = null,
      overwrite = false
    } = options;

    console.log(`\n🚀 开始翻译 ${files.length} 个文件`);
    console.log(`📋 策略: ${this.config.strategies[strategy].name}`);
    console.log(`⚡ 并发数: ${concurrency}`);
    console.log('');

    this.stats.total = files.length;
    this.queue = [...files];

    // 创建工作池
    const workers = [];
    for (let i = 0; i < Math.min(concurrency, files.length); i++) {
      workers.push(this.processQueue(strategy, outputDir, overwrite));
    }

    // 等待所有工作完成
    await Promise.all(workers);

    this.printStats();
  }

  /**
   * 处理队列中的文件
   */
  async processQueue(strategy, outputDir, overwrite) {
    while (this.queue.length > 0) {
      const file = this.queue.shift();
      if (!file) continue;

      try {
        await this.translateFile(file, {
          strategy,
          outputDir,
          overwrite
        });
        
        this.stats.completed++;
        this.completed.add(file);
        
        console.log(`✅ [${this.stats.completed}/${this.stats.total}] ${path.basename(file)}`);
      } catch (error) {
        this.stats.failed++;
        this.failed.set(file, error.message);
        
        console.error(`❌ [${this.stats.completed + this.stats.failed}/${this.stats.total}] ${path.basename(file)}: ${error.message}`);
        
        // 重试逻辑
        if (this.shouldRetry(file)) {
          console.log(`🔄 重试: ${path.basename(file)}`);
          this.queue.push(file);
        }
      }
    }
  }

  /**
   * 翻译单个文件
   */
  async translateFile(filePath, options = {}) {
    const { strategy = 'smart', outputDir = null, overwrite = false } = options;
    
    // 读取文件
    const content = await fs.readFile(filePath, 'utf-8');
    
    // 检查是否已经是中文
    if (!overwrite && this.isChinese(content)) {
      console.log(`⏭️  跳过已翻译: ${path.basename(filePath)}`);
      this.stats.skipped++;
      return;
    }
    
    // 根据策略翻译
    let translatedContent;
    switch (strategy) {
      case 'full':
        translatedContent = await this.translateFull(content, filePath);
        break;
      case 'chunked':
        translatedContent = await this.translateChunked(content, filePath);
        break;
      case 'smart':
        translatedContent = await this.translateSmart(content, filePath);
        break;
      case 'incremental':
        translatedContent = await this.translateIncremental(content, filePath);
        break;
      default:
        throw new Error(`未知策略: ${strategy}`);
    }
    
    // 保存翻译结果
    const outputPath = outputDir 
      ? path.join(outputDir, path.basename(filePath))
      : filePath;
    
    await fs.writeFile(outputPath, translatedContent, 'utf-8');
  }

  /**
   * 策略1：完整文档翻译
   */
  async translateFull(content, filePath) {
    const fileType = this.getFileType(filePath);
    return await this.translateWithClaude(content, {
      fileType,
      strategy: 'full',
      includeGlossary: true
    });
  }

  /**
   * 策略2：分段翻译
   */
  async translateChunked(content, filePath) {
    const chunks = this.splitIntoChunks(content);
    const translatedChunks = [];
    
    for (const chunk of chunks) {
      const translated = await this.translateWithClaude(chunk, {
        fileType: this.getFileType(filePath),
        strategy: 'chunked'
      });
      translatedChunks.push(translated);
    }
    
    return translatedChunks.join('\n\n');
  }

  /**
   * 策略3：智能翻译
   */
  async translateSmart(content, filePath) {
    const fileType = this.getFileType(filePath);
    
    // 提取需要保留的部分
    const preserved = this.extractPreservedContent(content, fileType);
    
    // 替换为占位符
    let processedContent = content;
    const placeholders = new Map();
    preserved.forEach((item, index) => {
      const placeholder = `__PRESERVE_${index}__`;
      placeholders.set(placeholder, item.content);
      processedContent = processedContent.replace(item.content, placeholder);
    });
    
    // 翻译处理后的内容
    let translated = await this.translateWithClaude(processedContent, {
      fileType,
      strategy: 'smart',
      includeGlossary: true
    });
    
    // 恢复保留的内容
    placeholders.forEach((content, placeholder) => {
      translated = translated.replace(placeholder, content);
    });
    
    return translated;
  }

  /**
   * 策略4：增量翻译
   */
  async translateIncremental(content, filePath) {
    // 检测已翻译和未翻译的部分
    const sections = this.detectTranslationStatus(content);
    const untranslatedSections = sections.filter(s => !s.translated);
    
    if (untranslatedSections.length === 0) {
      return content; // 全部已翻译
    }
    
    // 只翻译未翻译的部分
    for (const section of untranslatedSections) {
      const translated = await this.translateWithClaude(section.content, {
        fileType: this.getFileType(filePath),
        strategy: 'incremental'
      });
      content = content.replace(section.content, translated);
    }
    
    return content;
  }

  /**
   * 将内容分成块
   */
  splitIntoChunks(content, chunkSize = 500) {
    const chunks = [];
    const lines = content.split('\n');
    let currentChunk = [];
    let currentSize = 0;
    
    for (const line of lines) {
      if (currentSize + line.length > chunkSize && currentChunk.length > 0) {
        chunks.push(currentChunk.join('\n'));
        currentChunk = [];
        currentSize = 0;
      }
      currentChunk.push(line);
      currentSize += line.length;
    }
    
    if (currentChunk.length > 0) {
      chunks.push(currentChunk.join('\n'));
    }
    
    return chunks;
  }

  /**
   * 提取需要保留的内容
   */
  extractPreservedContent(content, fileType) {
    const preserved = [];
    const config = this.config.fileTypes[fileType];
    
    if (!config) return preserved;
    
    for (const pattern of config.preservePatterns) {
      const matches = content.match(pattern);
      if (matches) {
        matches.forEach(match => {
          preserved.push({
            content: match,
            type: 'preserved'
          });
        });
      }
    }
    
    return preserved;
  }

  /**
   * 检测内容是否已经是中文
   */
  isChinese(content) {
    const chineseChars = content.match(/[\u4e00-\u9fa5]/g);
    const totalChars = content.replace(/\s/g, '').length;
    return chineseChars && (chineseChars.length / totalChars) > 0.3;
  }

  /**
   * 检测翻译状态
   */
  detectTranslationStatus(content) {
    const sections = [];
    const paragraphs = content.split(/\n\n+/);
    
    for (const paragraph of paragraphs) {
      sections.push({
        content: paragraph,
        translated: this.isChinese(paragraph)
      });
    }
    
    return sections;
  }

  /**
   * 获取文件类型
   */
  getFileType(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    for (const [type, config] of Object.entries(this.config.fileTypes)) {
      if (config.extensions.includes(ext)) {
        return type;
      }
    }
    return 'text';
  }

  /**
   * 判断是否应该重试
   */
  shouldRetry(file) {
    const attempts = this.failed.get(file) || 0;
    return attempts < this.config.claudeCode.retryAttempts;
  }

  /**
   * 打印统计信息
   */
  printStats() {
    const duration = Date.now() - this.stats.startTime;
    const minutes = Math.floor(duration / 60000);
    const seconds = Math.floor((duration % 60000) / 1000);
    
    console.log('\n📊 翻译统计:');
    console.log('─'.repeat(40));
    console.log(`✅ 成功: ${this.stats.completed}`);
    console.log(`❌ 失败: ${this.stats.failed}`);
    console.log(`⏭️  跳过: ${this.stats.skipped}`);
    console.log(`⏱️  耗时: ${minutes}分${seconds}秒`);
    console.log(`🚀 速度: ${(this.stats.completed / (duration / 1000)).toFixed(2)} 文件/秒`);
    
    if (this.failed.size > 0) {
      console.log('\n❌ 失败文件:');
      this.failed.forEach((error, file) => {
        console.log(`  - ${path.basename(file)}: ${error}`);
      });
    }
  }
}

// CLI 接口
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0 || args.includes('--help')) {
    console.log(`
高并发文档翻译工具 v1.0.0

使用方法:
  node translator.js [选项] <文件或目录>

选项:
  --strategy <策略>    翻译策略 (full|chunked|smart|incremental) [默认: smart]
  --concurrency <数量> 并发数量 [默认: 5]
  --output <目录>      输出目录 [默认: 原地覆盖]
  --overwrite         覆盖已翻译的文件
  --pattern <模式>     文件匹配模式 [默认: *.md]
  --help              显示帮助信息

策略说明:
  full        - 完整文档翻译，适合小文件
  chunked     - 分段翻译，适合大文件
  smart       - 智能翻译，自动处理代码块等
  incremental - 增量翻译，只翻译未翻译部分

示例:
  # 翻译单个文件
  node translator.js --strategy smart README.md
  
  # 并发翻译目录中的所有markdown文件
  node translator.js --concurrency 10 --pattern "*.md" ./docs
  
  # 使用增量翻译策略
  node translator.js --strategy incremental --overwrite ./docs
`);
    process.exit(0);
  }

  // 解析命令行参数
  const options = {
    strategy: 'smart',
    concurrency: 5,
    outputDir: null,
    overwrite: false,
    pattern: '*.md'
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--strategy':
        options.strategy = args[++i];
        break;
      case '--concurrency':
        options.concurrency = parseInt(args[++i]);
        break;
      case '--output':
        options.outputDir = args[++i];
        break;
      case '--overwrite':
        options.overwrite = true;
        break;
      case '--pattern':
        options.pattern = args[++i];
        break;
    }
  }

  // 获取目标路径
  const targetPath = args[args.length - 1];
  if (!targetPath || targetPath.startsWith('--')) {
    console.error('❌ 请指定要翻译的文件或目录');
    process.exit(1);
  }

  try {
    const translator = new DocumentTranslator();
    const stats = await fs.stat(targetPath);
    
    let files = [];
    if (stats.isDirectory()) {
      // 扫描目录中的文件
      const entries = await fs.readdir(targetPath, { withFileTypes: true });
      files = entries
        .filter(entry => entry.isFile() && entry.name.match(options.pattern))
        .map(entry => path.join(targetPath, entry.name));
    } else {
      files = [targetPath];
    }

    if (files.length === 0) {
      console.log('⚠️  没有找到匹配的文件');
      process.exit(0);
    }

    // 开始翻译
    await translator.translateFiles(files, options);
    
    console.log('\n✨ 翻译完成!');
  } catch (error) {
    console.error(`\n❌ 错误: ${error.message}`);
    process.exit(1);
  }
}

// 导出模块
module.exports = { DocumentTranslator, CONFIG };

// 如果直接运行
if (require.main === module) {
  main().catch(console.error);
}