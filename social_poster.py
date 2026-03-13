#!/usr/bin/env python3
"""
Social Media Auto-Poster with Human Approval
Multi-platform posting with keyword review before publishing
"""

import os
import json
from datetime import datetime

class SocialMediaPoster:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        self.pending_posts = []
        
    def load_config(self):
        """Load configuration"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            'platforms': ['twitter', 'linkedin'],
            'keywords_block': ['spam', 'scam', 'free money'],
            'keywords_review': ['AI', 'news', 'urgent']
        }
    
    def create_draft(self, content, platform=None):
        """Create a draft post for review"""
        draft = {
            'id': len(self.pending_posts) + 1,
            'content': content,
            'platform': platform or 'all',
            'created_at': datetime.now().isoformat(),
            'status': 'pending_review'
        }
        
        # Check for blocked keywords
        blocked = [kw for kw in self.config.get('keywords_block', []) 
                   if kw.lower() in content.lower()]
        
        if blocked:
            draft['status'] = 'blocked'
            draft['block_reason'] = f"Blocked keywords: {', '.join(blocked)}"
            print(f"❌ Blocked: {blocked}")
            return draft
        
        # Check for review keywords
        review_needed = [kw for kw in self.config.get('keywords_review', [])
                        if kw.lower() in content.lower()]
        
        if review_needed:
            draft['review_keywords'] = review_needed
            draft['status'] = 'needs_review'
            print(f"⚠️ Needs review: {review_needed}")
        
        self.pending_posts.append(draft)
        print(f"✅ Draft created: {content[:50]}...")
        return draft
    
    def review_drafts(self):
        """Show all pending drafts for review"""
        print("\n" + "="*50)
        print("📋 PENDING DRAFTS")
        print("="*50)
        
        for draft in self.pending_posts:
            if draft['status'] in ['pending_review', 'needs_review']:
                print(f"\n[{draft['id']}] {draft['status']}")
                print(f"Content: {draft['content']}")
                if 'review_keywords' in draft:
                    print(f"Review needed for: {draft['review_keywords']}")
                    
        return self.pending_posts
    
    def approve_post(self, draft_id):
        """Approve a post for publishing"""
        for draft in self.pending_posts:
            if draft['id'] == draft_id:
                draft['status'] = 'approved'
                draft['approved_at'] = datetime.now().isoformat()
                print(f"✅ Post {draft_id} approved!")
                return draft
        return None
    
    def reject_post(self, draft_id):
        """Reject a post"""
        for draft in self.pending_posts:
            if draft['id'] == draft_id:
                draft['status'] = 'rejected'
                print(f"❌ Post {draft_id} rejected")
                return draft
        return None
    
    def publish_approved(self):
        """Publish all approved posts (simulated)"""
        for draft in self.pending_posts:
            if draft['status'] == 'approved':
                print(f"📤 Publishing to {draft['platform']}: {draft['content'][:30]}...")
                draft['status'] = 'published'
                draft['published_at'] = datetime.now().isoformat()

# Example usage
if __name__ == "__main__":
    poster = SocialMediaPoster()
    
    # Create some drafts
    poster.create_draft("Check out our new AI product!")
    poster.create_draft("Free money! Click here!")
    poster.create_draft("Breaking news about tech industry")
    
    # Review drafts
    poster.review_drafts()
    
    # Approve first draft
    poster.approve_post(1)
    
    # Publish approved
    poster.publish_approved()
