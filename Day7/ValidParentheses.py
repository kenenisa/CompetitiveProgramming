class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {'(':1,'[':2,'{':3,')':4,']':5,'}':6}
        result = True
        for i in s:
            b = braces[i]
            if(b < 4):
                stack.append(i)
            else:
                n = len(stack)
                if(n != 0):
                    if(braces[stack[n - 1]] + 3 == b):
                        stack.pop()
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
        return result if len(stack) == 0 else False