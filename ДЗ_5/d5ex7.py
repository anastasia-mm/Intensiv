s = []
n = int(input())
for i in range(n):
    number = int(input())
    s.append(number)
s_1 = []
for i in range(0, n-1):
    summa = s[i] + s[i+1]
    s_1.append(summa)
<<<<<<< HEAD
print(s_1)
=======
print(s_1)
>>>>>>> 292b7163a0185ca1ef5ee9f05a968107791dce19
