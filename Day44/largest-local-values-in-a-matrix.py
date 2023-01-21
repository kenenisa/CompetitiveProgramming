class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def max3x3(r,c):
            mx = 0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    mx = max(mx,grid[i][j])
            return mx
        result = []
        for i in range(n-2):
            r = []
            for j in range(n-2):
                r.append(max3x3(i,j))
            result.append(r)
        return result
