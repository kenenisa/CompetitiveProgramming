class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(1,len(arr)):
        #     if arr[i-1] < arr[i] > arr[i+1]:
        #         return i
        # return -1 

        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left