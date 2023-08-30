import random
n = 3
m = 4
matrix = []
for j in range(n):
    a = []
    for i in range(m):
        a.append(random.randint(1,12))
    matrix.append(a)
print(matrix)

