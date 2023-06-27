class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        ex,ey = entrance
        def isExit(x,y):
            return (x == 0 or y == 0 or x == n - 1 or y == m - 1) and ((x,y) != (ex,ey))
        q = deque([(ex,ey,0)])
        visited = set([(ex,ey)])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while q:
            i,j,d = q.popleft()
            if isExit(i,j):
                return d
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and maze[x][y] == '.' and (x,y) not in visited:
                    q.append((x,y,d+1))
                    visited.add((x,y))
        return -1