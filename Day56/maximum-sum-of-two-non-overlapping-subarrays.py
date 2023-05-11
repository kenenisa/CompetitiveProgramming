class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        maxl = maxm = summ = 0
        for x in nums:
            prefix.append(prefix[-1] + x)

        for x in range(firstLen, len(prefix) - secondLen):
            maxm = max(maxm, prefix[x] - prefix[x - firstLen])
            summ = max(summ, maxm + prefix[x + secondLen] - prefix[x])
        
        for x in range(secondLen, len(prefix) - firstLen):
            maxl = max(maxl, prefix[x] - prefix[x - secondLen])
            summ = max(summ, maxl + prefix[x + firstLen] - prefix[x])
        
        return summ