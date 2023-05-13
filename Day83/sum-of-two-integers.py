class Solution:
    def getSum(self, a: int, b: int) -> int:
        limit = 0xffffffff
        while b & limit != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        if b > limit:
            return a & limit 
        return a