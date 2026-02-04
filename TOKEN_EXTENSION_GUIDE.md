# How to Extend Your Facebook Access Token

Your current token will expire soon. Follow these steps to get a long-lived token (60 days).

## Quick Steps

### Step 1: Get Your App Secret

1. Go to [Facebook Developers](https://developers.facebook.com/apps/)
2. Find your app (App ID: **4203651156566800**)
3. Click on your app
4. Go to **"Settings"** → **"Basic"**
5. Find **"App Secret"**
6. Click **"Show"** to reveal it
7. **Copy the App Secret** (keep it safe!)

### Step 2: Run the Extension Script

**Option A: Using Environment Variable (Recommended)**

```powershell
# Set your App Secret
$env:FACEBOOK_APP_SECRET='your_app_secret_here'

# Run the script
python extend_token_simple.py
```

**Option B: Edit the Script Directly**

1. Open `extend_token_simple.py`
2. Find line 12: `APP_SECRET = os.getenv('FACEBOOK_APP_SECRET', '')`
3. Change it to: `APP_SECRET = 'your_app_secret_here'`
4. Save and run: `python extend_token_simple.py`

### Step 3: Update main.py

The script will output a new long-lived token. Copy it and update `main.py`:

```python
ACCESS_TOKEN = 'your_new_long_lived_token_here'
```

## What Happens

1. **Short-lived token** (current) → Expires in 1-2 hours
2. **Long-lived token** → Expires in 60 days
3. **Page Access Token** → Extracted from long-lived token, also lasts 60 days

## Security Note

⚠️ **Never share your App Secret publicly!**
- Don't commit it to Git
- Don't share it in screenshots
- Keep it private

## Troubleshooting

### "Invalid App Secret"
- Double-check you copied the entire App Secret
- Make sure there are no extra spaces
- Verify you're using the correct app

### "Token expired"
- Your current token might have already expired
- Get a new token from [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- Then run the extension script again

### "No pages found"
- The token might already be a Page token
- Use the long-lived token directly in `main.py`

## After 60 Days

When your token expires (in 60 days), you'll need to:
1. Get a new short-lived token from Graph API Explorer
2. Run the extension script again
3. Update `main.py` with the new token

## Making It Permanent (Advanced)

For tokens that last longer than 60 days, you need to:
1. Submit your app for review
2. Request `pages_manage_posts` permission
3. Once approved, tokens can be longer-lived

See `FACEBOOK_SETUP_GUIDE.md` for more details.
