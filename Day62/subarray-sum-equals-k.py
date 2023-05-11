class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        df= {0: 1}
        acc = 0
        result = 0

        for num in nums:
            acc += num
            if df.get(acc - k):
                result += df[acc-k]

            if df.get(acc):
                df[acc] += 1
            else:
                df[acc] = 1
        return result