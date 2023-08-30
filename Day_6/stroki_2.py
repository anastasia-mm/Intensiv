p = ['txt', 'pdf', 'doc', 'exe']
filename = input()
print('YES' if filename.split('.')[1] in p else 'NO')