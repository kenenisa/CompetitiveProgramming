class Solution:
    def updateBoard(self, matrix: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m = len(matrix)
        n =  len(matrix[0])
        
        if not matrix or not matrix[0]:
            return matrix
        if matrix[click[0]][click[1]] == 'M':
            matrix[click[0]][click[1]] = 'X'
            return matrix
        
        def check(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or matrix[r][c] != 'M':
                return 0
            return 1
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or matrix[r][c] != 'E':
                return 0
            mines = 0
            d = [[1, 0], [1, -1], [-1, -1],[-1, 0 ], [-1, 1], [0, 1], [1, 1],[0, -1]]
            for mr, mc in d:
                mines += check(r + mr, c + mc)   
            matrix[r][c] = str(mines) if mines else 'B'
            if mines:
                return 0     
            for mr, mc in d:
                dfs(r + mr, c + mc)
        dfs(click[0], click[1])
        return matrix 
