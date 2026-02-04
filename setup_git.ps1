# PowerShell script to set up Git and push to GitHub

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Git Setup for Hindi Shayari Poster" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Configure Git (you'll need to enter your details)
Write-Host "Step 1: Configure Git" -ForegroundColor Yellow
Write-Host "Enter your GitHub email address:" -ForegroundColor White
$email = Read-Host
Write-Host "Enter your name (for Git commits):" -ForegroundColor White
$name = Read-Host

git config user.email $email
git config user.name $name

Write-Host ""
Write-Host "Git configured!" -ForegroundColor Green
Write-Host ""

# Create initial commit
Write-Host "Step 2: Creating initial commit..." -ForegroundColor Yellow
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster with 24/7 deployment support"
git branch -M main

Write-Host ""
Write-Host "Commit created!" -ForegroundColor Green
Write-Host ""

# Instructions for GitHub
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create a new repository on GitHub:" -ForegroundColor White
Write-Host "   https://github.com/new" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Name it: shayari-poster" -ForegroundColor White
Write-Host ""
Write-Host "3. DO NOT initialize with README (we already have files)" -ForegroundColor Red
Write-Host ""
Write-Host "4. After creating, run these commands:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "5. Then deploy to Railway (see QUICK_START.md)" -ForegroundColor White
Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
