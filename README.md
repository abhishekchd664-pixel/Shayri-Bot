# Hindi Shayari Facebook Auto-Poster

A fully automated Python script that generates beautiful images with Hindi Shayari and posts them to your Facebook Page every 5 minutes.

## Features

- 🎨 **Automatic Image Generation**: Creates 1080x1080 square images with dark aesthetic backgrounds
- 📝 **100+ Hindi Shayaris**: Pre-loaded collection of high-quality Shayaris
- 🤖 **Fully Automated**: Posts every ~5 minutes with random jitter (3-7 minutes) to avoid spam detection
- 🎯 **Facebook Integration**: Uses Facebook Graph API to post directly to your page
- 💧 **Watermark Support**: Adds your page name watermark to each image
- 🛡️ **Error Handling**: Robust error handling to prevent crashes

## Project Structure

```
Text poster/
├── main.py              # Main script
├── shayaris.json        # Collection of Hindi Shayaris
├── requirements.txt     # Python dependencies
├── fonts/               # Folder for Hindi fonts (e.g., Lohit-Devanagari.ttf)
└── output/              # Generated images are saved here
```

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Hindi Font** (Optional but Recommended):
   - Download a Hindi/Devanagari font (e.g., `Lohit-Devanagari.ttf`)
   - Place it in the `fonts/` folder
   - The script will use default font if not found, but Hindi text may not render properly

3. **Set Up Facebook Credentials**:
   - Set environment variables or edit `main.py` directly
   - See "Getting Facebook Access Token" section below

## Configuration

### Method 1: Environment Variables (Recommended)

Set these environment variables before running:

**Windows (PowerShell)**:
```powershell
$env:FACEBOOK_PAGE_ID="your_page_id"
$env:FACEBOOK_ACCESS_TOKEN="your_access_token"
```

**Windows (Command Prompt)**:
```cmd
set FACEBOOK_PAGE_ID=your_page_id
set FACEBOOK_ACCESS_TOKEN=your_access_token
```

**Linux/Mac**:
```bash
export FACEBOOK_PAGE_ID="your_page_id"
export FACEBOOK_ACCESS_TOKEN="your_access_token"
```

### Method 2: Edit main.py Directly

Edit these lines in `main.py`:
```python
PAGE_ID = os.getenv('FACEBOOK_PAGE_ID', 'YOUR_PAGE_ID_HERE')
ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_HERE')
WATERMARK_TEXT = "@YourPageName"  # Change to your page name
```

## Getting Facebook Page Access Token

### Step 1: Create a Facebook App

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click "My Apps" → "Create App"
3. Choose "Business" as the app type
4. Fill in app details and create the app

### Step 2: Add Facebook Login Product

1. In your app dashboard, click "Add Product"
2. Find "Facebook Login" and click "Set Up"
3. Use default settings and save

### Step 3: Get Page Access Token

#### Option A: Using Graph API Explorer (Easiest)

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app from the dropdown
3. Click "Generate Access Token"
4. Select these permissions:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `pages_read_user_content`
5. Click "Generate Access Token" and approve permissions
6. Copy the generated token

#### Option B: Using Access Token Tool

1. Go to [Access Token Tool](https://developers.facebook.com/tools/accesstoken/)
2. Find your page in the list
3. Click "Generate Token" next to your page
4. Copy the Page Access Token

### Step 4: Get Your Page ID

1. Go to your Facebook Page
2. Click "About" on the left sidebar
3. Scroll down to find "Page ID" (or check the URL: `facebook.com/YourPageID`)
4. Alternatively, use [Find My Facebook ID](https://findmyfbid.in/)

### Step 5: Make Token Permanent (Important!)

The token from Graph API Explorer expires in 1-2 hours. To make it permanent:

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app
3. Click "Generate Access Token" → "Get User Access Token"
4. Select permissions: `pages_manage_posts`, `pages_read_engagement`
5. Generate token and copy it
6. Use this URL (replace `YOUR_TOKEN` with your token):
   ```
   https://graph.facebook.com/v18.0/me/accounts?access_token=YOUR_TOKEN
   ```
7. This will return a JSON with a long-lived token (60 days)
8. For even longer tokens, exchange it:
   ```
   https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_SHORT_LIVED_TOKEN
   ```

### Step 6: Test Your Token

Test if your token works:
```bash
curl "https://graph.facebook.com/v18.0/YOUR_PAGE_ID?fields=name&access_token=YOUR_ACCESS_TOKEN"
```

## Usage

1. **Set your credentials** (see Configuration above)

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **The script will**:
   - Post immediately on startup
   - Continue posting every 5 minutes
   - Save all generated images in the `output/` folder
   - Log all activities to console

4. **Stop the script**: Press `Ctrl+C`

## Customization

### Change Posting Interval

Edit `main.py`:
```python
BASE_INTERVAL_MINUTES = 5  # Base interval: 5 minutes
JITTER_MINUTES = 2  # Random variation: ±2 minutes (posts between 3-7 minutes)
```

The script automatically adds random jitter to avoid spam detection. Each post is scheduled at a random interval around the base time.

### Change Image Size

Edit `main.py`:
```python
IMAGE_SIZE = (1080, 1080)  # Change to (1920, 1080) for landscape, etc.
```

### Add More Shayaris

Edit `shayaris.json` and add more strings to the array.

### Change Color Schemes

Edit the `COLOR_SCHEMES` list in `main.py` to customize background and text colors.

## Troubleshooting

### Font Not Found
- Download a Hindi font (e.g., Lohit-Devanagari.ttf) and place it in `fonts/`
- The script will use default font if not found, but Hindi may not render correctly

### Facebook API Errors
- **Invalid Token**: Regenerate your access token
- **Permission Denied**: Make sure you have `pages_manage_posts` permission
- **Rate Limiting**: Facebook has rate limits. If posting too frequently, increase the interval

### Image Generation Issues
- Make sure `output/` folder exists and is writable
- Check that Pillow is installed correctly: `pip install Pillow`

## Notes

- The script posts every ~5 minutes with random jitter (3-7 minutes) to avoid Facebook's spam detection
- Jitter is configurable in `main.py`: `BASE_INTERVAL_MINUTES` and `JITTER_MINUTES`
- Generated images are saved in `output/` folder for backup
- The script uses random color schemes for variety
- Make sure your Facebook Page has posting permissions enabled

## 🚀 Deploy to Run 24/7

Want your script to run continuously? Deploy it to the cloud!

### Quick Deploy (Railway - Recommended)

1. **Push to GitHub** (see `GITHUB_SETUP.md`)
2. **Deploy on Railway**: [railway.app](https://railway.app)
   - Sign up with GitHub
   - New Project → Deploy from GitHub repo
   - Add environment variables
   - Done! Runs 24/7 automatically

### Detailed Guides

- **`QUICK_START.md`** - Fastest deployment (5 minutes)
- **`GITHUB_SETUP.md`** - GitHub setup instructions
- **`DEPLOYMENT_GUIDE.md`** - Complete deployment options

### What's Configured

- ✅ `Procfile` for Railway/Render
- ✅ `requirements.txt` with dependencies
- ✅ Environment variables ready
- ✅ `.gitignore` excludes sensitive files
- ✅ All deployment files included

## License

This project is open source and available for personal use.

## Support

For issues or questions:
1. Check Facebook Graph API documentation
2. Verify your access token has correct permissions
3. Check console output for error messages
4. See deployment guides for hosting issues
