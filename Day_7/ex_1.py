import random
n = 3
m = 4
matrix = [[random.randint(1, 12) for i in range(m)] for j in range(n)]
for line in matrix:
    for element in line:
        print("%4d" % element, end=' ')
    print()
a = int(input("введите правую границу диапазона "))
b = int(input("введите левую границу диапазона "))

