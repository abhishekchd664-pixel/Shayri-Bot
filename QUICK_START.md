# Quick Start: Deploy to Run 24/7

## 🚀 Fastest Way: Railway (Recommended)

### Step 1: Push to GitHub

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: Hindi Shayari Auto-Poster"

# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Railway

1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub
3. **Click**: "New Project" → "Deploy from GitHub repo"
4. **Select**: Your `shayari-poster` repository
5. **Add Environment Variables**:
   - `FACEBOOK_PAGE_ID` = `992326403963839`
   - `FACEBOOK_ACCESS_TOKEN` = `your_long_lived_token_here`
6. **Deploy**: Railway auto-detects Python and deploys!

### Step 3: Verify

- Check Railway logs to see if it's running
- Visit your Facebook page to see posts
- Script runs 24/7 automatically!

## 📋 What You Need

- ✅ GitHub account (free)
- ✅ Railway account (free tier: 500 hours/month)
- ✅ Facebook Page Access Token (already have it!)

## 🔐 Security

**IMPORTANT**: Never commit your access token to GitHub!

- ✅ Use environment variables (already configured)
- ✅ Set tokens in Railway dashboard, not in code
- ✅ `.gitignore` already excludes sensitive files

## 🎯 Alternative: Render

If Railway doesn't work:

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. New → Background Worker
4. Connect your GitHub repo
5. Set environment variables
6. Deploy!

## 📊 Platform Comparison

| Feature | Railway | Render |
|---------|---------|--------|
| Free Tier | ✅ 500 hrs/month | ✅ Limited |
| Auto Deploy | ✅ Yes | ✅ Yes |
| Easy Setup | ✅ Very Easy | ✅ Easy |
| Best For | This project | Alternative |

## 🆘 Troubleshooting

**Script stops?**
- Check Railway logs
- Verify token is still valid
- Check if you hit free tier limits

**No posts appearing?**
- Verify Facebook token
- Check Facebook API rate limits
- Review Railway logs for errors

## 📝 Next Steps After Deployment

1. Monitor logs in Railway dashboard
2. Check your Facebook page for posts
3. Set up alerts (optional)
4. Enjoy automated posting! 🎉
