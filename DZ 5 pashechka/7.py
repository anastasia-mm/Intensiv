n = int(input())
a = [int(input()) for i in range(n)]
b=[]
for i in range(len(a)-1):
    b.append(a[i]+a[i+1])
print(a,b)