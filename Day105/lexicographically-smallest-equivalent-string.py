class UnionFind: # i made this :)
    def __init__(self):
        self.head = {}
        for a in string.ascii_lowercase:
            self.head[a] = a
    def find(self,a):
        while(self.head[a] != a):
            a = self.head[a]
        return a
    def union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            if x > y:
                x,y=y,x
            self.head[y] = x
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        u = UnionFind()
        for i in range(len(s1)):
            u.union(s1[i],s2[i])
        result = ""
        for b in baseStr:
            result += u.find(b)
        return result
        
