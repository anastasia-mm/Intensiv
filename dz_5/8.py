n = int(input())
s = []
for i in range (n):
    s.append(int(input()))
for i in range(1, n):
    if i>=len(s):
        break
    del s[i]
print(s)
             
