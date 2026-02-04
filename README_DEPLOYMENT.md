# 🚀 Deploy Your Hindi Shayari Auto-Poster to Run 24/7

Your code is ready to deploy! Follow these simple steps.

## 📋 Quick Setup (5 minutes)

### Step 1: Configure Git

Run this PowerShell script:
```powershell
.\setup_git.ps1
```

Or manually:
```powershell
git config user.email "your_email@example.com"
git config user.name "Your Name"
```

### Step 2: Create GitHub Repository

1. Go to: **https://github.com/new**
2. Name: `shayari-poster`
3. **Don't** initialize with README
4. Click "Create repository"

### Step 3: Push to GitHub

```powershell
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git
git push -u origin main
```

### Step 4: Deploy to Railway (24/7 Hosting)

1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Select**: Your `shayari-poster` repository
5. **Add Environment Variables**:
   - `FACEBOOK_PAGE_ID` = `992326403963839`
   - `FACEBOOK_ACCESS_TOKEN` = `your_token_here`
6. **Done!** Your script runs 24/7 automatically!

## 📚 Detailed Guides

- **`QUICK_START.md`** - Fastest deployment guide
- **`GITHUB_SETUP.md`** - Detailed GitHub setup
- **`DEPLOYMENT_GUIDE.md`** - Complete deployment options

## ✅ What's Already Configured

- ✅ Git repository initialized
- ✅ `.gitignore` excludes sensitive files
- ✅ `Procfile` for Railway/Render
- ✅ `requirements.txt` with dependencies
- ✅ Environment variables configured
- ✅ All deployment files ready

## 🔐 Security

**Your tokens are safe!**
- ✅ Sensitive files excluded from Git
- ✅ Tokens use environment variables
- ✅ No secrets in code

## 🎯 What Happens After Deployment

1. Script runs 24/7 on Railway
2. Posts every 5 minutes automatically
3. Logs available in Railway dashboard
4. Auto-restarts if it crashes
5. Updates when you push to GitHub

## 🆘 Need Help?

- Check `DEPLOYMENT_GUIDE.md` for troubleshooting
- Railway has great documentation
- All guides are in this repository

## 🎉 Ready to Deploy?

Start with `QUICK_START.md` - it's the fastest way!
