class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,sm,result = 0,0,0
        for j in range(len(nums)):
            sm += nums[j]
            while (k < (j - i + 1) *nums[j] - sm):
                sm -= nums[i]
                i += 1

            result = max(result, j - i + 1)
        return result