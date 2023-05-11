class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            return s
        stack = []
        d = ''
        i = 0
        n = len(s)
        start = 0
        end = 0
        while i < n:
            if s[i].isdigit():
                if not d:
                    start = i
                d += s[i]
            elif d:
                i += 1
                stack.append("[")
                while stack:
                    if s[i] == "[":
                        stack.append("[")
                    elif s[i] == "]":
                        stack.pop()
                    i += 1
                end = i
                break
            i += 1
        inside = s[start+len(d)+1:end-1]
        return self.decodeString(s[:start] + (inside * int(d)) + s[end:])




