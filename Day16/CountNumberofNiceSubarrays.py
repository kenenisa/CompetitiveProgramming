class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        df = defaultdict(int)
        df[0] = 1
        prefix = 0
        result = 0
        for i in nums:
            prefix += 0 if i % 2 == 0 else 1
            result += df[prefix - k]
            df[prefix] += 1
        return result
            