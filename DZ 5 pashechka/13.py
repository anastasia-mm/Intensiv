a = list(map(int, input().split()))
a = sorted(a)
print(a)
minn = a[0]
maxx = a[-1]
a[0] = maxx
a[-1] = minn
print(a)
