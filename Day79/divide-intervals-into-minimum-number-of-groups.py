class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        count = [0] * ((10**6)+2)

        for i in intervals:
            count[i[0]] += 1
            count[i[1]+1] -= 1

        for i in range(1,len(count)):
            count[i] += count[i-1]
        return max(count)