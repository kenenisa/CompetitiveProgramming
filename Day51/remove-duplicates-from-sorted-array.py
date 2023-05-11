class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 1
        while p < n:
            if nums[p-1] == nums[p]:
                nums.pop(p)
                n -= 1
            else:
                p+=1
        return len(nums)