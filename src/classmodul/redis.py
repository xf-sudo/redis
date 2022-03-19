
class Redis:

    def __init__(self):
        self.data = dict()

    def set(self, key, value):
        self.data[key] = value

