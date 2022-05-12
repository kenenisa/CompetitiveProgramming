class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        nums = [0] + nums
        total = 0
        sum1 = 0
        for i in range(firstLen, len(nums) - secondLen):
            s = nums[i] - nums[i - firstLen]
            if s > sum1:
                sum1 = s
            t = sum1 + nums[i + secondLen] - nums[i]
            if t > total:
                total = t

        sum2 = 0
        for j in range(secondLen, len(nums) - firstLen):
            s = nums[j] - nums[j - secondLen]
            if s > sum2:
                sum2 = s
            t = sum2 + nums[j + firstLen] - nums[j]
            if t > total:
                total = t

        return total