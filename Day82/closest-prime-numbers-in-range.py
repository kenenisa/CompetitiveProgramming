class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right+1)
        i = 2
        while i * i <= right:
            if primes[i]:
                for j in range(i*i,right+1,i):
                    primes[j] = False
            i += 1
        p = []
        result = [-1,-1]
        m = float('inf')
        if left == 1: left = 2
        for i in range(left,right+1):
            if primes[i]:
                p.append(i)
                if len(p) > 1:
                    diff = p[-1] - p[-2]
                    if m > diff:
                        m = diff
                        result = [p[-2],p[-1]]
        if len(p) < 2:
            return result
        return result
            

        