class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(num == "0"): return "0"
        stack = deque()
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == "0":
            stack.popleft()
        return "".join(stack) if stack else "0"