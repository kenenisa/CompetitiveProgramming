t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    for i in range(n):
        s.append((a[i], i))
    s.sort()
    result = [0] * n
    left = 0
    right = sum(a)
    for i in range(n):
        j = s[i][1]
        rr =right-(a[j]*(n-i))
        ll = (a[j]*i)-left
        result[j] = rr+n-i+ll+i
        left += a[j]
        right -= a[j]
    print(*result)
