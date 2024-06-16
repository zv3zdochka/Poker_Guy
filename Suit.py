import cv2
from sklearn.cluster import KMeans


class Suit:
    def __init__(self):
        self.image = None
        self.out = None
        self.colors = None

    def get_colors(self):
        img = self.image.reshape((self.image.shape[0] * self.image.shape[1], 3))
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(img)
        self.colors = kmeans.cluster_centers_.astype(int)

    def select_suit(self):
        two_colors = list(self.colors)

        for i in two_colors:
            if i[0] > 235 and i[1] > 235 and i[2] > 235:
                continue
            elif i[0] < 80 and i[1] < 80 and i[2] < 80:
                return 3
            elif i[0] > 150 > i[1] + i[2]:
                return 0
            elif i[0] < 70 and i[1] > 100:
                if i[2] > 200:
                    return 2
                else:
                    return 1

    def run(self, img):
        self.image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.get_colors()
        return self.select_suit()

    def _run_path(self, path):
        self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
        self.get_colors()
        return self.select_suit()


if __name__ == "__main__":
    img = r'C:\Users\batsi\PycharmProjects\Poker_Guy\Cards_c\2_C.jpg'
    image = cv2.imread(img)
    dc = Suit()
    print(dc.run(image))
