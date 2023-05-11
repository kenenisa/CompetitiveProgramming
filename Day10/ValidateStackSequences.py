class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        poppedStack = deque(popped)
        stack = deque([])
        n = len(pushed)

        for i in pushed:
            stack.append(i)
            while stack and poppedStack and stack[-1] == poppedStack[0]:
                stack.pop()
                poppedStack.popleft()
        return False if stack else True