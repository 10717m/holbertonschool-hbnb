from ..persistence.memory_repo import MemoryRepository
from .models.user import User

class Facade:
    def __init__(self):
        self.repo = MemoryRepository()

    def create_user(self, first_name, last_name, email):
        user = User(first_name, last_name, email)
        self.repo.add_user(user)
        return user

    def list_users(self):
        return self.repo.get_all_users()

    def get_user(self, user_id):
        return self.repo.get_user(user_id)

    def delete_user(self, user_id):
        return self.repo.delete_user(user_id)
