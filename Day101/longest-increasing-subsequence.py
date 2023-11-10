class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            idx = bisect_left(s,i)
            n = len(s)
            if n==idx:
                s.append(i)
            else:
                s[idx] = i
        return len(s)
