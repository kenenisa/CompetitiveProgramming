class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base1 = 0
        base2 = 0
        for n in nums:
            base1 ^=  n & ~base2
            base2 ^=  n & ~base1
        return base1