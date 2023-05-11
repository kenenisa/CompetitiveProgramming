class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        # n = len(nums)
        # ans = []
        # for i in range(n):
        #     ans.append(nums[nums[i]])
        # return ans