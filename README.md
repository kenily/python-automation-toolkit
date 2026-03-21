# 🚀 OpenCLI

Production-ready automation CLI tools for developers and businesses.

## ✨ Features

### 📧 Email Sorter
- Automatic email categorization by keywords, sender, and patterns
- IMAP support for major email providers
- Custom sorting rules

### 📄 PDF Extractor
- Extract text from PDF files
- Batch processing support
- Multiple output formats (TXT, JSON, CSV)

### 🌐 Social Media Poster
- Multi-platform support (Twitter, LinkedIn, Reddit)
- Scheduled posting
- Content templates

### 🔄 Notion-Google Sheets Sync
- Two-way sync between Notion databases and Google Sheets
- Real-time updates
- Custom field mapping

## 📦 Installation

```bash
npm install -g opencli
```

## 🛠️ Usage

```bash
# Email Sorter
opencli email-sort --config config.json

# PDF Extractor
opencli pdf-extract document.pdf

# Social Poster
opencli post --twitter "Hello world!"

# Notion-Sheets Sync
opencli sync notion --sheet "Data"
```

## 📊 Requirements

- Node.js 18+
- npm 9+

## 🤝 Contributing

Contributions welcome! Please read our [contributing guidelines](CONTRIBUTING.md) first.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🛠️ Configuration

### Email Sorter Configuration (config.json)
```json
{
  "imap": {
    "host": "imap.example.com",
    "port": 993,
    "user": "your@email.com",
    "password": "your-password"
  },
  "rules": [
    {"from": "newsletter@*, "folder": "Newsletters"},
    {"subject": "invoice*", "folder": "Invoices"},
    {"keyword": "urgent", "priority": "high"}
  ]
}
```

### Environment Variables
```bash
export OPENCLI_EMAIL_USER="your@email.com"
export OPENCLI_EMAIL_PASS="your-password"
export OPENCLI_NOTION_TOKEN="your-notion-token"
export OPENCLI_SHEETS_CREDENTIALS="./credentials.json"
```

## 📊 Examples

### Batch PDF Processing
```bash
opencli pdf-extract ./invoices/*.pdf --output json --batch
```

### Scheduled Social Posting
```bash
opencli post schedule --twitter "Hello" --time "2024-01-01 10:00:00"
```

### Notion-Sheets Sync
```bash
opencli sync notion --db "My Database" --sheet "Sheet1" --auto
```

## 🔧 Development

```bash
# Clone and setup
git clone https://github.com/kenily/python-automation-toolkit.git
cd python-automation-toolkit
npm install

# Run tests
npm test

# Build
npm run build
```

## 📈 Roadmap

- [ ] AI-powered email responses
- [ ] More social platforms (Instagram, TikTok)
- [ ] Webhook integrations
- [ ] Cloud deployment guides

---

**Made with ❤️ for developers**

#OpenCLI #Automation #Productivity #NodeJS #OpenSource

## 🧠 Obsidian CLI

让AI真正"看懂"你的知识网络！

### 功能
- **智能搜索**: 一行命令找出所有同时涉及多个关键词的笔记
- **知识图谱**: 自动生成笔记间关系图谱
- **双向链分析**: 理解笔记间的链接关系
- **标签聚合**: 按标签组织和发现相关内容

### 安装
```bash
npm install -g opencli
opencli obsidian init
```

### 使用
```bash
# 搜索笔记
opencli obsidian search "AI + 知识管理"

# 生成图谱
opencli obsidian graph

# 分析链接
opencli obsidian links
```
