#better performance
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = ''
        mx = 0
        for i in s:
            while i in stack:
                stack = stack[1:]
            stack += i
            mx = mx  if mx > len(stack) else len(stack)
        return mx
# worse performance
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         stack = []
#         mx = 0
#         for i in s:
#             while i in stack:
#                 stack = stack[1:]
#             stack.append(i)
#             mx = mx  if mx > len(stack) else len(stack)
#         return mx