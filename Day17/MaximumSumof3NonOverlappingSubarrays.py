class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        first, second, third = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        sumFirst, sumSecond, sumThird = first, first+second, first+second+third
        firstIndex, secondIndex, thirdIndex = [0], [0,k], [0,k,2*k]
        for i in range(1, len(nums)-3*k+1):
            first += nums[i-1+k] - nums[i-1]
            second += nums[i-1+2*k] - nums[i-1+k]
            third += nums[i-1+3*k] - nums[i-1+2*k]
            if first > sumFirst:
                sumFirst, firstIndex = first, [i]
            if sumFirst + second > sumSecond:
                sumSecond, secondIndex = sumFirst + second, firstIndex + [i+k]
            if sumSecond + third > sumThird:
                sumThird, thirdIndex = sumSecond + third, secondIndex + [i+2*k]
        return thirdIndex