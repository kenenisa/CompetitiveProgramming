class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        s=0
        n = len(nums)
        left = 0
        result = n
        for right in range(n):
            s += nums[right]
            while s >= target:
                result = min(result,right - left + 1)
                s -= nums[left]
                left += 1
        return result