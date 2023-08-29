import random
s = []
for i in range(10):
    s.append(random.randint(1, 100))
print(s)
s[1] = 17
for i in range(4, 7):
    s.append(i)
del s[0]
s = s*2
s.insert(3, 25)
print(s)

