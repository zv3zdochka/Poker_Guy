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
            (0, 520, 1920, 390),  # hand 1
            (0, 100, 200, 450),  # hand 2
        ]
        self.cards_on_table = [
            (0, 520, 1920, 390),
            (0, 100, 200, 450),
            (160, 250, 1900, 280)
        ]


    def take_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        self.data = img

    def crop_image(self):
        for region in self.regions:
            x, y, w, h = region
            self.all.append(self.data[y:y + h, x:x + w])

    def show(self):
        for i, img in enumerate(self.all):
            cv2.imshow(f'Image {i + 1}', img)
            cv2.waitKey(10000)  # 1 sec
        cv2.destroyAllWindows()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_images(self, folder="go"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        print(len(self.all))
        for img in self.all:
            unique_filename = str(uuid.uuid4()) + ".png"
            filepath = os.path.join(folder, unique_filename)
            cv2.imwrite(filepath, img)
            print(f"Saved image to {filepath}")


    def run(self):
        self.take_screenshot()
        self.crop_image()
        self.save_images()


if __name__ == "__main__":
    time.sleep(3)
    r = Cropper()
    r.run()
