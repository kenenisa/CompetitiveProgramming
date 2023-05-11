class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # if not grid:
        #     return 0
        def validate(x, y):
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                return False
            if (x,y) in visited:
                return False
            return True

            
        heap = [ (grid[0][0],0,0) ]
        time = 0
        n = len(grid)
        visited = {(0,0)}
        
        dc = [(-1,0),(1,0),(0,1),(0,-1)]
        while heap:
            elevation, i, j = heapq.heappop(heap)
            time = max(time, elevation)

            if i == j and j == n-1:
                return time
            for dx, dy in dc:
                nx = i + dx
                ny = j + dy
                if validate(nx, ny):
                    heapq.heappush(heap, (grid[nx][ny],nx,ny))
                    visited.add((nx,ny))
                    
        
            
