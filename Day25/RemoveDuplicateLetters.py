class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        visited = {el: index for index, el in enumerate(s)}

        stack = []
        n = len(s)
        for i in range(n):
            if s[i] not in stack:
                while stack and i < visited[stack[-1]] and  s[i] < stack[-1]:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
