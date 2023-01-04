class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = []
        block = False
        line = ''
        for s in source:
            n = len(s)
            i = 0
            while i < n: 
                if not block:
                    if s[i] == '/' and i != n - 1 and s[i+1] == '/': 
                        break
                    elif s[i] == '/' and i != n - 1 and s[i+1] == '*':
                        block = True
                        i+=1
                    else:
                        line += s[i]
                else:
                    if s[i] == '*' and i < n-1 and s[i+1] == '/':
                        block = False
                        i+=1
                i += 1
            if not block and len(line) > 0:
                code.append(line)
                line = ''
        return code