file = input()
norm = ['txt', 'pdf', 'docx']
rassh = file.split('.')[1]
if rassh in norm:
    print('OK')
else:
    print('FUCK YOU')