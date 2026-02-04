#!/bin/bash
# Setup script for GitHub deployment

echo "=========================================="
echo "Setting up GitHub repository"
echo "=========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files
echo "Adding files to git..."
git add .

# Create initial commit
echo "Creating initial commit..."
git commit -m "Initial commit: Hindi Shayari Auto-Poster with 24/7 deployment support"

# Rename branch to main
git branch -M main

echo ""
echo "=========================================="
echo "Next steps:"
echo "=========================================="
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo ""
echo "2. Name it: shayari-poster (or any name you like)"
echo ""
echo "3. Don't initialize with README (we already have one)"
echo ""
echo "4. Copy the repository URL and run:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/shayari-poster.git"
echo "   git push -u origin main"
echo ""
echo "5. Then deploy to Railway or Render (see DEPLOYMENT_GUIDE.md)"
echo "=========================================="
