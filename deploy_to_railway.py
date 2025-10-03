#!/usr/bin/env python3
"""
🚀 RAILWAY DEPLOYMENT HELPER - DIGITAL POLICE TG
Deploy your website to Railway for FREE worldwide access!
"""

import webbrowser
import os
import sys

def main():
    print("=" * 60)
    print("🚀 DIGITAL POLICE TG - FREE WORLDWIDE DEPLOYMENT")
    print("=" * 60)
    
    print("\n🎯 STEP 1: Open Railway Website")
    print("   I'll open railway.app in your browser...")
    input("   Press Enter to continue...")
    
    # Open Railway website
    webbrowser.open("https://railway.app")
    
    print("\n🎯 STEP 2: Sign Up (FREE)")
    print("   1. Click 'Start a New Project'")
    print("   2. Sign up with GitHub account")
    print("   3. Verify your email")
    
    input("\n   Press Enter when you're signed up...")
    
    print("\n🎯 STEP 3: Deploy Your App")
    print("   1. Click 'Deploy from GitHub repo'")
    print("   2. Select your 'fir_project' repository")
    print("   3. Railway will auto-detect Python app")
    print("   4. Click 'Deploy'")
    
    input("\n   Press Enter when deployment starts...")
    
    print("\n🎯 STEP 4: Get Your Worldwide URL")
    print("   Wait 2-3 minutes for build to complete...")
    print("   You'll get a URL like: https://your-app.railway.app")
    
    input("\n   Press Enter when you have your URL...")
    
    print("\n🎯 STEP 5: Test Your Website")
    print("   - Open your Railway URL in browser")
    print("   - Test citizen registration")
    print("   - Test police dashboard")
    print("   - Share URL with everyone!")
    
    print("\n" + "=" * 60)
    print("🎉 CONGRATULATIONS! Your website is now LIVE worldwide!")
    print("🌍 Anyone with internet can access your DIGITAL POLICE TG!")
    print("💰 Total Cost: FREE!")
    print("=" * 60)
    
    # Ask if they want to open their deployed site
    open_site = input("\n   Do you want to open your deployed website? (y/n): ")
    if open_site.lower() in ['y', 'yes']:
        site_url = input("   Enter your Railway URL: ")
        if site_url:
            webbrowser.open(site_url)
            print(f"   Opening: {site_url}")
    
    print("\n🚀 Your DIGITAL POLICE TG is now accessible to EVERYONE worldwide!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Deployment cancelled. Your website is still ready to deploy!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Don't worry! You can still deploy manually by following the guide.")
