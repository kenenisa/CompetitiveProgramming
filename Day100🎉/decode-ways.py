class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        
        n = len(s)
        memo = {}
        def decode(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            ones = 0
            twos = 0
            if s[i] != '0':
                # one 
                ones = decode(i+1)
                # two
                if i < n-1:
                    two = int(s[i] + s[i+1])
                    if two <= 26:
                        twos = decode(i+2)
            memo[i] = ones + twos
            return memo[i]
        
        return decode(0)
