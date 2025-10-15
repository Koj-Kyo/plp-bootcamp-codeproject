"""Script to check data integrity"""
from extensions import db
from models.appointment import Appointment
from models.doctor import Doctor
from app import create_app

app = create_app()

with app.app_context():
    # Check appointments
    appointments = Appointment.query.all()
    print(f'Total appointments: {len(appointments)}')

    # Check for NULL doctors
    problematic_appointments = []
    for a in appointments:
        if a.doctor is None:
            problematic_appointments.append(a)
            print(f'Appointment ID {a.id} has NULL doctor (doctor_id: {a.doctor_id})')

    print(f'\nTotal appointments with NULL doctor: {len(problematic_appointments)}')

    # Check doctors without health_center
    doctors = Doctor.query.all()
    print(f'\nTotal doctors: {len(doctors)}')

    problematic_doctors = []
    for d in doctors:
        if d.health_center is None:
            problematic_doctors.append(d)
            print(f'Doctor ID {d.id} ({d.first_name} {d.last_name}) has NULL health_center (health_center_id: {d.health_center_id})')

    print(f'\nTotal doctors with NULL health_center: {len(problematic_doctors)}')
