t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    result = [0] * n
    m = b[-1]
    for i in range(n):
        if a[i] == m:
            result[i] = a[i] - b[-2]
        else:
            result[i] = a[i] - m
    print(*result)