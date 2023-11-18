class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        level = 0
        result = []
        n = len(nums)
        for i in range(n):
            level += nums[i]
            result.append((level + i)//(i+1))
        return max(result)
