# PDF Extractor Hand

PDF文本提取 - 从PDF文件中提取文本和表格

## 功能
- 文本提取
- 表格识别
- 批量处理
- 多语言支持

## 安装
```bash
pip install pdf-extractor
```

## 配置
```yaml
input_dir: ./pdfs
output_dir: ./output
format: markdown  # markdown, text, json
extract_tables: true
language: en
```

## 使用
```bash
# 单文件
pdf-extractor file.pdf

# 批量
pdf-extractor --batch ./pdfs/
```
