class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        for i in range(len(nums1)):
            val = -1
            find = nums2.index(nums1[i])
            for j in range(find,n):
                if nums1[i] < nums2[j]: 
                    val = nums2[j]
                    break
            stack.append(val)
        return stack