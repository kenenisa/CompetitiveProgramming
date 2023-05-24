class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            # n = len(q)
            for _ in range(len(q)):
                i,j = q.popleft()
                
                for di,dj in directions:
                    ni = i + di
                    nj = j + dj
                    
                    if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append([ni,nj])
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1
                