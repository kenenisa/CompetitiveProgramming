t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    i = 0
    result = 0
    rs = 0
    for j in range(n):
        if h[j-1] % h[j] != 0:
            i = j
            rs = a[j]
        else:
            rs += a[j]
        while i < n and rs > k:
            rs -= a[i]
            i += 1
        result = max(result, j-i+1)
    print(result)