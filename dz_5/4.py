s = []
n = chr(ord('a')-1)
for i in range (1, 27):
    s.append(chr(ord(n)+i)*i)
print(s)
