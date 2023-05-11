class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        while n > 2 and nums[n - 3] + nums[n - 2] <= nums[n-1]:
            n -= 1
        if n < 3:
            return 0
        return nums[n-3] + nums[n-2] + nums[n-1]
    # first attempt: TLE
    # def largestPerimeter(self, nums: List[int]) -> int:
    #     def checkTriangle(a,b,c):
    #         return a + b > c and b + c > a and a + c > b
    #     p1 = 0
    #     p2 = 1
    #     p3 = 2
    #     n = len(nums)
    #     result = 0
    #     while p1 < n - 2:
    #         if checkTriangle(nums[p1],nums[p2],nums[p3]):
    #             result = max(result, nums[p1] + nums[p2] +nums[p3])
    #         if p2 == n - 2 and p3 == n - 1:
    #             p1 += 1
    #             p2 = p1 + 1
    #             p3 = p1 + 2
    #         elif p3 == n - 1:
    #             p2 += 1
    #             p3 = p2 + 1
    #         elif p3 < n - 1:
    #             p3 += 1

    #     return result
