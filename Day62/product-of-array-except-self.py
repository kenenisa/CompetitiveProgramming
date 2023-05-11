class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeroes = 0
        acc = 1

        for i in range(n):
            if nums[i] == 0:
                zeroes += 1
            else:
                acc *= nums[i]
        
        result = [0]*n
        if zeroes > 1:
            return result
        elif zeroes == 1:
            for i in range(n):
                if nums[i] == 0:
                    result[i] = acc
                    return result
        else:
            for i in range(n):
                result[i] = acc//nums[i]
            return result
