class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * 366
        day,week,month = costs
        dp[0]=0
        j = 0
        passes = [1,7,30]
        for i in range(1,366):
            if j == n: break
            if i < days[j]:
                dp[i] = dp[i-1]
            else:
                for k in range(3):
                    x = 0
                    if i-passes[k] > -1:
                        x = dp[i-passes[k]]
                    dp[i] = min(dp[i],x + costs[k])
                j+=1
        return dp[days[-1]]
