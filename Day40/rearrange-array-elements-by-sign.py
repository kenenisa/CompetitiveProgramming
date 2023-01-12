class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i] > 0:
                result.insert(pos,nums[i])
                pos += 2
            if nums[i] < 0:
                result.insert(neg,nums[i])
                neg += 2
        return result
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         positive = True
#         n = len(nums)
#         result = []
#         index = 0
#         while index < n:
#             search = index + 1
#             #if it's at the right pos
#             if positive == (nums[index] > 0):
#                 positive = not positive
#                 result.append(nums[index])
#                 index += 1
#                 continue
#             #look for a replacement
#             while search < n - 1 and positive == (nums[search] < 0): 
#                 search += 1
#             #switch place
#             result.append(nums[search])
#             nums.pop(search)
#             n -= 1
#             #switch sign
#             positive = not positive
#         return result
            
            