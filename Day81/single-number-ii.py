class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base1 = 0
        base2 = 0
        for n in nums:
            base1 ^=  n & ~base2
            base2 ^=  n & ~base1
        return base1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = set()
        twice = set()
        for num in nums:
            if num in once:
                twice.add(num)
            else:
                once.add(num)
        return once.difference(twice).pop()