class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        def srt(key):
            return key[0]
        intervals.sort(key=srt)
        result = [intervals[0]]
        for i in range(n):
            last = len(result) - 1
            if result[last][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[last][1] = result[last][1] if result[last][1] > intervals[i][1] else intervals[i][1]
        return result
