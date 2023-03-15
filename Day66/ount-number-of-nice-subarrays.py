class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        df = defaultdict(int)
        df[0] = 1
        prefix = 0
        result = 0
        for i in nums:
            if i % 2:
                prefix += 1
            result += df[prefix - k]
            df[prefix] += 1
        return result
            