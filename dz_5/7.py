n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s1 = []
for i in range(n-1):
    s1.append(s[i]+s[i+1])
print(s1)
