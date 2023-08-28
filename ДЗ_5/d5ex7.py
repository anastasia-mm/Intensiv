s = []
n = int(input())
for i in range(n):
    number = int(input())
    s.append(number)
s_1 = []
for i in range(0, n-1):
    summa = s[i] + s[i+1]
    s_1.append(summa)
print(s_1)
