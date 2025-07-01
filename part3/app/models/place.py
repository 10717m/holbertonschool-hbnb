from datetime import datetime
from .. import db
import uuid

class Place(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    price_by_night = db.Column(db.Float, nullable=False, default=0.0)

    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    reviews = db.relationship('Review', backref='place', cascade="all, delete-orphan")
    amenities = db.relationship('Amenity', secondary='place_amenity', backref='places')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

