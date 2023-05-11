# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(start:int,end:int):
            if start == end: return start
            middle = int((start + end)/2)
            if isBadVersion(middle):
                if not isBadVersion(middle-1):
                    return middle
                return binarySearch(start,middle-1)
            return binarySearch(middle+1,end)
        return binarySearch(0,n)
        