# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         def compareLargestDigit(a,b):
#             comb1 = int(a + b)
#             comb2 = int(b + a)
#             if(comb1 > comb2):
#                 return True
#             return False
#         for k in range(1, len(nums)):
#             key = nums[k]
#             print(nums,k,key)
#             i = k - 1
#             while i >= 0 and compareLargestDigit(str(key), str(nums[i])):
#                 nums[i + 1] = nums[i]
#                 i -= 1

#             nums[i + 1] = key
#         c = ''.join(map(str,nums))
#         return str(int(c))
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class CompareLargestDigit(str):
            def __lt__(a,b):
                return int(a+b) < int(b+a)
        nums.sort(key=CompareLargestDigit,reverse=True)
        c = ''.join(map(str,nums))
        return str(int(c))

        
        