# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# from pyngrok import ngrok  # Commented out for Railway deployment
import random
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'digital_police_tg_secret_key_2024')

# Use /tmp directory for SQLite on Vercel (serverless)
if os.environ.get('VERCEL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/police_cases.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///police_cases.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadhaar = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_police = db.Column(db.Boolean, default=False)
    station_id = db.Column(db.Integer, db.ForeignKey('police_station.id'), nullable=True)

class PoliceStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    complainant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('police_station.id'), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    priority = db.Column(db.String(20), default='Medium')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class OTPVerification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadhaar = db.Column(db.String(12), nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_used = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        aadhaar = request.form['aadhaar']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        password = request.form['password']
        
        if User.query.filter_by(aadhaar=aadhaar).first():
            flash('Aadhaar already registered!', 'error')
            return redirect(url_for('register'))
        
        # Find nearest police station by pincode
        station = PoliceStation.query.first()  # For demo, assign to first station
        
        user = User(
            aadhaar=aadhaar,
            name=name,
            phone=phone,
            address=address,
            password_hash=generate_password_hash(password),
            station_id=station.id if station else None
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        aadhaar = request.form['aadhaar']
        password = request.form['password']
        
        user = User.query.filter_by(aadhaar=aadhaar).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if user.is_police:
                return redirect(url_for('police_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid Aadhaar or password!', 'error')
    
    return render_template('login.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        aadhaar = request.form['aadhaar']
        otp = request.form['otp']
        
        otp_record = OTPVerification.query.filter_by(
            aadhaar=aadhaar, 
            otp=otp, 
            is_used=False
        ).first()
        
        if otp_record:
            otp_record.is_used = True
            db.session.commit()
            flash('OTP verified successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid OTP!', 'error')
    
    return render_template('verify_otp.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    aadhaar = request.form['aadhaar']
    otp = str(random.randint(100000, 999999))
    
    # Store OTP in database
    otp_record = OTPVerification(aadhaar=aadhaar, otp=otp)
    db.session.add(otp_record)
    db.session.commit()
    
    # In real app, send SMS/email here
    flash(f'OTP sent to your registered mobile: {otp}', 'success')
    return redirect(url_for('verify_otp'))

@app.route('/file_case', methods=['GET', 'POST'])
@login_required
def file_case():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        priority = request.form['priority']
        
        # Generate case number
        case_number = f"TG{datetime.datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}"
        
        case = Case(
            case_number=case_number,
            title=title,
            description=description,
            location=location,
            priority=priority,
            complainant_id=current_user.id,
            station_id=current_user.station_id
        )
        
        db.session.add(case)
        db.session.commit()
        
        flash(f'Case filed successfully! Case Number: {case_number}', 'success')
        return redirect(url_for('user_dashboard'))
    
    return render_template('file_case.html')

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    if current_user.is_police:
        return redirect(url_for('police_dashboard'))
    
    cases = Case.query.filter_by(complainant_id=current_user.id).order_by(Case.created_at.desc()).all()
    return render_template('user_dashboard.html', cases=cases)

@app.route('/police_dashboard')
@login_required
def police_dashboard():
    if not current_user.is_police:
        return redirect(url_for('user_dashboard'))
    
    cases = Case.query.filter_by(station_id=current_user.station_id).order_by(Case.created_at.desc()).all()
    users = User.query.filter_by(station_id=current_user.station_id, is_police=False).all()
    return render_template('police_dashboard.html', cases=cases, users=users)

@app.route('/update_case_status/<int:case_id>', methods=['POST'])
@login_required
def update_case_status(case_id):
    if not current_user.is_police:
        return redirect(url_for('user_dashboard'))
    
    case = Case.query.get_or_404(case_id)
    new_status = request.form['status']
    case.status = new_status
    case.updated_at = datetime.datetime.utcnow()
    
    db.session.commit()
    flash('Case status updated successfully!', 'success')
    return redirect(url_for('police_dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/nearby_stations')
def nearby_stations():
    stations = PoliceStation.query.all()
    return render_template('nearby_stations.html', stations=stations)

@app.route('/api/stations')
def api_stations():
    stations = PoliceStation.query.all()
    stations_data = [{
        'id': s.id,
        'name': s.name,
        'address': s.address,
        'pincode': s.pincode,
        'phone': s.phone,
        # Sample coordinates for Hyderabad area
        'lat': 17.385044 + (s.id * 0.01),
        'lng': 78.486671 + (s.id * 0.01)
    } for s in stations]
    return jsonify(stations_data)

@app.route('/track_case/<case_number>')
def track_case(case_number):
    case = Case.query.filter_by(case_number=case_number).first()
    if case:
        return render_template('track_case.html', case=case)
    else:
        flash('Case not found!', 'error')
        return redirect(url_for('home'))

# Initialize database and create sample data
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create sample police stations if none exists
        if not PoliceStation.query.first():
            stations_data = [
                {
                    'name': 'Central Police Station',
                    'address': '123 Main Street, Hyderabad, Telangana',
                    'pincode': '500001',
                    'phone': '0401234567'
                },
                {
                    'name': 'Cyberabad Police Station',
                    'address': 'HITEC City, Madhapur, Hyderabad',
                    'pincode': '500081',
                    'phone': '0401234568'
                },
                {
                    'name': 'Secunderabad Police Station',
                    'address': 'Paradise Circle, Secunderabad',
                    'pincode': '500003',
                    'phone': '0401234569'
                },
                {
                    'name': 'Banjara Hills Police Station',
                    'address': 'Road No 12, Banjara Hills, Hyderabad',
                    'pincode': '500034',
                    'phone': '0401234570'
                },
                {
                    'name': 'Jubilee Hills Police Station',
                    'address': 'Road No 36, Jubilee Hills, Hyderabad',
                    'pincode': '500033',
                    'phone': '0401234571'
                }
            ]
            
            for station_data in stations_data:
                station = PoliceStation(**station_data)
                db.session.add(station)
            
            db.session.commit()
            
            # Create sample police user for first station
            first_station = PoliceStation.query.first()
            police_user = User(
                aadhaar='123456789012',
                name='Inspector Rajesh Kumar',
                phone='9876543210',
                address='Police Quarters, Hyderabad',
                password_hash=generate_password_hash('police123'),
                is_police=True,
                station_id=first_station.id
            )
            db.session.add(police_user)
            
            # Create sample citizen user
            citizen_user = User(
                aadhaar='111111111111',
                name='Ramesh Sharma',
                phone='9876543211',
                address='Banjara Hills, Hyderabad',
                password_hash=generate_password_hash('citizen123'),
                is_police=False,
                station_id=first_station.id
            )
            db.session.add(citizen_user)
            db.session.commit()

# Initialize database on first request (for Vercel serverless)
@app.before_request
def initialize_database():
    if not hasattr(app, 'db_initialized'):
        try:
            db.create_all()
            # Check if we need to add sample data
            if not PoliceStation.query.first():
                init_db()
            app.db_initialized = True
        except Exception as e:
            print(f"Database initialization error: {e}")
            pass

if __name__ == '__main__':
    init_db()
    
    # Get port from Railway environment or use default
    port = int(os.environ.get('PORT', 5000))
    
    # Railway provides public URL automatically
    print(f'[RAILWAY] Your website is now accessible worldwide!')
    print(f'[URL] https://web-production-2f708.up.railway.app/')
    print(f'[SHARE] Share this link with anyone!')
    
    app.run(host='0.0.0.0', port=port, debug=False) 
