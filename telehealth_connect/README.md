# TeleHealth Connect 🏥

A modern web application built with Flask and MySQL that enables patients to find nearby health centers, search for doctors, and book medical appointments online.

## Features ✨

- **User Authentication**: Secure patient registration and login with password hashing
- **Doctor Search**: Search and filter doctors by specialization, name, or location
- **Health Centers**: Browse nearby medical facilities with complete information
- **Appointment Booking**: Schedule consultations with available doctors
- **Patient Dashboard**: View upcoming and past appointments
- **Responsive Design**: Mobile-friendly interface with modern UI/UX

## Technology Stack 🛠️

- **Backend**: Flask (Python)
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript
- **Password Security**: Werkzeug (bcrypt hashing)

## Project Structure 📁

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

## Usage Guide 📖

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

## API Routes 🛣️

### Authentication Routes
- `GET/POST /auth/register` - Patient registration
- `GET/POST /auth/login` - Patient login
- `GET /auth/logout` - Logout

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

## Security Features 🔒

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

## Future Enhancements 🌟

- Email notifications for appointments
- SMS reminders
- Doctor availability calendar
- Patient medical history
- Prescription management
- Video consultation integration
- Multi-language support
- Advanced search with geolocation

## Contributing 🤝

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License 📄

This project is open source and available for educational purposes.

## Contact & Support 💬

For questions or support, please open an issue in the repository.

---

**Built with ❤️ for better healthcare access**
