t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    m = n
    for i in range(1,n):
        if abs(a[i] - a[i-1]) <= 1:
            m -= 1
    if m <= 1:
        print("YES")
    else:
        print("NO")

