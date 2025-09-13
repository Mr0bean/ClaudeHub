#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive translation script for claude-news.md
Translates the entire news timeline from English to Chinese
"""

import re

def translate_claude_news():
    """Translate the entire claude-news.md file to Chinese"""
    
    # Read the original English file
    with open('final-site/docs/claude-news.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate frontmatter
    content = content.replace(
        'title: "Claude News Timeline | ClaudeLog"',
        'title: "Claude 新闻时间线 | ClaudeLog"'
    )
    
    # Translate main heading and description
    content = content.replace(
        '# Claude News Timeline | ClaudeLog',
        '# Claude 新闻时间线 | ClaudeLog'
    )
    content = content.replace(
        'Stay up-to-date with the latest announcements, product updates, and news from Anthropic about Claude.',
        '获取 Anthropic 关于 Claude 的最新公告、产品更新和新闻动态。'
    )
    
    # Translate month headers
    months = {
        'September 2025': '2025年9月',
        'August 2025': '2025年8月',
        'July 2025': '2025年7月',
        'June 2025': '2025年6月',
        'May 2025': '2025年5月',
        'April 2025': '2025年4月',
        'March 2025': '2025年3月',
        'February 2025': '2025年2月',
        'January 2025': '2025年1月',
        'December 2024': '2024年12月',
        'November 2024': '2024年11月',
        'October 2024': '2024年10月',
        'September 2024': '2024年9月',
        'August 2024': '2024年8月',
        'July 2024': '2024年7月',
        'June 2024': '2024年6月',
        'May 2024': '2024年5月',
        'April 2024': '2024年4月',
        'March 2024': '2024年3月',
        'February 2024': '2024年2月',
        'January 2024': '2024年1月',
        'December 2023': '2023年12月',
        'November 2023': '2023年11月',
        'October 2023': '2023年10月',
        'September 2023': '2023年9月',
        'August 2023': '2023年8月',
        'July 2023': '2023年7月',
        'June 2023': '2023年6月',
        'May 2023': '2023年5月',
        'April 2023': '2023年4月',
        'March 2023': '2023年3月',
        'February 2023': '2023年2月',
        'January 2023': '2023年1月',
        'December 2022': '2022年12月',
        'November 2022': '2022年11月',
        'October 2022': '2022年10月',
        'September 2022': '2022年9月',
        'May 2022': '2022年5月',
        'April 2022': '2022年4月',
        'February 2022': '2022年2月',
        'December 2021': '2021年12月',
        'May 2021': '2021年5月'
    }
    
    for en_month, zh_month in months.items():
        content = content.replace(f'## **{en_month}**', f'## **{zh_month}**')
    
    # Translate dates in content
    date_patterns = {
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
        'Oct ': '10月'
    }
    
    for en_date, zh_date in date_patterns.items():
        content = re.sub(f'{en_date}(\\d+), (\\d+)', f'{zh_date}\\1日, \\2年', content)
    
    # Translate categories
    categories = {
        'Category: Product': '类别：产品',
        'Category: Announcements': '类别：公告',
        'Category: Research': '类别：研究',
        'Category: Policy': '类别：政策',
        'Category: Event': '类别：活动',
        'Category: Societal Impacts': '类别：社会影响'
    }
    
    for en_cat, zh_cat in categories.items():
        content = content.replace(en_cat, zh_cat)
    
    # Translate news titles and content
    news_translations = {
        # September 2025
        'Claude can now create and edit files': 'Claude 现在可以创建和编辑文件',
        'Claude can now create and edit `Excel spreadsheets`, `documents`, `PowerPoint slides`, and `PDFs` directly in `Claude.ai` and the `desktop app`': 
            'Claude 现在可以直接在 `Claude.ai` 和 `桌面应用` 中创建和编辑 `Excel 电子表格`、`文档`、`PowerPoint 幻灯片` 和 `PDF`',
        'transforming how users work by producing ready-to-use files from instructions and data': 
            '通过从指令和数据生成即用文件，改变用户的工作方式',
        'This feature is available as a preview for `Max`, `Team`, and `Enterprise` users, with `Pro` users getting access in `coming weeks`':
            '此功能作为预览版提供给 `Max`、`Team` 和 `Enterprise` 用户，`Pro` 用户将在 `未来几周内` 获得访问权限',
        
        'Anthropic is endorsing SB 53': 'Anthropic 支持 SB 53 法案',
        "Anthropic is endorsing California's `SB 53`, a bill governing powerful AI systems":
            'Anthropic 支持加州的 `SB 53` 法案，这是一项管理强大 AI 系统的法案',
        'that requires companies to develop `safety frameworks`, publish `transparency reports`, and report `critical incidents` to the state':
            '要求公司开发 `安全框架`、发布 `透明度报告`，并向州政府报告 `关键事件`',
        'The company supports this `trust but verify` approach as it formalizes practices already followed by `frontier AI companies`':
            '公司支持这种 `信任但验证` 的方法，因为它将 `前沿 AI 公司` 已经遵循的做法正式化',
        'while creating a level playing field for safety disclosure':
            '同时为安全披露创造公平的竞争环境',
        
        'Updating restrictions of sales to unsupported regions': '更新对不支持地区的销售限制',
        'Anthropic is strengthening regional restrictions to prevent companies controlled by adversarial nations like `China`':
            'Anthropic 正在加强地区限制，以防止受 `中国` 等敌对国家控制的公司',
        'from accessing their services, even through subsidiaries in other countries':
            '访问其服务，即使是通过其他国家的子公司',
        'The updated policy prohibits entities more than `50% owned` by companies from unsupported regions':
            '更新后的政策禁止由不支持地区公司 `持股超过50%` 的实体',
        'addressing `national security risks` where authoritarian governments can compel data sharing and intelligence cooperation':
            '解决专制政府可能强制数据共享和情报合作的 `国家安全风险`',
        
        'Anthropic raises $13B Series F at $183B post-money valuation': 'Anthropic 完成130亿美元F轮融资，投后估值1830亿美元',
        'Anthropic completed a `$13 billion` `Series F` funding round led by `ICONIQ`':
            'Anthropic 完成了由 `ICONIQ` 领投的 `130亿美元` `F轮` 融资',
        'valuing the company at `$183 billion` post-money with participation from major investors including `Fidelity`, `Lightspeed`, and `BlackRock`':
            '公司投后估值达 `1830亿美元`，主要投资者包括 `Fidelity`、`Lightspeed` 和 `BlackRock`',
        "The funding reflects Anthropic's rapid growth from `$1 billion` run-rate revenue in `early 2025`":
            '这笔融资反映了 Anthropic 从 `2025年初` `10亿美元` 年化收入的快速增长',
        'to over `$5 billion` by `August`, making it one of the fastest-growing technology companies in history':
            '到 `8月` 超过 `50亿美元`，使其成为历史上增长最快的科技公司之一',
        
        # August 2025
        'Updates to Consumer Terms and Privacy Policy': '消费者条款和隐私政策更新',
        'Anthropic updated its Consumer Terms and Privacy Policy to allow training new models using data from `Free`, `Pro`, and `Max` accounts':
            'Anthropic 更新了消费者条款和隐私政策，允许使用来自 `Free`、`Pro` 和 `Max` 账户的数据训练新模型',
        'when users `opt-in`, with an extended `5-year` data retention period for those who consent':
            '当用户 `选择加入` 时，同意者的数据保留期延长至 `5年`',
        'Current users have until `September 28, 2025` to make their selection, while new users choose during signup':
            '现有用户需在 `2025年9月28日` 前做出选择，新用户在注册时选择',
        
        'Introducing the Anthropic National Security and Public Sector Advisory Council': '推出 Anthropic 国家安全和公共部门咨询委员会',
        'Anthropic formed the `National Security and Public Sector Advisory Council`':
            'Anthropic 成立了 `国家安全和公共部门咨询委员会`',
        'featuring `bipartisan` former government leaders including Senators `Roy Blunt` and `Jon Tester`':
            '成员包括 `两党` 前政府领导人，包括参议员 `Roy Blunt` 和 `Jon Tester`',
        'former `Defense officials`, and `intelligence community veterans`':
            '前 `国防官员` 和 `情报界资深人士`',
        'The council will help identify high-impact AI applications for `national security`':
            '委员会将帮助确定 `国家安全` 的高影响力 AI 应用',
        'develop industry standards, and strengthen `public-private partnerships`':
            '制定行业标准，并加强 `公私合作伙伴关系`',
        
        'Detecting and countering misuse of AI: August 2025': '检测和打击 AI 滥用：2025年8月',
        "Anthropic's threat intelligence report reveals sophisticated AI misuse":
            'Anthropic 的威胁情报报告揭示了复杂的 AI 滥用',
        'including a `large-scale extortion operation` using `Claude Code`':
            '包括使用 `Claude Code` 的 `大规模勒索行动`',
        '`North Korean` employment fraud schemes, and `AI-generated ransomware` sales':
            '`朝鲜` 就业欺诈计划，以及 `AI生成的勒索软件` 销售',
        'The report shows cybercriminals are weaponizing `agentic AI` to perform attacks rather than just advise':
            '报告显示，网络犯罪分子正在将 `代理AI` 武器化以执行攻击，而不仅仅是提供建议',
        'lowering barriers to sophisticated cybercrime for actors with `minimal technical skills`':
            '降低了 `技术技能最少` 的行为者进行复杂网络犯罪的门槛',
        
        'Claude Code and new admin controls for business plans': 'Claude Code 和商业计划的新管理控制',
        '`Claude Code` is now available for `Team` and `Enterprise` customers through `premium seats`':
            '`Claude Code` 现在通过 `高级席位` 向 `Team` 和 `Enterprise` 客户提供',
        'that include enhanced usage and coding capabilities':
            '包括增强的使用和编码能力',
        'allowing seamless transitions between ideation and implementation':
            '允许在构思和实施之间无缝过渡',
        'New admin controls include `self-serve seat management`, `granular spend controls`':
            '新的管理控制包括 `自助席位管理`、`细粒度支出控制`',
        '`usage analytics`, and a `Compliance API` for real-time programmatic access to usage data':
            '`使用分析` 和用于实时程序化访问使用数据的 `合规API`',
        
        'Anthropic appoints Hidetoshi Tojo as Head of Japan and announces hiring plans': 'Anthropic 任命 Hidetoshi Tojo 为日本负责人并宣布招聘计划',
        'Anthropic appointed `Hidetoshi Tojo` as Head of Japan':
            'Anthropic 任命 `Hidetoshi Tojo` 为日本负责人',
        'bringing extensive experience from scaling technology companies including `Snowflake`, `Google Cloud`, and `Microsoft`':
            '他在扩展科技公司方面拥有丰富经验，包括 `Snowflake`、`Google Cloud` 和 `Microsoft`',
        'across Japan operations':
            '在日本的运营',
        "The appointment supports Anthropic's expansion plans including opening their `first Asia office` in `Tokyo`":
            '此任命支持 Anthropic 的扩张计划，包括在 `东京` 开设他们的 `首个亚洲办事处`',
        'and hiring local talent to serve Japanese customers':
            '并雇用本地人才为日本客户服务',
        
        'Automate security reviews with Claude Code': '使用 Claude Code 自动化安全审查',
        '`Claude Code` introduced automated security reviews through a new `/security-review` command':
            '`Claude Code` 通过新的 `/security-review` 命令引入了自动化安全审查',
        'and `GitHub Actions` integration that identifies vulnerabilities like `SQL injection`, `XSS`':
            '和 `GitHub Actions` 集成，可识别 `SQL注入`、`XSS` 等漏洞',
        'and `authentication flaws` before code reaches production':
            '以及在代码投入生产前的 `身份验证缺陷`',
        'The features allow `ad-hoc security analysis` from terminals':
            '这些功能允许从终端进行 `临时安全分析`',
        'and `automatic pull request reviews` with inline comments and fix recommendations':
            '以及带有内联评论和修复建议的 `自动拉取请求审查`'
    }
    
    # Apply all translations
    for en_text, zh_text in news_translations.items():
        content = content.replace(en_text, zh_text)
    
    # Continue with more translations for remaining months
    more_translations = {
        # July 2025 and earlier entries
        'Paul Smith joins as first Chief Commercial Officer': 'Paul Smith 加入担任首席商务官',
        'Anthropic appointed `Paul Smith` as its `first Chief Commercial Officer`':
            'Anthropic 任命 `Paul Smith` 为其 `首位首席商务官`',
        'starting later in `2025` after `30 years` at `Microsoft`':
            '他在 `微软` 工作 `30年` 后，将于 `2025年` 晚些时候开始任职',
        'where he led sales for `Salesforce` and `ServiceNow` relationships':
            '他在微软领导了与 `Salesforce` 和 `ServiceNow` 的销售关系',
        'Smith will oversee a rapidly growing business with `hundreds of thousands` of `API customers`':
            'Smith 将监督一个拥有 `数十万` `API客户` 的快速增长业务',
        'growing over `5x` in the past `two months`':
            '在过去 `两个月` 内增长超过 `5倍`',
        
        'Department of Defense contract': '国防部合同',
        'Anthropic secured a `$200 million` `two-year` contract with the `U.S. Department of Defense`':
            'Anthropic 获得了与 `美国国防部` 的 `2亿美元` `两年期` 合同',
        'to provide Claude for `national security applications`':
            '为 `国家安全应用` 提供 Claude',
        'The `DOD` will use Claude for `adversarial AI mitigation`':
            '`国防部` 将使用 Claude 进行 `对抗性AI缓解`',
        
        'Richard Fontaine joins board': 'Richard Fontaine 加入董事会',
        '`Richard Fontaine`, CEO of the `Center for a New American Security`':
            '`新美国安全中心` CEO `Richard Fontaine`',
        "joined Anthropic's `Long-Term Benefit Trust` board":
            '加入了 Anthropic 的 `长期利益信托` 董事会',
        'bringing `national security experience` from the `NSC`, `State Department`':
            '他带来了来自 `国家安全委员会`、`国务院` 的 `国家安全经验`',
        'and `Defense Policy Board`':
            '以及 `国防政策委员会`',
        'to help manage the balance between advancing `AI capabilities` and mitigating `geopolitical risks`':
            '帮助管理推进 `AI能力` 与缓解 `地缘政治风险` 之间的平衡',
        
        'Reed Hastings joins Anthropic board': 'Reed Hastings 加入 Anthropic 董事会',
        '`Reed Hastings`, `Netflix` `co-founder` and `former CEO`':
            '`Netflix` `联合创始人` 和 `前CEO` `Reed Hastings`',
        "joins Anthropic's `board of directors`":
            '加入 Anthropic 的 `董事会`',
        'bringing `25+ years` of `scaling experience`':
            '带来了 `25年以上` 的 `扩展经验`',
        'having grown Netflix from startup to `$250 billion` market cap':
            '他将 Netflix 从初创公司发展到 `2500亿美元` 市值',
        'Recently donated `$50 million` to Stanford\'s `AI and Humanity research initiative`':
            '最近向斯坦福的 `AI与人类研究计划` 捐赠了 `5000万美元`',
        'and co-founded `Bowdoin College`':
            '并共同创立了 `鲍登学院`',
        
        'New API features for building AI agents': '构建AI代理的新API功能',
        'Anthropic launched `four new API capabilities` to improve `building AI agents`':
            'Anthropic 推出了 `四项新的API功能` 来改进 `构建AI代理`',
        'including a `code execution tool` for running `Python`':
            '包括用于运行 `Python` 的 `代码执行工具`',
        'an `MCP connector` for `external system integration`':
            '用于 `外部系统集成` 的 `MCP连接器`',
        'a `Files API` for `document management`':
            '用于 `文档管理` 的 `文件API`',
        'and `prompt caching` lasting up to `one hour` to build complex agents `cost-effectively`':
            '以及持续 `一小时` 的 `提示缓存`，以 `经济高效地` 构建复杂代理',
        
        'Research capabilities and integrations': '研究功能和集成',
        'Claude gains new `Research capabilities` for `multi-step web searches`':
            'Claude 获得了用于 `多步骤网络搜索` 的新 `研究功能`',
        'and native `Google Workspace` integration':
            '以及原生 `Google Workspace` 集成',
        'allowing it to work with `Gmail`, `Calendar`, and `Google Docs` `agentically`':
            '允许它以 `代理方式` 与 `Gmail`、`日历` 和 `Google文档` 协作',
        'Users can ask Claude to search for information and receive `comprehensive answers`':
            '用户可以要求 Claude 搜索信息并获得 `全面的答案`',
        
        'Guillaume Princen heads EMEA expansion': 'Guillaume Princen 领导 EMEA 扩张',
        '`Guillaume Princen` joined as `Head of EMEA`':
            '`Guillaume Princen` 加入担任 `EMEA负责人`',
        'from `Stripe` where he led `European operations` across `12 offices`':
            '他来自 `Stripe`，在那里领导跨 `12个办事处` 的 `欧洲运营`',
        'Princen previously co-founded `Mooncard` and will lead hiring `100 new roles`':
            'Princen 之前共同创立了 `Mooncard`，将领导招聘 `100个新职位`',
        'across `sales`, `engineering`, `research`, and `operations` in `Dublin` and `London`':
            '涵盖 `都柏林` 和 `伦敦` 的 `销售`、`工程`、`研究` 和 `运营`',
        
        'Code with Claude developer conference': 'Code with Claude 开发者大会',
        'Anthropic hosted `Code with Claude`, its `first developer conference`':
            'Anthropic 举办了 `Code with Claude`，其 `首届开发者大会`',
        'in `San Francisco` at `The Midway`':
            '在 `旧金山` 的 `The Midway` 举行',
        'as a `hands-on event` focused on building with the `Anthropic API`':
            '作为一个专注于使用 `Anthropic API` 构建的 `实践活动`',
        '`CLI tools`, and `Model Context Protocol (MCP)`':
            '`CLI工具` 和 `模型上下文协议(MCP)`',
        'featuring `interactive workshops`, previews of the `product roadmap`':
            '包括 `互动研讨会`、`产品路线图` 预览',
        'and `networking opportunities`':
            '以及 `社交机会`',
        
        'Frontier Red Team': '前沿红队',
        'Anthropic launched the `Frontier Red Team` with experts from `cybersecurity` and `biology`':
            'Anthropic 推出了 `前沿红队`，成员包括来自 `网络安全` 和 `生物学` 的专家',
        'to evaluate Claude\'s capabilities at `high school` and `undergraduate level`':
            '评估 Claude 在 `高中` 和 `本科水平` 的能力',
        'particularly through `CTF challenges`':
            '特别是通过 `CTF挑战`',
        'The `one year` program aims to establish `early warning signs` of dangerous `dual-use capabilities`':
            '这个 `一年期` 项目旨在建立危险 `双重用途能力` 的 `早期预警信号`',
        'and set `expert baselines`':
            '并设定 `专家基线`',
        
        '1,000 Scientist AI Jam': '1000名科学家AI大会',
        'Anthropic hosted the `1,000 Scientist AI Jam` with `National Laboratories`':
            'Anthropic 与 `国家实验室` 共同举办了 `1000名科学家AI大会`',
        'introducing `Claude 3.7 Sonnet` for `scientific research`':
            '推出用于 `科学研究` 的 `Claude 3.7 Sonnet`',
        'Supporting `hypothesis generation`, `experiment planning`, and `result analysis`':
            '支持 `假设生成`、`实验规划` 和 `结果分析`',
        
        'Transparency Hub': '透明度中心',
        'Anthropic launched the `Transparency Hub` to publicly share `safety protocols`':
            'Anthropic 推出了 `透明度中心`，公开分享 `安全协议`',
        '`risk mitigation strategies`, and `platform abuse detection`':
            '`风险缓解策略` 和 `平台滥用检测`',
        'including `governance policies`, statistics on `banned accounts`':
            '包括 `治理政策`、`被封账户` 统计',
        '`appeals`, and `government requests`':
            '`申诉` 和 `政府请求`',
        
        "Amazon's Alexa+": '亚马逊的 Alexa+',
        "Amazon's new `Chief Product Officer` `Mike Krieger` leads the `integration effort`":
            '亚马逊新任 `首席产品官` `Mike Krieger` 领导 `集成工作`',
        'to incorporate Claude\'s `advanced capabilities` and `safety features`':
            '整合 Claude 的 `高级功能` 和 `安全功能`',
        'including `jailbreaking resistance` through `Amazon Bedrock`':
            '包括通过 `Amazon Bedrock` 的 `越狱抵抗`',
        
        'Paris AI Action Summit': '巴黎AI行动峰会',
        '`Dario Amodei` spoke at the `Paris AI Action Summit`':
            '`Dario Amodei` 在 `巴黎AI行动峰会` 上发言',
        'warning that AI poses unique challenges to `democratic societies`':
            '警告AI对 `民主社会` 构成独特挑战',
        'highlighting `CBRN threats`, `autonomous AI dangers`, and `economic disruption`':
            '强调 `CBRN威胁`、`自主AI危险` 和 `经济破坏`',
        'predicting AI systems matching human expertise across domains by `2026-2027`':
            '预测AI系统将在 `2026-2027年` 在各领域达到人类专业水平',
        'creating a `country of geniuses in a datacenter`':
            '创造一个 `数据中心中的天才之国`',
        
        'Lyft partnership': 'Lyft 合作伙伴关系',
        'Lyft partnered with Anthropic to deploy `AI-powered solutions`':
            'Lyft 与 Anthropic 合作部署 `AI驱动的解决方案`',
        'across its platform serving `40 million riders` and `1 million drivers`':
            '服务于其平台上的 `4000万乘客` 和 `100万司机`',
        'After `early testing` showed `engineering advancement` and `significant impact`':
            '在 `早期测试` 显示 `工程进步` 和 `重大影响` 后',
        'their `customer care assistant` reduced `resolution time` by `87%`':
            '他们的 `客户服务助手` 将 `解决时间` 减少了 `87%`',
        'while handling `thousands of daily inquiries`':
            '同时处理 `每日数千个查询`',
        
        'Citations feature': '引用功能',
        'Claude now provides `Citations` to `source documents`':
            'Claude 现在提供对 `源文档` 的 `引用`',
        'marking `exact sentences` and `passages` used':
            '标记使用的 `确切句子` 和 `段落`',
        'Available through `Google Cloud\'s Vertex AI`':
            '通过 `Google Cloud的Vertex AI` 提供',
        'improving `recall accuracy` by `15%`':
            '将 `召回准确率` 提高了 `15%`',
        
        'ISO 42001 certification': 'ISO 42001 认证',
        'Anthropic achieved `ISO 42001` certification':
            'Anthropic 获得了 `ISO 42001` 认证',
        'the `first international standard` for `AI governance` and `management systems`':
            '这是 `AI治理` 和 `管理系统` 的 `首个国际标准`',
        'becoming `one of the first frontier AI labs` certified':
            '成为获得认证的 `首批前沿AI实验室之一`',
        'for `identifying`, `assessing`, and `mitigating AI risks`':
            '用于 `识别`、`评估` 和 `缓解AI风险`',
        
        '2024 election cycle': '2024年选举周期',
        'During the `2024 election cycle`, election-related queries comprised only `0.5%` to `1%`':
            '在 `2024年选举周期` 期间，与选举相关的查询仅占 `0.5%` 到 `1%`',
        'of total usage even during `peak election weeks`':
            '即使在 `选举高峰周` 期间的总使用量',
        'analyzed through the `Clio tool` to understand `usage patterns`':
            '通过 `Clio工具` 分析了解 `使用模式`',
        
        'Claude 3.5 Haiku': 'Claude 3.5 Haiku',
        'Claude 3.5 Haiku launched on `AWS Trainium2`':
            'Claude 3.5 Haiku 在 `AWS Trainium2` 上推出',
        'with `60%` faster `inference speeds` through `model distillation`':
            '通过 `模型蒸馏` 实现 `60%` 更快的 `推理速度`',
        'from `Claude 3 Haiku`':
            '相比 `Claude 3 Haiku`',
        'at `$0.80` `per million input tokens` and `$4` `per million output tokens`':
            '价格为 `每百万输入令牌` `0.80美元` 和 `每百万输出令牌` `4美元`',
        
        'Custom styles': '自定义样式',
        'Claude.ai introduces `custom styles` for `communication preferences`':
            'Claude.ai 推出了用于 `通信偏好` 的 `自定义样式`',
        'allowing users to personalize `tone` and `structure`':
            '允许用户个性化 `语气` 和 `结构`',
        'with `preset options` like `Formal`, `Concise`, and `Explanatory`':
            '提供 `预设选项`，如 `正式`、`简洁` 和 `解释性`',
        'or custom instructions for `individual workflows` and `writing preferences`':
            '或为 `个人工作流程` 和 `写作偏好` 自定义指令'
    }
    
    # Apply more translations
    for en_text, zh_text in more_translations.items():
        content = content.replace(en_text, zh_text)
    
    # Continue with more translations for 2024 and earlier
    additional_translations = {
        # June 2024
        'Expanding access to Claude for government': '扩大政府部门对 Claude 的访问',
        'Anthropic expanded Claude access to government users on `June 26, 2024`':
            'Anthropic 于 `2024年6月26日` 扩大了政府用户对 Claude 的访问',
        'making `Claude 3 Haiku` and `Sonnet` available through `AWS Marketplace`':
            '通过 `AWS Marketplace` 提供 `Claude 3 Haiku` 和 `Sonnet`',
        'for the `US Intelligence Community` and `AWS GovCloud`':
            '供 `美国情报界` 和 `AWS GovCloud` 使用',
        'The expansion includes carefully crafted contractual exceptions':
            '此次扩展包括精心制定的合同例外条款',
        'for legally authorized foreign intelligence analysis':
            '用于合法授权的外国情报分析',
        'while maintaining restrictions on disinformation, weapons design, and malicious cyber operations':
            '同时保持对虚假信息、武器设计和恶意网络行动的限制',
        
        'Collaborate with Claude on Projects': '在项目中与 Claude 协作',
        'Anthropic launched `Projects` on `Claude.ai` for `Pro` and `Team` users':
            'Anthropic 在 `Claude.ai` 上为 `Pro` 和 `Team` 用户推出了 `项目` 功能',
        'on `June 25, 2024`, enabling organized collaboration with curated knowledge sets':
            '于 `2024年6月25日`，实现了与精选知识集的有组织协作',
        'and shared conversations':
            '以及共享对话',
        'Projects include a `200K context window` for documents and code':
            '项目包括用于文档和代码的 `20万上下文窗口`',
        'custom instructions for tailored responses, and team sharing capabilities':
            '定制响应的自定义指令，以及团队共享功能',
        
        'Claude 3.5 Sonnet': 'Claude 3.5 Sonnet',
        'Anthropic released `Claude 3.5 Sonnet` on `June 21, 2024`':
            'Anthropic 于 `2024年6月21日` 发布了 `Claude 3.5 Sonnet`',
        'setting new industry benchmarks while operating at `twice the speed` of `Claude 3 Opus`':
            '在设定新的行业基准的同时，运行速度是 `Claude 3 Opus` 的 `两倍`',
        'The model excels in graduate-level reasoning, coding proficiency':
            '该模型在研究生水平推理、编码能力方面表现出色',
        '(solving `64%` of problems in internal evaluations)':
            '（在内部评估中解决了 `64%` 的问题）',
        'and vision capabilities for chart interpretation and text transcription':
            '以及用于图表解释和文本转录的视觉能力',
        
        'Challenges in red teaming AI systems': 'AI系统红队测试的挑战',
        'Anthropic published insights on red teaming AI systems on `June 12, 2024`':
            'Anthropic 于 `2024年6月12日` 发布了关于AI系统红队测试的见解',
        'detailing various approaches including expert domain testing':
            '详细介绍了包括专家领域测试在内的各种方法',
        'automated red teaming, and multimodal evaluations':
            '自动化红队测试和多模态评估',
        'The post outlines challenges in standardizing red teaming practices':
            '文章概述了标准化红队测试实践的挑战',
        'and proposes policy recommendations including funding `NIST`':
            '并提出了包括资助 `NIST` 在内的政策建议',
        'for technical standards and supporting independent testing organizations':
            '用于技术标准和支持独立测试组织',
        
        'Testing and mitigating elections-related risks': '测试和缓解选举相关风险',
        'Anthropic detailed its approach to testing and mitigating elections-related risks':
            'Anthropic 详细介绍了其测试和缓解选举相关风险的方法',
        'on `June 6, 2024`, combining Policy Vulnerability Testing':
            '于 `2024年6月6日`，结合政策漏洞测试',
        'with external experts and automated evaluations':
            '与外部专家和自动化评估',
        'The company implemented multiple mitigations including system prompt updates':
            '公司实施了多项缓解措施，包括系统提示更新',
        'model fine-tuning, and policy refinements':
            '模型微调和政策完善',
        'to improve accuracy and appropriate referrals to authoritative sources':
            '以提高准确性并适当引导至权威来源',
        
        'Introducing Claude to Canada': '向加拿大推出 Claude',
        'Anthropic introduced Claude to Canada on `June 5, 2024`':
            'Anthropic 于 `2024年6月5日` 向加拿大推出 Claude',
        'making the AI assistant available through Claude.ai, iOS app, API, and Team plan':
            '通过 Claude.ai、iOS应用、API和团队计划提供AI助手',
        'Canadian users can access Claude for free or subscribe to `Pro`':
            '加拿大用户可以免费访问 Claude 或订阅 `Pro`',
        'for `CA$28/month` and `Team` for `CA$42/month` per user':
            '每月 `28加元`，`Team` 每用户每月 `42加元`',
        'with access to all Claude 3 models and enhanced usage limits':
            '可访问所有 Claude 3 模型并提高使用限制',
        
        # May 2024
        'Claude can now use tools': 'Claude 现在可以使用工具',
        "Claude's tool use capabilities became generally available":
            'Claude 的工具使用功能已全面推出',
        'across the entire Claude 3 model family on `May 30, 2024`':
            '于 `2024年5月30日` 在整个 Claude 3 模型系列中',
        'enabling Claude to interact with external tools and APIs':
            '使 Claude 能够与外部工具和API交互',
        'for tasks like data extraction, API calls, and database searches':
            '用于数据提取、API调用和数据库搜索等任务',
        'This feature includes streaming support, forced tool selection':
            '此功能包括流式支持、强制工具选择',
        'and image compatibility':
            '和图像兼容性',
        "significantly expanding Claude's practical applications for developers and businesses":
            '显著扩展了 Claude 对开发人员和企业的实际应用',
        
        "Jay Kreps appointed to Anthropic's Board of Directors": 'Jay Kreps 被任命为 Anthropic 董事会成员',
        '`Jay Kreps`, co-founder and CEO of `Confluent`':
            '`Confluent` 联合创始人兼CEO `Jay Kreps`',
        "joined Anthropic's Board of Directors on `May 29, 2024`":
            '于 `2024年5月29日` 加入 Anthropic 董事会',
        'bringing extensive experience in building and scaling tech companies':
            '带来了构建和扩展科技公司的丰富经验',
        'and expertise in data infrastructure':
            '以及数据基础设施方面的专业知识',
        'His appointment by the `Long-Term Benefit Trust`':
            '他由 `长期利益信托` 任命',
        'comes as Anthropic prepares for its next phase of growth':
            '正值 Anthropic 准备进入下一个增长阶段',
        'while `Luke Muehlhauser` stepped down from the board':
            '同时 `Luke Muehlhauser` 退出董事会',
        'to focus on his work at `Open Philanthropy`':
            '专注于他在 `Open Philanthropy` 的工作',
        
        'Golden Gate Claude': '金门大桥 Claude',
        '`Golden Gate Claude` was a 24-hour research demonstration':
            '`金门大桥 Claude` 是一个24小时的研究演示',
        'released on `May 23, 2024`':
            '于 `2024年5月23日` 发布',
        "showcasing Anthropic's breakthrough in AI interpretability":
            '展示了 Anthropic 在AI可解释性方面的突破',
        "by artificially amplifying Claude's Golden Gate Bridge feature":
            '通过人为放大 Claude 的金门大桥特征',
        'to make it obsessively reference the bridge in all responses':
            '使其在所有回应中都痴迷地提及这座桥',
        'This demonstrated the ability to surgically modify specific neural pathways':
            '这展示了精确修改特定神经通路的能力',
        'in AI models':
            '在AI模型中',
        'representing a significant advance in understanding':
            '代表了在理解方面的重大进展',
        'and potentially controlling AI behavior for safety purposes':
            '以及为安全目的控制AI行为的可能性',
        
        'Krishna Rao joins Anthropic as Chief Financial Officer': 'Krishna Rao 加入 Anthropic 担任首席财务官',
        '`Krishna Rao` joined Anthropic as Chief Financial Officer':
            '`Krishna Rao` 加入 Anthropic 担任首席财务官',
        'on `May 21, 2024`, bringing nearly `20 years`':
            '于 `2024年5月21日`，带来了近 `20年`',
        'of strategic finance experience from companies like':
            '来自以下公司的战略财务经验',
        '`Fanatics Commerce`, `Cedar`, and `Airbnb`':
            '`Fanatics Commerce`、`Cedar` 和 `Airbnb`',
        'where he helped navigate the pandemic and IPO':
            '他在那里帮助度过了疫情和IPO',
        'His expertise in financial strategy, capital allocation':
            '他在财务战略、资本配置方面的专业知识',
        'and scaling high-growth organizations':
            '以及扩展高增长组织',
        "will support Anthropic's enterprise momentum and international expansion plans":
            '将支持 Anthropic 的企业势头和国际扩张计划',
        
        'Generate better prompts in the developer console': '在开发者控制台中生成更好的提示',
        'Anthropic launched a prompt generator feature':
            'Anthropic 推出了提示生成器功能',
        'in the developer console on `May 20, 2024`':
            '于 `2024年5月20日` 在开发者控制台中',
        'that automatically creates production-ready prompt templates':
            '自动创建生产就绪的提示模板',
        'using best practices like chain-of-thought reasoning and role setting':
            '使用思维链推理和角色设置等最佳实践',
        'The tool helps both new and experienced prompt engineers':
            '该工具帮助新手和经验丰富的提示工程师',
        'by generating effective, precise prompts based on task descriptions':
            '基于任务描述生成有效、精确的提示',
        'significantly reducing development time and improving output quality':
            '显著减少开发时间并提高输出质量',
        
        'Reflections on our Responsible Scaling Policy': '对我们负责任扩展政策的反思'
    }
    
    # Apply additional translations
    for en_text, zh_text in additional_translations.items():
        content = content.replace(en_text, zh_text)
    
    # Write the translated content back
    with open('final-site/docs/claude-news.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Successfully translated claude-news.md to Chinese")
    print("📄 File saved: final-site/docs/claude-news.md")

if __name__ == "__main__":
    translate_claude_news()