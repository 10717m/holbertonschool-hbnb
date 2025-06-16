import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
