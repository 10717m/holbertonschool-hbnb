# app/models/place.py

from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name="", description="", owner_id=None, amenity_ids=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.owner_id = owner_id  # refers to a User
        self.amenity_ids = amenity_ids or []  # list of Amenity ids
        self.review_ids = []  # list of Review ids

