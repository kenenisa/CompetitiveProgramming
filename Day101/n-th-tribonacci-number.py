class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tri(n:int):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n <= 2: return 1
            memo[n] =  tri(n-1) + tri(n-2) + tri(n-3)
            return memo[n]
        return tri(n)
    
