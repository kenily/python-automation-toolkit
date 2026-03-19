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
