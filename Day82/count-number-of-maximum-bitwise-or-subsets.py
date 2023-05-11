class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_bitwise = 0
        for x in nums:
            max_bitwise |= x
        result = 0
        def backtrack(i,m):
            nonlocal result
            if i >= n:
                if m == max_bitwise:
                    result += 1
            else:
                backtrack(i+1,m | nums[i])
                backtrack(i+1,m)
        backtrack(0,0)
        return result
        