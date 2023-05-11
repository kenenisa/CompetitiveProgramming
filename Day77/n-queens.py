class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []
        def backtrack(i, queens):
            if i >= n:
                result.append(board[::])
            else:
                for j in range(n):
                    valid = True
                    for row,col in queens:
                        if col == j:
                            valid = False
                        if abs(j - col) == abs(i - row):
                            valid = False
                        if not valid: break
                    if valid:
                        queens.append([i,j])
                        board.append("".join(['.' for _ in range(j)]) + "Q" + ("".join(['.' for _ in range(n-j-1)])))
                        backtrack(i+1,queens)
                        queens.pop()
                        board.pop()
        backtrack(0,[])
        return result