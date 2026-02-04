# GitHub Setup Instructions

## ✅ Step 1: Create GitHub Repository

1. Go to: **https://github.com/new**
2. **Repository name**: `shayari-poster` (or any name you like)
3. **Description**: "Automated Hindi Shayari poster for Facebook Page"
4. **Visibility**: Choose Public or Private
5. **⚠️ IMPORTANT**: Do NOT check "Initialize with README" (we already have files)
6. Click **"Create repository"**

## ✅ Step 2: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git

# Push your code
git push -u origin main
```

**Example:**
If your username is `john`, the command would be:
```bash
git remote add origin https://github.com/john/shayari-poster.git
git push -u origin main
```

## ✅ Step 3: Verify on GitHub

1. Go to your repository on GitHub
2. You should see all your files
3. Check that sensitive files (like `quick_extend.py`) are NOT visible
4. Your code is now on GitHub! 🎉

## ✅ Step 4: Deploy to Railway (24/7 Hosting)

Now that your code is on GitHub, deploy it:

1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub (one-click signup)
3. **Click**: "New Project"
4. **Select**: "Deploy from GitHub repo"
5. **Choose**: Your `shayari-poster` repository
6. **Add Environment Variables**:
   - Click on your project → "Variables" tab
   - Add: `FACEBOOK_PAGE_ID` = `992326403963839`
   - Add: `FACEBOOK_ACCESS_TOKEN` = `your_long_lived_token_here`
7. **Deploy**: Railway automatically detects Python and starts your app!

## 🔐 Security Checklist

Before pushing, verify:
- ✅ `.gitignore` excludes sensitive files
- ✅ No tokens in `main.py` (using environment variables)
- ✅ Token files are in `.gitignore`

## 📝 Quick Commands Reference

```bash
# Check what will be committed
git status

# Add all files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Check remote
git remote -v
```

## 🆘 Troubleshooting

### "Repository not found"
- Check your GitHub username is correct
- Verify repository name matches
- Make sure you created the repository first

### "Authentication failed"
- Use GitHub Personal Access Token instead of password
- Or use GitHub Desktop app

### "Files not showing on GitHub"
- Make sure you ran `git add .` and `git commit`
- Check `.gitignore` isn't excluding important files

## 🎯 Next: Deploy to Railway

Once your code is on GitHub, follow `QUICK_START.md` to deploy to Railway for 24/7 hosting!
