s = [1, 5, 7, 9, 55, 1717]
print(s)
print(f'Длина = {len(s)}')
print(f'Последний элемент: {s[-1]}')
s.reverse()
print(s)

if 55 and 1717 in s:
    print('Yes!')
else:
    print('No!')

del s[0]
del s[-1]
s.reverse()
print(s)


