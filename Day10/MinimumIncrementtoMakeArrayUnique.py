class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        srt = sorted(nums)
        res = []
        result = 0

        for i in range(len(srt) - 1):
            if srt[i] < srt[i + 1]:
                res.append(srt[i])
            else:
                res.append(srt[i])
                srt[i + 1] = srt[i] + 1
        res.append(srt[-1])  

        srt = sorted(nums)
        for i in range(len(srt)):
            result += res[i] - srt[i]
        return result