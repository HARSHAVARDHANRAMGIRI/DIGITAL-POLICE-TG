# 🚀 Deploy to Render - Step-by-Step Guide

Deploy your **Digital Police TG** application to Render for FREE with this comprehensive guide.

---

## 📋 Prerequisites

1. **GitHub Account** - Your code is already on GitHub
2. **Render Account** - Sign up at [render.com](https://render.com) (FREE)
3. **Your Repository** - https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG

---

## 🎯 Method 1: One-Click Deploy (Easiest)

### Step 1: Click the Deploy Button

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)

### Step 2: Connect Your GitHub Account
- Click "Connect GitHub"
- Authorize Render to access your repositories

### Step 3: Configure Service
- **Service Name:** `digital-police-tg`
- **Region:** Choose closest to your users
- **Branch:** `main`
- **Plan:** Free
- Click **Create Web Service**

### Step 4: Wait for Deployment
- Render will automatically build and deploy your app
- Takes about 3-5 minutes
- You'll get a live URL like: `https://digital-police-tg.onrender.com`

---

## 🛠️ Method 2: Manual Deploy via Render Dashboard

### Step 1: Sign Up/Login to Render
1. Go to [render.com](https://render.com)
2. Click **Get Started** (or Login)
3. Choose **Sign up with GitHub**

### Step 2: Create New Web Service
1. Click **New +** → **Web Service**
2. Click **Connect a repository**
3. Find your repository: `HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG`
4. Click **Connect**

### Step 3: Configure Build Settings

Fill in these details:

**Basic Settings:**
```
Name: digital-police-tg
Region: Oregon (US West) or closest to you
Branch: main
Runtime: Python 3
```

**Build Settings:**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

**Instance Type:**
```
Plan: Free
```

### Step 4: Add Environment Variables
Click **Advanced** → **Add Environment Variable**

Add these variables:
```
FLASK_ENV = production
SECRET_KEY = your-secret-key-here
PYTHON_VERSION = 3.12.0
```

To generate a secure SECRET_KEY:
```python
import secrets
print(secrets.token_hex(32))
```

### Step 5: Deploy
1. Click **Create Web Service**
2. Wait 3-5 minutes for build to complete
3. Your app will be live at: `https://digital-police-tg.onrender.com`

---

## ⚙️ Configuration Files

Your project already has `render.yaml` configured:

```yaml
services:
  - type: web
    name: digital-police-tg
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
      - key: PYTHON_VERSION
        value: 3.12.0
```

---

## 🗄️ Add PostgreSQL Database (Optional)

Render's free tier includes PostgreSQL database!

### Step 1: Create Database
1. Go to Render Dashboard
2. Click **New +** → **PostgreSQL**
3. Fill in:
   ```
   Name: digital-police-tg-db
   Database: police_db
   User: police_user
   Region: Same as your web service
   Plan: Free
   ```
4. Click **Create Database**

### Step 2: Get Database URL
1. Open your database in Render
2. Copy the **Internal Database URL**
3. It looks like: `postgresql://user:pass@host/dbname`

### Step 3: Update Your Web Service
1. Go to your web service
2. Click **Environment** → **Add Environment Variable**
3. Add:
   ```
   DATABASE_URL = postgresql://user:pass@host/dbname
   ```

### Step 4: Update app.py
```python
import os

# Use PostgreSQL if DATABASE_URL is set, otherwise SQLite
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # Render uses postgresql:// but SQLAlchemy needs postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///police_system.db'
```

### Step 5: Update requirements.txt
Add PostgreSQL driver:
```
psycopg2-binary==2.9.9
```

### Step 6: Redeploy
Render will automatically redeploy when you push to GitHub.

---

## 🌐 Custom Domain Setup

### Step 1: Go to Settings
1. Open your web service in Render
2. Click **Settings** → **Custom Domains**

### Step 2: Add Your Domain
1. Click **Add Custom Domain**
2. Enter your domain (e.g., `digitalpolice.com`)
3. Click **Save**

### Step 3: Configure DNS
Add these records to your domain provider:

**For Root Domain:**
```
Type: CNAME
Name: @
Value: digital-police-tg.onrender.com
```

**For www Subdomain:**
```
Type: CNAME
Name: www
Value: digital-police-tg.onrender.com
```

### Step 4: Verify
- Wait 5-10 minutes for DNS propagation
- Render will automatically issue SSL certificate
- Your app will be accessible at your custom domain

---

## 🔄 Automatic Deployments

Render automatically deploys when you push to GitHub:

### Enable Auto-Deploy
1. Go to **Settings** → **Build & Deploy**
2. Enable **Auto-Deploy**
3. Choose branch: `main`

### How to Update Your App
```bash
# Make changes to your code
git add .
git commit -m "Update app"
git push origin main
```

Render will automatically detect the push and redeploy!

### Manual Deploy
1. Go to your service dashboard
2. Click **Manual Deploy** → **Deploy latest commit**

---

## 📊 Monitoring & Logs

### View Logs
1. Go to your service dashboard
2. Click **Logs** tab
3. View real-time logs of your application

### View Metrics
1. Click **Metrics** tab
2. View:
   - CPU usage
   - Memory usage
   - Request count
   - Response times

### Set Up Alerts
1. Go to **Settings** → **Notifications**
2. Add email or Slack webhook
3. Get notified of:
   - Deploy failures
   - Service crashes
   - High resource usage

---

## 🐛 Troubleshooting

### Issue 1: Build Failed
**Error:** `Failed to install requirements`

**Solution:** Check your `requirements.txt`:
```bash
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
gunicorn==21.2.0
```

### Issue 2: Service Won't Start
**Error:** `Web service failed to bind to $PORT`

**Solution:** Update `app.py` to use PORT environment variable:
```python
import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Issue 3: Database Connection Failed
**Error:** `could not connect to server`

**Solution:** 
1. Verify DATABASE_URL is set correctly
2. Ensure database and web service are in same region
3. Use **Internal Database URL** (not External)

### Issue 4: App Goes to Sleep
**Issue:** Free tier apps sleep after 15 minutes of inactivity

**Solution:** Use a service to ping your app:
- **UptimeRobot** (free): https://uptimerobot.com
- **Cron-Job.org** (free): https://cron-job.org

Set up a ping every 10 minutes to: `https://digital-police-tg.onrender.com`

### Issue 5: Slow Cold Starts
**Issue:** First request after sleep takes 30+ seconds

**Solution:**
1. Upgrade to paid plan ($7/month) for no sleep
2. Or use UptimeRobot to keep app awake
3. Or optimize your app startup time

---

## 💡 Render Free Tier Limits

| Feature | Free Tier |
|---------|-----------|
| **RAM** | 512 MB |
| **CPU** | Shared |
| **Bandwidth** | 100 GB/month |
| **Build Minutes** | 500 minutes/month |
| **Instances** | 1 |
| **Sleep After** | 15 minutes inactivity |
| **Cold Start** | ~30 seconds |
| **Custom Domains** | ✅ Unlimited |
| **SSL Certificates** | ✅ Free (automatic) |
| **PostgreSQL** | ✅ 90 days (then expires) |

⚠️ **Note:** Free PostgreSQL databases expire after 90 days. Upgrade to paid plan ($7/month) for permanent database.

---

## 🎯 Best Practices

### 1. Use Environment Variables
Never hardcode secrets:
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
```

### 2. Optimize Cold Starts
Reduce startup time:
```python
# Lazy load heavy imports
def get_model():
    from heavy_module import Model
    return Model()
```

### 3. Use Persistent Storage
For file uploads, use external storage:
- AWS S3
- Cloudinary
- Render Disks (paid)

### 4. Monitor Resource Usage
- Check **Metrics** tab regularly
- Optimize memory-heavy operations
- Use caching for repeated queries

### 5. Set Up Health Checks
Add a health check endpoint:
```python
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200
```

Configure in Render:
- **Health Check Path:** `/health`

---

## 🔗 Useful Links

- **Render Dashboard:** https://dashboard.render.com
- **Your Service:** https://dashboard.render.com/web/digital-police-tg
- **Render Docs:** https://render.com/docs
- **Python on Render:** https://render.com/docs/deploy-flask
- **GitHub Repo:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG

---

## 🆚 Render vs Other Platforms

| Feature | Render | Vercel | Railway | PythonAnywhere |
|---------|--------|--------|---------|----------------|
| **Free Tier** | ✅ Yes | ✅ Yes | $5 credit | ✅ Yes |
| **Sleep Mode** | ⚠️ 15 min | ❌ No | ❌ No | ❌ No |
| **Database** | ✅ PostgreSQL | ❌ External | ✅ Built-in | ✅ SQLite |
| **Custom Domain** | ✅ Free | ✅ Free | ✅ Free | 💰 $5/month |
| **SSL Certificate** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **Build Time** | 3-5 min | 1-2 min | 2-3 min | Manual |
| **Best For** | Full-stack | Serverless | Full-stack | Python apps |

---

## 🎉 Success!

Your app is now live on Render! 🚀

**Your Live URL:** `https://digital-police-tg.onrender.com`

### Next Steps:
1. ✅ Test all features on live site
2. ✅ Set up UptimeRobot to prevent sleep
3. ✅ Add custom domain (optional)
4. ✅ Set up PostgreSQL database (optional)
5. ✅ Monitor logs and metrics
6. ✅ Share your app with users!

---

## 📞 Need Help?

- **Render Support:** https://render.com/support
- **Community:** https://community.render.com
- **Your GitHub Issues:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG/issues

---

**Built with ❤️ for Telangana Student Police Department**