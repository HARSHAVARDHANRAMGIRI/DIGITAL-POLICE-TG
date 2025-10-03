# 🚀 Deploy to Vercel - Step-by-Step Guide

Deploy your **Digital Police TG** application to Vercel for FREE with this comprehensive guide.

---

## 📋 Prerequisites

1. **GitHub Account** - Your code is already on GitHub
2. **Vercel Account** - Sign up at [vercel.com](https://vercel.com) (FREE)
3. **Your Repository** - https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG

---

## 🎯 Method 1: One-Click Deploy (Easiest)

### Step 1: Click the Deploy Button

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)

### Step 2: Connect Your GitHub Account
- Click "Continue with GitHub"
- Authorize Vercel to access your repositories

### Step 3: Configure Project
- **Project Name:** `digital-police-tg` (or your choice)
- **Framework Preset:** Other
- **Root Directory:** `./`
- Click **Deploy**

### Step 4: Wait for Deployment
- Vercel will automatically build and deploy your app
- Takes about 2-3 minutes
- You'll get a live URL like: `https://digital-police-tg.vercel.app`

---

## 🛠️ Method 2: Manual Deploy via Vercel Dashboard

### Step 1: Sign Up/Login to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click **Sign Up** (or Login if you have an account)
3. Choose **Continue with GitHub**

### Step 2: Import Your GitHub Repository
1. Click **Add New** → **Project**
2. Click **Import Git Repository**
3. Find your repository: `HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG`
4. Click **Import**

### Step 3: Configure Build Settings
```
Framework Preset: Other
Build Command: (leave empty)
Output Directory: (leave empty)
Install Command: pip install -r requirements.txt
```

### Step 4: Add Environment Variables (Optional)
Click **Environment Variables** and add:
```
FLASK_ENV = production
SECRET_KEY = your-secret-key-here
```

To generate a secure SECRET_KEY:
```python
import secrets
print(secrets.token_hex(32))
```

### Step 5: Deploy
1. Click **Deploy**
2. Wait 2-3 minutes for build to complete
3. Your app will be live at: `https://your-project-name.vercel.app`

---

## 🔧 Method 3: Deploy via Vercel CLI

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Navigate to Your Project
```bash
cd c:\Users\rhars\Downloads\DIGITAL-POLICE-TG-main\DIGITAL-POLICE-TG-main
```

### Step 4: Deploy
```bash
vercel
```

Follow the prompts:
- **Set up and deploy?** → Yes
- **Which scope?** → Your account
- **Link to existing project?** → No
- **Project name?** → digital-police-tg
- **Directory?** → ./

### Step 5: Deploy to Production
```bash
vercel --prod
```

---

## ⚙️ Configuration Files

Your project already has `vercel.json` configured:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

---

## 🌐 Custom Domain Setup

### Step 1: Go to Project Settings
1. Open your project in Vercel dashboard
2. Click **Settings** → **Domains**

### Step 2: Add Your Domain
1. Enter your domain name (e.g., `digitalpolice.com`)
2. Click **Add**

### Step 3: Configure DNS
Add these records to your domain provider:

**For Root Domain:**
```
Type: A
Name: @
Value: 76.76.21.21
```

**For www Subdomain:**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### Step 4: Verify
- Wait 5-10 minutes for DNS propagation
- Vercel will automatically issue SSL certificate

---

## 🔄 Automatic Deployments

Vercel automatically deploys when you push to GitHub:

### Production Deployments
- Push to `main` branch → Deploys to production URL

### Preview Deployments
- Push to any other branch → Creates preview URL
- Open Pull Request → Creates preview URL

### How to Update Your App
```bash
# Make changes to your code
git add .
git commit -m "Update app"
git push origin main
```

Vercel will automatically detect the push and redeploy!

---

## 📊 Monitoring & Logs

### View Deployment Logs
1. Go to Vercel Dashboard
2. Click on your project
3. Click on a deployment
4. View **Build Logs** and **Function Logs**

### Real-time Analytics
- Go to **Analytics** tab
- View page views, visitors, and performance metrics

---

## 🐛 Troubleshooting

### Issue 1: Build Failed
**Error:** `No Python version specified`

**Solution:** Add `runtime.txt`:
```bash
python-3.12
```

### Issue 2: Module Not Found
**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:** Ensure `requirements.txt` is in root directory:
```bash
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
gunicorn==21.2.0
```

### Issue 3: Database Not Working
**Error:** `sqlite3.OperationalError: unable to open database file`

**Solution:** Vercel's serverless functions are read-only. You need to:
1. Use external database (PostgreSQL, MySQL)
2. Or use Vercel's KV storage
3. Or deploy to a platform with persistent storage (Railway, Render)

**For SQLite on Vercel:**
```python
# In app.py, use /tmp directory for SQLite
import os
basedir = '/tmp' if os.environ.get('VERCEL') else os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "police_system.db")}'
```

⚠️ **Note:** Data in `/tmp` is temporary and will be lost on redeployment.

### Issue 4: Static Files Not Loading
**Error:** CSS/JS files return 404

**Solution:** Ensure static files are in `static/` directory and referenced correctly:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### Issue 5: App Timeout
**Error:** `FUNCTION_INVOCATION_TIMEOUT`

**Solution:** Vercel has 10-second timeout for free tier. Optimize your code:
- Reduce database queries
- Use caching
- Optimize imports

---

## 💡 Vercel Free Tier Limits

| Feature | Free Tier |
|---------|-----------|
| **Bandwidth** | 100 GB/month |
| **Builds** | 6,000 minutes/month |
| **Serverless Functions** | 100 GB-hours |
| **Function Duration** | 10 seconds max |
| **Deployments** | Unlimited |
| **Custom Domains** | Unlimited |
| **SSL Certificates** | Free (automatic) |
| **Team Members** | 1 (just you) |

---

## 🎯 Best Practices

### 1. Use Environment Variables
Never hardcode secrets in your code:
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
```

### 2. Enable Caching
Add caching headers for static files:
```python
@app.after_request
def add_header(response):
    if 'static' in request.path:
        response.cache_control.max_age = 31536000
    return response
```

### 3. Use CDN for Assets
Host large files (images, videos) on external CDN:
- Cloudinary (free tier)
- AWS S3
- Vercel Blob Storage

### 4. Monitor Performance
- Check **Analytics** tab regularly
- Optimize slow endpoints
- Use Vercel Speed Insights

---

## 🔗 Useful Links

- **Vercel Dashboard:** https://vercel.com/dashboard
- **Your Project:** https://vercel.com/HARSHAVARDHANRAMGIRI/digital-police-tg
- **Vercel Docs:** https://vercel.com/docs
- **Python on Vercel:** https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **GitHub Repo:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG

---

## 🆚 Vercel vs Other Platforms

| Feature | Vercel | Railway | Render | PythonAnywhere |
|---------|--------|---------|--------|----------------|
| **Free Tier** | ✅ Yes | $5 credit | ✅ Yes | ✅ Yes |
| **Custom Domain** | ✅ Free | ✅ Free | ✅ Free | 💰 $5/month |
| **SSL Certificate** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **Build Time** | Fast | Medium | Slow | Manual |
| **Database** | ❌ External | ✅ Built-in | ✅ Built-in | ✅ SQLite |
| **Sleep Mode** | ❌ No | ❌ No | ⚠️ Yes | ❌ No |
| **Best For** | Static/Serverless | Full-stack | Full-stack | Python apps |

---

## 🎉 Success!

Your app is now live on Vercel! 🚀

**Your Live URL:** `https://digital-police-tg.vercel.app`

### Next Steps:
1. ✅ Test all features on live site
2. ✅ Add custom domain (optional)
3. ✅ Set up environment variables
4. ✅ Monitor analytics and logs
5. ✅ Share your app with users!

---

## 📞 Need Help?

- **Vercel Support:** https://vercel.com/support
- **Community:** https://github.com/vercel/vercel/discussions
- **Your GitHub Issues:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG/issues

---

**Built with ❤️ for Telangana Student Police Department**