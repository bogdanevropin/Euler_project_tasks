
class Champernowne(object):
    def __init__(self):
        self._constant = '0.'
        self._last = 0

    def __getitem__(self, item):
        item += 1
        while len(self._constant) - 1 < item:
            self._generate()

        return int(self._constant[item])

    def _generate(self):
        self._last += 1
        self._constant += str(self._last)

c = Champernowne()

print(str(c[1] * c[10] * c[100] * c[1000] * c[10000] * c[100000] * c[1000000]))
