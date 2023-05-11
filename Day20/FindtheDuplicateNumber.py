class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def binarySearch(start,end):
            if start >= end: return start
            mid = (start+end)//2
            
            amount = (sum(i<=mid for i in nums))
            
            if amount <= mid:
                return binarySearch(mid+1,end)
            return binarySearch(start,mid)
        return binarySearch(0,len(nums)-1)
