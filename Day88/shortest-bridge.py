class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
        # color 
        sx = -1
        for i in range(n):
            if sx > -1: break
            for j in range(m):
                if grid[i][j] == 1:
                    sx = i
                    sy = j
                    break
        color_q = deque([(sx,sy)])
        color_visited = set([(sx,sy)])

        while color_q:
            ci,cj = color_q.popleft()
            grid[ci][cj] = 2
            for dx,dy in directions:
                x = ci + dx
                y = cj + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and (x,y) not in color_visited:
                    color_q.append((x,y))
                    color_visited.add((x,y))

        q = deque()
        visited = set()
        result = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,-1))
                    visited.add((i,j))
        while q:
            ci,cj,d = q.popleft()
            if grid[ci][cj] == 1:
                result = min(result,d)
            else:
                for dx,dy in directions:
                    x = ci + dx
                    y = cj + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] != 2 and (x,y) not in visited:
                        q.append((x,y,d+1))
                        visited.add((x,y))
        return result

            