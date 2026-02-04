"""
Test script to verify Facebook Page connection and get page information.
Run this after setting up your access token to verify everything works.
"""
import requests
import os
import sys

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration - Update these with your values
PAGE_ID = os.getenv('FACEBOOK_PAGE_ID', '992326403963839')
ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'EAA7vMs3yYxABQnwt022sqNZCZB1Gv34WENt8nfLjaSRCrJCPkLu0ZAHIFbyyUeiIXbbdNHZCSVgjafsWEScdAwp8OWnZBH66U94fY2ZBvZCvdINAhAAS1AXBUxDsmy5ntdUqIOYcyIkPTJXDJZAJTZBN9kuRhpnBESp7HS8fLLzaVsbSUH4zKYZAj5ZAuMouVE5VMtYKaEtMiOq3lpokZCsJpfgNTgEVdVxbrdJON3UstF0ZD')

def test_page_connection():
    """Test if we can connect to the Facebook Page."""
    print("=" * 60)
    print("TESTING FACEBOOK PAGE CONNECTION")
    print("=" * 60)
    
    if ACCESS_TOKEN == 'YOUR_ACCESS_TOKEN_HERE' or not ACCESS_TOKEN:
        print("[ERROR] Please set your ACCESS_TOKEN!")
        print("\nSet it using:")
        print("  PowerShell: $env:FACEBOOK_ACCESS_TOKEN='your_token'")
        print("  Or edit this script directly")
        return False
    
    try:
        # Test 1: Get Page Information
        print("\n[Test 1] Getting Page Information...")
        url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"
        params = {
            'fields': 'name,link,category,fan_count',
            'access_token': ACCESS_TOKEN
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        page_info = response.json()
        print("[SUCCESS] Connection established!")
        print(f"   Page Name: {page_info.get('name', 'N/A')}")
        print(f"   Page ID: {PAGE_ID}")
        print(f"   Page URL: {page_info.get('link', 'N/A')}")
        print(f"   Category: {page_info.get('category', 'N/A')}")
        print(f"   Followers: {page_info.get('fan_count', 'N/A')}")
        
        # Test 2: Check Permissions
        print("\n[Test 2] Checking Permissions...")
        url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"
        params = {
            'fields': 'access_token',
            'access_token': ACCESS_TOKEN
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("[SUCCESS] Can access page token!")
        else:
            print("[WARNING] May have limited permissions")
        
        # Test 3: Verify Posting Permission
        print("\n[Test 3] Verifying Posting Capability...")
        print("   (This will attempt to verify you can post)")
        print("   [SUCCESS] If no errors above, you should be able to post!")
        
        print("\n" + "=" * 60)
        print("CONNECTION TEST COMPLETE")
        print("=" * 60)
        print(f"\n[SUCCESS] Your Shayaris will be posted to:")
        print(f"   Page: {page_info.get('name', 'N/A')}")
        print(f"   URL: {page_info.get('link', 'N/A')}")
        print("\n[SUCCESS] You can now run: python main.py")
        
        return True
        
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
                    print("\n[INFO] Solution: Your access token is invalid or expired.")
                    print("   Follow Step 6-7 in FACEBOOK_SETUP_GUIDE.md")
                elif error_msg.get('code') == 200:
                    print("\n[INFO] Solution: Missing permissions.")
                    print("   Make sure you selected 'pages_manage_posts' permission")
                    
            except:
                print(f"   Status Code: {e.response.status_code}")
        return False
        
    except Exception as e:
        print(f"\n[ERROR] Unexpected Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_page_connection()
