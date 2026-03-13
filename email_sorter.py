#!/usr/bin/env python3
"""
Email Auto-Sorter
Automatically sort emails into folders based on keywords
"""

import imaplib
import email
from email.header import decode_header
import os

class EmailSorter:
    def __init__(self, config, rules):
        """
        Initialize EmailSorter
        
        Args:
            config: dict with 'email', 'password', 'imap_server'
            rules: list of dicts with 'keyword' and 'folder'
        """
        self.email = config['email']
        self.password = config['password']
        self.imap_server = config['imap_server']
        self.rules = rules
        
    def connect(self):
        """Connect to IMAP server"""
        self.mail = imaplib.IMAP4_SSL(self.imap_server)
        self.mail.login(self.email, self.password)
        print(f"✅ Connected to {self.email}")
        
    def get_email_body(self, msg):
        """Extract email body"""
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    return part.get_payload(decode=True).decode('utf-8', errors='ignore')
        else:
            return msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        return ""
    
    def search_and_sort(self, folder='INBOX'):
        """
        Search emails and sort based on keywords
        
        Args:
            folder: IMAP folder to search (default: INBOX)
        """
        self.mail.select(folder)
        
        # Search all emails (limit to last 100 for demo)
        status, messages = self.mail.search(None, 'ALL')
        email_ids = messages[0].split()[-100:]
        
        sorted_count = 0
        
        for email_id in email_ids:
            # Fetch email
            status, msg_data = self.mail.fetch(email_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Get email content
                    body = self.get_email_body(msg)
                    subject = msg['subject'] or ""
                    
                    # Check each rule
                    for rule in self.rules:
                        keyword = rule['keyword'].lower()
                        target_folder = rule['folder']
                        
                        # Check if keyword in subject or body
                        if keyword in subject.lower() or keyword in body.lower():
                            # Create folder if not exists
                            try:
                                self.mail.create(target_folder)
                            except:
                                pass  # Folder already exists
                            
                            # Move email
                            self.mail.copy(email_id, target_folder)
                            print(f"📧 Moved: {subject[:50]}... → {target_folder}")
                            sorted_count += 1
                            break
        
        print(f"\n✅ Sorted {sorted_count} emails!")
        return sorted_count
    
    def close(self):
        """Close connection"""
        self.mail.close()
        self.mail.logout()
        print("🔌 Disconnected")


# Example usage
if __name__ == "__main__":
    # Configuration
    config = {
        'email': 'your_email@gmail.com',
        'password': 'your_app_password',  # Use App Password for Gmail
        'imap_server': 'imap.gmail.com'
    }
    
    # Sorting rules - customize these!
    rules = [
        {'keyword': 'newsletter', 'folder': 'Newsletters'},
        {'keyword': 'invoice', 'folder': 'Invoices'},
        {'keyword': 'receipt', 'folder': 'Invoices'},
        {'keyword': 'meeting', 'folder': 'Meetings'},
        {'keyword': 'calendar', 'folder': 'Meetings'},
        {'keyword': 'support', 'folder': 'Support'},
        {'keyword': 'help', 'folder': 'Support'},
        {'keyword': 'promo', 'folder': 'Promotions'},
        {'keyword': 'sale', 'folder': 'Promotions'},
    ]
    
    # Run sorter
    sorter = EmailSorter(config, rules)
    sorter.connect()
    sorter.search_and_sort()
    sorter.close()
