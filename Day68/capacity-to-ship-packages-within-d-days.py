class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calcShipment(val):
            s = 0
            d = 1
            for w in weights:
                s += w
                if val < s:
                    d += 1
                    s = w
                
            return d
        def binarySearch(start,end):
            if start == end:
                return start
            mid = (start + end) // 2
            if calcShipment(mid) > days:
                return binarySearch(mid+1,end)
            return binarySearch(start,mid)
        return binarySearch(max(weights),sum(weights))
    