import numpy as np
import cv2
from tensorflow.keras.models import load_model


class Recognizer:
    def __init__(self):
        self.model = load_model('CardsRecognizer.h5')
        self.label_to_index = {'10': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'A': 9, 'D': 10,
                               'j': 11, 'K': 12}
        self.image = None
        self.input = None

    def preprocess_image(self):
        data = cv2.resize(self.input, (28, 28))

        data = data.astype('float32') / 255.0

        data = data.reshape(1, 28, 28, 1)

        self.image = data

    def _run_path(self, path):
        data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if data is None:
            raise ValueError(f"Can't load image: {path}")
        self.input = data
        self.preprocess_image()
        predicted_class = np.argmax(self.model.predict(self.image), axis=1)[0]

        output = {v: k for k, v in self.label_to_index.items()}[predicted_class]
        return output

    def run(self, im):
        self.input = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        self.preprocess_image()
        predicted_class = np.argmax(self.model.predict(self.image), axis=1)[0]

        output = {v: k for k, v in self.label_to_index.items()}[predicted_class]
        return output


if __name__ == "__main__":
    R = Recognizer()
    image_path = r"C:\Users\batsi\PycharmProjects\Poker_Guy\Cards_bl\4\4.jpg"
    print(R._run_path(r"D:\Dataset\Cards\F\e779adc5-f2ed-4e49-9de6-ba0ba37c4186_gray_copy_1.png"))
