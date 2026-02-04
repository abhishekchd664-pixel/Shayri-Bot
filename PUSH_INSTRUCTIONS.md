# Push to GitHub - Step by Step Instructions

## Quick Commands (Copy & Paste)

### Step 1: Configure Git (One Time)

```powershell
git config user.email "your_email@example.com"
git config user.name "Your Name"
```

**Replace:**
- `your_email@example.com` with your GitHub email
- `Your Name` with your name

### Step 2: Create Commit

```powershell
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster with 24/7 deployment support"
git branch -M main
```

### Step 3: Create GitHub Repository

1. **Go to**: https://github.com/new
2. **Repository name**: `shayari-poster` (or any name)
3. **Description**: "Automated Hindi Shayari poster for Facebook Page"
4. **Visibility**: Public or Private (your choice)
5. **⚠️ IMPORTANT**: Do NOT check "Initialize with README"
6. **Click**: "Create repository"

### Step 4: Connect and Push

After creating the repository, GitHub will show you commands. Use these:

```powershell
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git
git push -u origin main
```

**Example:**
If your username is `john`, the command would be:
```powershell
git remote add origin https://github.com/john/shayari-poster.git
git push -u origin main
```

## ✅ Verification

After pushing, you should see:
- All your files on GitHub
- Repository URL: `https://github.com/YOUR_USERNAME/shayari-poster`

## 🚀 Next Step: Deploy to Railway

Once your code is on GitHub:
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Deploy from your GitHub repo
4. Add environment variables
5. Done! Runs 24/7!

See `START_HERE.md` for complete deployment guide.

## 🆘 Troubleshooting

### "Repository not found"
- Check your GitHub username is correct
- Make sure you created the repository first

### "Authentication failed"
- Use GitHub Personal Access Token instead of password
- Or use GitHub Desktop app

### "Permission denied"
- Make sure you're logged into GitHub
- Check repository name matches
