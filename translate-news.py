#!/usr/bin/env python3
import re

def translate_news():
    file_path = 'final-site/docs/claude-news.md'
    
    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Comprehensive translations
    translations = {
        # Header
        'title: "Claude News Timeline | Claude Hub"': 'title: "Claude 新闻时间线 | Claude Hub"',
        '# Claude News Timeline | Claude Hub': '# Claude 新闻时间线 | Claude Hub',
        'Stay up-to-date with the latest announcements, product updates, and news from Anthropic about Claude.': '及时了解 Anthropic 关于 Claude 的最新公告、产品更新和新闻。',
        
        # Months
        '## **September 2025**': '## **2025年9月**',
        '## **August 2025**': '## **2025年8月**',
        '## **July 2025**': '## **2025年7月**',
        '## **June 2025**': '## **2025年6月**',
        '## **May 2025**': '## **2025年5月**',
        '## **April 2025**': '## **2025年4月**',
        '## **March 2025**': '## **2025年3月**',
        '## **February 2025**': '## **2025年2月**',
        '## **January 2025**': '## **2025年1月**',
        '## **December 2024**': '## **2024年12月**',
        '## **November 2024**': '## **2024年11月**',
        '## **October 2024**': '## **2024年10月**',
        
        # Date formats
        'Sep ': '9月',
        'Aug ': '8月',
        'Jul ': '7月',
        'Jun ': '6月',
        'May ': '5月',
        'Apr ': '4月',
        'Mar ': '3月',
        'Feb ': '2月',
        'Jan ': '1月',
        'Dec ': '12月',
        'Nov ': '11月',
        'Oct ': '10月',
        
        # Categories
        'Category: Product': '类别：产品',
        'Category: Announcements': '类别：公告',
        'Category: Research': '类别：研究',
        
        # Common terms
        'Direct link to': '直接链接到',
        
        # September 2025 news
        '[Claude can now create and edit files]': '[Claude 现在可以创建和编辑文件]',
        'Claude can now create and edit': 'Claude 现在可以创建和编辑',
        'Excel spreadsheets': 'Excel 电子表格',
        'documents': '文档',
        'PowerPoint slides': 'PowerPoint 幻灯片',
        'and': '和',
        'PDFs': 'PDF 文件',
        'directly in': '直接在',
        'Claude.ai': 'Claude.ai',
        'the': '',
        'desktop app': '桌面应用程序',
        'transforming how users work by producing ready-to-use files from instructions and data': '通过从指令和数据生成即用型文件来改变用户的工作方式',
        'This feature is available as a preview for': '此功能作为预览版提供给',
        'Max': 'Max',
        'Team': 'Team',
        'Enterprise': 'Enterprise',
        'users, with': '用户，',
        'Pro': 'Pro',
        'users getting access in': '用户将在',
        'coming weeks': '未来几周内获得访问权限',
        
        '[Anthropic is endorsing SB 53]': '[Anthropic 支持 SB 53 法案]',
        'Anthropic is endorsing California\'s': 'Anthropic 支持加州的',
        'SB 53': 'SB 53',
        'a bill governing powerful AI systems that requires companies to develop': '一项管理强大 AI 系统的法案，要求公司开发',
        'safety frameworks': '安全框架',
        'publish': '发布',
        'transparency reports': '透明度报告',
        'and report': '并报告',
        'critical incidents': '关键事件',
        'to the state': '给州政府',
        'The company supports this': '公司支持这种',
        'trust but verify': '信任但验证',
        'approach as it formalizes practices already followed by': '的方法，因为它将已经被',
        'frontier AI companies': '前沿 AI 公司',
        'while creating a level playing field for safety disclosure': '遵循的做法正式化，同时为安全披露创造公平的竞争环境',
        
        '[Updating restrictions of sales to unsupported regions]': '[更新对不支持地区的销售限制]',
        'Anthropic is strengthening regional restrictions to prevent companies controlled by adversarial nations like': 'Anthropic 正在加强地区限制，以防止受敌对国家控制的公司如',
        'China': '中国',
        'from accessing their services, even through subsidiaries in other countries': '通过其他国家的子公司访问其服务',
        'The updated policy prohibits entities more than': '更新的政策禁止超过',
        '50% owned': '50% 所有权',
        'by companies from unsupported regions, addressing': '由不支持地区的公司拥有的实体，解决',
        'national security risks': '国家安全风险',
        'where authoritarian governments can compel data sharing and intelligence cooperation': '威权政府可以强制数据共享和情报合作的问题',
        
        '[Anthropic raises $13B Series F at $183B post-money valuation]': '[Anthropic 以1830亿美元投后估值完成130亿美元F轮融资]',
        'Anthropic completed a': 'Anthropic 完成了',
        '$13 billion': '130亿美元',
        'Series F': 'F轮',
        'funding round led by': '融资，由',
        'ICONIQ': 'ICONIQ',
        'valuing the company at': '领投，公司估值',
        '$183 billion': '1830亿美元',
        'post-money with participation from major investors including': '投后，主要投资者包括',
        'Fidelity': 'Fidelity',
        'Lightspeed': 'Lightspeed',
        'BlackRock': 'BlackRock',
        'The funding reflects Anthropic\'s rapid growth from': '此次融资反映了 Anthropic 从',
        '$1 billion': '10亿美元',
        'run-rate revenue in': '年化收入在',
        'early 2025': '2025年初',
        'to over': '增长到超过',
        '$5 billion': '50亿美元',
        'by': '在',
        'August': '8月',
        'making it one of the fastest-growing technology companies in history': '使其成为历史上增长最快的科技公司之一',
        
        # August 2025 news
        '[Updates to Consumer Terms and Privacy Policy]': '[消费者条款和隐私政策更新]',
        'Anthropic updated its Consumer Terms and Privacy Policy to allow training new models using data from': 'Anthropic 更新了其消费者条款和隐私政策，允许使用来自',
        'Free': '免费',
        'accounts when users': '账户的数据训练新模型，当用户',
        'opt-in': '选择加入',
        'with an extended': '时，延长',
        '5-year': '5年',
        'data retention period for those who consent': '数据保留期限给予同意的用户',
        'Current users have until': '现有用户有时间直到',
        'September 28, 2025': '2025年9月28日',
        'to make their selection, while new users choose during signup': '做出选择，而新用户在注册时选择',
        
        '[Introducing the Anthropic National Security and Public Sector Advisory Council]': '[介绍 Anthropic 国家安全和公共部门咨询委员会]',
        'Anthropic formed the': 'Anthropic 成立了',
        'National Security and Public Sector Advisory Council': '国家安全和公共部门咨询委员会',
        'featuring': '成员包括',
        'bipartisan': '两党',
        'former government leaders including Senators': '前政府领导人，包括参议员',
        'Roy Blunt': 'Roy Blunt',
        'Jon Tester': 'Jon Tester',
        'former': '前',
        'Defense officials': '国防官员',
        'intelligence community veterans': '情报界资深人士',
        'The council will help identify high-impact AI applications for': '委员会将帮助确定高影响力的 AI 应用于',
        'national security': '国家安全',
        'develop industry standards, and strengthen': '制定行业标准，并加强',
        'public-private partnerships': '公私合作伙伴关系',
        
        '[Detecting and countering misuse of AI: August 2025]': '[检测和对抗 AI 滥用：2025年8月]',
        'Anthropic\'s threat intelligence report reveals sophisticated AI misuse including a': 'Anthropic 的威胁情报报告揭示了复杂的 AI 滥用，包括',
        'large-scale extortion operation': '大规模勒索行动',
        'using': '使用',
        'Claude Code': 'Claude Code',
        'North Korean': '朝鲜',
        'employment fraud schemes': '就业欺诈计划',
        'AI-generated ransomware': 'AI 生成的勒索软件',
        'sales': '销售',
        'The report shows cybercriminals are weaponizing': '报告显示网络犯罪分子正在武器化',
        'agentic AI': '代理 AI',
        'to perform attacks rather than just advise, lowering barriers to sophisticated cybercrime for actors with': '来执行攻击而不仅仅是提供建议，降低了具有',
        'minimal technical skills': '最少技术技能的行为者进行复杂网络犯罪的门槛',
        
        '[Claude Code and new admin controls for business plans]': '[Claude Code 和商业计划的新管理控制]',
        'is now available for': '现在可供',
        'customers through': '客户通过',
        'premium seats': '高级席位',
        'that include enhanced usage and coding capabilities': '使用，包括增强的使用和编码功能',
        'allowing seamless transitions between ideation and implementation': '允许在构思和实施之间无缝过渡',
        'New admin controls include': '新的管理控制包括',
        'self-serve seat management': '自助席位管理',
        'granular spend controls': '细粒度支出控制',
        'usage analytics': '使用分析',
        'Compliance API': '合规 API',
        'for real-time programmatic access to usage data': '用于实时程序化访问使用数据',
        
        '[Anthropic appoints Hidetoshi Tojo as Head of Japan and announces hiring plans]': '[Anthropic 任命 Hidetoshi Tojo 为日本负责人并宣布招聘计划]',
        'Anthropic appointed': 'Anthropic 任命了',
        'Hidetoshi Tojo': 'Hidetoshi Tojo',
        'as Head of Japan': '为日本负责人',
        'bringing extensive experience from scaling technology companies including': '带来了扩展技术公司的丰富经验，包括',
        'Snowflake': 'Snowflake',
        'Google Cloud': 'Google Cloud',
        'Microsoft': 'Microsoft',
        'across Japan operations': '在日本的运营',
        'The appointment supports Anthropic\'s expansion plans including opening their': '这项任命支持 Anthropic 的扩张计划，包括开设他们的',
        'first Asia office': '第一个亚洲办事处',
        'in': '在',
        'Tokyo': '东京',
        'and hiring local talent to serve Japanese customers': '并雇用当地人才为日本客户服务',
        
        '[Automate security reviews with Claude Code]': '[使用 Claude Code 自动化安全审查]',
        'introduced automated security reviews through a new': '通过新的',
        'command and': '命令和',
        'GitHub Actions': 'GitHub Actions',
        'integration that identifies vulnerabilities like': '集成引入了自动化安全审查，可识别漏洞如',
        'SQL injection': 'SQL 注入',
        'XSS': 'XSS',
        'authentication flaws': '身份验证缺陷',
        'before code reaches production': '在代码进入生产之前',
        'The features allow': '这些功能允许',
        'ad-hoc security analysis': '临时安全分析',
        'from terminals and': '从终端和',
        'automatic pull request reviews': '自动拉取请求审查',
        'with inline comments and fix recommendations': '包含内联评论和修复建议',
    }
    
    # Apply translations
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated news page: {file_path}")

if __name__ == "__main__":
    translate_news()