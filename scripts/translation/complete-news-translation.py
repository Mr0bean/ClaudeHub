#!/usr/bin/env python3
import re

def complete_news_translation():
    file_path = 'final-site/docs/claude-news.md'
    
    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix all remaining English text
    translations = {
        # Fix partially translated words
        ' in': ' ',
        'the ': '',
        ' and ': '和',
        'ing ': '',
        'ed ': '',
        ' on ': '在',
        ' for ': '',
        ' with ': '',
        ' of ': '',
        ' at ': '在',
        ' to ': '',
        ' by ': '由',
        ' from ': '从',
        ' as ': '作为',
        
        # Months not yet translated
        'July': '7月',
        'June': '6月',
        'May': '5月',
        'April': '4月',
        'March': '3月',
        'February': '2月',
        'January': '1月',
        
        # Common terms
        'Category: Policy': '类别：政策',
        'Category: Event': '类别：活动',
        'Category: Societal Impacts': '类别：社会影响',
        
        # Fix specific broken translations
        '在tention': 'intention',
        '在g': 'ing',
        '在': 'in',
        '和': 'and',
        
        # Dates
        'September': '9月',
        'August': '8月',
        
        # Proper translations for common phrases
        'Anthropic announced': 'Anthropic 宣布',
        'Anthropic launched': 'Anthropic 推出',
        'Anthropic introduced': 'Anthropic 推出',
        'Anthropic released': 'Anthropic 发布',
        'Anthropic partnered': 'Anthropic 与',
        
        # Fix specific sections
        'EU\'s General-Purpose AI Code of Practice': '欧盟通用人工智能实践准则',
        'transparency': '透明度',
        'safety': '安全',
        'accountability': '问责制',
        'Safety and Security Frameworks': '安全和保障框架',
        'Responsible Scaling Policy': '负责任扩展政策',
        
        'Paul Smith': 'Paul Smith',
        'first Chief Commercial Officer': '首席商务官',
        'later in': '将于',
        '30 years': '30年',
        'Microsoft': '微软',
        'Salesforce': 'Salesforce',
        'ServiceNow': 'ServiceNow',
        'hundreds of thousands': '数十万',
        'API customers': 'API 客户',
        'growing over': '增长超过',
        '5x': '5倍',
        'two months': '两个月',
        
        'Department of Defense': '国防部',
        '$200 million': '2亿美元',
        'two-year': '两年期',
        'U.S. Department of Defense': '美国国防部',
        'national security applications': '国家安全应用',
        'DOD': '国防部',
        'adversarial AI mitigation': '对抗性AI缓解',
        
        'Richard Fontaine': 'Richard Fontaine',
        'Center for a New American Security': '新美国安全中心',
        'Long-Term Benefit Trust': '长期利益信托',
        'national security experience': '国家安全经验',
        'NSC': '国家安全委员会',
        'State Department': '国务院',
        'Defense Policy Board': '国防政策委员会',
        'AI capabilities': 'AI能力',
        'geopolitical risks': '地缘政治风险',
        
        'Reed Hastings': 'Reed Hastings',
        'Netflix': 'Netflix',
        'co-founder': '联合创始人',
        'former CEO': '前CEO',
        'board of directors': '董事会',
        '25+ years': '25年以上',
        'scaling experience': '扩展经验',
        '$50 million': '5000万美元',
        'AI and Humanity research initiative': 'AI与人类研究计划',
        'Bowdoin College': '鲍登学院',
        
        'four new API capabilities': '四项新的API功能',
        'building AI agents': '构建AI代理',
        'code execution tool': '代码执行工具',
        'Python': 'Python',
        'MCP connector': 'MCP连接器',
        'external system integration': '外部系统集成',
        'Files API': '文件API',
        'document management': '文档管理',
        'prompt caching': '提示缓存',
        'one hour': '一小时',
        'cost-effectively': '经济高效地',
        
        'Research capabilities': '研究功能',
        'multi-step web searches': '多步骤网络搜索',
        'Google Workspace': 'Google Workspace',
        'Gmail': 'Gmail',
        'Calendar': '日历',
        'Google Docs': 'Google文档',
        'agentically': '以代理方式',
        'comprehensive answers': '全面的答案',
        
        'Guillaume Princen': 'Guillaume Princen',
        'Head of EMEA': 'EMEA负责人',
        'Stripe': 'Stripe',
        'European operations': '欧洲运营',
        '12 offices': '12个办事处',
        'Mooncard': 'Mooncard',
        '100 new roles': '100个新职位',
        'sales': '销售',
        'engineering': '工程',
        'research': '研究',
        'operations': '运营',
        'Dublin': '都柏林',
        'London': '伦敦',
        
        'Code with Claude': 'Code with Claude',
        'first developer conference': '首届开发者大会',
        'San Francisco': '旧金山',
        'The Midway': 'The Midway',
        'hands-on event': '实践活动',
        'Anthropic API': 'Anthropic API',
        'CLI tools': 'CLI工具',
        'Model Context Protocol (MCP)': '模型上下文协议(MCP)',
        'interactive workshops': '互动研讨会',
        'product roadmap': '产品路线图',
        'networking opportunities': '社交机会',
        
        'Frontier Red Team': '前沿红队',
        'cybersecurity': '网络安全',
        'biology': '生物学',
        'high school': '高中',
        'undergraduate level': '本科水平',
        'CTF challenges': 'CTF挑战',
        'one year': '一年',
        'early warning signs': '早期预警信号',
        'dual-use capabilities': '双重用途能力',
        'expert baselines': '专家基线',
        
        '1,000 Scientist AI Jam': '1000名科学家AI大会',
        'National Laboratories': '国家实验室',
        'Claude 3.7 Sonnet': 'Claude 3.7 Sonnet',
        'scientific research': '科学研究',
        'hypothesis generation': '假设生成',
        'experiment planning': '实验规划',
        'result analysis': '结果分析',
        
        'Transparency Hub': '透明度中心',
        'safety protocols': '安全协议',
        'risk mitigation strategies': '风险缓解策略',
        'platform abuse detection': '平台滥用检测',
        'governance policies': '治理政策',
        'banned accounts': '被封账户',
        'appeals': '申诉',
        'government requests': '政府请求',
        
        'Amazon\'s Alexa+': '亚马逊的Alexa+',
        'Chief Product Officer': '首席产品官',
        'Mike Krieger': 'Mike Krieger',
        'integration effort': '集成工作',
        'advanced capabilities': '高级功能',
        'safety features': '安全功能',
        'jailbreaking resistance': '越狱抵抗',
        'Amazon Bedrock': 'Amazon Bedrock',
        
        'Paris AI Action Summit': '巴黎AI行动峰会',
        'Dario Amodei': 'Dario Amodei',
        'democratic societies': '民主社会',
        'CBRN threats': 'CBRN威胁',
        'autonomous AI dangers': '自主AI危险',
        'economic disruption': '经济破坏',
        '2026-2027': '2026-2027年',
        'country of geniuses in a datacenter': '数据中心中的天才之国',
        
        'Lyft': 'Lyft',
        '40 million riders': '4000万乘客',
        '1 million drivers': '100万司机',
        'AI-powered solutions': 'AI驱动的解决方案',
        'early testing': '早期测试',
        'engineering advancement': '工程进步',
        'significant impact': '重大影响',
        'customer care assistant': '客户服务助手',
        'resolution time': '解决时间',
        '87%': '87%',
        'thousands of daily inquiries': '每日数千个查询',
        
        'Citations': '引用',
        'source documents': '源文档',
        'exact sentences': '确切句子',
        'passages': '段落',
        'Google Cloud\'s Vertex AI': 'Google Cloud的Vertex AI',
        '15%': '15%',
        'recall accuracy': '召回准确率',
        
        'ISO 42001': 'ISO 42001',
        'first international standard': '首个国际标准',
        'AI governance': 'AI治理',
        'management systems': '管理系统',
        'one of the first frontier AI labs': '首批前沿AI实验室之一',
        'identifying': '识别',
        'assessing': '评估',
        'mitigating AI risks': '缓解AI风险',
        
        '2024 election cycle': '2024年选举周期',
        '0.5%': '0.5%',
        '1%': '1%',
        'peak election weeks': '选举高峰周',
        'Clio tool': 'Clio工具',
        'usage patterns': '使用模式',
        
        'Claude 3.5 Haiku': 'Claude 3.5 Haiku',
        'AWS Trainium2': 'AWS Trainium2',
        '60%': '60%',
        'inference speeds': '推理速度',
        'model distillation': '模型蒸馏',
        'Claude 3 Haiku': 'Claude 3 Haiku',
        '$0.80': '0.80美元',
        'per million input tokens': '每百万输入令牌',
        '$4': '4美元',
        'per million output tokens': '每百万输出令牌',
        
        'custom styles': '自定义样式',
        'Claude.ai': 'Claude.ai',
        'communication preferences': '通信偏好',
        'tone': '语气',
        'structure': '结构',
        'preset options': '预设选项',
        'Formal': '正式',
        'Concise': '简洁',
        'Explanatory': '解释性',
        'individual workflows': '个人工作流程',
        'writing preferences': '写作偏好',
    }
    
    # Apply all translations
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # Fix remaining specific patterns
    content = re.sub(r'\b在([a-z])', r'in\1', content)
    content = re.sub(r'([a-z])在g\b', r'\1ing', content)
    content = re.sub(r'([a-z])和([a-z])', r'\1 and \2', content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Completed full news translation: {file_path}")

if __name__ == "__main__":
    complete_news_translation()