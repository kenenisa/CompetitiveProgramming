class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for _ in range(n)]
        result = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                # print(i,j)
                if text1[i] == text2[j]:
                    dp[i][j] += 1
                    if i-1 >=0 and j-1>=0:
                        dp[i-1][j-1] = max(dp[i-1][j-1],dp[i][j])
                else:
                    if i-1 >= 0:
                        dp[i-1][j] = max(dp[i-1][j],dp[i][j]) 
                    if j-1 >= 0:
                        dp[i][j-1] = max(dp[i][j-1],dp[i][j]) 
                result = max(result,dp[i][j])
        return result
#    a. c. e
# [a[2, 1, 0], 
#  b[2, 1, 0], 
#  c[1, 1, 0], 
#  d[1, 1, 0], 
#  e[0, 0, 0]]
# [[2, 2, 2, 2, 2, 0, 0, 0, 0], 
#  [1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [1, 1, 0, 0, 0, 0, 0, 0, 0], 
#  [1, 1, 0, 0, 0, 0, 0, 0, 0], 
#  [1, 1, 0, 0, 0, 0, 0, 0, 0], 
#  [1, 1, 0, 0, 0, 0, 0, 0, 0], 
#  [1, 1, 0, 0, 0, 0, 0, 0, 0]]
