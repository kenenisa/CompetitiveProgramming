t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = sorted(a)
    df = {}
    for i in range(n-1):
        df[b[i]] = b[i+1]
    j = 0
    for i in range(n-1):
        if a[i+1] != df.get(a[i], int(1e9)+7):
            j += 1
    print("No" if j >= k else "Yes")
