#!/usr/bin/env python3
"""
Social Media Analytics Fetcher
Fetches Instagram and Twitter analytics data
"""

import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')

def fetch_instagram_stats():
    """Fetch Instagram analytics (demo data for now)"""
    print("📸 Fetching Instagram stats...")
    
    # Demo data - replace with actual API calls when you have tokens
    stats = {
        "followers": 1250 + int(datetime.now().hour),  # Simulated growth
        "profile_views": 3420 + int(datetime.now().minute) * 10,
        "posts": [
            {"id": 1, "likes": 145, "comments": 23, "timestamp": datetime.now().isoformat()},
            {"id": 2, "likes": 189, "comments": 31, "timestamp": datetime.now().isoformat()},
            {"id": 3, "likes": 234, "comments": 45, "timestamp": datetime.now().isoformat()},
        ]
    }
    
    print(f"   ✅ Followers: {stats['followers']}")
    print(f"   ✅ Profile Views: {stats['profile_views']}")
    print(f"   ✅ Posts: {len(stats['posts'])}")
    
    return stats

def fetch_twitter_stats():
    """Fetch Twitter analytics (demo data for now)"""
    print("🐦 Fetching Twitter stats...")
    
    # Demo data - replace with actual API calls when you have tokens
    stats = {
        "followers": 890 + int(datetime.now().hour / 2),
        "tweets": [
            {"id": 1, "likes": 67, "retweets": 12, "timestamp": datetime.now().isoformat()},
            {"id": 2, "likes": 89, "retweets": 18, "timestamp": datetime.now().isoformat()},
        ]
    }
    
    print(f"   ✅ Followers: {stats['followers']}")
    print(f"   ✅ Tweets: {len(stats['tweets'])}")
    
    return stats

def update_analytics():
    """Fetch and update analytics.json"""
    print("\n" + "="*60)
    print("🚀 Social Media Analytics Fetcher")
    print("="*60 + "\n")
    
    # Fetch stats
    instagram_stats = fetch_instagram_stats()
    twitter_stats = fetch_twitter_stats()
    
    # Load existing data
    try:
        with open('analytics.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"history": []}
    
    # Update data
    data['last_updated'] = datetime.now().isoformat()
    data['instagram'] = instagram_stats
    data['twitter'] = twitter_stats
    
    # Update history
    today = datetime.now().strftime("%Y-%m-%d")
    history_entry = {
        "date": today,
        "followers": instagram_stats['followers']
    }
    
    # Add to history if not already present for today
    if not data.get('history'):
        data['history'] = []
    
    if not any(h['date'] == today for h in data['history']):
        data['history'].append(history_entry)
    else:
        # Update today's entry
        for h in data['history']:
            if h['date'] == today:
                h['followers'] = instagram_stats['followers']
    
    # Keep only last 30 days
    data['history'] = data['history'][-30:]
    
    # Save updated data
    with open('analytics.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("\n" + "="*60)
    print("✅ Analytics updated successfully!")
    print(f"📊 Data saved to analytics.json")
    print("="*60 + "\n")
    
    return data

if __name__ == '__main__':
    update_analytics()
