class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        def binarySearch(start,end,lookinFor):
            if start == end: return end
            if end - start == 1: 
                if nums[start] == target:
                    return start
                return end
            middle = int((start + end)/2)
            if lookinFor == 'start':
                if nums[middle] == target:
                    return binarySearch(start,middle,lookinFor)
                elif nums[middle] < target:
                    return binarySearch(middle,end,lookinFor)
                return binarySearch(start,middle,lookinFor)
            
            if nums[middle] == target:
                return binarySearch(middle,end,lookinFor)
            elif nums[middle] < target:
                return binarySearch(middle,end,lookinFor)
            return binarySearch(start,middle,lookinFor)
        if target in nums:
            result[0] = binarySearch(0,len(nums),'start')
            result[1] = binarySearch(0,len(nums),'end')
        return result
