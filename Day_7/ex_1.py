import random
n = 3
m = 4
matrix = [[random.randint(1, 12) for i in range(m)] for j in range(n)]
for line in matrix:
    for element in line:
        print("%4d" % element, end=' ')
    print()
count_1 = 0
count_2 = 0
x = int(input("введите правую границу диапазона "))
y = int(input("введите левую границу диапазона "))
for i in range(n):
    for j in range(m):
        if x <= matrix[i][j] <= y:
            count_1 += 1
for line in matrix:
    for element in line:
        if x <= element <=y:
            count_2 += 1
print(count_1, count_2)
