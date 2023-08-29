import math
def d(a):
    s = []
    for i in range(1, round(math.sqrt(a))+1):
        if a%i == 0:
            if i*i == a:
                s.extend([i])
            else:
                s.extend([i, a//i])
    s.sort()
    return s
n = int(input())
print(d(n))
