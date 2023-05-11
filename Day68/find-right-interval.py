class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = []

        for i in range(n):
            starts.append((intervals[i][0],i))
        starts.sort(key=lambda item: item[0])

        def find(end):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == n:
                return -1
            return starts[left][1]
        result = []
        for i in range(n):
            result.append(find(intervals[i][1]))
        return result
                    