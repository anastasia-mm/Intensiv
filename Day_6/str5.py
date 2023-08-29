n = input()
n = n.split(' ')
n = sorted(n, key=len)
print(len(n[0]))