from datetime import datetime
from .. import db
import uuid

class Review(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.String, db.ForeignKey('place.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

