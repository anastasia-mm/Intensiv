import random
n = random.randint(3, 6)
matrix = [[random.randint(1, 12) for i in range(n)] for j in range(n)]
S_main = 0
S_side = 0
for i in range(n):
    S_main += matrix[i][i]
    S_side += matrix[i][n-i-1]
for line in matrix:
    for column in line:
        print('%4d' % column, end=' ')
    print()
print("Cумма элементов главой диагонали матрицы:", S_main)
print("Cумма элементов побочной диагонали матрицы:", S_side)
