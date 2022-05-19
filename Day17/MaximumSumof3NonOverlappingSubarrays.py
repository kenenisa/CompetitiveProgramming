class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        df = {}
        def recur(nums, k, index, x,df):
            if x == 3:
                return [0, []]

            if index - (x * k) > n:
                return [0, []]
            if (index,x) in df:
                return df[(index,x)]

            r = recur(nums, k, index + k, x + 1,df)
            r[0] += sum(nums[index:index + k])

            rn = recur(nums, k, index + 1, x,df)
            if r[0] >= rn[0]:
                df[(index,x)] = [r[0],([index] + r[1])]
            else:
                df[(index,x)] = [rn[0],rn[1]]
            return df[(index,x)]
        result = recur(nums, k, 0, 0,df)
        return result[1]