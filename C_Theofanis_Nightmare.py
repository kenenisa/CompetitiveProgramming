def run():
    n = int(input())
    a = list(map(int,input().split()))
    s = 0
    dp = [0]*(n+1)
    count = [1]*(n+1)
    i = n-1
    while i >= 0:
        dp[i] = dp[i+1]+a[i]
        inc = dp[i+1]+s+a[i]
        if inc > dp[i] or (inc == dp[i] and count[i+1]+1 > count[i]): 
            dp[i] = inc
            count[i] = count[i+1]+1
        s += a[i]
        i-=1
    return dp[0]
t = int(input())
for _ in range(t):
    print(run())