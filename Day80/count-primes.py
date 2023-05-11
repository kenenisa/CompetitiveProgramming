class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        df = defaultdict(bool)
        if n > 2:
            primes += 1
        for i in range(3,n,2):
            if df[i]: continue
            for j in range(i*i,n,i):
                df[j] = True
            primes += 1
        return primes