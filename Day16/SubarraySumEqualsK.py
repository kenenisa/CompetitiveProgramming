class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        df= {0: 1}
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            if df.get(prefix - k):
                result = result + df[prefix-k]

            if df.get(prefix):
                df[prefix] = df[prefix] + 1
            else:
                df[prefix] = 1
        return result