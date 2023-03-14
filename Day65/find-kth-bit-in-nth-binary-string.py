class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            b = {"0":"1","1":"0"}
            ss = []
            for i in range(len(s)):
                ss.append(b[s[i]])
            return "".join(ss)
        @lru_cache
        def S(i):
            if i == 1:
                return "0"
            return S(i-1) + "1" + invert(S(i-1))[::-1]
        return S(n)[k-1]