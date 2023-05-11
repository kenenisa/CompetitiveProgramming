class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(words)
        def f(s):
            al = [0] * 26
            for c in s:
                al[ord(c) - 97] += 1
            for a in al:
                if a > 0:
                    return a
        ws = []
        for w in words:
            ws.append(f(w))
        ws.sort()
        result = []
        for q in queries:
            freq = 0
            qf = f(q)
            result.append(n - bisect_right(ws,qf))
        return result
