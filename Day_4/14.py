n = int(input("введите число: "))
print(n)
digital_max = -1
digital_min = 10
while n != 0:
    ost = n % 10
    if ost > digital_max:
        digital_max = ost
        n = n//10
    elif ost < digital_min:
        digital_min = ost
        n = n//10
print("Максимальная цифра - ",digital_max)
print("Минимальная цифра - ",digital_min)