"""
Main Routes - Home, Dashboard, Doctor Search
"""
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from models.doctor import Doctor
from models.health_center import HealthCenter
from models.appointment import Appointment
from sqlalchemy import or_

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Home page"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Patient dashboard"""
    # Get patient's upcoming appointments with joined relations
    from datetime import date
    upcoming_appointments = Appointment.query.options(
        joinedload(Appointment.doctor).joinedload(Doctor.health_center)
    ).filter(
        Appointment.patient_id == current_user.id,
        Appointment.appointment_date >= date.today(),
        Appointment.status == 'scheduled'
    ).order_by(Appointment.appointment_date, Appointment.appointment_time).all()

    # Get recent appointments with joined relations
    past_appointments = Appointment.query.options(
        joinedload(Appointment.doctor).joinedload(Doctor.health_center)
    ).filter(
        Appointment.patient_id == current_user.id,
        Appointment.appointment_date < date.today()
    ).order_by(Appointment.appointment_date.desc(), Appointment.appointment_time.desc()).limit(5).all()

    return render_template('dashboard.html',
                          upcoming_appointments=upcoming_appointments,
                          past_appointments=past_appointments)


@main_bp.route('/doctors')
@login_required
def doctors():
    """List all doctors with search and filter"""
    # Get query parameters
    search = request.args.get('search', '')
    specialization = request.args.get('specialization', '')
    city = request.args.get('city', '')

    # Base query with eager loading
    query = Doctor.query.options(joinedload(Doctor.health_center)).filter_by(available=True)

    # Apply filters
    if search:
        query = query.join(HealthCenter).filter(
            or_(
                Doctor.first_name.ilike(f'%{search}%'),
                Doctor.last_name.ilike(f'%{search}%'),
                Doctor.specialization.ilike(f'%{search}%'),
                HealthCenter.name.ilike(f'%{search}%')
            )
        )

    if specialization:
        query = query.filter(Doctor.specialization.ilike(f'%{specialization}%'))

    if city:
        query = query.join(HealthCenter).filter(HealthCenter.city.ilike(f'%{city}%'))

    doctors_list = query.all()

    # Get unique specializations and cities for filters
    specializations = db.session.query(Doctor.specialization).distinct().all()
    specializations = sorted([s[0] for s in specializations])

    cities = db.session.query(HealthCenter.city).distinct().all()
    cities = sorted([c[0] for c in cities])

    return render_template('doctors.html',
                          doctors=doctors_list,
                          specializations=specializations,
                          cities=cities,
                          current_search=search,
                          current_specialization=specialization,
                          current_city=city)


@main_bp.route('/health-centers')
@login_required
def health_centers():
    """List all health centers"""
    search = request.args.get('search', '')
    city = request.args.get('city', '')

    query = HealthCenter.query

    if search:
        query = query.filter(
            or_(
                HealthCenter.name.ilike(f'%{search}%'),
                HealthCenter.address.ilike(f'%{search}%')
            )
        )

    if city:
        query = query.filter(HealthCenter.city.ilike(f'%{city}%'))

    centers = query.all()

    # Get unique cities for filter
    cities = db.session.query(HealthCenter.city).distinct().all()
    cities = sorted([c[0] for c in cities])

    return render_template('health_centers.html',
                          centers=centers,
                          cities=cities,
                          current_search=search,
                          current_city=city)


from flask import redirect, url_for
from extensions import db
