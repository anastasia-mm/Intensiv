import random
s = []
for i in range(random.randint(1, 10)):
    s.append(random.randint(1, 2000))
print(len(s), s[-1])
print(s [-1::-1])
if 55 in s and 1717 in s:
    print("YES")
s.pop(0)
s.pop(-1)
print(s)
