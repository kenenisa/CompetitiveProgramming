from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left**2 + right**2 - c != 0 and left < right:
            if left**2 + right**2 - c > 0:
                right -=1
            else:
                left += 1
        if left**2 + right**2 == c:
            return True
        return False
# from math import sqrt
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         df = {}
#         for i in range(int(sqrt(c) + 1)):
#             df[i**2] = i
#             if (c - i**2) in df:
#                 return True
#         return False

        
        