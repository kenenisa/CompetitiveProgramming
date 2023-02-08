class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        temp = [0] * (m+n)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp[i+j] = nums1[i]
                i += 1
            else:
                temp[i+j] = nums2[j]
                j += 1
        while i < m:
            temp[i+j] = nums1[i]
            i+=1
        while j < n:
            temp[i+j] = nums2[j]
            j+=1
        nums1[:] = temp