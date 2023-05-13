class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        result = 0
        for i in range(32):
            if a & (1 << i):
                result += 1
        return result