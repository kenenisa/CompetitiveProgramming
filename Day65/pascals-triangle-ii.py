class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        row = self.getRow(rowIndex-1)
        result = [1]
        for i in range(1,len(row)):
            result.append(row[i-1] + row[i])
        result.append(1)
        return result
        