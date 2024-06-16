import time

import pyautogui

from Card import Card
from Cropper import Cropper as Cut
from Suit import Suit as Back
from Recognizer import Recognizer as Reco
import mss
import cv2
import pyautogui as pt
import numpy as np
from sklearn.cluster import KMeans


class Utils:
    def __init__(self):
        print("Prepare for start")
        self.cutter = Cut()
        self.color = Back()
        self.reco = Reco()
        self.screen = None
        self.image = None
        self.right_buttons = [
            (1695, 160, 150, 170),  # high
            (1695, 510, 150, 170),
            (1695, 860, 150, 170)
        ]
        print("System ready")

    def take_cards(self):
        data = self.cutter.run()
        table_cards = data[0]
        hand_cards = data[1]
        table = []
        hand = []
        for card in table_cards:
            card_data = Card(self.reco.run(card), self.color.run(card))
            table.append(card_data)

        for card in hand_cards:
            card_data = Card(self.reco.run(card), self.color.run(card))
            hand.append(card_data)
        [print(x) for x in hand]
        [print(x) for x in table]

    def take_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        self.screen = img

    @staticmethod
    def get_colors(i_imp):
        image = cv2.cvtColor(i_imp, cv2.COLOR_BGR2RGB)
        img = image.reshape((image.shape[0] * image.shape[1], 3))
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(img)
        return list(kmeans.cluster_centers_.astype(int))

    def check_buttons_right(self):
        self.take_screen()
        self.crop_right()
        colors = self.get_colors(self.image)
        for i in colors:
            if i[0] > 235 and i[1] > 235 and i[2] > 235:
                continue
            elif i[0] < 200 and i[1] + i[2] > 100:
                return True

    def crop_right(self):
        region = self.right_buttons[0]
        x, y, w, h = region
        self.image = self.screen[y:y + h, x:x + w]
    @staticmethod
    def click_check():
        pyautogui.click(1800, 230)

    @staticmethod
    def click_call():
        pyautogui.click(1800, 585)

    @staticmethod
    def click_raise_any():
        pyautogui.click(1800, 925)


if __name__ == "__main__":
    U = Utils()
    time.sleep(3)
    U.check_buttons_right()
