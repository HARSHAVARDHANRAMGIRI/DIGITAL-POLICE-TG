# 🚔 DIGITAL POLICE TG - Online FIR Portal

A modern, full-stack Python web application for citizens to file FIRs online and police officers to manage cases efficiently.

## ✨ Features

### 🏠 **For Citizens**
- **Aadhaar-based Registration** with OTP verification
- **File FIRs Online** from anywhere, anytime
- **Real-time Case Tracking** with status updates and timeline
- **Auto-routing** to nearest police station
- **User Dashboard** showing all filed cases with metrics
- **📍 Location Detection** - Auto-fill incident location using GPS
- **🗺️ Nearby Stations Finder** - Find and navigate to nearest police station
- **🔍 Case Tracking** - Track case status with visual timeline

### 👮 **For Police Officers**
- **Police Command Center** with professional dashboard
- **Case Status Updates** (Pending, In Progress, Completed, etc.)
- **Citizen Management** view all registered users
- **Statistics & Analytics** with visual metrics
- **Priority-based Case Handling** with SLA tracking
- **Investigation Heatmap** showing case distribution
- **Live Dispatch Timeline** for real-time updates
- **Case Escalation Queue** for high-priority cases

### 🔒 **Security Features**
- **JWT Authentication** for secure sessions
- **Aadhaar Verification** with OTP system
- **Role-based Access Control** (Citizen vs Police)
- **Password Hashing** for user security

### 🎨 **Modern UI/UX**
- **Professional Logo** - Custom police badge design
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Modern Animations** - Smooth transitions and hover effects
- **Color-coded Status** - Visual indicators for case status
- **Card-based Layout** - Clean and organized interface
- **Font Awesome Icons** - Professional iconography

## 🚀 Quick Start

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Run the Application**
```bash
python app.py
```

### 3. **Access the Website**
Open your browser and go to: `http://localhost:5000`

## 👥 Demo Accounts

### **Citizen Login:**
- **Aadhaar:** 111111111111
- **Password:** citizen123

### **Police Login:**
- **Aadhaar:** 123456789012  
- **Password:** police123

## 🏗️ Project Structure

```
digital_police_tg/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Homepage
│   ├── register.html     # User registration
│   ├── login.html        # User login
│   ├── verify_otp.html   # OTP verification
│   ├── user_dashboard.html # Citizen dashboard
│   ├── police_dashboard.html # Police dashboard
│   └── file_case.html    # Case filing form
└── README.md             # This file
```

## 🔧 Technology Stack

- **Backend:** Flask (Python)
- **Database:** SQLite (with SQLAlchemy ORM)
- **Frontend:** Bootstrap 5 + Font Awesome
- **Authentication:** Flask-Login + JWT
- **Styling:** Custom CSS with modern gradients

## 📱 Key Pages

### **Home Page (`/`)**
- Hero section with call-to-action buttons
- Feature overview for citizens and police
- How it works step-by-step guide

### **Registration (`/register`)**
- Aadhaar number input (12 digits)
- Personal information collection
- Password creation with validation

### **Login (`/login`)**
- Aadhaar-based authentication
- Demo credentials display
- Link to OTP verification

### **OTP Verification (`/verify_otp`)**
- Two-step verification process
- Send OTP to registered mobile
- Verify OTP for account activation

### **User Dashboard (`/user_dashboard`)**
- Welcome message with user info
- Quick actions (file case, verify OTP)
- List of all filed cases with status

### **Police Dashboard (`/police_dashboard`)**
- Statistics cards (total, pending, in progress, completed)
- Case management table
- Registered citizens list
- Case status update functionality

### **File Case (`/file_case`)**
- Comprehensive case filing form
- Priority level selection
- Location and incident details
- Evidence and witness information

## 🗄️ Database Models

### **User**
- Aadhaar number (unique identifier)
- Name, phone, address
- Password hash
- Police officer flag
- Police station assignment

### **PoliceStation**
- Station name and address
- Pincode and contact details

### **Case**
- Case number (auto-generated)
- Title, description, location
- Priority level and status
- Timestamps and complainant info

### **OTPVerification**
- Aadhaar number
- 6-digit OTP
- Creation and usage tracking

## 🔄 Workflow

1. **Citizen Registration**
   - Enter Aadhaar and personal details
   - System assigns to nearest police station
   - Account created and ready for login

2. **Case Filing**
   - Citizen logs in and files case
   - Case automatically routed to assigned station
   - Police officers can view and manage cases

3. **Case Management**
   - Police update case status
   - Citizens track progress in real-time
   - System maintains audit trail

## 🌐 Deployment

### **🚀 Quick Deploy (1-Click)**

Deploy to your favorite platform instantly:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/HARSHAVARDHANRAMGIRI/DIGITAL-POLICE-TG)

### **🆓 FREE LIFETIME HOSTING**

Deploy for **FREE FOREVER** on PythonAnywhere:
- ✅ **100% Free** - No credit card required
- ✅ **No Sleep Mode** - Always online 24/7
- ✅ **Easy Setup** - Deploy in 10 minutes

**📖 Deployment Guides:**
- [FREE_LIFETIME_HOSTING.md](FREE_LIFETIME_HOSTING.md) - Compare all free platforms
- [DEPLOY_PYTHONANYWHERE.md](DEPLOY_PYTHONANYWHERE.md) - PythonAnywhere (100% free forever)
- [DEPLOY_VERCEL.md](DEPLOY_VERCEL.md) - Vercel (Serverless deployment)
- [DEPLOY_RENDER.md](DEPLOY_RENDER.md) - Render (Full-stack with database)
- [QUICK_START.md](QUICK_START.md) - Quick deployment guide
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Comprehensive guide for all platforms

### **📚 Supported Platforms**

| Platform | Free Tier | Sleep Mode | Database | Best For |
|----------|-----------|------------|----------|----------|
| **PythonAnywhere** | ✅ Forever | ❌ No | ✅ SQLite | Python apps (Recommended) |
| **Vercel** | ✅ Yes | ❌ No | ⚠️ External | Serverless/Static |
| **Render** | ✅ Yes | ⚠️ 15 min | ✅ PostgreSQL | Full-stack apps |
| **Railway** | 💰 $5 credit | ❌ No | ✅ Built-in | Full-stack apps |
| **Heroku** | ⚠️ Limited | ⚠️ 30 min | ✅ PostgreSQL | Popular choice |
| **Google Cloud** | 💰 Credits | ❌ No | ✅ Built-in | Enterprise |
| **AWS** | 💰 Credits | ❌ No | ✅ Built-in | Enterprise |

**🏆 Recommended:** PythonAnywhere for 100% free forever hosting!

### **Local Development**
```bash
python app.py
```

### **Production Deployment**
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### **Docker Deployment**
```bash
# Build image
docker build -t digital-police-tg .

# Run container
docker run -p 5000:5000 digital-police-tg
```

### **Environment Variables**
```bash
export FLASK_ENV=production
export SECRET_KEY=your_secret_key_here
```

## 🔒 Security Considerations

- **Aadhaar Verification:** Currently mocked for demo purposes
- **Password Security:** All passwords are hashed using Werkzeug
- **Session Management:** Flask-Login handles secure sessions
- **Input Validation:** Form validation on both client and server side

## 🚧 Future Enhancements

- **Real Aadhaar API Integration**
- **SMS/Email Notifications**
- **File Upload for Evidence**
- **Mobile App Development**
- **Advanced Analytics Dashboard**
- **Multi-language Support**
- **API Endpoints for Mobile Apps**

## 📞 Support

For technical support or questions [9876543210 ]about the DIGITAL POLICE TG system, please contact the development team.

---

**Built with ❤️ for Telangana Student Police Department**
