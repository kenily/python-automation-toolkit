# 🚀 Python Automation Toolkit

Production-ready Python automation scripts for developers and businesses.

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
git clone https://github.com/kenily/python-automation-toolkit.git
cd python-automation-toolkit
pip install -r requirements.txt
```

## 🛠️ Usage

### Email Sorter
```python
from email_sorter import EmailSorter

sorter = EmailSorter(
    imap_server='imap.gmail.com',
    username='your@email.com',
    password='your-password'
)
sorter.run()
```

### PDF Extractor
```python
from pdf_extractor import extract_text

text = extract_text('document.pdf')
print(text)
```

### Social Poster
```python
from social_poster import SocialPoster

poster = SocialPoster()
poster.post_twitter("Hello from Python! 🚀")
```

## 📊 Requirements

- Python 3.8+
- See requirements.txt for dependencies

## 🤝 Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) first.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=kenily/python-automation-toolkit&type=Date)](https://star-history.com/#kenily/python-automation-toolkit&Date)

---

**Made with ❤️ for developers**

#Python #Automation #Productivity #OpenSource #DevTools
