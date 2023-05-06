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