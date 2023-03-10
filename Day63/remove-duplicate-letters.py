class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i

        stack = []
        n = len(s)
        for i in range(n):
            if s[i] not in stack:
                while stack and i < lastIndex[stack[-1]] and  s[i] < stack[-1]:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)