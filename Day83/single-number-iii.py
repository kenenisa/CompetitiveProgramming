class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        t = 0
        for n in nums:
            t ^= n
        diff =  t & (-t)
        x = 0
        for n in nums:
            if n & diff != 0:
                x ^= n
        return [x,  t^x]
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         df = {}
#         result = []
        
#         for n in nums:
#             if n not in df:
#                 df[n] = True
#                 result.append(n)
#                 continue
#             else:
#                 result.remove(n)
#         return result