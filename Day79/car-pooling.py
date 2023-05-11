class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip = [0]*1001

        for t in trips:
            trip[t[1]] += t[0]
            trip[t[2]] -= t[0]
        for i in range(1001):
            if i > 0:
                trip[i] += trip[i-1]
            if trip[i] > capacity:
                return False
        return True