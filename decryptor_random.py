import random


class Shifr:
    def roll(self):
        a, b, c = 1, 1, 1
        while a == b or b == c or a == c:
            a = random.randint(1, 4)
            b = random.randint(1, 4)
            c = random.randint(1, 4)
        return a, b, c


shifr = Shifr()
print(shifr.roll())

