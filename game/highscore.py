from game.save import Save

class Highscore(Save):
    def __init__(self):
        super().__init__()
        self.min_score = 10000
        self.player_min_score = None
        self.isSave = False

    def add(self, player_name, score: int):

        for i in self.file:
            if self.file[i] < self.min_score:
                self.min_score = self.file[i]
                self.player_min_score = i
        if len(self.file) < 5:
            self.file[player_name] = score
        else:
            if score > self.min_score:
                self.file.pop(self.player_min_score)
                self.file[player_name] = score
    def get(self, key):
        sorted_dict = {}
        sorted_keys = sorted(self.file, key=self.file.get, reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = self.file[w]
        return sorted_dict[key]

    def get_all(self):

        sorted_dict = {}
        sorted_keys = sorted(self.file, key=self.file.get, reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = self.file[w]
        return sorted_dict

    def clear(self):
        self.file.clear()

    def __del__(self):
        self.file.close()

