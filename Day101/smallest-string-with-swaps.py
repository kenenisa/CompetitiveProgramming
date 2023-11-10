
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


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # bfs
        # df = defaultdict(list)
        # for p in pairs:
        #     u,v = p
        #     df[u].append(v)
        #     df[v].append(u)
        
        # visited = set()
        # n = len(s)
        # s = list(s)
        # def bfs(start):
        #     q = deque([start])
        #     visited.add(start)
        #     connected = []
        #     while q:
        #         node = q.popleft()
        #         connected.append(node)
        #         for v in df[node]:
        #             if v not in visited:
        #                 q.append(v)
        #                 visited.add(v)
        #     letter = [s[i] for i in connected]
        #     connected.sort()
        #     letter.sort()
        #     for i in range(len(connected)):
        #         s[connected[i]] = letter[i]

        # union find
        n = len(s)
        s = list(s)
        connected = defaultdict(list) 
        graph = UnionFind(n)
        for u,v in pairs:
            graph.union(u,v)
        for i in range(n):
            root = graph.find(i)
            connected[root].append(i)
        for c in connected.values():
            letter = [s[i] for i in c]
            c.sort()
            letter.sort()
            for i in range(len(c)):
                s[c[i]] = letter[i]
        return "".join(s)



