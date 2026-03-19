# Email Sorter Hand

自动邮件分类 - 检测重要邮件并分类到对应文件夹

## 功能
- IMAP连接支持
- 智能关键词分类
- 自动标记/归档
- 定时检查

## 安装
```bash
pip install email-sorter
email-sorter --config
```

## 配置
```yaml
imap_host: imap.gmail.com
imap_port: 993
username: your@email.com
password: AppPassword

rules:
  - keywords: ["invoice", "bill"]
    folder: Bills
  - keywords: ["github", "PR"]
    folder: Dev
  - keywords: ["meeting", "calendar"]
    folder: Calendar
```

## 使用
```bash
# 手动运行
email-sorter run

# 守护进程模式
email-sorter daemon --interval 300
```
