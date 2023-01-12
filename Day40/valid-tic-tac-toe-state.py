# 93% time
class Solution:
    def findWinner(self,s:str,board: List[str]) -> bool:
            win = [s] * 3
            d1 = []
            d2 = []
            for i in range(3):
                #row
                if board[i] == "".join(win):
                    return True
                #cols
                col = []
                for j in range(3):
                    col.append(board[j][i])
                if col == win:
                    return True
                #diiagonal
                d1.append(board[i][i])
                d2.append(board[2 - i][i])
            if win == d1 or win == d2:
                return True
            return False
    def validTicTacToe(self, board: List[str]) -> bool:
        # for i in range(3):
        #     board[i] = [i for i in board[i]]
        xCount = 0
        oCount = 0
        xWin = False
        oWin = False
        for b in board:
            for l in b:
                if l == 'X':
                    xCount += 1
                elif l == 'O':
                    oCount += 1
        #check for turn by turn play
        if oCount > xCount or not 0 <= xCount - oCount < 2:
            return False
        #find if x won
        xWin = self.findWinner('X',board)
        if xWin and xCount - oCount != 1:
            return False
        #find if o won
        oWin = self.findWinner('O',board)
        if oWin and xCount - oCount != 0:
            return False
        #both can't win
        if xWin and oWin:
            return False
        return True