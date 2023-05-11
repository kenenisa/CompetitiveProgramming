class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distnict = set(nums)
        for num in nums:
            if num > 9:
                distnict.add(int(str(num)[::-1]))
        return len(distnict)
            
         