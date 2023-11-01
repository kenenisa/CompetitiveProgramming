class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        n = len(heights)
        m = len(heights[0])
        def bfs(i,j):
            q = deque([(i,j)])
            visited =set([(i,j)])
            pacific = False
            atlantic = False
            while q:
                if pacific and atlantic:
                    return True
                x,y = q.popleft()
                if 0 in (x,y):
                    pacific = True
                if x == n-1 or y == m-1:
                    atlantic = True
                for dx,dy in direction:
                    ux = x + dx     
                    uy = y + dy
                    if 0 <= ux < n and 0 <= uy < m and (ux,uy) not in visited and heights[x][y] >= heights[ux][uy]:
                        q.append((ux,uy))
                        visited.add((ux,uy))
            return pacific and atlantic
        result = []
        for i in range(n):
            for j in range(m):
                if (0 in (i,j) and (i == n-1 or j == m-1)) or bfs(i,j):
                    result.append((i,j))
        return result
