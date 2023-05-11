class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(mid):
            tot = 0
            for i in range(1,m+1):
                if mid//i < n:
                    tot += mid//i
                else:
                    tot += n
            return tot
        def binarySearch(start,end):
            if start == end:
                return start
            mid = (start+end)//2
            c = count(mid)
            if c >= k:
                return binarySearch(start,mid)
            return binarySearch(mid+1,end)
        return binarySearch(1,m*n)
