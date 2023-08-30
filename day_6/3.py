a = list(map(str, input().split()))
for i in range(len(a)-1):
    while len(a[i]) > len(a[i+1]):
        flag = a[i+1]
        a[i+1] = a[i]
        a[i] = flag
print(*a)
