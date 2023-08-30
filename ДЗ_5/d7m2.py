import random
n = int(input())
a = int(input())
b = int(input())
matrix = [[random.randint(a, b) for i in range(n)] for j in range(n)]
for line in matrix:
    for column in line:
        print("%4d" % column, end=' ')
    print()
print()

main = 0
x = 0
for i in range(n):
    s = matrix[x]
    main += s[x]
    x = x + 1
print('Сумма главной диагонали:', main)

b = 0
x = 0
for i in range(n):
    s = matrix[-1]
    b += s[x]
    del matrix[-1]
    x = x + 1
print('Сумма побочной диагонали:', b)



