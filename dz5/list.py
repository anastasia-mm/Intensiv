'''
n = int(input())
a = [1]
while a[-1] < n:
    a.append(a[-1] + 1)
print('1)', a)

n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
print('3)', a)

a = []
for i in range(1,27):
    a.append(chr(i+96)*i)
print('4)', a)

n = int(input())
a = []
for r in range(n):
    t = int(input())
    a.append(t**3)
print('5)', a)

def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a
n = int(input())
print('6)', f(n))

n = int(input())
a = []
for i in range(n):
    a1 = int(input())
    a.append(a1)
q = [a[i] + a[i + 1] for i in range(len(a) - 1)]
print('7)', q)

n = input()
n = n.split(' ')
for i in range(len(n)):
    print('9)', n[i])

n = input('ФИО: ')
s = n.split(' ')
print('10)', f'{s[0][0]}{s[1][0]}{s[2][0]}')

n = input()
s = n.split('\\')
for i in range(len(s)):
    print(s[i])
'''
n = input()
n = n.split(' ')
a = [int(y) for y in n]
maxa = max(a)
mina = min(a)
x = a.index(maxa)
y = a.index(mina)
a[x], a[y] = a[y], a[x]
print('13)', a)
