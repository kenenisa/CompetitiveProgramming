t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    dp = [False] * (n+1)
    dp[0] = True

    for i in range(1,n+1):
        if dp[i-1]:
            if i + b[i-1] <= n:
                dp[i + b[i-1]] = True
        if i - b[i-1] - 1 >= 0:
            if dp[i-b[i-1]-1]:
                dp[i] = True
    print("YES" if dp[n] else "NO")

