# app/models/user.py

from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name="", last_name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

