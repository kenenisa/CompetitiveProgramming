class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s # add this
        text2 = s[::-1] # and this

        # longest common subsequence
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
