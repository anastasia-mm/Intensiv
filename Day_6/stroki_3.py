text = input()
print(' '.join(sorted(text.split(), key=len)))