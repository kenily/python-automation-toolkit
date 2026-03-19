# Social Poster Hand

多平台社交媒体自动发布

## 功能
- Twitter/X
- LinkedIn
- Reddit
- 内容排程
- 画廊管理

## 安装
```bash
pip install social-poster
social-poster init
```

## 配置
```yaml
platforms:
  twitter:
    api_key: xxx
    api_secret: xxx
    access_token: xxx
  
  linkedin:
    cookie: xxx

  reddit:
    client_id: xxx
    client_secret: xxx

queue_dir: ./queue
post_interval: 3600
```

## 使用
```bash
# 添加到队列
social-poster add --platform twitter --file post.md

# 开始发布
social-poster run

# 查看状态
social-poster status
```
