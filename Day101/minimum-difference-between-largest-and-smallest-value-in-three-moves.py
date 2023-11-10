class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0
        nums.sort()
        window = n - 4
        mi = float('inf')
        for i in range(n-window):
            m = nums[i+window] - nums[i]
            if m < mi:
                mi = min(mi,m)
        return mi
# [12,123,1,1,3,4]
#   i+2      
