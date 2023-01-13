class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)  # row
        n = len(matrix[0])  # column
        first_row = (0, 0)  # step 1
        last_column = (0, n-1)  # step 2
        last_row = (m-1, n-1)  # step 3
        first_column = (m-1, 0)  # step 4
        result = []
        while len(result) < m*n:
            for fr in range(first_row[1], last_column[1] + 1):
                result.append(matrix[first_row[1]][fr])
            first_row = (first_row[0]+1, first_row[1]+1)
            if m > 1:
                #last column
                for lc in range(last_column[0] + 1, last_row[0] + 1):
                    result.append(matrix[lc][last_column[1]])

                last_column = (last_column[0]+1, last_column[1]-1)
            if first_row[0] <= last_row[0]:
                #last row
                for lr in range(last_row[1] - 1, first_column[1] - 1, -1):
                    result.append(matrix[last_row[0]][lr])

                last_row = (last_row[0]-1, last_row[1]-1)
            if first_column[1] <= last_column[1]:
                #first column
                for fc in range(first_column[0] - 1, first_row[0] - 1, -1):
                    result.append(matrix[fc][first_column[1]])
                first_column = (first_column[0]-1, first_column[1]+1)
        return result