t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(m):
        a.sort()
        a[0] = b[i]
    print(sum(a))