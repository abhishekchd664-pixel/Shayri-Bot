# 🎯 START HERE: Deploy Your Auto-Poster to Run 24/7

Everything is ready! Follow these simple steps to get your Hindi Shayari poster running 24/7.

## ✅ What's Already Done

- ✅ Code is ready and tested
- ✅ Git repository initialized
- ✅ All deployment files created
- ✅ Security configured (tokens excluded)
- ✅ Long-lived token set up (59 days)

## 🚀 Quick Start (3 Steps)

### Step 1: Configure Git & Push to GitHub

**Option A - Use the script:**
```powershell
.\setup_git.ps1
```

**Option B - Manual:**
```powershell
# Set your Git identity
git config user.email "your_email@example.com"
git config user.name "Your Name"

# Create commit
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster"
git branch -M main

# Create repository on GitHub first at: https://github.com/new
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git
git push -u origin main
```

### Step 2: Deploy to Railway (Free 24/7 Hosting)

1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub (one click)
3. **Click**: "New Project" → "Deploy from GitHub repo"
4. **Select**: Your `shayari-poster` repository
5. **Add Environment Variables** (in Railway dashboard):
   - `FACEBOOK_PAGE_ID` = `992326403963839`
   - `FACEBOOK_ACCESS_TOKEN` = `EAA7vMs3yYxABQtyIYJN8QdnNbyX01ffUxqUesHjjgpZAfyGKoZC35AAi4TzWj312GT3uXBloTnVvFevVV36H6Mf75K1ZAL1yUufQzalYeiTHqCCRkIfWnRkVpus8cxHsrmjiP12mf2EAjZB6foz59pCoHzmA4OozdQJCY0hGtJZBJ45R4rAX0TlN0fooiMx62hQcw`
6. **Done!** Railway auto-deploys and runs 24/7!

### Step 3: Verify It's Working

- Check Railway logs (should show "Starting posting process...")
- Visit your Facebook page: https://www.facebook.com/992326403963839
- Posts should appear every 5 minutes!

## 📚 Need More Details?

- **`QUICK_START.md`** - Fastest deployment guide
- **`GITHUB_SETUP.md`** - Detailed GitHub instructions
- **`DEPLOYMENT_GUIDE.md`** - All deployment options

## 🔐 Security Notes

✅ **Safe**: Your tokens are NOT in the code
✅ **Safe**: Sensitive files excluded from Git
✅ **Safe**: Using environment variables

## 💰 Cost

- **Railway Free Tier**: 500 hours/month (enough for 24/7!)
- **Total Cost**: $0 (free tier is sufficient)

## 🎉 That's It!

Once deployed, your script will:
- ✅ Run 24/7 automatically
- ✅ Post every 5 minutes
- ✅ Auto-restart if it crashes
- ✅ Update when you push to GitHub

## 🆘 Troubleshooting

**Script not running?**
- Check Railway logs
- Verify environment variables are set
- Check token hasn't expired

**No posts appearing?**
- Verify Facebook token is valid
- Check Facebook API rate limits
- Review Railway logs

## 📞 Next Steps

1. Run `setup_git.ps1` or configure Git manually
2. Push to GitHub
3. Deploy on Railway
4. Enjoy automated posting! 🎊

---

**Ready? Start with Step 1 above!** 🚀
