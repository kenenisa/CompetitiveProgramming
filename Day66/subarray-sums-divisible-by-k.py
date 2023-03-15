class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        df = defaultdict(int)
        prefixSum = [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + nums[i])
        df[0] = 1
        result = 0
        for i in range(n):
            result += df[prefixSum[i+1]%k]
            df[prefixSum[i+1]%k] += 1
        return result 
        