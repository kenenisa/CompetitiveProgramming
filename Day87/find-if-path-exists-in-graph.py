class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        df = defaultdict(list)
        for u,v in edges:
            df[u].append(v)
            df[v].append(u)
        visited = set([source])
        q = deque([source])

        while q:
            look = q.popleft()
            for e in df[look]:
                if e == destination:
                    return True
                if e not in visited:
                    q.append(e)
                    visited.add(e)
        return False

        def dfs(look):
            if look in visited: return False
            visited.add(look)
            found = False
            for e in df[look]:
                if e == destination:
                    return True
                found = found or dfs(e)
            return found
        return dfs(source)
            
