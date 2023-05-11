class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        directions = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]]
        #up,down,left,right,up-left,up-right,down-left,down-right
        for direction in directions:
            i,j = king
            while 0 <= i < 8 and 0 <= j < 8:
                pos = [i,j]
                if pos in queens:
                    result.append(pos)
                    break
                i += direction[0]
                j += direction[1]
        return result
        