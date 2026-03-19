# Email Sorter - 使用示例

## 基础用法

```python
from email_sorter import EmailSorter

# 初始化
sorter = EmailSorter(
    imap_server='imap.gmail.com',
    username='your@email.com',
    password='your-app-password'
)

# 添加分类规则
sorter.add_rule(
    keyword='newsletter',
    folder='Newsletters'
)

sorter.add_rule(
    sender='boss@company.com',
    folder='Work'
)

# 运行
sorter.run()
```

## 高级用法

### 自定义过滤函数
```python
def custom_filter(email):
    """自定义过滤逻辑"""
    if 'urgent' in email.subject.lower():
        return 'Urgent'
    if email.attachments:
        return 'Has Attachments'
    return None

sorter.add_custom_filter(custom_filter)
```

### 批量处理
```python
# 处理最近100封邮件
sorter.process_emails(count=100)

# 只处理特定文件夹
sorter.process_folder('INBOX')
```

## 配置示例

```json
{
    "imap_server": "imap.gmail.com",
    "folders": {
        "Newsletters": ["newsletter", "subscribe"],
        "Work": ["boss", "meeting", "project"],
        "Personal": ["family", "friend"]
    }
}
```

## 故障排除

### 问题: 认证失败
**解决**: 使用应用专用密码而非登录密码
- Gmail: 启用两步验证 → 创建应用密码

### 问题: 连接超时
**解决**: 检查防火墙/网络设置，或增加超时时间
```python
sorter.timeout = 60
```
