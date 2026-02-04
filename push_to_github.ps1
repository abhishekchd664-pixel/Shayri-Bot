# PowerShell script to push to GitHub

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Push to GitHub - Hindi Shayari Poster" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git user is configured
$email = git config user.email
$name = git config user.name

if (-not $email -or -not $name) {
    Write-Host "Git user not configured. Let's set it up:" -ForegroundColor Yellow
    Write-Host ""
    $email = Read-Host "Enter your GitHub email address"
    $name = Read-Host "Enter your name (for Git commits)"
    
    git config user.email $email
    git config user.name $name
    Write-Host ""
    Write-Host "Git configured!" -ForegroundColor Green
    Write-Host ""
}

# Create commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git add .
git commit -m "Initial commit: Hindi Shayari Auto-Poster with 24/7 deployment support"
git branch -M main

Write-Host ""
Write-Host "Commit created successfully!" -ForegroundColor Green
Write-Host ""

# Check if remote exists
$remote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Next Step: Create GitHub Repository" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Go to: https://github.com/new" -ForegroundColor White
    Write-Host ""
    Write-Host "2. Repository name: shayari-poster" -ForegroundColor White
    Write-Host "   (or any name you like)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "3. DO NOT check 'Initialize with README'" -ForegroundColor Red
    Write-Host ""
    Write-Host "4. Click 'Create repository'" -ForegroundColor White
    Write-Host ""
    Write-Host "5. After creating, run this command:" -ForegroundColor Yellow
    Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "6. Then push:" -ForegroundColor Yellow
    Write-Host "   git push -u origin main" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host "Remote already configured: $remote" -ForegroundColor Green
    Write-Host ""
    Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
    git push -u origin main
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "Successfully pushed to GitHub!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Next: Deploy to Railway (see START_HERE.md)" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "Push failed. Check your GitHub credentials." -ForegroundColor Red
    }
}

Write-Host "==========================================" -ForegroundColor Cyan
