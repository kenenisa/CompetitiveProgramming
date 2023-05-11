class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        cols = []
        for j in range(n): #columns 
            cols.append(tuple([grid[i][j] for i in range(n)]))

        for i in range(n):
            row = tuple(grid[i])
            for j in range(n):
                col = cols[j]
                if row == col:
                    result += 1
        return result
            