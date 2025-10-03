# ⚡ Quick Deploy Reference Card

**GitHub:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG

---

## 🚀 One-Click Deploy

### Vercel (Fastest - 2 min)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
- ⚡ 2 minutes
- ❌ No sleep
- 🆓 Free forever

### Render (With Database - 5 min)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
- ⏱️ 5 minutes
- ✅ PostgreSQL
- 🆓 Free tier

### Railway (Production - 3 min)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
- ⚡ 3 minutes
- ❌ No sleep
- 💰 $5 credit

---

## 📖 Documentation Quick Links

| Guide | Purpose | Time |
|-------|---------|------|
| [SETUP_SUMMARY.md](SETUP_SUMMARY.md) | What's been set up | 5 min read |
| [DEPLOYMENT_COMPLETE.md](DEPLOYMENT_COMPLETE.md) | Complete setup guide | 10 min read |
| [QUICK_START.md](QUICK_START.md) | Quick deployment | 5 min deploy |
| [DEPLOY_VERCEL.md](DEPLOY_VERCEL.md) | Vercel guide | 2 min deploy |
| [DEPLOY_RENDER.md](DEPLOY_RENDER.md) | Render guide | 5 min deploy |
| [DEPLOY_PYTHONANYWHERE.md](DEPLOY_PYTHONANYWHERE.md) | PythonAnywhere | 10 min deploy |
| [DEPLOYMENT_OPTIONS.md](DEPLOYMENT_OPTIONS.md) | All platforms | Reference |
| [FREE_LIFETIME_HOSTING.md](FREE_LIFETIME_HOSTING.md) | Free hosting | Reference |

---

## 🎯 Choose Your Platform

### Need it FAST? → Vercel
- Click: [![Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
- Time: 2 minutes
- Guide: [DEPLOY_VERCEL.md](DEPLOY_VERCEL.md)

### Need DATABASE? → Render
- Click: [![Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
- Time: 5 minutes
- Guide: [DEPLOY_RENDER.md](DEPLOY_RENDER.md)

### Need FREE FOREVER? → PythonAnywhere
- Sign up: [pythonanywhere.com](https://www.pythonanywhere.com)
- Time: 10 minutes
- Guide: [DEPLOY_PYTHONANYWHERE.md](DEPLOY_PYTHONANYWHERE.md)

---

## 🔑 Demo Credentials

**Citizen Login:**
- Aadhaar: `111111111111`
- Password: `citizen123`

**Police Login:**
- Aadhaar: `123456789012`
- Password: `police123`

---

## ⚙️ Environment Variables

```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

**Generate SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

---

## 📊 Platform Comparison

| Platform | Time | Cost | Sleep | Database |
|----------|------|------|-------|----------|
| Vercel | 2 min | Free | No | External |
| Render | 5 min | Free | 15 min | PostgreSQL |
| Railway | 3 min | $5 | No | Built-in |
| PythonAnywhere | 10 min | Free | No | SQLite |

---

## 🐛 Quick Troubleshooting

### Build Failed?
Check `requirements.txt`:
```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
gunicorn==21.2.0
```

### App Won't Start?
Check PORT in `app.py`:
```python
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Database Issues?
- Vercel: Use /tmp or external DB
- Render: Use PostgreSQL
- PythonAnywhere: SQLite works

---

## 📞 Support

- **GitHub:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG
- **Issues:** https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG/issues
- **Vercel:** https://vercel.com/support
- **Render:** https://render.com/support

---

**🚀 Click a button above and deploy now!**