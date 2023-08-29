s = input()
s1 = ""
numbers = []
for i in range(len(s)):
    if ord(s[i])>47 and ord(s[i])<58:
        s1 += s[i]
    elif s1 != "":
        numbers.append(s1)
        s1 = ""
if s1 != "":
    numbers.append(s1)
print(numbers)
