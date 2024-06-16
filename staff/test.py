import os
from CardRecognizer import Recognizer
from Suit import Suit
import time

d = {0: 'H', 1: "C", 2: "S", 3: "P"}
names = list(os.walk(r"/Cards_c"))[0][2]
eye = Recognizer()
back = Suit()
c = 0
n = 0
for i in names:
    n += 1
    f = rf'Cards_c\{i}'
    rank = eye.run(f)
    color = back.run(f)
    if i[0] == '1':
        r = '10'
    else:
        r = i[0]
    if r.upper() == rank.upper() and i[-5] == d.get(color):
        c += 1
    else:
        print(rank)
        print(color)
        print(i)
        print(r)
        print(d.get(color))
print((n / c) * 100)

