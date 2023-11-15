class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        memo = {}
        def dp(i,j):
            if j == m: return 1
            if j> m or i >= n: return 0
            if (i,j) in memo: return memo[(i,j)]
            count = 0
            if s[i] == t[j]: 
                count += dp(i+1,j+1)
            count += dp(i+1,j)
            memo[(i,j)] = count
            return count
        return dp(0,0)
        # dp = [0 for _ in range(n+1)] * (m+1)
        # dp[0][0] = 1
        # for i in range(n):
        #     for j in range(m):



            
        
