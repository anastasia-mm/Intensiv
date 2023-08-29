n = int(input())
s_1 = []
s_2 = []
for i in range(n):
    n = int(input())
    s_1.append(n)
    s_2.append(n)
print(s_1)
x = 1
if len(s_1) % 2 == 0:
    while len(s_1) != len(s_2)/2:
        del s_1[-1*x]
        x = x + 1
else:
    y = 2
    while len(s_1) != (len(s_2)-1)/2 + 1:
        del s_1[-1*y]
        y = y + 1
print(s_1)





