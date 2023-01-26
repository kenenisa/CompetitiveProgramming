class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            m = i
            for j in range(i+1,n):
                if nums[m] > nums[j]:
                    m = j
            if nums[m] == 2:
                break
            nums[i],nums[m] = nums[m],nums[i]