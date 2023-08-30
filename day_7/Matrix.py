import random
n = 3
m = 4
matrix = [[random.randint(10, 100) for j in range(m)]for i in range(n)]
print(matrix)
sl = ''
for i in range(n):
    for j in range(m):
        sl += str(matrix[i][j]) + '  '
    print(sl)
    sl = ''
