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
    def equationsPossible(self, equations: List[str]) -> bool:
        u = UnionFind(26)
        A = lambda x: ord(x) - ord('a')
        for eq in equations:
            if eq[1] == "=":
                u.union(A(eq[0]),A(eq[3]))
        for eq in equations:
             if eq[1] == "!":
                a = u.find(A(eq[0]))
                b = u.find(A(eq[3]))
                if a == b:
                    return False
        return True

        
