n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
q = int(input())
for _ in range(q):
    inp = input().split()
    s = inp[0]
    p = map(int,inp[1:])
    if s == 's':
        l,r,mod = p
        s = 0
        for i in range(l,r+1):
            if a[i-1] == mod:
                s += a[i-1]
        print(s)
    elif s == '+':
        x,r = p
        a[x-1] += r
        print(a[x-1])
    else:
        x,r = p
        if a[x-1] - r > -1:
            a[x-1] -= r
        print(a[x-1])
