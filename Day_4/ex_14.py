n = int(input())
digital_max = -1
digital_min = 10
while n != 0:
    ost = n % 10
    if ost > digital_max:
        digital_max = ost

    n = n // 10