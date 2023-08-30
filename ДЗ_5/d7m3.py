import random
n = int(input())
matrix = [[random.randint(1, 9) for i in range(n)] for j in range(n)]
for line in matrix:
    for column in line:
        print("%4d" % column, end=' ')
    print()
print()
x = 0
for i in range(n):
    s = matrix[x]
    s[-1] = s[-2] + s[-3]
    x = x + 1
for line in matrix:
    for column in line:
        print("%4d" % column, end=' ')
    print()
print()
