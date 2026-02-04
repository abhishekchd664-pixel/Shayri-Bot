"""
Script to get your Facebook Page information and verify access.
This will help you find the correct Page ID and verify your token works.
"""
import requests
import os
import sys

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'EAA7vMs3yYxABQnwt022sqNZCZB1Gv34WENt8nfLjaSRCrJCPkLu0ZAHIFbyyUeiIXbbdNHZCSVgjafsWEScdAwp8OWnZBH66U94fY2ZBvZCvdINAhAAS1AXBUxDsmy5ntdUqIOYcyIkPTJXDJZAJTZBN9kuRhpnBESp7HS8fLLzaVsbSUH4zKYZAj5ZAuMouVE5VMtYKaEtMiOq3lpokZCsJpfgNTgEVdVxbrdJON3UstF0ZD')

print("=" * 70)
print("GETTING YOUR FACEBOOK PAGES")
print("=" * 70)
print("\nThis script will list all Pages you have access to with this token.\n")

try:
    # Get all pages the user has access to
    url = "https://graph.facebook.com/v18.0/me/accounts"
    params = {
        'fields': 'id,name,link,category,access_token',
        'access_token': ACCESS_TOKEN
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    pages = data.get('data', [])
    
    if not pages:
        print("[WARNING] No pages found!")
        print("\nPossible reasons:")
        print("  1. This token doesn't have access to any pages")
        print("  2. You need to grant 'pages_show_list' permission")
        print("  3. You might be using a User token instead of Page token")
        print("\nSolution:")
        print("  - Go to Graph API Explorer")
        print("  - Select 'pages_show_list' and 'pages_manage_posts' permissions")
        print("  - Generate a new token")
    else:
        print(f"[SUCCESS] Found {len(pages)} page(s) you can manage:\n")
        print("-" * 70)
        
        for i, page in enumerate(pages, 1):
            print(f"\nPage #{i}:")
            print(f"  Name: {page.get('name', 'N/A')}")
            print(f"  ID: {page.get('id', 'N/A')}")
            print(f"  URL: {page.get('link', 'N/A')}")
            print(f"  Category: {page.get('category', 'N/A')}")
            
            # Check if this matches the target page
            if page.get('id') == '61587193634873':
                print(f"  >>> THIS IS YOUR TARGET PAGE! <<<")
                print(f"  >>> Use this Page Access Token for posting: <<<")
                print(f"  {page.get('access_token', 'N/A')[:50]}...")
        
        print("\n" + "-" * 70)
        print("\n[INFO] To use a page:")
        print("  1. Copy the Page ID from above")
        print("  2. Copy the Page Access Token (access_token) from above")
        print("  3. Update main.py with these values")
        print("\n[NOTE] The Page Access Token is different from User Access Token!")
        print("       Use the 'access_token' value from the page object above.")
        
except requests.exceptions.HTTPError as e:
    print(f"\n[ERROR] HTTP Error: {e}")
    if hasattr(e, 'response') and e.response is not None:
        try:
            error_detail = e.response.json()
            error_msg = error_detail.get('error', {})
            print(f"\nError Details:")
            print(f"   Type: {error_msg.get('type', 'N/A')}")
            print(f"   Message: {error_msg.get('message', 'N/A')}")
            print(f"   Code: {error_msg.get('code', 'N/A')}")
            
            if error_msg.get('code') == 190:
                print("\n[INFO] Your access token is invalid or expired.")
                print("   Get a new token from Graph API Explorer")
            elif error_msg.get('code') == 200:
                print("\n[INFO] Missing permissions.")
                print("   You need 'pages_show_list' permission")
                print("   Go to Graph API Explorer and add this permission")
                
        except:
            print(f"   Status Code: {e.response.status_code}")
            
except Exception as e:
    print(f"\n[ERROR] Unexpected Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
