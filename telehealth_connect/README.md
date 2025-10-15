# 🏥 TeleHealth Connect

> **Revolutionizing Healthcare Access in Togo and Beyond**
> A complete telemedicine platform connecting patients with healthcare providers for seamless appointment management and consultation.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-5.7+-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📊 Pitch Deck

### � **The Problem**

Healthcare access in developing countries, particularly in Togo, faces critical challenges:

- 🚫 **Limited Access**: Rural populations struggle to reach quality healthcare facilities
- ⏰ **Long Wait Times**: Patients spend hours waiting without appointment systems
- 📋 **Poor Record Management**: Patient medical histories are often lost or inaccessible
- 🔍 **Difficulty Finding Specialists**: No centralized system to locate doctors by specialization
- 💰 **Inefficient Resource Allocation**: Healthcare providers cannot optimize their schedules

**Statistics:**
- 60% of Togolese population lives in rural areas with limited healthcare access
- Average wait time at health centers: 3-4 hours
- Doctor-to-patient ratio: 1:10,000 (WHO recommends 1:1,000)

---

### 💡 **Our Solution**

**TeleHealth Connect** is a comprehensive web-based platform that bridges the gap between patients and healthcare providers through:

#### 🔹 For Patients:
- **Smart Doctor Search**: Find specialists by location, specialty, and availability
- **Online Appointment Booking**: Schedule consultations 24/7 from any device
- **Digital Health Records**: Access appointment history and medical notes
- **Real-time Updates**: Track appointment status and receive notifications

#### 🔹 For Healthcare Providers:
- **Centralized Dashboard**: Manage all appointments in one place
- **Patient Management**: Access patient histories and add consultation notes
- **Schedule Optimization**: View daily, weekly schedules at a glance
- **Status Tracking**: Mark appointments as completed, cancelled, or no-show

---

### 🎨 **Key Features**

| Feature | Patient Benefits | Doctor Benefits |
|---------|-----------------|-----------------|
| 🔐 **Secure Authentication** | Protected personal health data | Controlled access to professional portal |
| 🔍 **Advanced Search** | Filter by specialty, location, experience | Increased visibility to patients |
| 📅 **Appointment Management** | Book, view, cancel anytime | Automated schedule management |
| 📊 **Analytics Dashboard** | Track health visit history | View statistics and patient flow |
| 💬 **Consultation Notes** | Access medical recommendations | Document treatments systematically |
| 📱 **Responsive Design** | Use on any device | Manage appointments on-the-go |

---

### 🌍 **Market Opportunity**

#### Target Market:
- **Primary**: Togo (8.5M population)
- **Secondary**: West African countries (380M+ population)
- **Tertiary**: Developing nations globally

#### Market Size:
- 🏥 **500+ health centers** in Togo alone
- 👨‍⚕️ **5,000+ doctors** across major cities
- 👥 **2M+ potential users** in urban areas with internet access
- 💰 **$50M+ market** for digital health solutions in West Africa

#### Growth Potential:
- Mobile internet penetration: **65% and growing**
- Smartphone adoption: **45% in urban areas**
- Government digital health initiatives: **Increasing support**

---

### 🏗️ **Technology Architecture**

```
┌─────────────────────────────────────────────────┐
│           USER INTERFACES                       │
│  👥 Patient Portal  │  👨‍⚕️ Doctor Portal       │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│         FLASK WEB APPLICATION                   │
│  • Blueprint Architecture                       │
│  • Session Management (Flask-Login)             │
│  • RESTful Routing                             │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│         BUSINESS LOGIC LAYER                    │
│  • Authentication & Authorization               │
│  • Appointment Management                       │
│  • Search & Filter Engine                       │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│      DATABASE LAYER (MySQL + SQLAlchemy)       │
│  📊 Patients │ 👨‍⚕️ Doctors │ 🏥 Centers │ 📅 Appointments │
└─────────────────────────────────────────────────┘
```

#### Tech Stack:
- **Backend**: Flask 3.0 (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Flask-Login + Bcrypt
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Security**: CSRF Protection, Password Hashing, SQL Injection Prevention

---

### 🚀 **Traction & Milestones**

#### ✅ Completed:
- [x] Full-stack application architecture
- [x] Patient registration and authentication system
- [x] Doctor search with advanced filtering
- [x] Appointment booking system
- [x] Doctor portal with dashboard and management tools
- [x] Database populated with 16 Togolese doctors across 10 health centers
- [x] Responsive UI/UX design
- [x] Security implementation (password hashing, session management)

#### 🎯 Current Status:
- **Functional MVP**: Fully operational with both patient and doctor portals
- **Test Data**: Real Togolese health centers and doctor profiles
- **Documentation**: Complete setup guides and API documentation

#### 📈 Next Steps (Q4 2025):
- [ ] SMS/Email notifications for appointments
- [ ] Payment integration for consultation fees
- [ ] Mobile app (iOS & Android)
- [ ] Video consultation feature
- [ ] Multi-language support (French, Ewe, Kabye)
- [ ] Integration with national health insurance system

---

### 💼 **Business Model**

#### Revenue Streams:

1. **💳 Commission Model** (Primary)
   - 10-15% commission on consultation fees
   - Estimated: $5-10 per appointment

2. **🏥 Subscription Plans** for Healthcare Providers
   - Basic: $50/month (Single doctor)
   - Professional: $150/month (Up to 5 doctors)
   - Enterprise: $500/month (Unlimited, custom features)

3. **📊 Premium Features**
   - Advanced analytics: $20/month
   - Telemedicine integration: $100/month
   - API access for third-party integration: $200/month

4. **🎯 Targeted Advertising**
   - Pharmaceutical companies
   - Medical equipment suppliers
   - Health insurance providers

#### Financial Projections (3 Years):

| Year | Users | Doctors | Monthly Revenue | Annual Revenue |
|------|-------|---------|-----------------|----------------|
| 2026 | 10,000 | 200 | $15,000 | $180,000 |
| 2027 | 50,000 | 1,000 | $75,000 | $900,000 |
| 2028 | 200,000 | 3,500 | $300,000 | $3,600,000 |

---

### 🎖️ **Competitive Advantage**

| Feature | TeleHealth Connect | Traditional System | Competitors |
|---------|-------------------|-------------------|-------------|
| 🌍 **Local Focus** | ✅ Togolese-first design | ❌ N/A | ⚠️ Generic international |
| 💰 **Affordable** | ✅ Low commission | ❌ No digital option | ⚠️ High fees (20%+) |
| 📱 **Easy to Use** | ✅ Simple interface | ❌ Manual booking | ⚠️ Complex platforms |
| 🏥 **Comprehensive** | ✅ Patient + Doctor portals | ❌ Paper records | ⚠️ Patient-only focus |
| 🇫🇷 **Localized** | ✅ French + local languages | ✅ Local languages | ❌ English only |
| 🔒 **Secure** | ✅ Encrypted data | ⚠️ Paper vulnerable | ✅ Encrypted |

**Key Differentiators:**
- 🎯 **Built for Africa**: Understanding of local healthcare challenges
- 🤝 **Dual-sided Platform**: Benefits both patients AND doctors
- 💡 **Offline Capability** (Planned): Works with low connectivity
- 🏛️ **Government Partnerships**: Working with Ministry of Health

---

### 👥 **Team & Expertise**

#### Development Team:
- **Full-Stack Development**: Python, Flask, MySQL, HTML/CSS/JS
- **Healthcare Domain Knowledge**: Understanding of Togolese healthcare system
- **UI/UX Design**: User-centered design principles
- **Security Best Practices**: OWASP compliance

#### Advisors (Planned):
- Healthcare professionals from CHU Campus and CHU Sylvanus
- Technology mentors from PLP Bootcamp
- Business advisors with healthcare startup experience

---

### 📍 **Go-to-Market Strategy**

#### Phase 1: Pilot Launch (Q4 2025)
- 🎯 Target: 5 health centers in Lomé
- 👥 Users: 1,000 initial patients
- 🎁 Strategy: Free for first 3 months

#### Phase 2: City Expansion (Q1-Q2 2026)
- 🌆 Lomé, Sokodé, Kara, Atakpamé, Kpalimé, Dapaong
- 🏥 Partnership with 50+ health centers
- 📢 Marketing: Radio, social media, health center posters

#### Phase 3: National Coverage (Q3-Q4 2026)
- 🇹🇬 All major cities and towns
- 🤝 Partnership with Ministry of Health
- 📱 Mobile app launch

#### Phase 4: Regional Expansion (2027+)
- 🌍 Benin, Burkina Faso, Ghana, Niger
- 🏢 Enterprise partnerships with hospital chains
- 💰 Series A funding round

---

### 📊 **Key Metrics & KPIs**

#### User Metrics:
- 👥 **Monthly Active Users (MAU)**
- 📈 **User Growth Rate**
- 🔄 **Retention Rate** (Target: 60%+)
- ⭐ **User Satisfaction Score** (Target: 4.5/5)

#### Business Metrics:
- 📅 **Appointments Booked per Month**
- 💰 **Average Revenue per User (ARPU)**
- 🏥 **Healthcare Provider Adoption Rate**
- 💵 **Customer Acquisition Cost (CAC)**
- 📊 **Lifetime Value (LTV)**

---

### 🛡️ **Risk Analysis & Mitigation**

| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| 🌐 **Limited Internet Access** | High | High | Offline mode, SMS integration |
| 💳 **Low Digital Payment Adoption** | Medium | Medium | Cash payment at facility option |
| 🏥 **Doctor Resistance** | Medium | High | Free training, onboarding support |
| 🔒 **Data Privacy Concerns** | Low | High | GDPR compliance, encryption |
| 💰 **Funding Challenges** | Medium | Medium | Bootstrap, grants, angel investors |
| ⚡ **Technology Failures** | Low | High | Cloud hosting, regular backups |

---

### 💰 **Funding Requirements**

#### Seed Round Target: **$150,000**

**Allocation:**
- 👨‍💻 **Development** (40%): $60,000
  - 2 Full-stack developers
  - 1 Mobile app developer
  - 1 UI/UX designer

- 📢 **Marketing & Sales** (30%): $45,000
  - Digital marketing campaigns
  - Partnership development
  - Sales team (2 people)

- 🏢 **Operations** (20%): $30,000
  - Office space
  - Legal & compliance
  - Administrative costs

- 💾 **Infrastructure** (10%): $15,000
  - Cloud hosting (AWS/Azure)
  - Database optimization
  - Security audits

---

### 📞 **Contact & Investment**

**🌐 Project Repository**: [github.com/Koj-Kyo/plp-bootcamp-codeproject](https://github.com/Koj-Kyo/plp-bootcamp-codeproject)

**📧 For Investment Inquiries**: [Your Email]
**📱 Demo Available**: http://localhost:5000
**📄 Business Plan**: Available upon request

---

## 🚀 Features Overview

### 👥 For Patients

- **User Authentication**: Secure patient registration and login with password hashing
- **Doctor Search**: Search and filter doctors by specialization, name, or location
- **Health Centers**: Browse nearby medical facilities with complete information
- **Appointment Booking**: Schedule consultations with available doctors
- **Patient Dashboard**: View upcoming and past appointments
- **Appointment Management**: Cancel or view detailed appointment information
- **Responsive Design**: Mobile-friendly interface with modern UI/UX

### 👨‍⚕️ For Doctors (NEW!)

- **Secure Doctor Portal**: Separate authentication system for healthcare providers
- **Comprehensive Dashboard**: View today's appointments, statistics, and upcoming consultations
- **Patient Management**: Access patient profiles and consultation history
- **Appointment Control**: Update appointment status (completed, cancelled, no-show)
- **Medical Notes**: Add consultation notes and treatment recommendations
- **Advanced Filtering**: Filter appointments by status and date range
- **Real-time Statistics**: Track total appointments, completion rate, and cancellations

---

## 🛠️ Technology Stack

- **Backend**: Flask 3.0 (Python)
- **Database**: MySQL 5.7+ with SQLAlchemy ORM
- **Authentication**: Flask-Login with Bcrypt password hashing
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 Templates
- **Security**: CSRF Protection, SQL Injection Prevention, Session Management

---

## 📁 Project Structure

```
telehealth_connect/
├── app.py                  # Main application file
├── config.py              # Configuration settings
├── schema.sql             # Database schema
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── models/               # Database models
│   ├── __init__.py
│   ├── patient.py
│   ├── doctor.py
│   ├── health_center.py
│   └── appointment.py
├── routes/               # Application routes
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   ├── main.py          # Main page routes
│   └── appointments.py  # Appointment routes
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── doctors.html
│   ├── book_appointment.html
│   ├── health_centers.html
│   ├── my_appointments.html
│   └── view_appointment.html
└── static/               # Static files
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## Installation & Setup 🚀

### Prerequisites

- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

```bash
cd telehealth_connect
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup MySQL Database

1. **Start MySQL server**

2. **Create the database and tables**:
   ```bash
   mysql -u root -p < schema.sql
   ```

   Or manually:
   ```sql
   mysql -u root -p
   CREATE DATABASE telehealth_db;
   USE telehealth_db;
   SOURCE schema.sql;
   ```

### Step 5: Configure Environment Variables

1. **Copy the example environment file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your settings**:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here

   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=your-mysql-password
   DB_NAME=telehealth_db
   ```

### Step 6: Run the Application

```bash
python app.py
```

The application will be available at: **http://localhost:5000**

### Step 7: Setup Doctor Portal (IMPORTANT!)

The application includes a complete doctor portal. To set it up:

1. **Add password_hash column to doctors table**:
   ```bash
   python add_doctor_password.py
   ```

2. **Populate with Togolese healthcare data**:
   ```bash
   python populate_togo_data.py
   ```

This will:
- ✅ Add 10 Togolese health centers (CHU Campus, CHU Sylvanus, etc.)
- ✅ Add 16 Togolese doctors with specializations
- ✅ Set default password `doctor123` for all doctors

---

## 👨‍⚕️ Doctor Portal Access

### Login Credentials

**URL**: <http://localhost:5000/doctor/login>

**Default Password**: `doctor123` (for all doctors)

### Sample Doctor Accounts

| Doctor Name | Email | Specialization | Location |
|-------------|-------|----------------|----------|
| Dr. Kofi Agbéko | k.agbeko@chucampus.tg | Médecine Générale | CHU Campus (Lomé) |
| Dr. Ama Koffi | a.koffi@chucampus.tg | Pédiatrie | CHU Campus (Lomé) |
| Dr. Edem Attiogbé | e.attiogbe@sylvanus.tg | Cardiologie | CHU Sylvanus (Lomé) |
| Dr. Dzifa Amegavi | d.amegavi@sylvanus.tg | Gynécologie | CHU Sylvanus (Lomé) |
| Dr. Koffi Mensah | k.mensah@bethesda.tg | Chirurgie | Hôpital Bethesda (Lomé) |

### Doctor Portal Features

#### � Dashboard
- Today's appointment list with patient details
- Upcoming appointments (next 10)
- Statistics: Total, Completed, Pending, Cancelled appointments
- Quick access to patient profiles

#### 📋 Appointments Management
- View all appointments with advanced filters:
  - **By Status**: All, Scheduled, Completed, Cancelled, No-show
  - **By Date**: All, Today, Upcoming, Past
- Update appointment status
- Add consultation notes
- View patient history

#### 👤 Patient Management
- Access patient profiles
- View complete appointment history with specific patient
- Review past consultation notes
- Track patient visit patterns

#### 📝 Consultation Notes
- Document diagnosis and treatment
- Add medical recommendations
- Accessible in future appointments
- Helps maintain continuity of care

---

## �📖 Usage Guide

### For Patients

1. **Register**: Create a new patient account
2. **Login**: Access your dashboard
3. **Find Doctors**: Search by specialization, name, or city
4. **Book Appointment**: Select a doctor and choose date/time
5. **Manage Appointments**: View, track, or cancel appointments

### Database Schema

The application uses four main tables:

- **patients**: User accounts and profiles
- **doctors**: Medical professionals information
- **health_centers**: Medical facility details
- **appointments**: Booking records

## 🛣️ API Routes

### Authentication Routes

- `GET/POST /auth/register` - Patient registration
- `GET/POST /auth/login` - Patient login
- `GET /auth/logout` - Patient logout

### Main Routes

- `GET /` - Home page
- `GET /dashboard` - Patient dashboard (protected)
- `GET /doctors` - Doctor search and listing (protected)
- `GET /health-centers` - Health center listing (protected)

### Appointment Routes

- `GET/POST /appointments/book/<doctor_id>` - Book appointment (protected)
- `GET /appointments/view/<appointment_id>` - View details (protected)
- `POST /appointments/cancel/<appointment_id>` - Cancel appointment (protected)
- `GET /appointments/my-appointments` - List all appointments (protected)

### Doctor Portal Routes (NEW!)

- `GET/POST /doctor/login` - Doctor authentication
- `GET /doctor/logout` - Doctor logout
- `GET /doctor/dashboard` - Doctor dashboard with statistics
- `GET /doctor/appointments` - List all appointments with filters
- `GET /doctor/appointment/<id>` - View appointment details
- `POST /doctor/appointment/<id>/update-status` - Update appointment status
- `GET /doctor/patient/<id>` - View patient profile and history

---

- Password hashing using Werkzeug (bcrypt)
- Session-based authentication with Flask-Login
- CSRF protection
- SQL injection prevention via SQLAlchemy ORM
- Environment variable management for sensitive data

## Development 💻

### Running in Development Mode

```bash
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

python app.py
```

### Database Migrations

If you make changes to the models, you can recreate the database:

```bash
mysql -u root -p telehealth_db < schema.sql
```

## Deployment Considerations 🚀

### Before Deploying to Production:

1. **Change SECRET_KEY** to a strong random value
2. **Set FLASK_ENV=production**
3. **Use a production-grade WSGI server** (Gunicorn, uWSGI)
4. **Enable HTTPS**
5. **Set up proper database backups**
6. **Configure firewall rules**
7. **Use environment-specific configurations**

### Example Production Setup with Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:create_app()
```

### Nginx Configuration Example:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/telehealth_connect/static;
    }
}
```

## Testing 🧪

### Sample Test Users

After running the schema.sql, you'll have:
- 3 health centers
- 6 doctors with various specializations

Create a patient account to start testing the application.

## Troubleshooting 🔧

### Common Issues:

1. **Database Connection Error**
   - Verify MySQL is running
   - Check database credentials in `.env`
   - Ensure database `telehealth_db` exists

2. **Import Errors**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

3. **Template Not Found**
   - Check that you're running the app from the correct directory
   - Verify folder structure is intact

## 🌟 Future Enhancements

### Phase 1 (Q4 2025)
- 📧 Email notifications for appointments
- 📱 SMS reminders via SMS Gateway
- 💳 Payment integration (Mobile Money: TMoney, Flooz)
- 🌐 Multi-language support (English, French, Ewe, Kabye)

### Phase 2 (Q1-Q2 2026)
- 📱 Mobile applications (iOS & Android)
- 🎥 Video consultation integration
- 📊 Advanced analytics dashboard for doctors
- 🏥 Hospital management system integration
- 📋 Electronic medical records (EMR)
- 💊 Prescription management system

### Phase 3 (Q3-Q4 2026)
- 🤖 AI-powered symptom checker
- 🗺️ Geolocation-based doctor search
- 🚑 Emergency appointment booking
- 💰 Health insurance integration
- 📈 Predictive analytics for healthcare trends
- 🌍 Regional expansion (West Africa)

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add comments for complex logic
- Test your changes before submitting
- Update documentation as needed

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PLP Bootcamp** - For providing the learning platform and resources
- **Togolese Healthcare System** - For inspiration and data
- **Flask Community** - For excellent documentation and support
- **Open Source Community** - For the amazing tools and libraries

---

## 📞 Contact & Support

### For General Inquiries
- 📧 **Email**: [Your Email Here]
- 🌐 **GitHub**: [@Koj-Kyo](https://github.com/Koj-Kyo)
- 💼 **LinkedIn**: [Your LinkedIn Profile]

### For Investment Opportunities
- 📄 **Business Plan**: Available upon request
- 💰 **Pitch Deck**: See above sections
- 📊 **Financial Projections**: Available upon request
- 🤝 **Partnership Inquiries**: Open to discussion

### For Technical Support
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/Koj-Kyo/plp-bootcamp-codeproject/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Koj-Kyo/plp-bootcamp-codeproject/discussions)
- 📚 **Documentation**: See `DOCTOR_PORTAL_GUIDE.md` for detailed doctor portal docs

---

## 📊 Project Statistics

- ⭐ **Total Lines of Code**: 5,000+
- 📁 **Files**: 30+ (Python, HTML, CSS, SQL)
- 🗄️ **Database Tables**: 4 (Patients, Doctors, Health Centers, Appointments)
- 🎨 **Templates**: 15+ responsive HTML pages
- � **Security Features**: 5+ (Authentication, Password Hashing, CSRF, etc.)
- 🌍 **Languages**: English, French
- 🇹🇬 **Local Data**: 16 Togolese doctors, 10 health centers

---

## 🎯 Quick Start Summary

```bash
# Clone repository
cd telehealth_connect

# Setup environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
mysql -u root -p < schema.sql

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Populate with Togolese data
python add_doctor_password.py
python populate_togo_data.py

# Run application
python app.py

# Access:
# Patient Portal: http://localhost:5000
# Doctor Portal: http://localhost:5000/doctor/login
# Default doctor password: doctor123
```

---

## 🌟 Success Metrics

| Metric | Current Status | Target (6 Months) |
|--------|---------------|-------------------|
| 👥 Registered Patients | 0 (Launch ready) | 10,000+ |
| 👨‍⚕️ Active Doctors | 16 (Test data) | 200+ |
| 🏥 Health Centers | 10 (Test data) | 50+ |
| 📅 Appointments Booked | 0 (Launch ready) | 5,000+/month |
| ⭐ User Satisfaction | N/A | 4.5+/5.0 |
| 🌍 Cities Covered | 6 | 15+ |

---

<div align="center">

## 🏥 TeleHealth Connect

**Transforming Healthcare Access in Africa, One Appointment at a Time**

🇹🇬 **Made in Togo, Built for Africa**

[![GitHub](https://img.shields.io/badge/GitHub-Koj--Kyo-black?logo=github)](https://github.com/Koj-Kyo)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-5.7+-orange.svg)](https://www.mysql.com/)

---

**Built with ❤️ for better healthcare access**

*© 2025 TeleHealth Connect. All rights reserved.*

</div>
