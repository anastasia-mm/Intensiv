n = int(input())
'''a = []
for i in range(n):
    a.append(int(input()))'''
a = [int(input()) for i in range(n)]
# print(a)
# print(a[0::2])
i = 1
while i < len(a):
    del(a[i])
    i += 1
print(a)
# haha