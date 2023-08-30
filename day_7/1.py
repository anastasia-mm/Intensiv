import random
numb = [n for n in range(20, 50)]
print(numb)
c=0
n = 3
m = 4
matrix = [[random.randint(10, 100) for j in range(m)] for i in range(n)]
sl = ''
for i in range(n):
    for j in range(m):
        if matrix[i][j] in numb:
            c+=1
        sl += str(matrix[i][j]) + '  '
    print(sl)
    sl = ''
print(c)