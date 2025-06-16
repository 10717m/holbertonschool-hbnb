class MemoryRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.email in [u.email for u in self.users.values()]:
            raise ValueError("User already exists")
        self.users[user.id] = user

    def get_all_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)

    def delete_user(self, user_id):
        return self.users.pop(user_id, None)
