class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def binarySearch(start,end):
            if start == end:
                return start
            
            mid = (start + end)//2
            
            time = 1
            total = 0
            # check shipment
            for w in weights:
                total += w
                if mid < total:
                    total = w
                    time +=1
                    
            if time <= days:
                return binarySearch(start,mid)
            return binarySearch(mid+1,end)
        return binarySearch(max(weights),sum(weights))
