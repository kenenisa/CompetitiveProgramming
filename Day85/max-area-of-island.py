class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        mx = 0

        def dfs(r,c):
            if (not ((r,c) in visited)) and 0 <= r < m and 0 <= c < n and grid[r][c] == 1: 
                visited.add((r,c))                
                area = 1
                area += dfs(r+1,c)
                area += dfs(r-1,c)
                area += dfs(r,c+1)
                area += dfs(r,c-1)
                return area
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (not ((i,j) in visited)):
                    mx = max(mx,dfs(i,j))
        return mx
            