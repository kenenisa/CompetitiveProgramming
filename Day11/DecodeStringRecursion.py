class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        def fn(s):
            i = s[0]
            if i == ']':
                word = stack.pop()
                stack.pop()
                k = stack.pop()
                if not stack or stack[-1] in '[]':
                    stack.append(word * int(k))
                else:
                    stack[-1] += word * int(k)
            elif i == '[':
                stack.append(i)
            else:
                if stack and i.isdigit() == stack[-1].isdigit():
                    if stack[-1] in '[]':
                        stack.append(i)
                    else:
                        stack[-1] += i
                else:
                    stack.append(i)
            sn = s[1:]
            return fn(sn) if len(sn) else "".join(stack)
        return fn(s)