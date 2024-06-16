import time
import cv2
from Cropper import Cropper as Cut
from Suit import Suit as Back
from Recognizer import Recognizer as Reco
from Card import Card


class Game():
    # n players at the table
    def __init__(self):
        self.n = self.get_players()

    def get_players(self):
        return 1


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
            card_data = Card(reco.run(card), color.run(card))
            table.append(card_data)

        for card in hand_cards:
            card_data = Card(reco.run(card), color.run(card))
            hand.append(card_data)
        [print(x) for x in hand]
        [print(x) for x in table]


p = Player()
p.get_info()
