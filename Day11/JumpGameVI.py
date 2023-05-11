class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        mx = 0
        for n in range(1, len(nums)):
            a = max((n - k) , 0)
            if mx < a:
                mx = a
                for i in range(a + 1, n):
                    if nums[i] >= nums[mx]:
                        mx = i
            nums[n] = nums[n] + nums[mx]
            if nums[n] >= nums[mx]:
                mx = n
        return nums[-1]