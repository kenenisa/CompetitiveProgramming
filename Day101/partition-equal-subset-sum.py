class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1: return False
        s //=2 
        memo = {}
        def dp(i,num):
            if num == 0: return True
            if num < 0 or i >= len(nums): return False
            if (i,num) in memo:
                return memo[(i,num)]
            op1 = dp(i+1,num)
            if op1:
                return True
            op2 = dp(i+1,num-nums[i])
            memo[(i,num)] = op2
            return op2
        return dp(0,s)
