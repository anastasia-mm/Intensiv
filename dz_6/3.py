s = input().split()
s1 = ""
for i in range(len(s)):
    s1 += max(s, key=len) + " "
    s.remove(max(s, key=len))
print(s1 [:-2])
