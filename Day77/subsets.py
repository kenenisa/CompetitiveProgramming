class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        sub = []
        def backtrack(i):
            if i >= n:
                result.append(sub[::])
            else:
                sub.append(nums[i])
                backtrack(i+1)
                sub.pop()
                backtrack(i+1)
        backtrack(0)
        return result