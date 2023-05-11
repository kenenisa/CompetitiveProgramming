class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix= [0]
        # nums = [2,1,-1]
        for i in range(0, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # prefix = prefix[1:]
        nums = nums + [0]
        result = -1
        for j in range(len(prefix) - 1):
            if prefix[j] == (prefix[-1] - prefix[j]) - nums[j]:
                result = j
                break
        return result