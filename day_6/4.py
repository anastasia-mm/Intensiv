sl = input()
stroch = 0
propis = 0
for i in range(len(sl)):
    if 97 <= ord(sl[i]) <= 122:
        stroch += 1
    elif 65 <= ord(sl[i]) <= 90:
        propis += 1
    else:
        print('Error')
proz_stroch = stroch/len(sl)*100
proz_propis = propis/len(sl)*100
print('Процент строчных = ', '%.3f' % proz_stroch, '% Процент прописных = ', '%.3f' % proz_propis, '%', sep='')
