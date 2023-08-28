import math
import random


def problem_2_10():
    print(f'x |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9')
    print(f'')
    for i in range(1, 10):
        print(f'{i} ', end="")
        for j in range(1, 10):
            print(f'|{i * j :^5d}', end="")
        print()


def problem_1_14():
    s = input()
    arr = [x for x in s]
    arr.sort()
    print(f'{arr[0]} | {arr[-1]}')


def problem_1_15():
    digit = input()
    n = input()
    for i in n:
        if i == digit:
            print('wow, a problem')
            exit(5789197573841)
    print('norm')


def problem_1_16():
    count = 0
    digit = int(input())
    n = int(input())
    while n > 0:
        if n % 10 == digit:
            count += 1
        n = n // 10
    print(count)


def problem_1_17():
    digit = int(input())
    n = int(input())
    print(f'{digit}{n}')


def problem_3_1():
    arr = []
    for i in range(0, 100000):
        n = random.randint(0, 10000)
        count = 1
        guess = random.randint(0, 10000)
        while n != guess:
            guess = random.randint(0, 10000)
            count += 1
            # print(f'Попытка {count}, число: {guess}')
        # print(f'{i} --- Попыток {count} --- Загаданное число: {n}')
        arr.append(count)
    print(sum(arr)/len(arr))


problem_3_1()
