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
        if x != y:
            if self.size[x] > self.size[y]:
                x,y=y,x
            self.head[x] = y
            self.size[y] += self.size[x]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        u = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    x,y = stones[i]
                    w,z = stones[j]
                    if x == w or y == z:
                        u.union(i,j)
        roots = set()
        for i in range(n):
            roots.add(u.find(i))
        result = 0
        for r in roots:
            result += (u.size[r] - 1)
        return result
