import time
import cv2
from Cropper import Cropper as Cut
from Suit import Suit as Back
from Recognizer import Recognizer as Reco


class Card:
    def __init__(self, rank, suit):
        self.suit_data = {0: 'red', 1: "green", 2: "blue", 3: "black"}
        self.rank_data = {'10': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'A': 9, 'D': 10,
                          'j': 11, 'K': 12}
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_rank_id(self):
        return self.rank_data.get(self.rank)

    def get_suit_id(self):
        return self.suit_data.get(self.suit)


class Player:
    def get_info(self):
        cutter = Cut()
        color = Back()
        reco = Reco()
        print(123123)
        time.sleep(3)
        data = cutter.run()
        table_cards = data[0]
        hand_cards = data[1]
        table = []
        hand = []
        for card in table_cards:
            card_data = (reco.run(card), color.run(card))
            table.append(card_data)

        for card in hand_cards:
            card_data = (reco.run(card), color.run(card))
            hand.append(card_data)
        print(hand)
        print(table)


p = Player()
p.get_info()
