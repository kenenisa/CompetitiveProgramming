class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        edges = [0]*n
        df = defaultdict(list)
        for u,v in prerequisites:
            df[v].append(u)
            edges[u] += 1
        done = set()
        def findZeros():
            r = []
            for i in range(n):
                if i not in done and edges[i] == 0:
                    r.append(i)
            return r
        zeros = findZeros()
        while zeros:
            zeros = findZeros()
            for z in zeros:
                for u in df[z]:
                    edges[u] -= 1
                done.add(z)
        return sum(edges) == 0

