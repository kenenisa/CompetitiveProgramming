class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1

n,m1,m2=list(map(int,input().split()))

mocha = UnionFind(n+1)
diana = UnionFind(n+1)

for _ in range(m1):
    u,v=list(map(int,input().split()))
    mocha.union(u,v)
for _ in range(m2):
    u,v=list(map(int,input().split()))
    diana.union(u,v)

result = []

for i in range(1,n+1):
    for j in range(i+1,n+1):
        r1 = mocha.find(i)
        r2 = mocha.find(j)
        if r1 != r2:
            d1 = diana.find(i)
            d2 = diana.find(j)
            
            if d1 != d2:
                result.append((i,j))
                mocha.union(i,j)
                diana.union(i,j)
print(len(result))
for u,v in result:
    print(u,v)
