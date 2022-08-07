class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def binarySearch(start,end,row):
        #     mid = (start+end)//2
        #     if row == -1:
        #         if end - start == 1:
        #             if matrix[start][0] <= target:
        #                 return start
        #             return end
        #         if matrix[mid][0] > target:
        #             return binarySearch(start,mid,row)
        #         return binarySearch(mid,end,row)
        #     if end - start == 1:
        #         if matrix[row][start] == target or (len(matrix[row]) > end and matrix[row][end] == target):
        #             return True
        #         return False
        #     if matrix[row][mid] > target:
        #         return binarySearch(start,mid,row)
        #     return binarySearch(mid,end,row)
        # n = len(matrix)
        # row = 0
        # if n > 1:
        #     row = binarySearch(0,n,-1)
        # return binarySearch(0,len(matrix[row]),row)
        flatten = [j for sub in matrix for j in sub]
        
        def binarySearch(start,end):
            if end - start == 1:
                if flatten[start] == target or flatten[end] == target:
                    return True
                return False
            mid = (start+end)//2
            if flatten[mid] > target:
                return binarySearch(start,mid)
            return binarySearch(mid,end)
        n = len(flatten)
        if n > 1:
            return binarySearch(0,len(flatten)-1)
        return flatten[0] == target
