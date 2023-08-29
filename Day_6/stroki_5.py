text = input()
print(len(min(text.split(), key=len)))