s = input()
ks = 0
kb = 0
for i in range(len(s)):
    if ord(s[i])>64 and ord(s[i])<91:
        kb += 1
    elif ord(s[i])>96 and ord(s[i])<123:
        ks += 1
kb = kb/(kb+ks)*100
ks = 100 - kb
print("Capital letters = ", "%.2f" % kb , "%")
print("Small letters = ", "%.2f" % ks , "%")
        
