class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = 0
        w = 0
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        while r < n:
            while w < n and nums[w] != 0:
                w += 1
            r = w + 1
            while r < n and nums[r] == 0:
                r += 1
            if r < n and w < n and nums[w] == 0 and nums[r] != 0:
                nums[w],nums[r] = nums[r],nums[w]
                w += 1
        return nums
