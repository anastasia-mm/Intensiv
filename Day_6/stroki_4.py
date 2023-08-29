text = input()
low = len(list(filter(lambda x: x.islower(), text)))
up = len(list(filter(lambda x: x.isupper(), text)))
print(f'''Прописные: {low/len(text)*100}%
Строчные: {up/len(text)*100}%''')