class InMemoryRepository:
    def __init__(self):
        self.data = {}

    def save(self, collection, obj):
        if collection not in self.data:
            self.data[collection] = []
        self.data[collection].append(obj)
        return obj

    def get_all(self, collection):
        return self.data.get(collection, [])
