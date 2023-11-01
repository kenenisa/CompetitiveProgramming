class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append((0,0,1))
        n = len(grid)
        directions = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
        visited = set([(0,0)])
        while q:
            x,y,d = q.popleft()
            if (x,y) == (n-1,n-1):
                return d
            for dx,dy in directions:
                i = x + dx
                j = y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i,j) not in visited:
                    q.append((i,j,d+1))
                    visited.add((i,j))
        return -1
