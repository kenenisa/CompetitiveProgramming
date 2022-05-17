class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 1
        y = 1
        result = 1
        for i in range(1,n):
            if prices[i - 1] - prices[i] == 1:
                y += 1 
            else: 
                y = 1
            result += y
        return result