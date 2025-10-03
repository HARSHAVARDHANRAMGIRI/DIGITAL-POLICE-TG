# 🚀 Deploy to PythonAnywhere - Step by Step

## 📋 Complete Deployment Guide for FREE Lifetime Hosting

---

## ✅ Prerequisites

- ✅ A GitHub account (to host your code)
- ✅ 10 minutes of your time
- ❌ NO credit card needed
- ❌ NO payment required

---

## 🎯 Step 1: Push Your Code to GitHub

### Option A: Using Git Command Line

```bash
# Navigate to your project folder
cd "c:\Users\rhars\Downloads\DIGITAL-POLICE-TG-main\DIGITAL-POLICE-TG-main"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for PythonAnywhere deployment"

# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/digital-police-tg.git
git branch -M main
git push -u origin main
```

### Option B: Using GitHub Desktop

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop
3. Click **"Add"** → **"Add Existing Repository"**
4. Select your project folder
5. Click **"Publish repository"**
6. Choose repository name: `digital-police-tg`
7. Click **"Publish repository"**

---

## 🎯 Step 2: Create PythonAnywhere Account

1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Click **"Pricing & signup"**
3. Scroll down to **"Create a Beginner account"**
4. Click **"Create a Beginner account"** (100% FREE)
5. Fill in:
   - Username (this will be your URL: `username.pythonanywhere.com`)
   - Email
   - Password
6. Click **"Register"**
7. Verify your email

✅ **Account created! No credit card needed!**

---

## 🎯 Step 3: Clone Your Repository

1. In PythonAnywhere, click **"Consoles"** tab
2. Click **"Bash"** to start a new console
3. In the console, run:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/digital-police-tg.git

# Navigate to the project
cd digital-police-tg

# Verify files are there
ls -la
```

✅ **Code uploaded to PythonAnywhere!**

---

## 🎯 Step 4: Install Dependencies

In the same Bash console:

```bash
# Make sure you're in the project directory
cd ~/digital-police-tg

# Install all required packages
pip3.10 install --user -r requirements.txt

# Wait for installation to complete (1-2 minutes)
```

You should see messages like:
```
Successfully installed Flask-2.3.3 Flask-SQLAlchemy-3.0.5 ...
```

✅ **Dependencies installed!**

---

## 🎯 Step 5: Create Web App

1. Click **"Web"** tab (at the top)
2. Click **"Add a new web app"**
3. Click **"Next"** (for free domain)
4. Choose **"Manual configuration"** (NOT Flask!)
5. Select **"Python 3.10"**
6. Click **"Next"**

✅ **Web app created!**

---

## 🎯 Step 6: Configure WSGI File

1. On the **"Web"** tab, scroll to **"Code"** section
2. Click on the **WSGI configuration file** link (blue link)
3. **DELETE ALL** existing content
4. **PASTE** this code:

```python
import sys
import os

# IMPORTANT: Replace YOUR_USERNAME with your actual PythonAnywhere username
project_home = '/home/YOUR_USERNAME/digital-police-tg'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['FLASK_ENV'] = 'production'

from app import app as application
```

5. **IMPORTANT:** Replace `YOUR_USERNAME` with your actual PythonAnywhere username
   - Example: If your username is `john123`, change to:
   - `/home/john123/digital-police-tg`

6. Click **"Save"** (top right)

✅ **WSGI configured!**

---

## 🎯 Step 7: Configure Static Files

1. Still on the **"Web"** tab, scroll to **"Static files"** section
2. Click **"Enter URL"** and type: `/static/`
3. Click **"Enter path"** and type: `/home/YOUR_USERNAME/digital-police-tg/static/`
   - Replace `YOUR_USERNAME` with your username
4. Click the ✓ (checkmark) to save

✅ **Static files configured!**

---

## 🎯 Step 8: Set Working Directory (Optional but Recommended)

1. On the **"Web"** tab, scroll to **"Code"** section
2. Find **"Working directory"**
3. Click **"Enter path"**
4. Type: `/home/YOUR_USERNAME/digital-police-tg/`
   - Replace `YOUR_USERNAME` with your username
5. Click the ✓ (checkmark)

✅ **Working directory set!**

---

## 🎯 Step 9: Initialize Database

1. Go back to **"Consoles"** tab
2. Open your Bash console (or start a new one)
3. Run:

```bash
cd ~/digital-police-tg
python3.10 -c "from app import db, app; app.app_context().push(); db.create_all(); print('Database created!')"
```

You should see: `Database created!`

✅ **Database initialized!**

---

## 🎯 Step 10: Reload and Launch! 🚀

1. Go back to **"Web"** tab
2. Scroll to the top
3. Click the big green **"Reload"** button
4. Wait for reload to complete (5-10 seconds)
5. Click on your app URL: `https://YOUR_USERNAME.pythonanywhere.com`

✅ **YOUR APP IS LIVE!** 🎉

---

## 🎊 Success! Your App is Online!

Your Digital Police TG application is now live at:
```
https://YOUR_USERNAME.pythonanywhere.com
```

### Test Your App:

1. ✅ Visit the homepage
2. ✅ Check if logo is visible
3. ✅ Try registering a new user
4. ✅ Login with demo credentials:
   - **Aadhaar:** 123456789012
   - **Password:** police123
5. ✅ Test nearby stations feature
6. ✅ File a test case

---

## 🔧 Troubleshooting

### Issue 1: "ImportError: No module named 'flask'"
**Solution:** Install dependencies again:
```bash
cd ~/digital-police-tg
pip3.10 install --user -r requirements.txt
```

### Issue 2: "500 Internal Server Error"
**Solution:** Check error log:
1. Go to **"Web"** tab
2. Scroll to **"Log files"**
3. Click **"Error log"**
4. Check for errors and fix them

### Issue 3: Static files (logo) not loading
**Solution:** Verify static files path:
1. Go to **"Web"** tab
2. Check **"Static files"** section
3. Ensure path is: `/home/YOUR_USERNAME/digital-police-tg/static/`

### Issue 4: Database errors
**Solution:** Recreate database:
```bash
cd ~/digital-police-tg
rm -f instance/police_cases.db
python3.10 -c "from app import db, app; app.app_context().push(); db.create_all()"
```

---

## 🔄 Updating Your App

When you make changes to your code:

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Updated features"
git push
```

### Step 2: Pull on PythonAnywhere
```bash
# In PythonAnywhere Bash console
cd ~/digital-police-tg
git pull
```

### Step 3: Reload
1. Go to **"Web"** tab
2. Click **"Reload"**

✅ **App updated!**

---

## 📊 Monitor Your App

### Check Logs:
1. Go to **"Web"** tab
2. Scroll to **"Log files"**
3. View:
   - **Error log** - For errors
   - **Server log** - For requests
   - **Access log** - For traffic

### Check Traffic:
1. Go to **"Web"** tab
2. See **"Statistics"** section
3. View daily hits

---

## 🎯 Free Tier Limits

Your free PythonAnywhere account includes:
- ✅ **512 MB disk space** (plenty for this app)
- ✅ **100,000 hits per day** (more than enough)
- ✅ **1 web app** (this app)
- ✅ **Always-on** (no sleep mode)
- ✅ **Free subdomain** (username.pythonanywhere.com)

### Need More?
Upgrade to paid plan ($5/month) for:
- Custom domain support
- More disk space
- More web apps
- SSH access

---

## 🌐 Share Your App

Your app is now live! Share it with:

```
🔗 App URL: https://YOUR_USERNAME.pythonanywhere.com

👮 Demo Police Login:
   Aadhaar: 123456789012
   Password: police123

👤 New users can register with any Aadhaar number
```

---

## 🎉 Congratulations!

You've successfully deployed your Digital Police TG application to PythonAnywhere!

### What You've Achieved:
- ✅ Free lifetime hosting
- ✅ 24/7 uptime (no sleep mode)
- ✅ Professional subdomain
- ✅ SSL certificate (HTTPS)
- ✅ Easy updates via Git

### Next Steps:
1. Share your app URL with others
2. Test all features
3. Monitor logs for any issues
4. Consider upgrading for custom domain

---

## 📞 Need Help?

- 📖 [PythonAnywhere Help](https://help.pythonanywhere.com/)
- 💬 [PythonAnywhere Forums](https://www.pythonanywhere.com/forums/)
- 📧 [Contact Support](https://www.pythonanywhere.com/contact/)
- 🎥 [Video Tutorials](https://www.youtube.com/results?search_query=pythonanywhere+flask)

---

**Your app is live and ready to serve citizens of Telangana!** 🚔👮‍♂️

Made with ❤️ for Digital Police TG