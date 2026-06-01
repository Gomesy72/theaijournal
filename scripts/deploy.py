#!/usr/bin/env python3
"""
Deploy The AI Journal to GitHub Pages
Usage: python deploy.py
"""

import os
import subprocess
import datetime

def deploy():
    """Deploy the site to GitHub Pages"""
    
    # Check if we're in the right directory
    if not os.path.exists("index.html"):
        print("Error: Must run from theaijournal directory")
        return False
    
    # Configure git (if not already done)
    os.system("git config user.email 'shellyai2026@gmail.com'")
    os.system("git config user.name 'Shelly AI'")
    
    # Add all files
    result = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git add failed: {result.stderr}")
        return False
    
    # Commit
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    result = subprocess.run(
        ["git", "commit", "-m", f"Update site - {date_str}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Git commit failed: {result.stderr}")
        return False
    
    # Push to main
    result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git push failed: {result.stderr}")
        return False
    
    print("✅ Deployed successfully!")
    print("🌐 Site will be live at: https://gomesy72.github.io/theaijournal/")
    print("⏳ Allow 1-2 minutes for GitHub Pages to update")
    return True

if __name__ == "__main__":
    deploy()
