class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        mod = []
        j = 0
        n = len(spaces)
        for i in range(len(s)):
            if j < n and i == spaces[j]:
                mod.append(" " + s[i])
                j+=1
            else:
                mod.append(s[i])
        return "".join(mod)