s = list(map(int, input().split()))
imax = s.index(max(s))
imin = s.index(min(s))
c = min(s)
s[imin] = max(s)
s[imax] = c
print(s)
