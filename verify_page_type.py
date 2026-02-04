"""
Script to verify if the Facebook ID is a Page or Profile.
Pages can be posted to via API, Profiles typically cannot.
"""
import requests
import os

PAGE_ID = '61587193634873'
ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_HERE')

print("=" * 60)
print("VERIFYING FACEBOOK PAGE TYPE")
print("=" * 60)
print(f"Checking ID: {PAGE_ID}")
print(f"URL: https://www.facebook.com/profile.php?id={PAGE_ID}")
print()

if ACCESS_TOKEN == 'YOUR_ACCESS_TOKEN_HERE':
    print("⚠️  Note: You need an access token to verify.")
    print("   Set it using: $env:FACEBOOK_ACCESS_TOKEN='your_token'")
    print()
    print("📋 Manual Check:")
    print("   1. Visit: https://www.facebook.com/profile.php?id=61587193634873")
    print("   2. Check if it's a:")
    print("      - 📄 PAGE: Has 'Like' button, shows 'Page' in About section")
    print("      - 👤 PROFILE: Personal profile (cannot post via API)")
    print()
    print("   ⚠️  IMPORTANT: Facebook API only allows posting to Pages,")
    print("      not personal Profiles!")
else:
    try:
        # Try to get page information
        url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"
        params = {
            'fields': 'name,link,category,is_verified',
            'access_token': ACCESS_TOKEN
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        info = response.json()
        
        print("✅ SUCCESS - This appears to be a Facebook Page!")
        print()
        print("Page Information:")
        print(f"   Name: {info.get('name', 'N/A')}")
        print(f"   ID: {PAGE_ID}")
        print(f"   Link: {info.get('link', 'N/A')}")
        print(f"   Category: {info.get('category', 'N/A')}")
        
        if 'category' in info:
            print()
            print("✅ This is a PAGE - You can post to it!")
            print("   Your script is configured correctly.")
        else:
            print()
            print("⚠️  This might be a Profile, not a Page.")
            print("   Profiles cannot be posted to via API.")
            
    except requests.exceptions.HTTPError as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error = e.response.json().get('error', {})
                if error.get('code') == 100:
                    print("❌ This appears to be a PROFILE, not a PAGE!")
                    print()
                    print("Facebook API does not allow posting to personal Profiles.")
                    print("You need to convert this to a Page or use a different Page.")
                    print()
                    print("To convert Profile to Page:")
                    print("   1. Go to Facebook Settings")
                    print("   2. Look for 'Convert to Page' option")
                    print("   OR create a new Facebook Page")
                else:
                    print(f"Error: {error.get('message', 'Unknown error')}")
            except:
                print(f"Error: Status {e.response.status_code}")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

print()
print("=" * 60)
