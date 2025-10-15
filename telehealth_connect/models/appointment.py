"""
Appointment Model
"""
from extensions import db
from datetime import datetime


class Appointment(db.Model):
    """Appointment model for patient-doctor consultations"""

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False, index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False, index=True)
    appointment_date = db.Column(db.Date, nullable=False, index=True)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.Enum('scheduled', 'completed', 'cancelled', 'no-show'), default='scheduled')
    reason = db.Column(db.String(500))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Unique constraint for doctor availability
    __table_args__ = (
        db.UniqueConstraint('doctor_id', 'appointment_date', 'appointment_time', name='unique_appointment'),
    )

    @property
    def datetime_str(self):
        """Return formatted datetime string"""
        return f"{self.appointment_date.strftime('%B %d, %Y')} at {self.appointment_time.strftime('%I:%M %p')}"

    def to_dict(self):
        """Convert appointment object to dictionary"""
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'patient_name': self.patient.full_name if self.patient else None,
            'doctor_id': self.doctor_id,
            'doctor_name': self.doctor.full_name if self.doctor else None,
            'doctor_specialization': self.doctor.specialization if self.doctor else None,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None,
            'appointment_time': self.appointment_time.isoformat() if self.appointment_time else None,
            'datetime_str': self.datetime_str,
            'status': self.status,
            'reason': self.reason,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Appointment {self.id} - Patient: {self.patient_id}, Doctor: {self.doctor_id}>'
