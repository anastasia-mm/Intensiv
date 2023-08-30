text = input()
res = []
for a in text:
    if a not in res and a != ' ':
        res.append(a)
print(*res, sep='')