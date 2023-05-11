class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checkThreshold(num):
            total = 0
            for x in nums:
                total += ceil(x/num)
                if total > threshold:
                    return False
            return True
        def binarySearch(start,end):
            if start >= end:
                return start
            mid = (start+end)//2
            if checkThreshold(mid):
                return binarySearch(start,mid)
            return binarySearch(mid+1,end)
        
        
        return binarySearch(1,max(nums))