class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        x = 0
        y = 0
        increasing = [0] * n
        decreasing = [0] * n
        result = []
        if time > 0:
            for i in range(1,n):
                if security[i - 1] >= security[i]:
                    y += 1 
                else: 
                    y = 0
                decreasing[i] = y
            for i in range(n-1,0,-1):
                if security[i - 1] <= security[i]:
                    x += 1
                else: 
                    x = 0
                increasing[i-1] = x
            for i in range(n):
                if decreasing[i] >= time and increasing[i] >= time:
                    result.append(i)
        else:
            for i in range(n):
                result.append(i)
        return result