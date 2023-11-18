t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0]*(n+1)
    result = 0

    for i in range(1, n+1):
        if i + a[i-1] <= n:
            dp[i + a[i-1]] = max(dp[i + a[i-1]], dp[i] + a[i-1])
        else:
            result = max(result, dp[i]+a[i-1])
    print(result)
