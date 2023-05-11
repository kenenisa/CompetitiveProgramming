class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        newArr = []
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                newArr.append(i)
        return newArr