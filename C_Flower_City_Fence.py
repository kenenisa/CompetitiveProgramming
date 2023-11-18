t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if a[0] != n:
        print("NO")
        continue
    hor = [0] * n

    for i in range(n):
        hor[0] += 1
        if a[i] < n:
            hor[a[i]] -= 1
    for i in range(1,n):
        hor[i] += hor[i-1]
    print("YES" if hor == a else "NO")
