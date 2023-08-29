a=str(input())
s=0
g=0
b=0
for i in a:
    if 65<=ord(i)<91:
        b+=1
        g+=1
    elif 97<=ord(i)<123:
        s+=1
        g+=1
print('Big: '+str(b*100/g) + '%')
print('Shmol: '+str(s*100/g) + '%')