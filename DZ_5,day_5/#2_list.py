import random
a = []
n = random.randint(1,10)
for i in range(n):
    # d = random.randint(1, 10)
    # a.append(d)
    a.append(random.randint(1, 10))
print(a)
# a.reverse()
# print(a)
print(a[::-1])
print(a)
k = 0
for x in a:  # ищем количество четных элементов в списке
    if x % 2 == 0:
        k += 1
if (55 in a) and (1717 in a):
    print('YES')
else:
    print("NO")
