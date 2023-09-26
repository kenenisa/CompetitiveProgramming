# from collections import defaultdict,Counter
# n = int(input())
# a = list(map(int,input().split()))
# c = Counter(a)
# memo = {}
# def dfs(i):
#     if i < 2: return c[i]
#     # if i in memo: return memo[i]
#     op1 = dfs(i-1)
#     op2 = dfs(i-2)
#     return max(op1,op2 + c[i]*i)
# print(dfs(n))
n = int(input())
a = list(map(int,input().split()))
dp = [0]*(10**5 + 2)
for i in range(n):
    dp[a[i]] += a[i]
for i in range(2, len(dp)):
    dp[i] = max(dp[i-1], dp[i-2]+dp[i])
print(dp[-1])
