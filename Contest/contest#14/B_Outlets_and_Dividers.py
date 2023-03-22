t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    a = list(map(int,input().split()))
    if n <= 2:
        print(0)
        continue
    a.sort()
    o = 2
    for i in range(m-1,-1,-1):
        o += a[i] - 1
        if o >= n:
            print(m-i)
            break
    if o < n:
        print(-1)

