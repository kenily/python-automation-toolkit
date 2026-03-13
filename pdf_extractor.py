#!/usr/bin/env python3
"""
PDF Data Extractor
Extract tables and text from PDF files automatically
"""

import pdfplumber
import csv
import os

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.results = []
        
    def extract_text(self):
        """Extract all text from PDF"""
        text_results = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_results.append(f"--- Page {page_num} ---\n{text}")
        return "\n".join(text_results)
    
    def extract_tables(self):
        """Extract tables from PDF"""
        table_results = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                tables = page.extract_tables()
                if tables:
                    for table_idx, table in enumerate(tables):
                        table_results.append({
                            'page': page_num,
                            'table': table_idx + 1,
                            'data': table
                        })
        return table_results
    
    def save_to_csv(self, output_path):
        """Save extracted tables to CSV"""
        tables = self.extract_tables()
        if not tables:
            print("No tables found!")
            return
            
        for table_info in tables:
            page = table_info['page']
            table_idx = table_info['table']
            table_data = table_info['data']
            
            csv_path = f"{output_path}_page{page}_table{table_idx}.csv"
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for row in table_data:
                    writer.writerow([cell or '' for cell in row])
            print(f"✅ Saved: {csv_path}")
    
    def save_to_text(self, output_path):
        """Save extracted text to file"""
        text = self.extract_text()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Saved text to: {output_path}")

if __name__ == "__main__":
    # Usage example
    extractor = PDFExtractor("input.pdf")
    
    # Extract text
    extractor.save_to_text("output.txt")
    
    # Extract tables to CSV
    extractor.save_to_csv("tables")
