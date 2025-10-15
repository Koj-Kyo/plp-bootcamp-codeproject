"""
Doctor Model
"""
from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Doctor(db.Model):
    """Doctor model for medical professionals"""

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    health_center_id = db.Column(db.Integer, db.ForeignKey('health_centers.id'), nullable=False, index=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(150), nullable=False, index=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(255))
    qualification = db.Column(db.String(200))
    experience_years = db.Column(db.Integer)
    consultation_fee = db.Column(db.Numeric(10, 2))
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with appointments
    appointments = db.relationship('Appointment', backref='doctor', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def full_name(self):
        """Return the full name of the doctor"""
        return f"Dr. {self.first_name} {self.last_name}"

    def set_password(self, password):
        """Hash and set the password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the password"""
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convert doctor object to dictionary"""
        return {
            'id': self.id,
            'health_center_id': self.health_center_id,
            'health_center_name': self.health_center.name if self.health_center else None,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'specialization': self.specialization,
            'email': self.email,
            'phone': self.phone,
            'qualification': self.qualification,
            'experience_years': self.experience_years,
            'consultation_fee': float(self.consultation_fee) if self.consultation_fee else None,
            'available': self.available,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Doctor {self.full_name} - {self.specialization}>'
