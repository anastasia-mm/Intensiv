n = input()
countp = 0
counts = 0
prop = [chr(a) for a in range(65, 91)]
stroch = [chr(a) for a in range(97, 122)]
for s in prop:
    if s in n:
        countp += 1 * n.count(s)
for s in stroch:
    if s in n:
        counts += 1 * n.count(s)
print(countp/len(n)*100, counts/len(n)*100)