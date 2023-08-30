alphabet = []
i = 1
for x in range(97,97+26):
    alphabet.append(chr(x)*i)
    i += 1
print(alphabet)