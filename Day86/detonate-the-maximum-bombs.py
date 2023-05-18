class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        df = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i != j:
                    ax,ay,ar = bombs[i]
                    bx,by,br = bombs[j]
                    d = sqrt(((bx - ax) ** 2) + ((by-ay)**2))
                    if d <= ar:
                        df[i].append(j)
        self.result = 0
        def dfs(item,detonated):
            if detonated[item] == 1: return 
            detonated[item] = 1
            self.result = max(self.result,sum(detonated))
            for d in df[item]:
                dfs(d,detonated)

        for i in range(n):
            dfs(i,[0]*n)
        return self.result


                    