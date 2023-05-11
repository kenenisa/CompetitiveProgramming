class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        result = []
        up = True
        r = 0
        c = 0
        while len(result) < n * m:
            while up and c < m and r > -1:
                result.append(mat[r][c])
                c += 1
                r -= 1
            while not up and r < n and c > -1:
                result.append(mat[r][c])
                c -= 1
                r += 1
            # adjust overflow 
            if up:
                r += 2 if c == m else 1
                c -= 1 if c == m else 0
                up = not up
            else: 
                c += 2 if r == n else 1
                r -= 1 if r == n else 0
                up = not up
        return result
# from collections import defaultdict
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# n = len(mat)
# m = len(mat[0])
# result = []
# up = False
# result.append(mat[0][0])
# r = 0
# c = 1
# df = defaultdict(bool)
# while not (r == n - 1 and c == m - 1):
#     print(mat[r][c],up)
#     result.append(mat[r][c])
#     df[mat[r][c]] = True
#     # print(result)
#     if not up and r < n - 1:
#         r += 1
#     elif up and  r > 0:
#         r -= 1
#     elif r == 0:
#         r += 1
#     else:
#         up = not up
#     # col
#     if up and c < n - 1:
#         c += 1 
#     elif not up and c > 0:
#         c -= 1
#     else:
#         up = not up
#     # 
# result.append(mat[n-1][m-1])
# print(result)
#     # if mat[r][c] in df:
#     #     break