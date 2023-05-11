class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col,by3 = [[set() for _ in range(9)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                b = board[i][j]
                if b is not ".":
                    if b in row[i] or b in col[j] or b in by3[((i//3)*3) + j//3]:
                        return False
                    row[i].add(b)
                    col[j].add(b)
                    by3[((i//3)*3) + j//3].add(b)
        return True