class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s = [ord(a)-97 for a in s]
        res = [0] * n 
        for start,end,direction in shifts:
            if direction == 1:
                res[start] += 1
                if end + 1 < n:
                    res[end+1] -= 1
            else:
                res[start] -= 1
                if end + 1 < n:
                    res[end+1] += 1
        prefix = [0]
        for r in res:
            prefix.append(prefix[-1] + r)
        result = []
        for i in range(1,len(prefix)):
            result.append(chr(((s[i-1] + prefix[i])%26) + 97))
        return "".join(result)
