from main import Game


class Player(Game):
    def __init__(self):
        super().__init__()
        self.id = self.n + 1
