# TeleHealth Connect - Quick Start Guide

## ✅ Problem Fixed!

The SQLAlchemy circular import error has been resolved. Your application is now running successfully!

## 🚀 How to Start the Application

```bash
# Navigate to project directory
cd d:\PLP\bootcampProject\telehealth_connect

# Activate virtual environment (if not already activated)
venv\Scripts\activate

# Run the application
python app.py
```

## 🌐 Access the Application

Open your browser and visit:
- **Local:** http://127.0.0.1:5000
- **Network:** http://192.168.0.101:5000

## 📝 What Was Fixed

1. Created `extensions.py` to hold Flask extensions (db, login_manager)
2. Updated all imports from `from app import db` to `from extensions import db`
3. This fixed the circular import issue with Flask's application factory pattern

## 🎯 Next Steps

1. **Register a new patient account** at http://localhost:5000/auth/register
2. **Login** to access the dashboard
3. **Browse doctors** and book appointments
4. **Test all features**:
   - Patient registration ✅
   - Login/Logout ✅
   - Doctor search ✅
   - Appointment booking ✅
   - View appointments ✅

## 📁 Files Modified

- ✅ `extensions.py` (NEW - centralized extensions)
- ✅ `app.py` (updated imports)
- ✅ `models/*.py` (updated all model imports)
- ✅ `routes/*.py` (updated all route imports)

## 🔧 If You Need to Stop the Server

Press `CTRL+C` in the terminal

## 📚 Additional Resources

- Full documentation: See `README.md`
- Database schema: See `schema.sql`
- Fix details: See `FIX_SUMMARY.md`

---

**Your TeleHealth Connect app is ready to use! 🎉**
