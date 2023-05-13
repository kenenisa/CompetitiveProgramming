class Solution:
    def minSteps(self, n: int) -> int:
        factors = []
        if n == 1: return 0
        if n == 2: return 2
        for i in range(2, ceil(sqrt(n))+1):
            if n % i == 0:
                factors.append(i)
        if factors:
            m = float('inf')
            for f in factors:
                diff = self.minSteps(f) + self.minSteps((n//f))
                m = min(m,diff)
            return m
        return n