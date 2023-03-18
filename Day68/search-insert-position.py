class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #O(log N)
        # n = len(nums)
        # left = 0
        # right = n - 1
        # while left <= right:
        #     middle = (right+left)//2
        #     if nums[middle] == target:
        #         return middle 
        #     if nums[middle] > target:
        #         right = middle - 1
        #     else:
        #         left = middle + 1
            
        # return left 
        return bisect_left(nums,target)
        # O(N)
        # for i in range(n):
        #     if nums[i] == target or nums[i] > target:
        #         return i
        # return n