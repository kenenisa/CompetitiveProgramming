class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        result = nums[-1] - nums[0]
        for i in range(len(nums)):
            result = min(result,max(nums[i-1]+k,nums[-1]-k) - min(nums[0]+k,nums[i]-k))           
        return result
