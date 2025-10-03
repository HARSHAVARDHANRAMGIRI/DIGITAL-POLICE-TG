# 🚀 Digital Police TG - Deployment Guide

Deploy your Digital Police TG application to various cloud platforms for FREE!

---

## 📋 Table of Contents
1. [Railway](#1-railway-recommended)
2. [Render](#2-render)
3. [PythonAnywhere](#3-pythonanywhere)
4. [Vercel](#4-vercel)
5. [Heroku](#5-heroku)
6. [Google Cloud Run](#6-google-cloud-run)
7. [AWS Elastic Beanstalk](#7-aws-elastic-beanstalk)

---

## 🎯 Prerequisites

Before deploying, ensure you have:
- ✅ Git installed on your computer
- ✅ GitHub account (free)
- ✅ Account on your chosen platform
- ✅ All files in this repository

---

## 1. 🚂 Railway (Recommended)

**Why Railway?**
- ✅ FREE $5/month credit (enough for small apps)
- ✅ Automatic deployments from GitHub
- ✅ Built-in database support
- ✅ Easy environment variables
- ✅ Custom domains

### Deployment Steps:

#### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/digital-police-tg.git
git push -u origin main
```

#### Step 2: Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Railway will auto-detect Python and deploy!

#### Step 3: Configure Environment Variables (Optional)
- Go to your project → Variables
- Add any custom variables if needed:
  ```
  FLASK_ENV=production
  SECRET_KEY=your-secret-key-here
  ```

#### Step 4: Get Your URL
- Railway will provide a URL like: `https://your-app.railway.app`
- Click **"Generate Domain"** in the Settings tab

**✅ Done! Your app is live!**

---

## 2. 🎨 Render

**Why Render?**
- ✅ FREE tier available
- ✅ Automatic SSL certificates
- ✅ Easy database integration
- ✅ GitHub auto-deploy

### Deployment Steps:

#### Step 1: Create `render.yaml`
Already included in this repository!

#### Step 2: Deploy
1. Go to [Render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Render will detect the configuration automatically
5. Click **"Create Web Service"**

#### Configuration:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Environment**: Python 3

**✅ Your app will be live at: `https://your-app.onrender.com`**

---

## 3. 🐍 PythonAnywhere

**Why PythonAnywhere?**
- ✅ FREE tier (always free)
- ✅ Python-focused hosting
- ✅ Easy Flask deployment
- ✅ No credit card required

### Deployment Steps:

#### Step 1: Sign Up
1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Create a FREE account

#### Step 2: Upload Files
1. Go to **"Files"** tab
2. Upload your project files or clone from GitHub:
   ```bash
   git clone https://github.com/YOUR_USERNAME/digital-police-tg.git
   ```

#### Step 3: Install Dependencies
1. Open a **Bash console**
2. Navigate to your project:
   ```bash
   cd digital-police-tg
   pip install -r requirements.txt
   ```

#### Step 4: Configure Web App
1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Choose **"Flask"**
4. Set Python version to **3.10**
5. Point to your `app.py` file

#### Step 5: Configure WSGI
Edit the WSGI configuration file:
```python
import sys
path = '/home/YOUR_USERNAME/digital-police-tg'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

**✅ Your app will be live at: `https://YOUR_USERNAME.pythonanywhere.com`**

---

## 4. ▲ Vercel

**Why Vercel?**
- ✅ FREE tier
- ✅ Lightning-fast deployments
- ✅ Automatic HTTPS
- ✅ GitHub integration

### Deployment Steps:

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Deploy
```bash
cd digital-police-tg
vercel
```

Follow the prompts and your app will be deployed!

**Alternative: Deploy via GitHub**
1. Go to [Vercel.com](https://vercel.com)
2. Click **"Import Project"**
3. Connect your GitHub repository
4. Vercel will auto-deploy!

**✅ Your app will be live at: `https://your-app.vercel.app`**

---

## 5. 🟣 Heroku

**Why Heroku?**
- ✅ Popular platform
- ✅ Easy deployment
- ✅ Add-ons available
- ⚠️ FREE tier discontinued (requires credit card)

### Deployment Steps:

#### Step 1: Install Heroku CLI
Download from [Heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

#### Step 2: Login
```bash
heroku login
```

#### Step 3: Create App
```bash
heroku create your-app-name
```

#### Step 4: Deploy
```bash
git push heroku main
```

#### Step 5: Open App
```bash
heroku open
```

**✅ Your app will be live at: `https://your-app-name.herokuapp.com`**

---

## 6. ☁️ Google Cloud Run

**Why Google Cloud Run?**
- ✅ FREE tier (2 million requests/month)
- ✅ Serverless (scales to zero)
- ✅ Fast and reliable

### Deployment Steps:

#### Step 1: Install Google Cloud SDK
Download from [cloud.google.com](https://cloud.google.com/sdk/docs/install)

#### Step 2: Create Dockerfile
Already included in this repository!

#### Step 3: Deploy
```bash
gcloud run deploy digital-police-tg \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

**✅ Your app will be live at the provided Cloud Run URL**

---

## 7. 🟠 AWS Elastic Beanstalk

**Why AWS?**
- ✅ FREE tier (12 months)
- ✅ Scalable
- ✅ Enterprise-grade

### Deployment Steps:

#### Step 1: Install EB CLI
```bash
pip install awsebcli
```

#### Step 2: Initialize
```bash
eb init -p python-3.10 digital-police-tg
```

#### Step 3: Create Environment
```bash
eb create digital-police-tg-env
```

#### Step 4: Deploy
```bash
eb deploy
```

**✅ Your app will be live at the provided AWS URL**

---

## 🔧 Configuration Files Included

This repository includes all necessary configuration files:

- ✅ `Procfile` - For Heroku/Railway
- ✅ `railway.json` - For Railway
- ✅ `render.yaml` - For Render
- ✅ `vercel.json` - For Vercel
- ✅ `Dockerfile` - For containerized deployments
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version

---

## 🌐 Custom Domain Setup

### Railway
1. Go to Settings → Domains
2. Click **"Custom Domain"**
3. Add your domain and update DNS records

### Render
1. Go to Settings → Custom Domains
2. Add your domain
3. Update DNS with provided CNAME

### Vercel
1. Go to Settings → Domains
2. Add your domain
3. Follow DNS configuration steps

---

## 🔒 Environment Variables

For production, set these environment variables:

```bash
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=your-database-url (if using external DB)
```

### How to Generate SECRET_KEY:
```python
import secrets
print(secrets.token_hex(32))
```

---

## 📊 Database Configuration

### SQLite (Default)
- Works out of the box
- Good for testing
- ⚠️ Not recommended for production

### PostgreSQL (Recommended for Production)
Update `app.py`:
```python
import os
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///police_cases.db')
```

Add to `requirements.txt`:
```
psycopg2-binary
```

---

## 🐛 Troubleshooting

### Issue: App crashes on startup
**Solution**: Check logs
```bash
# Railway
railway logs

# Render
Check dashboard logs

# Heroku
heroku logs --tail
```

### Issue: Database not persisting
**Solution**: Use external database (PostgreSQL) instead of SQLite

### Issue: Static files not loading
**Solution**: Ensure `static` folder is included in deployment

---

## 📞 Support

Need help? Check:
- 📖 [Flask Documentation](https://flask.palletsprojects.com/)
- 🚂 [Railway Docs](https://docs.railway.app/)
- 🎨 [Render Docs](https://render.com/docs)
- 🐍 [PythonAnywhere Help](https://help.pythonanywhere.com/)

---

## 🎉 Quick Deploy Buttons

Click to deploy instantly:

### Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/YOUR_USERNAME/digital-police-tg)

### Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/digital-police-tg)

---

## ✅ Recommended Platform Comparison

| Platform | Free Tier | Ease | Database | Custom Domain | Best For |
|----------|-----------|------|----------|---------------|----------|
| **Railway** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | **Recommended** |
| **Render** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Great alternative |
| **PythonAnywhere** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ❌ (paid) | Python projects |
| **Vercel** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | ✅ | Serverless apps |
| **Heroku** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | Requires card |

---

## 🚀 Ready to Deploy?

**Recommended Path:**
1. ✅ Push code to GitHub
2. ✅ Deploy on Railway (easiest)
3. ✅ Configure custom domain (optional)
4. ✅ Share your live app!

**Your app will be accessible worldwide in minutes!** 🌍

---

Made with ❤️ for Telangana Police Digital Initiative