'''
n = int(input())
a = [1]
while a[-1] < n:
    a.append(a[-1] + 1)
print(a)

n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
print(a)

a = []
for i in range(1,27):
    a.append(chr(i+96)*i)
print(a)

n = int(input())
a = []
for r in range(n):
    t = int(input())
    a.append(t**3)
print(a)

def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a
print(f(625))
'''
