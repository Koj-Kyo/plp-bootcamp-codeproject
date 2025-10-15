"""Script to fix orphaned appointments"""
from extensions import db
from models.appointment import Appointment
from models.doctor import Doctor
from app import create_app

app = create_app()

with app.app_context():
    # Find appointments with invalid doctor_id
    appointments = Appointment.query.all()
    doctors = Doctor.query.all()
    doctor_ids = [d.id for d in doctors]

    orphaned_appointments = []
    for appointment in appointments:
        if appointment.doctor_id not in doctor_ids:
            orphaned_appointments.append(appointment)
            print(f'Found orphaned appointment ID {appointment.id} with invalid doctor_id {appointment.doctor_id}')

    if orphaned_appointments:
        print(f'\nFound {len(orphaned_appointments)} orphaned appointment(s)')
        print('\nDeleting orphaned appointments...')

        for appointment in orphaned_appointments:
            db.session.delete(appointment)

        db.session.commit()
        print('✓ Orphaned appointments deleted successfully!')
    else:
        print('No orphaned appointments found.')
