"""
Doctor Routes - Login, Dashboard, Appointment Management
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy.orm import joinedload
from extensions import db
from models.doctor import Doctor
from models.appointment import Appointment
from models.patient import Patient
from datetime import datetime, date

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctor')

# Current doctor session (simple approach - can be improved with Flask-Login)
current_doctor = None


@doctor_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Doctor login"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not email or not password:
            flash('Veuillez remplir tous les champs.', 'danger')
            return render_template('doctor_login.html')

        # Find doctor by email
        doctor = Doctor.query.filter_by(email=email).first()

        # Check credentials
        if doctor and doctor.check_password(password):
            global current_doctor
            current_doctor = doctor
            flash(f'Bienvenue Dr. {doctor.last_name}!', 'success')
            return redirect(url_for('doctor.dashboard'))
        else:
            flash('Email ou mot de passe incorrect.', 'danger')

    return render_template('doctor_login.html')


@doctor_bp.route('/logout')
def logout():
    """Doctor logout"""
    global current_doctor
    current_doctor = None
    flash('Vous êtes déconnecté.', 'info')
    return redirect(url_for('doctor.login'))


@doctor_bp.route('/dashboard')
def dashboard():
    """Doctor dashboard"""
    if not current_doctor:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('doctor.login'))

    # Get today's appointments
    today = date.today()
    today_appointments = Appointment.query.options(
        joinedload(Appointment.patient)
    ).filter_by(
        doctor_id=current_doctor.id,
        appointment_date=today
    ).order_by(Appointment.appointment_time).all()

    # Get upcoming appointments (excluding today)
    upcoming_appointments = Appointment.query.options(
        joinedload(Appointment.patient)
    ).filter(
        Appointment.doctor_id == current_doctor.id,
        Appointment.appointment_date > today,
        Appointment.status == 'scheduled'
    ).order_by(Appointment.appointment_date, Appointment.appointment_time).limit(10).all()

    # Get statistics
    total_appointments = Appointment.query.filter_by(doctor_id=current_doctor.id).count()
    completed_appointments = Appointment.query.filter_by(
        doctor_id=current_doctor.id,
        status='completed'
    ).count()
    pending_appointments = Appointment.query.filter_by(
        doctor_id=current_doctor.id,
        status='scheduled'
    ).count()
    cancelled_appointments = Appointment.query.filter_by(
        doctor_id=current_doctor.id,
        status='cancelled'
    ).count()

    return render_template('doctor_dashboard.html',
                           doctor=current_doctor,
                           today_appointments=today_appointments,
                           upcoming_appointments=upcoming_appointments,
                           total_appointments=total_appointments,
                           completed_appointments=completed_appointments,
                           pending_appointments=pending_appointments,
                           cancelled_appointments=cancelled_appointments,
                           today=today)


@doctor_bp.route('/appointments')
def appointments():
    """View all appointments"""
    if not current_doctor:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('doctor.login'))

    # Filter parameters
    status_filter = request.args.get('status', 'all')
    date_filter = request.args.get('date', 'all')

    query = Appointment.query.options(
        joinedload(Appointment.patient)
    ).filter_by(doctor_id=current_doctor.id)

    # Apply status filter
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)

    # Apply date filter
    if date_filter == 'today':
        query = query.filter_by(appointment_date=date.today())
    elif date_filter == 'upcoming':
        query = query.filter(Appointment.appointment_date >= date.today())
    elif date_filter == 'past':
        query = query.filter(Appointment.appointment_date < date.today())

    appointments_list = query.order_by(
        Appointment.appointment_date.desc(),
        Appointment.appointment_time.desc()
    ).all()

    return render_template('doctor_appointments.html',
                           doctor=current_doctor,
                           appointments=appointments_list,
                           status_filter=status_filter,
                           date_filter=date_filter)


@doctor_bp.route('/appointment/<int:appointment_id>')
def appointment_detail(appointment_id):
    """View appointment details"""
    if not current_doctor:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('doctor.login'))

    appointment = Appointment.query.options(
        joinedload(Appointment.patient)
    ).get_or_404(appointment_id)

    # Check if this appointment belongs to the current doctor
    if appointment.doctor_id != current_doctor.id:
        flash('Accès non autorisé.', 'danger')
        return redirect(url_for('doctor.dashboard'))

    return render_template('doctor_appointment_detail.html',
                           doctor=current_doctor,
                           appointment=appointment)


@doctor_bp.route('/appointment/<int:appointment_id>/update-status', methods=['POST'])
def update_appointment_status(appointment_id):
    """Update appointment status"""
    if not current_doctor:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('doctor.login'))

    appointment = Appointment.query.options(
        joinedload(Appointment.patient)
    ).get_or_404(appointment_id)

    # Check if this appointment belongs to the current doctor
    if appointment.doctor_id != current_doctor.id:
        flash('Accès non autorisé.', 'danger')
        return redirect(url_for('doctor.dashboard'))

    new_status = request.form.get('status')
    notes = request.form.get('notes', '').strip()

    if new_status not in ['scheduled', 'completed', 'cancelled', 'no-show']:
        flash('Statut invalide.', 'danger')
        return redirect(url_for('doctor.appointment_detail', appointment_id=appointment_id))

    try:
        appointment.status = new_status
        if notes:
            appointment.notes = notes
        appointment.updated_at = datetime.utcnow()
        db.session.commit()

        status_messages = {
            'completed': 'Rendez-vous marqué comme complété.',
            'cancelled': 'Rendez-vous annulé.',
            'scheduled': 'Rendez-vous confirmé.',
            'no-show': 'Rendez-vous marqué comme non présenté.'
        }
        flash(status_messages.get(new_status, 'Statut mis à jour.'), 'success')

    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la mise à jour: {str(e)}', 'danger')

    return redirect(url_for('doctor.appointment_detail', appointment_id=appointment_id))


@doctor_bp.route('/patient/<int:patient_id>')
def patient_detail(patient_id):
    """View patient details and history"""
    if not current_doctor:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('doctor.login'))

    patient = Patient.query.get_or_404(patient_id)

    # Get patient's appointments with this doctor
    appointments_history = Appointment.query.filter_by(
        patient_id=patient_id,
        doctor_id=current_doctor.id
    ).order_by(Appointment.appointment_date.desc()).all()

    return render_template('doctor_patient_detail.html',
                           doctor=current_doctor,
                           patient=patient,
                           appointments_history=appointments_history)
