from random import randint
from collections import Counter
def analyz(data):
    c = Counter(data)
    return [f'{k} - {c[k]}' for k in sorted(c)]
def gen():
    data = []
    for i in range(randint(1, 100)):
        data.append(randint(-10, 10))
    return analyz(data)
print(*gen(), sep='\n')