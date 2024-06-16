class Card:
    def __init__(self, rank, suit):
        self.suit_data = {0: 'red', 1: "green", 2: "blue", 3: "black"}
        self.rank_data = {'10': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'A': 9, 'D': 10,
                          'j': 11, 'K': 12}
        self.rank = rank
        self.suit = suit
        if not suit:
            self.suit = None
            self.rank = None

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_rank_id(self):
        return self.rank_data.get(self.rank)

    def get_suit_id(self):
        return self.suit_data.get(self.suit)

    def __str__(self):
        return f"{self.rank} {self.get_suit_id()}"