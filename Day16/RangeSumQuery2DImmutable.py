class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.prefix = []
        for i in self.matrix:
            ary = [0]
            for j in i:
                ary.append(ary[-1] + j)
            self.prefix.append(ary)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1,row2+1):
            total += self.prefix[i][col2 + 1] - self.prefix[i][col1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)