class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        onesRow = [0] * n
        onesCol = [0] * m
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    onesCol[j] += 1
                    onesRow[i] += 1
        for i in range(n):
            for j in range(m):
                result[i][j] = onesRow[i] + onesCol[j] - (n - onesRow[i]) - (m - onesCol[j])
        return result
        
                