t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    m = 1
    while i < n:
        if a[i] % 2 == 0:
            m *= 2
            a[i] = a[i]//2
        else:
            i += 1
    a.sort()
    print(sum(a[:-1]) + (m * a[-1]))
