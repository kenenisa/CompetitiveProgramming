class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def binarySearch(start,end):
            if start > end:
                return start
            middle = int((start+end)/2)
            
            if n - middle <= citations[middle]:
                return binarySearch(start,middle-1)
            return binarySearch(middle+1,end)
            
        
        return n - binarySearch(0,n-1)
        