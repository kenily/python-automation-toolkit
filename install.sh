#!/bin/bash
# Python Automation Toolkit - 一键安装
# Usage: curl -fsSL https://kenily.github.io/python-automation-toolkit/install.sh | sh

set -e

echo "🚀 Installing Python Automation Toolkit..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q requests beautifulsoup4 python-dotenv schedule

# Create automation scripts
mkdir -p ~/automation/{email_sorter,pdf_extractor,notion_sheets_sync,social_poster}

echo "✅ Installation complete!"
echo ""
echo "Usage:"
echo "  python3 ~/automation/email_sorter/main.py --help"
echo "  python3 ~/automation/pdf_extractor/main.py --help"
echo ""
echo "Docs: https://github.com/kenily/python-automation-toolkit"
