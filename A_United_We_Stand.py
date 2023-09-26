from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    c = []
    for i in range(n-1,-1,-1):
        if a[i] == a[-1]:
            c.append(a[i])
        else:
            b.append(a[i])
    if b and c:
        print(len(b),len(c))
        print(*b)
        print(*c)
    else:
        print(-1)

