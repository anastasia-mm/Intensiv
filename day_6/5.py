b = list(map(str, input().split()))
dl = []
for i in range(len(b)):
    dl.append(len(b[i]))
print(min(dl))