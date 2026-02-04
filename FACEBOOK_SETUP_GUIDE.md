# Complete Guide: Connecting Facebook App to Your Page

This guide will help you properly connect your Facebook App to your Shayari Page and get the correct Page Access Token.

## Step 1: Verify Your Facebook Page

1. Go to your Facebook Page: `https://www.facebook.com/1560393975231461`
2. Make sure you are an **Admin** or **Editor** of the page
3. Note your Page Name (you'll need this later)

## Step 2: Create/Verify Your Facebook App

### If you don't have an app yet:

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click **"My Apps"** → **"Create App"**
3. Choose **"Business"** as the app type
4. Fill in:
   - **App Name**: "Shayari Poster" (or any name)
   - **App Contact Email**: Your email
5. Click **"Create App"**

### If you already have an app:

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click **"My Apps"** → Select your app

## Step 3: Add Required Products to Your App

1. In your app dashboard, find **"Add Products"** or **"Products"** section
2. Find **"Facebook Login"** and click **"Set Up"**
   - Use default settings
   - Click **"Save"**
3. Find **"Page Management API"** (if available) and add it
   - This gives you permission to manage pages

## Step 4: Get Your App ID and App Secret

1. In your app dashboard, go to **"Settings"** → **"Basic"**
2. Note down:
   - **App ID**: `YOUR_APP_ID`
   - **App Secret**: Click **"Show"** to reveal it → `YOUR_APP_SECRET`
   - Keep these safe!

## Step 5: Add Your Page to the App

1. In your app dashboard, go to **"Roles"** → **"Roles"**
2. Make sure you are listed as an **Admin** or **Developer**

## Step 6: Get Page Access Token Using Graph API Explorer

### Method A: Using Graph API Explorer (Recommended)

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)

2. **Select Your App**:
   - Click the dropdown next to "Meta App"
   - Select your app (the one you created)

3. **Generate User Access Token**:
   - Click **"Generate Access Token"** button
   - Select these permissions:
     - ✅ `pages_show_list` (to see your pages)
     - ✅ `pages_read_engagement` (to read page data)
     - ✅ `pages_manage_posts` (to post on page)
     - ✅ `pages_read_user_content` (to read user content)
   - Click **"Generate Access Token"**
   - **Approve** all permissions when prompted
   - **Copy the token** (this is a short-lived token, expires in 1-2 hours)

4. **Get Your Page Access Token**:
   - In Graph API Explorer, change the endpoint to:
     ```
     me/accounts
     ```
   - Click **"Submit"**
   - You'll see a JSON response with your pages
   - Find your page (Page ID: `1560393975231461`)
   - Copy the **`access_token`** value (this is your Page Access Token!)

### Method B: Using Access Token Tool

1. Go to [Access Token Tool](https://developers.facebook.com/tools/accesstoken/)
2. Find your page in the list
3. Click **"Generate Token"** next to your page
4. Copy the Page Access Token

## Step 7: Make Your Token Long-Lived (Important!)

The token from Step 6 expires quickly. To make it last longer:

### Exchange for Long-Lived Token (60 days):

1. Use this URL in your browser (replace values):
   ```
   https://graph.facebook.com/v18.0/oauth/access_token?
   grant_type=fb_exchange_token&
   client_id=YOUR_APP_ID&
   client_secret=YOUR_APP_SECRET&
   fb_exchange_token=YOUR_SHORT_LIVED_TOKEN
   ```

2. Replace:
   - `YOUR_APP_ID` with your App ID from Step 4
   - `YOUR_APP_SECRET` with your App Secret from Step 4
   - `YOUR_SHORT_LIVED_TOKEN` with the token from Step 6

3. This returns a JSON with a **long-lived token** (60 days)

### Get Page Access Token from Long-Lived Token:

1. Use this URL (replace `YOUR_LONG_LIVED_TOKEN`):
   ```
   https://graph.facebook.com/v18.0/me/accounts?access_token=YOUR_LONG_LIVED_TOKEN
   ```

2. Find your page in the response and copy its `access_token`

## Step 8: Test Your Connection

Use this Python script to test:

```python
import requests

PAGE_ID = "1560393975231461"
ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN_HERE"

url = f"https://graph.facebook.com/v18.0/{PAGE_ID}"
params = {
    'fields': 'name,link,category',
    'access_token': ACCESS_TOKEN
}

response = requests.get(url, params=params)
print(response.json())
```

If successful, you'll see your page name and details!

## Step 9: Update Your Script

Once you have the correct Page Access Token:

1. Update `main.py`:
   ```python
   PAGE_ID = '1560393975231461'
   ACCESS_TOKEN = 'YOUR_NEW_PAGE_ACCESS_TOKEN'
   ```

2. Or set environment variables:
   ```powershell
   $env:FACEBOOK_PAGE_ID="1560393975231461"
   $env:FACEBOOK_ACCESS_TOKEN="YOUR_NEW_PAGE_ACCESS_TOKEN"
   ```

## Step 10: Submit Your App for Review (For Permanent Access)

If you want the token to last longer than 60 days:

1. Go to your app dashboard → **"App Review"**
2. Request permissions:
   - `pages_manage_posts`
   - `pages_read_engagement`
3. Submit for review (may take a few days)
4. Once approved, tokens can be longer-lived

## Troubleshooting

### "Invalid OAuth access token"
- Token expired or incorrect
- Regenerate using Step 6

### "Insufficient permissions"
- Make sure you selected all required permissions in Step 6
- Verify you're an Admin of the page

### "Page not found"
- Verify Page ID is correct
- Make sure you're an Admin of the page

### Token expires quickly
- Use Step 7 to exchange for long-lived token
- Submit app for review (Step 10) for permanent access

## Quick Checklist

- [ ] Created Facebook App
- [ ] Added "Facebook Login" product
- [ ] Got App ID and App Secret
- [ ] Generated User Access Token with page permissions
- [ ] Got Page Access Token from `me/accounts`
- [ ] Exchanged for long-lived token (optional but recommended)
- [ ] Tested connection
- [ ] Updated main.py with new token

## Need Help?

- [Facebook Graph API Docs](https://developers.facebook.com/docs/graph-api)
- [Page Access Tokens Guide](https://developers.facebook.com/docs/pages/access-tokens)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
