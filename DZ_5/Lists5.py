n = int(input())

a = [int(input()) for i in range(n)]
k = 1
while k < len(a):
    del a[k]
    k += 1
print(a)