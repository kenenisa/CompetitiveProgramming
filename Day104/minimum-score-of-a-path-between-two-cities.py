class UnionFind: # i made this :)
    def __init__(self,n):
        self.head = []
        self.size = []      
        for i in range(n+1):
            self.head.append(i)
            self.size.append(1)
    def find(self,a):
        while(self.head[a] != a):
            a = self.head[a]
        return a
    def union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if self.size[x] > self.size[y]:
            x,y=y,x
        self.head[x] = y
        self.size[y] += self.size[x]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        u = UnionFind(n)
        for w,v,d in roads:
            u.union(w,v)
        one  = u.find(1)
        result = float('inf')
        for w,v,d in roads:
            wv =  u.find(w)
            if wv == one:
                result = min(result, d)
        return result
