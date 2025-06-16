from app.repository.memory_repository import InMemoryRepository

class Facade:
    def __init__(self):
        self.repo = InMemoryRepository()

    def create_user(self, data):
        return self.repo.save("users", data)

    def get_all_users(self):
        return self.repo.get_all("users")
