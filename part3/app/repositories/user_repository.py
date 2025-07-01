from app.models.user import User
from app import db

class UserRepository:
    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def create(self, data):
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update(self, user_id, data):
        user = self.get_by_id(user_id)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

