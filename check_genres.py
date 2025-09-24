#!/usr/bin/env python3
import requests

API_BASE = "https://script.google.com/macros/s/AKfycbxb7tR4h3x9YErM-e4mJusVl9oRfLkaqytgVPcZnyGZAklmx3jycd2Ouj0bo3SD6u7u/exec"

print("🔍 Checking all available genres in your database...")

try:
    # Get all songs to see what genres exist
    response = requests.get(API_BASE)
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            songs = data.get('songs', [])
            
            # Extract all unique genres
            genres = [song.get('genre', '').strip() for song in songs if song.get('genre')]
            unique_genres = sorted(list(set(genres)))
            
            print(f"✅ Found {len(unique_genres)} unique genres in your database:")
            for i, genre in enumerate(unique_genres, 1):
                print(f"   {i:2d}. '{genre}'")
                
            # Show current dropdown options
            current_dropdown = [
                "Children's",
                "Classical & Semi-Classical", 
                "Folk & Regional",
                "Devotional"
            ]
            
            print(f"\n📋 Current dropdown options:")
            for i, genre in enumerate(current_dropdown, 1):
                print(f"   {i}. '{genre}'")
                
            print(f"\n❗ Missing from dropdown:")
            missing = [g for g in unique_genres if g not in current_dropdown]
            for i, genre in enumerate(missing, 1):
                print(f"   {i}. '{genre}'")
                
            # Also check ranges and difficulties
            ranges = [song.get('range', '').strip() for song in songs if song.get('range')]
            unique_ranges = sorted(list(set(ranges)))
            print(f"\n🎤 Available voice ranges: {unique_ranges}")
            
            difficulties = [str(song.get('difficulty', '')).strip() for song in songs if song.get('difficulty')]
            unique_difficulties = sorted(list(set(difficulties)))
            print(f"\n⭐ Available difficulties: {unique_difficulties}")
            
        else:
            print(f"❌ API Error: {data.get('error', 'Unknown error')}")
    else:
        print(f"❌ HTTP Error: {response.status_code}")
        
except Exception as e:
    print(f"❌ Request failed: {e}")

print("\n🏁 Analysis complete!")
