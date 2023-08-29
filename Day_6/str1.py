n = input()
rn = ''.join(reversed(n))
if n == rn:
    print('1)', 'Это палиндром')
else:
    print('1)', 'Это не палиндром')