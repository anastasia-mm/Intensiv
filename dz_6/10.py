s = input()
unique = []
for i in s:
    if i not in unique and i != " ":
        unique.append(i)
print(*unique, sep="")
