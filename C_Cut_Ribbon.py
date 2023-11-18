n, a, b, c = list(map(int, input().split()))

dp = [float('-inf')]*(n+1)

dp[0] = 0
for i in range(n+1):
    for c in [a, b, c]:
        if dp[i] != float('-inf') and i+c <= n:
            dp[i+c] = max(dp[i+c], dp[i]+1)
print(dp[n])
