"""
Health Center Model
"""
from extensions import db
from datetime import datetime


class HealthCenter(db.Model):
    """Health Center model for medical facilities"""

    __tablename__ = 'health_centers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(100), nullable=False, index=True)
    state = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    latitude = db.Column(db.Numeric(10, 8))
    longitude = db.Column(db.Numeric(11, 8))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with doctors
    doctors = db.relationship('Doctor', backref='health_center', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def full_address(self):
        """Return the complete address"""
        return f"{self.address}, {self.city}, {self.state} {self.postal_code}"

    def to_dict(self):
        """Convert health center object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'full_address': self.full_address,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<HealthCenter {self.name}>'
