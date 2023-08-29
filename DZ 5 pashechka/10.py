print('Введите сначала имя и отчество, потом фамилию')
a = input()
b = list(map(str,a.split()))
name = b[0]
soname = b[2]
otch = b[1]
print(soname, name[0]+'.', otch[0]+'.')
