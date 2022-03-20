class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class CompStr(str):
            def __lt__(x, y):
                return x+y < y+x

        largest = ''.join(map(str,sorted(nums,key=CompStr,reverse=True)))
        return '0' if largest[0] == '0' else largest

#initial attempt but slower
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         def compareLargestDigit(a,b):
#             print(a,b)
#             comb1 = int(a + b)
#             comb2 = int(b + a)
#             if(comb1 > comb2):
#                 return 1
#             return 0
#         for k in range(1, len(nums)):
#             key = nums[k]
#             i = k - 1

#             while i >= 0 and compareLargestDigit(str(key), str(nums[i])):
#                 nums[i + 1] = nums[i]
#                 i = i - 1

#             nums[i + 1] = key
#         # print(''.join(map(str,nums)))
#         c = ''.join(map(str,nums))
#         return str(int(c))

        