import time
import uuid
import cv2
import numpy as np
import mss
import os


class Cropper:
    def __init__(self):
        self.data = None
        self.table = []
        self.hand = []
        self.cards_in_hand = [
            (740, 935, 100, 135),  # hand 1
            (870, 935, 100, 135),  # hand 2
        ]
        self.cards_on_table = [
            (600, 478, 95, 130),
            (705, 478, 95, 130),
            (808, 478, 95, 130),
            (910, 478, 95, 130),
            (1015, 478, 95, 130),
        ]

    def take_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        self.data = img

    def crop_image(self):
        for region in self.cards_in_hand:
            x, y, w, h = region
            self.hand.append(self.data[y:y + h, x:x + w])

        for region in self.cards_on_table:
            x, y, w, h = region
            self.table.append(self.data[y:y + h, x:x + w])

    def show(self):
        for i, img in enumerate(self.hand + self.table):
            cv2.imshow(f'Image {i + 1}', img)
            cv2.waitKey(10000)  # 1 sec
        cv2.destroyAllWindows()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_images(self, folder="hand"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        for img in self.hand:
            unique_filename = str(uuid.uuid4()) + ".png"
            filepath = os.path.join(folder, unique_filename)
            cv2.imwrite(filepath, img)
            print(f"Saved image to {filepath}")

    def save_images_t(self, folder="table"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        for img in self.table:
            unique_filename = str(uuid.uuid4()) + ".png"
            filepath = os.path.join(folder, unique_filename)
            cv2.imwrite(filepath, img)
            print(f"Saved image to {filepath}")

    def run(self):
        self.take_screen()
        self.crop_image()
        self.save_images()
        self.save_images_t()


if __name__ == "__main__":
    time.sleep(3)
    r = Cropper()
    r.run()
