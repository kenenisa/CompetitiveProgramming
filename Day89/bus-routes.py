class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        df = defaultdict(list)
        buses = defaultdict(list)
        dest = set()
        visited = set()
        q = deque()
        for i in range(len(routes)):
            for r in routes[i]:
                buses[r].append(i)
                if r == source:
                    q.append((i,1))
                    visited.add(i)
                if r == target:
                    dest.add(i)
        
        for b in buses.values():
            if len(b) > 1:
                for i in range(len(b)-1):
                    u = b[i]
                    v = b[i+1]
                    df[u].append(v)
                    df[v].append(u)
        while q:
            u,d = q.popleft()
            if u in dest:
                return d
            else:
                for v in df[u]:
                    if v not in visited:
                        q.append((v,d+1))
                        visited.add(v)
        return -1
