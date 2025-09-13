# ClaudeLog 中文翻译项目

![ClaudeLog Translation](./docs/project-banner.png)

## 🌟 项目简介

**ClaudeLog 中文翻译项目** 是一个完整的文档本地化工程，通过智能化网页爬取、自动化翻译和 VuePress 网站生成，为中文用户提供 claudelog.com 的完整中文版本。项目涵盖 68+ 页面的专业技术文档翻译，保持原站点的完整结构和功能。

### 核心功能

- **🕸️ 智能网页爬取** - 完整抓取原站点所有页面和资源
- **🔄 自动化翻译** - 集成多种翻译引擎的批量翻译流程
- **📚 VuePress 生成** - 生成功能完整的静态网站
- **🖼️ 资源管理** - 自动下载和优化图片资源
- **🔗 链接管理** - 智能处理内部链接和导航结构

## 📁 项目目录结构

```
claudelogTranslate/
├── docs/                       # 📚 项目文档
│   ├── TRANSLATION-GUIDE.md    # 翻译指南
│   └── project-requirements.md # 项目需求文档
├── scripts/                    # 🛠️ 脚本工具集
│   ├── scraper/               # 网页爬取工具
│   │   └── final-scraper.js   # 主要爬虫脚本
│   ├── translation/           # 翻译工具
│   │   ├── claude-translator.py      # Claude 翻译器
│   │   ├── translate-all.sh          # 批量翻译脚本
│   │   └── translation-checker.py    # 翻译质量检查
│   ├── utils/                 # 工具脚本
│   │   ├── check-links.py           # 链接检查
│   │   ├── fix-formatting.py       # 格式修复
│   │   └── cleanup.py              # 清理工具
│   └── validation/            # 验证工具
│       ├── comprehensive-scanner.py # 综合扫描器
│       └── quality-checker.py      # 质量检查器
├── tools/                      # 🔧 开发工具
│   ├── test_file.md           # 测试文件
│   └── temp_prompt.txt        # 临时提示文件
├── backups/                    # 💾 备份文件
│   ├── translation-backups/   # 翻译备份
│   ├── final-site-backups/   # 网站备份
│   └── working-copies/       # 工作副本
├── final-site/                 # 🌐 VuePress 网站
│   ├── docs/                  # Markdown 内容文件
│   │   ├── .vuepress/        # VuePress 配置
│   │   │   ├── config.js     # 网站配置
│   │   │   └── public/       # 静态资源
│   │   ├── img/              # 图片资源
│   │   └── *.md              # 页面内容 (68+ 页面)
│   └── package.json          # VuePress 依赖
├── translate/                  # 🈲 翻译工作目录
│   └── *.md                   # 翻译中的文件
├── CLAUDE.md                   # Claude Code 开发指南
├── README.md                   # 项目说明文档
├── package.json                # 项目依赖配置
└── .gitignore                  # Git 忽略配置
```

## 🛠️ 技术栈

### 前端技术
- **框架**: VuePress 2.0 + Vite 构建工具
- **语言**: JavaScript + Markdown
- **主题**: VuePress 默认主题 + 自定义配置
- **样式**: CSS + 内联 HTML 样式

### 后端工具
- **爬虫**: Node.js + Puppeteer/Cheerio
- **翻译**: Python + Claude API/GPT API
- **数据处理**: Turndown.js (HTML to Markdown)
- **文件管理**: Node.js 文件系统操作

### 开发工具
- **包管理**: npm
- **版本控制**: Git
- **代码规范**: ESLint + Prettier
- **质量检查**: 自定义 Python 脚本

## 🚀 快速开始

### 环境要求
- Node.js >= 16.0.0
- Python >= 3.8
- npm >= 8.0.0

### 安装依赖
```bash
# 克隆项目
git clone <repository-url>
cd claudelogTranslate

# 安装所有依赖
npm install
```

### 网站爬取
```bash
# 运行综合爬虫 (抓取英文原站)
node scripts/final-scraper.js

# 爬虫自动执行:
# - 下载所有页面和图片
# - 转换 HTML 为 Markdown
# - 保持代码格式
# - 转义 Vue 冲突语法
# - 生成 VuePress 配置
```

### 翻译流程
```bash
# 批量翻译所有页面
bash scripts/translate-all.sh

# 单个文件翻译
python scripts/claude-translator.py <file-path>

# 检查翻译质量
python scripts/translation-checker.py
```

### 开发环境
```bash
# 启动 VuePress 开发服务器
cd final-site
npm install
npm run dev    # 访问 http://localhost:8080

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

## 📊 项目统计

- **总页面数**: 68+ (包括所有 MCPs 子页面)
- **图片资源**: 50+ 张，自动尺寸优化
- **侧边栏章节**: 10 个主要章节，多级嵌套
- **代码块修复**: 25+ 个，保持换行格式
- **导航链接**: 100+ 个，全部验证可用
- **翻译进度**: 95% 完成，持续更新中

## 🐛 已知问题与解决方案

### 1. 图片显示问题
**问题**: 图片显示为损坏链接
**解决方案**: 爬虫自动下载图片并更新路径

### 2. 侧边栏导航 404 错误
**问题**: 目录式链接导致 404 错误
**解决方案**: 所有链接在 config.js 中转换为 .html 格式

### 3. 代码块换行丢失
**问题**: HTML 转 Markdown 过程中换行丢失
**解决方案**: Turndown 转换前预处理 BR 标签

### 4. Vue 解析错误
**问题**: 尖括号导致"元素缺少结束标签"错误
**解决方案**: 自动转义 markdown 中的尖括号

### 5. 图片尺寸问题
**问题**: 图片过大 (400px 而非 165px)
**解决方案**: 爬取时应用内联 HTML 样式和 max-width

## ✅ 质量保证

### 已应用的自动修复
- ✅ 从源站抓取全部 68 页面
- ✅ 下载图片并调整正确尺寸
- ✅ 代码块保持换行格式
- ✅ 解决 Vue 语法冲突
- ✅ 侧边栏导航功能完整
- ✅ 包含 MCPs 子页面 (20+)
- ✅ 修正首页路由
- ✅ 修复格式错误的 markdown 链接

### 测试检查清单
- [x] 所有侧边栏链接正确导航
- [x] 图片以正确尺寸显示
- [x] 代码块渲染带格式
- [x] 无 Vue 解析错误
- [x] 所有 MCPs 页面可访问
- [x] 首页正确加载
- [x] 支持页面布局匹配原站

## 📝 核心实现细节

### 图片处理
```html
<!-- 图片使用内联 HTML 以兼容 VuePress -->
<img src="/img/example.png" style="max-width: 165px; height: auto;" />
```

### 代码块保护
```javascript
// BR 标签在 markdown 转换前预处理
html = html.replace(/<br\s*\/?>/gi, '___LINEBREAK___');
// 后续转换为 markdown 中的实际换行
```

### Vue 冲突解决
```javascript
// 转义尖括号以防止解析错误
markdown = markdown.replace(/<(\d+%)/g, '&lt;$1');
```

## 🚧 未来改进计划

### 已完成功能
- [x] 中文翻译支持 (95% 完成)
- [x] 自动化测试套件
- [x] 质量检查流程
- [x] 批量处理工具

### 待开发功能
- [ ] CI/CD 自动更新流程
- [ ] 交互式图表重现
- [ ] 站内搜索功能
- [ ] 深色模式支持
- [ ] 移动端优化
- [ ] 多语言切换

## 📋 代码规范

### 文件命名规范
```
# Python 脚本：kebab-case
translate-all.py
check-links.py

# JavaScript 文件：camelCase
finalScraper.js
configUtils.js

# 文档文件：UPPERCASE
README.md
CLAUDE.md
```

### Git 提交规范
```bash
# 提交格式：<type>(<scope>): <description>

# 类型说明
feat:     新功能
fix:      修复问题
docs:     文档更新
refactor: 重构代码
script:   脚本更新
trans:    翻译更新

# 示例
feat(scraper): 添加图片自动优化功能
fix(translation): 修复代码块翻译问题
docs(readme): 更新项目结构说明
script(utils): 优化链接检查脚本
trans(pages): 完成 FAQ 页面翻译
```

## 📄 开源协议

本项目仅供教育和学习目的使用。原始内容版权归 claudelog.com 所有。

## 🤝 贡献指南

1. 本地测试变更 `npm run dev`
2. 验证所有链接正确工作
3. 检查图片尺寸匹配原站
4. 确保无 Vue 解析错误
5. 更新 CLAUDE.md 记录新问题/解决方案

## 📚 相关文档

- **[CLAUDE.md](./CLAUDE.md)** - 综合开发指南和问题跟踪
- **[翻译指南](./docs/TRANSLATION-GUIDE.md)** - 翻译流程和标准
- **[scripts/](./scripts/)** - 各类脚本的内联注释说明
- **[final-site/.vuepress/config.js](./final-site/.vuepress/config.js)** - 侧边栏结构文档

## 🔍 故障排除

如遇到问题：

1. **图片损坏**: 重新运行爬虫下载缺失图片
2. **404 错误**: 检查侧边栏链接使用 .html 格式
3. **构建错误**: 确保 `npm install` 安装所有依赖
4. **Vue 错误**: 查找 markdown 中未转义的尖括号
5. **页面缺失**: 验证爬虫在 getAllLinks() 中包含所有 URL

详细故障排除请参考 CLAUDE.md 中的综合问题文档和解决方案。

## 🔗 相关链接

- **原站点**: [https://claudelog.com](https://claudelog.com)
- **开发文档**: [./CLAUDE.md](./CLAUDE.md)
- **项目仓库**: [GitHub Repository](#)

---

**ClaudeLog 中文翻译项目 - 为中文 Claude 开发者社区提供专业文档支持**

*最后更新: 2025年9月13日*
*总开发时间: ~20 小时*
*已解决问题: 30+*
*成功迁移页面: 68+*