"""
Quick script to check which Facebook Page the Page ID corresponds to.
"""
import requests
import os

PAGE_ID = '1560393975231461'
ACCESS_TOKEN = '3bhyktj6ah4_863wFfRa6kg4LBo'

try:
    url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"
    params = {
        'fields': 'name,link,category',
        'access_token': ACCESS_TOKEN
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    page_info = response.json()
    print("=" * 60)
    print("FACEBOOK PAGE INFORMATION")
    print("=" * 60)
    print(f"Page Name: {page_info.get('name', 'N/A')}")
    print(f"Page ID: {PAGE_ID}")
    print(f"Page URL: {page_info.get('link', 'N/A')}")
    print(f"Category: {page_info.get('category', 'N/A')}")
    print("=" * 60)
    print(f"\n✅ Shayaris will be posted to: {page_info.get('name', 'N/A')}")
    print(f"   Visit: {page_info.get('link', 'N/A')}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    if hasattr(e, 'response') and e.response is not None:
        try:
            error_detail = e.response.json()
            print(f"Details: {error_detail}")
        except:
            print(f"Status Code: {e.response.status_code}")
