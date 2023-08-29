import random
a = []
n = random.randint(1, 10)
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
print(len(a))
print(a[-1])
t = a[-1::-1]
print(t)
if (55 in a) and (1717 in a):
    print("yes")
else: print("no")
a.pop(0)
a.pop(-1)
print(a)
