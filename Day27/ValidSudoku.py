#best attempt: runs faster than 94.12% submissions    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = c = 9
        row = [set() for _ in range(r)]
        col = [set() for _ in range(r)]
        by3 = [set() for _ in range(r)]
        for i in range(r):
            for j in range(c):
                b = board[i][j]
                if b is not ".":
                    if b in row[i] or b in col[j] or b in by3[((i//3)*3) + j//3]:
                        return False
                    row[i].add(b)
                    col[j].add(b)
                    by3[((i//3)*3) + j//3].add(b)
        return True
                    
                
#first attempt: runs faster than 5% submissions    
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = c = 9
        #check row
        for i in range(r):
            if self.checkDuplicate(board,[i,0],[i+1,c]):
                return False
        #check column
        for j in range(c):
            if self.checkDuplicate(board,[0,j],[r,j+1]):
                return False
        #check 3x3
        for i in range(0,r,3):
            for j in range(0,c,3):
                if self.checkDuplicate(board,[i,j],[i+3,j+3]):
                    return False
        return True
  

    def checkDuplicate(self,board,start,end):
        found = set()
        for i in range(start[0],end[0]):
            for j in range(start[1],end[1]):
                b = board[i][j]
                if b in found and b is not ".":
                    return True
                found.add(b)
        return False




