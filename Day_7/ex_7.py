import random
n = 7
sum_main = 0
sum_side = 0
matrix = [[random.randint(1, 12) for i in range(n)] for j in range(n)]
for line in matrix:
    for element in line:
        print("%4d" % element, end=' ')
    print()
for i in range(n):
    sum_main += matrix[i][i]
    sum_side += matrix[i][n-i-1]
print("sum_main:", sum_main, "\nsum_side:", sum_side)

