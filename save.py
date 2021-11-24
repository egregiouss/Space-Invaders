import shelve

class Save:
    def __init__(self):
        self.file = shelve.open("data")

    def add(self, player_name, score: int):
        self.file[player_name] = score

    def get(self, key):
        return self.file[key]
    def get_all(self):
        return self.file

    def __del__(self):
        self.file.close()
