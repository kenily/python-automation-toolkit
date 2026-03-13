#!/usr/bin/env python3
"""
Notion to Google Sheets Sync
Monitor Notion database changes and sync to Google Sheets automatically
"""

import os
import json
from datetime import datetime

class NotionSheetsSync:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        self.cache_file = "notion_cache.json"
        
    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            'notion_api_key': os.environ.get('NOTION_API_KEY'),
            'database_id': os.environ.get('NOTION_DATABASE_ID'),
            'sheets_credentials': os.environ.get('SHEETS_CREDS_FILE', 'credentials.json'),
            'sync_interval_minutes': 30
        }
    
    def get_notion_database(self):
        """Fetch all pages from Notion database"""
        # In production, use notion_client
        # from notion_client import Client
        # notion = Client(auth=self.config['notion_api_key'])
        # return notion.databases.query(database_id=self.config['database_id'])
        print("📡 Connecting to Notion API...")
        return []
    
    def parse_properties(self, page):
        """Parse Notion page properties to dict"""
        properties = {}
        props = page.get('properties', {})
        
        for key, value in props.items():
            prop_type = value.get('type')
            if prop_type == 'title':
                properties[key] = value.get('title', [{}])[0].get('plain_text', '')
            elif prop_type == 'rich_text':
                texts = value.get('rich_text', [])
                properties[key] = ' '.join([t.get('plain_text', '') for t in texts])
            elif prop_type == 'select':
                properties[key] = value.get('select', {}).get('name', '')
            elif prop_type == 'multi_select':
                items = value.get('multi_select', [])
                properties[key] = ', '.join([i.get('name', '') for i in items])
            elif prop_type == 'date':
                properties[key] = value.get('date', {}).get('start', '')
            elif prop_type == 'checkbox':
                properties[key] = value.get('checkbox', False)
            elif prop_type == 'number':
                properties[key] = value.get('number', 0)
            elif prop_type == 'url':
                properties[key] = value.get('url', '')
            elif prop_type == 'people':
                people = value.get('people', [])
                properties[key] = ', '.join([p.get('name', '') for p in people])
                
        return properties
    
    def sync_to_sheets(self, data):
        """Sync data to Google Sheets"""
        # In production, use gspread
        # import gspread
        # gc = gspread.service_account(filename=self.config['sheets_credentials'])
        # wks = gc.open("Notion Sync").sheet1
        # wks.clear()
        # wks.update([data.keys().tolist()] + data.values.tolist())
        print(f"📊 Syncing {len(data)} rows to Google Sheets...")
        print("✅ Sync complete!")
    
    def check_for_updates(self):
        """Check for new or updated pages"""
        current_data = self.get_notion_database()
        
        # Load cached data
        cached = {}
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                cached = json.load(f)
        
        updates = []
        for page in current_data:
            page_id = page.get('id', '')
            props = self.parse_properties(page)
            
            # Check if new or updated
            if page_id not in cached:
                updates.append({'type': 'new', 'page': props})
            elif cached[page_id] != props:
                updates.append({'type': 'updated', 'page': props})
            
            # Update cache
            cached[page_id] = props
        
        # Save cache
        with open(self.cache_file, 'w') as f:
            json.dump(cached, f)
            
        return updates
    
    def run_sync(self):
        """Main sync loop"""
        print(f"🔄 Notion → Sheets Sync Started")
        print(f"📁 Database: {self.config.get('database_id', 'Not configured')}")
        
        updates = self.check_for_updates()
        
        if updates:
            print(f"📝 Found {len(updates)} updates:")
            for u in updates:
                print(f"  - {u['type']}: {u['page'].get('Name', 'Untitled')}")
            
            # Sync to sheets
            all_data = self.get_notion_database()
            parsed_data = [self.parse_properties(p) for p in all_data]
            self.sync_to_sheets(parsed_data)
        else:
            print("✅ No changes detected")
        
        print(f"🏁 Sync complete. Next run in {self.config.get('sync_interval_minutes', 30)} minutes")

# Example usage
if __name__ == "__main__":
    sync = NotionSheetsSync()
    sync.run_sync()
