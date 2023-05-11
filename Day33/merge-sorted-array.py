class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i = 0
        j = 0
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[i+j] = temp[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        for k1 in range(i,m):
            nums1[i+j] = temp[i]
            i += 1
        for k2 in range(j,n):
            nums1[i+j] = nums2[j]
            j += 1
        temp += temp[i:] + nums2[j:]
        nums1 = temp

