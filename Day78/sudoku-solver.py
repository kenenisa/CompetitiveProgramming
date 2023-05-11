class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        by3 = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    b = int(board[i][j])
                    rows[i].add(b)
                    cols[j].add(b)
                    by3[((i//3)*3) + j//3].add(b)
        def nextCell(i,j):
            if j == 8:
                i += 1
                j = 0
                return [i,j]
            return [i,j+1]
        end = False    
        def backtrack(i,j):
            nonlocal end
            if i >= 9: # end has been reached
                end = True
                return 
            if board[i][j] != ".":
                backtrack(*nextCell(i,j))
            else:
                for val in range(1,10):
                    if val not in rows[i] and val not in cols[j] and val not in by3[((i//3)*3) + j//3]:
                        rows[i].add(val) 
                        cols[j].add(val) 
                        by3[((i//3)*3) + j//3].add(val) 
                        board[i][j] = str(val)
                        backtrack(*nextCell(i,j))
                        if not end:
                            rows[i].remove(val) 
                            cols[j].remove(val) 
                            by3[((i//3)*3) + j//3].remove(val) 
                            board[i][j] = "."
        backtrack(0,0)
            