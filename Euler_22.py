f = open('txt/names.txt', 'r')
d = f.read()

names = d.split(',')
names.sort()

def letter_score(char, _d={}):
    if char in _d:
        return _d[char]
    _d[char] = ord(char) - ord('A') + 1
    return _d[char]

def name_worth(name):
    return sum(letter_score(l) for l in name)

def names_score(name, index):
    return name_worth(name) * (index + 1)

print(sum(names_score(names[i], i) for i in range(0, len(names))))

print(letter_score('A'))
print(letter_score('C'))