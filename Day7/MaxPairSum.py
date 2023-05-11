class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        mx = 0
        for i in range(0,n//2):
            k = nums[i] + nums[(n-1)-i]
            if(k > mx):
                mx = k
        return mx
                    