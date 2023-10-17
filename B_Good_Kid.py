t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = 0
    for i in range(n):
        a[i] += 1
        p = 1
        for j in range(n):
            p *= a[j]
        m = max(m,p)
        a[i] -= 1
    print(m)

