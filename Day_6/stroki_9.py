from string import ascii_letters
text = input()
for a in ascii_letters:
    text = text.replace(a, '')
print(list(map(int, text.split())))