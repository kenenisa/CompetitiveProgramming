class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        n = len(mat)
        m = len(mat[0])

        result = [[0 for _ in range(m)] for _ in range(n)]
        visited = set()
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                   q.append((i,j,0))
                   visited.add((i,j))
        while q:
            ci,cj,d = q.popleft()
            result[ci][cj] = d
            for dx,dy in directions:
                x = ci + dx
                y = cj + dy
                if 0 <= x < n and 0 <= y < m and (x,y) not in visited:
                    q.append((x,y,d+1))
                    visited.add((x,y))

        return result
                     