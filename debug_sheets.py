#!/usr/bin/env python3
import requests

API_BASE = "https://script.google.com/macros/s/AKfycbxb7tR4h3x9YErM-e4mJusVl9oRfLkaqytgVPcZnyGZAklmx3jycd2Ouj0bo3SD6u7u/exec"

print("🔍 Debugging what's actually in the link field...")

try:
    # Get songs with the new rich text API
    response = requests.get(API_BASE)
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            songs = data.get('songs', [])
            
            print(f"📋 Sample link data from API:")
            for i, song in enumerate(songs[:3]):
                title = song.get('title', 'No title')
                link = song.get('link', 'No link')
                
                print(f"\n{i+1}. Title: '{title}'")
                print(f"   Link: '{link}'")
                print(f"   Starts with http: {str(link).startswith('http')}")
                print(f"   Contains youtube: {'youtube' in str(link).lower()}")
                print(f"   Length: {len(str(link))}")
                
                # Check if it's a YouTube URL pattern
                if 'youtube.com/watch' in str(link) or 'youtu.be/' in str(link):
                    print(f"   ✅ Valid YouTube URL!")
                elif 'youtube' in str(link).lower():
                    print(f"   🔍 Contains 'youtube' but not a URL")
                else:
                    print(f"   ❌ Not a YouTube URL")
            
        else:
            print(f"❌ API Error: {data.get('error', 'Unknown error')}")
    else:
        print(f"❌ HTTP Error: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
except Exception as e:
    print(f"❌ Request failed: {e}")

print("\n🏁 Link debugging complete!")
print("\n💡 If links are still not URLs, the Google Sheets cells might just be text, not actual hyperlinks.")
