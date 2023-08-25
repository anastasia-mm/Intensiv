a = int(input())
p = 1
while a != 0:
    ost = a % 10
    p *= ost #p = p * ost
    a = a // 10
print(p)
