class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = 0
        for i in range(k):
            s += nums[i]
        mx = s
        for i in range(n-k):
            s -= nums[i]
            s += nums[i+k]
            mx = max(mx,s)
        return mx/k
