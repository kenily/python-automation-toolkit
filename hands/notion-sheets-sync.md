# Notion-Sheets Sync Hand

Notion到Google Sheets双向同步

## 功能
- Notion数据库 → Sheets
- Sheets → Notion数据库
- 定时自动同步
- 冲突处理

## 安装
```bash
pip install notion-sheets-sync
notion-sheets-sync init
```

## 配置
```yaml
notion:
  api_key: your_notion_key
  database_id: your_db_id

sheets:
  spreadsheet_id: your_sheet_id
  sheet_name: Sheet1

sync:
  direction: bidirectional  # notion_to_sheets, sheets_to_notion, bidirectional
  interval: 300  # seconds
```

## 使用
```bash
# 手动同步
notion-sheets-sync run

# 守护进程
notion-sheets-sync daemon
```
