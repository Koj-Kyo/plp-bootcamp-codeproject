"""
Appointment Routes - Booking, Viewing, Cancellation
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from extensions import db
from models.appointment import Appointment
from models.doctor import Doctor
from datetime import datetime, date, time, timedelta

appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')


@appointments_bp.route('/book/<int:doctor_id>', methods=['GET', 'POST'])
@login_required
def book(doctor_id):
    """Book an appointment with a doctor"""
    doctor = Doctor.query.options(
        joinedload(Doctor.health_center)
    ).get_or_404(doctor_id)

    if not doctor.available:
        flash('This doctor is currently not available for appointments.', 'warning')
        return redirect(url_for('main.doctors'))

    if request.method == 'POST':
        appointment_date_str = request.form.get('appointment_date')
        appointment_time_str = request.form.get('appointment_time')
        reason = request.form.get('reason')

        if not appointment_date_str or not appointment_time_str:
            flash('Please select both date and time for the appointment.', 'danger')
            return render_template('book_appointment.html', doctor=doctor)

        try:
            # Parse date and time
            appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
            appointment_time = datetime.strptime(appointment_time_str, '%H:%M').time()

            # Validation: appointment must be in the future
            appointment_datetime = datetime.combine(appointment_date, appointment_time)
            if appointment_datetime <= datetime.now():
                flash('Appointment must be scheduled for a future date and time.', 'danger')
                return render_template('book_appointment.html', doctor=doctor)

            # Check if the slot is already booked
            existing_appointment = Appointment.query.filter_by(
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).first()

            if existing_appointment:
                flash('This time slot is already booked. Please choose another time.', 'danger')
                return render_template('book_appointment.html', doctor=doctor)

            # Create new appointment
            new_appointment = Appointment(
                patient_id=current_user.id,
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                reason=reason,
                status='scheduled'
            )

            db.session.add(new_appointment)
            db.session.commit()

            flash(f'Appointment booked successfully with {doctor.full_name} on {appointment_date_str} at {appointment_time_str}!', 'success')
            return redirect(url_for('main.dashboard'))

        except ValueError as e:
            flash('Invalid date or time format.', 'danger')
            return render_template('book_appointment.html', doctor=doctor)
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while booking the appointment. Please try again.', 'danger')
            print(f"Appointment booking error: {e}")
            return render_template('book_appointment.html', doctor=doctor)

    # GET request - show booking form
    return render_template('book_appointment.html', doctor=doctor)


@appointments_bp.route('/view/<int:appointment_id>')
@login_required
def view(appointment_id):
    """View appointment details"""
    appointment = Appointment.query.options(
        joinedload(Appointment.doctor).joinedload(Doctor.health_center)
    ).get_or_404(appointment_id)

    # Ensure the appointment belongs to the current user
    if appointment.patient_id != current_user.id:
        flash('You do not have permission to view this appointment.', 'danger')
        return redirect(url_for('main.dashboard'))

    return render_template('view_appointment.html', appointment=appointment)


@appointments_bp.route('/cancel/<int:appointment_id>', methods=['POST'])
@login_required
def cancel(appointment_id):
    """Cancel an appointment"""
    appointment = Appointment.query.get_or_404(appointment_id)

    # Ensure the appointment belongs to the current user
    if appointment.patient_id != current_user.id:
        flash('You do not have permission to cancel this appointment.', 'danger')
        return redirect(url_for('main.dashboard'))

    # Check if appointment is already cancelled
    if appointment.status == 'cancelled':
        flash('This appointment is already cancelled.', 'info')
        return redirect(url_for('main.dashboard'))

    # Check if appointment is in the past
    appointment_datetime = datetime.combine(appointment.appointment_date, appointment.appointment_time)
    if appointment_datetime <= datetime.now():
        flash('Cannot cancel past appointments.', 'warning')
        return redirect(url_for('main.dashboard'))

    try:
        appointment.status = 'cancelled'
        db.session.commit()
        flash('Appointment cancelled successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while cancelling the appointment.', 'danger')
        print(f"Appointment cancellation error: {e}")

    return redirect(url_for('main.dashboard'))


@appointments_bp.route('/my-appointments')
@login_required
def my_appointments():
    """View all appointments for the current patient"""
    appointments = Appointment.query.options(
        joinedload(Appointment.doctor).joinedload(Doctor.health_center)
    ).filter_by(
        patient_id=current_user.id
    ).order_by(Appointment.appointment_date.desc(), Appointment.appointment_time.desc()).all()

    return render_template('my_appointments.html', appointments=appointments)
