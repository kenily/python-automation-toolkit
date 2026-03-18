# 🐍 Python Automation Toolkit

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/kenily/python-automation-toolkit?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/kenily/python-automation-toolkit?style=for-the-badge)

**4 powerful automation scripts to save you hours of repetitive work**

[📖 Documentation](#-getting-started) • [🚀 Quick Start](#-installation) • [💬 Feedback](https://github.com/kenily/python-automation-toolkit/discussions)

</div>

---

## ✨ Why This Toolkit?

| Problem | Solution |
|---------|----------|
| Spending hours on repetitive tasks? | Automate them with Python |
| Manual data entry errors? | Let scripts handle it |
| Data sync headaches? | Keep Notion & Sheets in sync |
| Social media management time? | Schedule & post automatically |

**Save 10+ hours every week** with these ready-to-use automation scripts.

---

## 📦 What's Included

### 1. 📧 Email Sorter (`email_sorter.py`)
AI-powered email categorization and sorting.

**Features:**
- Automatic category detection
- CSV import/export
- Custom rules support

**Use cases:**
- Organize inbox by priority
- Filter spam & promotions
- Sort by sender, subject, or date

```python
# Quick example
from email_sorter import EmailSorter

sorter = EmailSorter()
sorter.sort_emails("emails.csv")
```

---

### 2. 📄 PDF Extractor (`pdf_extractor.py`)
Extract text from PDF files with ease.

**Features:**
- Batch processing
- Multiple output formats (TXT, JSON, CSV)
- OCR support for scanned PDFs

**Use cases:**
- Extract invoice data
- Convert documents to text
- Batch process reports

```python
from pdf_extractor import PDFExtractor

extractor = PDFExtractor()
extractor.extract("document.pdf", output="text")
```

---

### 3. 🔄 Notion-Google Sheets Sync (`notion_sheets_sync.py`)
Bidirectional sync between Notion and Google Sheets.

**Features:**
- Real-time sync
- Conflict resolution
- Multiple database support

**Use cases:**
- Keep team data updated
- Create dashboards from Notion
- Backup Notion data to Sheets

```python
from notion_sheets import Sync

sync = Sync("database_id")
sync.run()
```

---

### 4. 📱 Social Media Poster (`social_poster.py`)
Schedule and post to multiple platforms.

**Supported platforms:**
- Twitter/X
- LinkedIn
- (More coming soon)

**Features:**
- Bulk scheduling
- Media support
- Analytics tracking

```python
from social_poster import TwitterPoster

poster = TwitterPoster()
poster.post("Hello world!", schedule="2024-01-01 12:00")
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys (see below)

### Installation

```bash
# Clone the repository
git clone https://github.com/kenily/python-automation-toolkit.git
cd python-automation-toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Each script needs its own configuration. Check the individual script folders for details.

---

## 📋 Requirements

```
pandas>=1.3.0
requests>=2.25.0
beautifulsoup4>=4.9.0
selenium>=3.141.0
google-api-python-client>=1.12.0
notion-client>=0.1.0
python-twitter>=3.5
```

---

## 🤝 Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Support

- 💬 [Discussions](https://github.com/kenily/python-automation-toolkit/discussions)
- 🐛 [Issue Tracker](https://github.com/kenily/python-automation-toolkit/issues)
- 📧 Email: kenily553@gmail.com

---

## ⭐ Show Your Support

If this toolkit helped you, please give it a ⭐️!

---

<div align="center">

**Built with ❤️ by [kenily](https://github.com/kenily)**

</div>
