import random
n = 4
m = 4
matrix = [[random.randint(10, 100) for j in range(m)]for i in range(n)]
sl = ''
poboch_c = n
poboch_sum = 0
main_c = -1
main_sum = 0
for i in range(n):
    main_c += 1
    poboch_c -= 1
    for j in range(m):
        sl += str(matrix[i][j]) + '  '
        if j == main_c:
            main_sum += matrix[i][j]
        if j == poboch_c:
            poboch_sum += matrix[i][j]
    print(sl)
    sl = ''
print(main_sum)
print(poboch_sum)