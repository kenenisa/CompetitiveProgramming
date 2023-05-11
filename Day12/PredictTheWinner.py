class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache 
        def window(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - window(left + 1, right), nums[right] - window(left, right - 1))
        result = window(0,n - 1) >= 0
        return result