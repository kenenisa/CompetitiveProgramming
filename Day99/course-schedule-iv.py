class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        df = defaultdict(list)
        for u,v in prerequisites:
            df[u].append(v)
        def dfs(x,y):
            stack = [x]
            visited = set()
            while stack:
                node = stack.pop()
                if node == y:
                    return True
                if node not in visited:
                    visited.add(node)
                    for u in df[node]:
                        stack.append(u)
            return False
        return [dfs(u,v) for u,v in queries]
