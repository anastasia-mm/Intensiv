import random
import math


def problem_1_1():
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(i)
    print(a)
    a.index()


def problem_1_2():
    a = []
    for i in range(30):
        a.append(random.randint(0, 60))
    print(a)
    length = len(a)
    print(len(a))
    print(a[length - 1])
    print(a[::-1])
    if 55 in a or 1717 in a:
        print(f'YES, index {a.index(55)}')
    else:
        print("NO")
    del a[0]
    del a[-1]
    print(a)


def problem_1_3():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    print(a)


def problem_1_4():
    b = []
    num = ord('a')
    for i in range(26):
        b.append(chr(i + num) * (i + 1))
    print(b)


def problem_1_5():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()) ** 3)


def problem_1_6():
    n = int(input())
    a = []
    print(n ** (1 / 2).__round__())
    for i in range(1, round(n ** (1 / 2)) + 1):
        if n % i == 0:
            a.extend([i, n // i])
    a.sort()
    print(a)


def problem_1_7():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n - 1):
        print(a[i] + a[i + 1])


def problem_1_8():
    n = int(input())
    a = []
    for i in range(n):
        a.append(random.randint(0, 60))
    # for i in range(n):
    #     a.append(int(input()))
    print(a)
    print(a[1::2])
    for i in range(math.ceil(n / 2)):
        del a[i]
    print(a)


def problem_1_9():
    str = input()
    a = str.split()
    for i in range(len(a)):
        print(a[i])


def problem_1_10():
    str = input()
    a = str.split()
    print(a[0][0], a[1][0], a[2][0], sep= '. ', end = '. ')


def problem_1_11():
    str = input()
    a = str.split('\\')
    for i in range(len(a)):
        print(a[i])


def problem_1_12():
    n = int(input())
    a = []
    for i in range(n):
        a.append(random.randint(0, 60))
    print(a)
    del a[1]
    a.insert(1, 17)
    print(a)
    a.extend([4, 5, 6])
    print(a)
    del a[0]
    print(a)
    a.extend(a)
    print(a)
    a.insert(3, 25)
    print(a)


def problem_1_13():
    n = int(input())
    a = []
    for i in range(n):
        a.append(random.randint(0, 60))
    print(a)
    # a = list(map(int, input().split()))
    indMax = a.index(max(a))
    indMin = a.index(min(a))
    a[indMin], a[indMax] = a[indMax], a[indMin]
    print(a)


problem_1_13()
