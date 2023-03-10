class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        temp = 0
        flag = False
        for c in s:
            print(stack)
            if c == '(':
                stack.append(c)
            else:
                if stack[-1] != "(":
                    a = stack.pop()
                    stack.pop()
                    if stack:
                        if stack[-1] == "(":
                            stack.append(2*a)
                        else:
                            stack[-1] += 2*a
                    else:
                        stack.append(2*a)
                else:
                    stack.pop()
                    if stack:
                        if stack[-1] == "(":
                            stack.append(1)
                        else:
                            stack[-1] += 1
                    else:
                        stack.append(1)
        return stack[0]