class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(n):
            for j in [1,2]:
                if i+j <= n:
                    dp[i+j] = min(dp[i+j],dp[i] + cost[i])
        return dp[n]

        
