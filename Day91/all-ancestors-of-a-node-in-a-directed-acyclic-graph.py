class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        df = defaultdict(defaultdict)
        deg = defaultdict(int)
        for u, v in edges:
            df[u][v]=None
            deg[v]+=1
        q = deque()
        for u in range(n):
            if u not in deg:
                q.append(u)
        result = [set() for _ in range(n)]
        while q:
            u = q.popleft()
            for v in df[u]:
                deg[v]-=1
                if deg[v]==0:
                    q.append(v)
                result[v].update(result[u] | {u})
        return [sorted(list(i)) for i in result]
