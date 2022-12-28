from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = defaultdict(int)
        tt = defaultdict(int)
        for i in s:
            ss[i] += 1
        for i in t:
            tt[i] += 1
        
        for i,x in tt.items():
            if x != ss[i]:
                return i