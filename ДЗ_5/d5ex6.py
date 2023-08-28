n = int(input())
s = []
for i in range(1, n+1):
    a = n % i
    if a == 0:
        s.append(i)
print(s)


