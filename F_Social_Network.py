from collections import defaultdict,Counter
# n,d=list(map(int,input().split()))
# def recur(x):
#     if p[x] < 0: return x
#     return recur(p[x])
# p = [-1] * (n + 1)
# c = 0
# for _ in range(d):
#     x,y=list(map(int,input().split()))
#     parentX = recur(x)
#     parentY = recur(y)
#     if parentX != parentY:
#         p[parentX] += p[parentY]
#         p[parentY] = parentX
#     else:
#         c += 1
#     print(p)
#     result = 0
#     a = sorted(p)
#     for i in range(c + 1):
#         if a[i] < 0:
#             result += a[i]*-1
#     print(result  - 1)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = [1 for _ in range(size)]

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
                self.count[r1] += self.count[r2] 
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.count[r2] += self.count[r1] 
                self.root[r1] = r2
            else:
                self.count[r2] += self.count[r1] 
                self.root[r2] = r1
                self.rank[r1] += 1

n,d=list(map(int,input().split()))

c = 0
graph = UnionFind(n+1)

children = defaultdict(int)

for _ in range(d):
    u,v=list(map(int,input().split()))
    r1 = graph.find(u)
    r2 = graph.find(v)
    
    if r1 != r2:
        graph.union(u,v)
    else:
        c+=1
    result = 0
    print(graph.root)
    print(graph.rank)
    print(graph.count)
    a = sorted(Counter(graph.root).values(),reverse=True)
    # print(a)
    for i in range(c+1):
        if a[i] > 1:
            result += a[i]
    print(result - 1)

    




    
[-1, -2, 1, -1, -1, -1, -1, -1]
1
[-1, -2, 1, -2, 3, -1, -1, -1]
1
[-1, -4, 1, 1, 3, -1, -1, -1]
3
[-1, -4, 1, 1, 3, -1, 7, -2]
3
[-1, -4, 1, 1, 3, 7, 7, -3]
3
[-1, -7, 1, 1, 3, 7, 7, 1]
6

[0, 1, 1, 3, 4, 5, 6, 7]
[1, 2, 1, 1, 1, 1, 1, 1]
1
[0, 1, 1, 3, 3, 5, 6, 7]
[1, 2, 1, 2, 1, 1, 1, 1]
1
[0, 1, 1, 1, 3, 5, 6, 7]
[1, 3, 1, 2, 1, 1, 1, 1]
2
[0, 1, 1, 1, 3, 5, 7, 7]
[1, 3, 1, 2, 1, 1, 1, 2]
2
[0, 1, 1, 1, 3, 7, 7, 7]
[1, 3, 1, 2, 1, 1, 1, 2]
2
[0, 1, 1, 1, 3, 7, 7, 1]
[1, 3, 1, 2, 1, 1, 1, 2]
3