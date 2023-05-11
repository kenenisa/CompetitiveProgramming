class Solution:
    def getSum(self, grid: List[List[int]],startRow:int,startCol:int,endRow:int,endCol:int) -> int:
        return sum([grid[i][j] for i in range(startRow,endRow) for j in range(startCol,endCol)]) - grid[startRow + 1][startCol] - grid[startRow + 1][endCol-1]
    def maxSum(self, grid: List[List[int]]) -> int:
        mx = 0
        for i in range(len(grid) - 2):
             for j in range(len(grid[0]) - 2):
                sm = self.getSum(grid,i,j,i+3,j+3)
                mx = max(mx,sm)
        return mx