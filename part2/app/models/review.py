# app/models/review.py

from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text="", user_id=None, place_id=None, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.user_id = user_id
        self.place_id = place_id

