#!/usr/bin/env python3
import requests

API_BASE = "https://script.google.com/macros/s/AKfycbxb7tR4h3x9YErM-e4mJusVl9oRfLkaqytgVPcZnyGZAklmx3jycd2Ouj0bo3SD6u7u/exec"

print("🔍 Checking YouTube link formats...")

try:
    # Get a few songs to see link format
    response = requests.get(API_BASE)
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            songs = data.get('songs', [])
            
            print(f"📋 Sample song links:")
            for i, song in enumerate(songs[:5]):
                title = song.get('title', 'No title')
                link = song.get('link', 'No link')
                print(f"\n{i+1}. Title: '{title}'")
                print(f"   Link: '{link}'")
                print(f"   Link type: {type(link)}")
                print(f"   Link length: {len(str(link))}")
                
                # Check if it looks like a YouTube URL
                if 'youtube.com' in str(link) or 'youtu.be' in str(link):
                    print(f"   ✅ Looks like YouTube URL")
                elif 'http' in str(link):
                    print(f"   🔗 Looks like URL but not YouTube")
                else:
                    print(f"   ❌ Doesn't look like URL")
            
        else:
            print(f"❌ API Error: {data.get('error', 'Unknown error')}")
    else:
        print(f"❌ HTTP Error: {response.status_code}")
        
except Exception as e:
    print(f"❌ Request failed: {e}")

print("\n🏁 Link analysis complete!")
