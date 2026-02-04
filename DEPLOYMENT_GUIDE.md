# 24/7 Deployment Guide for Hindi Shayari Auto-Poster

This guide will help you deploy your script to run 24/7 on cloud platforms.

## ⚠️ Important: GitHub Actions Limitation

GitHub Actions is **NOT suitable** for 24/7 running scripts because:
- Actions have time limits (6 hours max for free tier)
- They're designed for CI/CD, not long-running processes
- Costs can add up quickly

## ✅ Recommended Solutions for 24/7 Hosting

### Option 1: Railway (Recommended - Free Tier Available)
- **Free tier**: 500 hours/month
- **Easy setup**: Connect GitHub repo
- **Auto-deploy**: Updates automatically
- **Best for**: This project

### Option 2: Render
- **Free tier**: Available (with limitations)
- **Easy setup**: Connect GitHub repo
- **Good alternative**: If Railway doesn't work

### Option 3: PythonAnywhere
- **Free tier**: Limited but works
- **Simple**: Upload and run
- **Good for**: Testing

### Option 4: Heroku
- **Paid only**: No free tier anymore
- **Reliable**: If you have budget

## 🚀 Quick Start: Railway Deployment

### Step 1: Prepare Your Code

1. **Keep secrets safe**: Don't commit tokens to GitHub
2. **Use environment variables**: Already configured in `main.py`
3. **Add requirements**: Already have `requirements.txt`

### Step 2: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git
git push -u origin main
```

### Step 3: Deploy on Railway

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables:
   - `FACEBOOK_PAGE_ID=992326403963839`
   - `FACEBOOK_ACCESS_TOKEN=your_token_here`
6. Railway will auto-detect Python and deploy!

### Step 4: Configure for 24/7

Railway keeps your app running automatically. No extra configuration needed!

## 📋 Environment Variables to Set

On your hosting platform, set these:

```
FACEBOOK_PAGE_ID=992326403963839
FACEBOOK_ACCESS_TOKEN=your_long_lived_token_here
```

## 🔧 Platform-Specific Setup

### Railway Setup

1. **Procfile** (already created): Tells Railway how to run your app
2. **runtime.txt** (optional): Specify Python version
3. **Environment variables**: Set in Railway dashboard

### Render Setup

1. Create `render.yaml` (already created)
2. Connect GitHub repo
3. Set environment variables
4. Deploy!

### PythonAnywhere Setup

1. Upload files via web interface
2. Create a scheduled task (runs every 5 minutes)
3. Or use "Always-on task" for continuous running

## 🔄 Updating Your Code

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update code"
   git push
   ```
3. Platform auto-deploys (if connected to GitHub)

## 💰 Cost Comparison

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Railway | 500 hrs/month | $5/month |
| Render | Limited | $7/month |
| PythonAnywhere | Limited | $5/month |
| Heroku | None | $7/month |

## 🛠️ Troubleshooting

### Script stops after a few hours
- Check platform logs
- Verify token hasn't expired
- Check if platform has time limits

### Posts not appearing
- Verify Facebook token is valid
- Check Facebook API rate limits
- Review platform logs for errors

### High costs
- Monitor usage on platform dashboard
- Consider switching to cheaper platform
- Optimize script (reduce posting frequency if needed)

## 📝 Next Steps

1. Choose a platform (Railway recommended)
2. Push code to GitHub
3. Deploy using platform's GitHub integration
4. Set environment variables
5. Monitor logs to ensure it's working

## 🔐 Security Notes

- **Never commit** access tokens to GitHub
- Use environment variables for all secrets
- Regularly rotate your Facebook tokens
- Monitor for unauthorized access
