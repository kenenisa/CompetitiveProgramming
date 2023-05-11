class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        mx = 0
        for i in range(n):
            if nums[i] == 1:  continue #go to the right untill we find zeros
            if k > 0: #exhaust zeros at first
                k -= 1
                continue
            mx = max(mx,i - j)
            while j < i and nums[j] != 0: #shrink the window from left to right
                j += 1
            j += 1
        mx = max(mx,n - j)
        return mx