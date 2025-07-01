from .. import db

place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String, db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.String, db.ForeignKey('amenity.id'), primary_key=True)
)

