class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swapThem():
            for i in range(1,len(nums) - 1):
                while((nums[i-1] + nums[i+1]) / 2 == nums[i]):
                    nums[i-1], nums[i] = nums[i], nums[i-1]

            for j in range(1,len(nums) - 1):
                if((nums[j-1] + nums[j+1]) / 2 == nums[j]):
                    swapThem()
        swapThem()
        return nums