#!/usr/bin/env python3
import requests
import json

API_BASE = "https://script.google.com/macros/s/AKfycbxb7tR4h3x9YErM-e4mJusVl9oRfLkaqytgVPcZnyGZAklmx3jycd2Ouj0bo3SD6u7u/exec"

print("🔍 Testing difficulty filtering formats...")

# Test different difficulty formats
difficulty_formats = [
    "★☆☆☆☆",
    "1",
    "★",
    "⭐",
    "star1",
    "beginner"
]

for diff in difficulty_formats:
    print(f"\n🧪 Testing difficulty: '{diff}'")
    try:
        response = requests.get(API_BASE, params={'difficulties': json.dumps([diff])})
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                count = data.get('count', 0)
                songs = data.get('songs', [])
                print(f"✅ Success! Found {count} songs")
                if songs:
                    # Show what difficulty values are actually in the data
                    difficulties = [song.get('difficulty') for song in songs[:3]]
                    print(f"   Sample difficulties from results: {difficulties}")
            else:
                print(f"❌ API Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Request failed: {e}")

# Test getting all songs to see what difficulty values exist
print(f"\n🔍 Getting sample songs to see actual difficulty formats...")
try:
    response = requests.get(API_BASE)
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            songs = data.get('songs', [])
            difficulties = [song.get('difficulty') for song in songs if song.get('difficulty')]
            unique_difficulties = list(set(difficulties))
            print(f"✅ Found these difficulty values in the data:")
            for i, diff in enumerate(unique_difficulties[:10]):  # Show first 10
                print(f"   {i+1}. '{diff}' (type: {type(diff).__name__})")
except Exception as e:
    print(f"❌ Request failed: {e}")

print("\n🏁 Test complete!")
