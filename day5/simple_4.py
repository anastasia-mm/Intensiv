a = [1, 9, 3, 9, 9]
for i in range(len(a)):  # вывод списка 1
    print(a[i], end=" ")
print()
print(*a)  # вывод списка 2
for x in a:  # вывод списка 3
    print(x, end=" ")
