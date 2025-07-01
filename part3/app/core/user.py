# app/core/user.py

class User:
    def __init__(self, id, email, password_hash, is_admin=False, ...):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin
        # ...

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
            # لا نرجع كلمة المرور
        }

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

