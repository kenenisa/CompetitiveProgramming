t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = 0
    dp = [0] * (n+1)
    for i in range(1,n+1):
        if a[i-1] < i:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = dp[i-1]
        if a[i-1] < i and a[i-1]-1>=1:
            result += dp[a[i-1]-1]
    print(result)
# o(n) - time
# o(n) - space