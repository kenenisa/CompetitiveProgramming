class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        df = defaultdict(list)
        colors = [0] * n
        valid = True
        for u,v in dislikes:
            df[u].append(v)
            df[v].append(u)
        def switchColor(c):
            if c == 1:
                return 2
            return 1
        def dfs(item, color):
            nonlocal valid
            if colors[item-1] != 0: return
            colors[item-1] = color
            for v in df[item]:
                if colors[v-1] == color:
                    valid = False
                dfs(v,switchColor(color))

        for i in range(1, n+1):
            dfs(i,1)
        return valid
