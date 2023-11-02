def run(s):
    if s[0] == '0':
        return 0

    result = []
    df = {}

    def backtrack(a, b):
        if len(b) == 0:
            result.append(a)
            return        
        if b[0] != '0':
            # one
            backtrack(a + chr(64 + int(b[0])), b[1:])
            # two
            two = int(b[:2])
            if two <= 26:
                backtrack(a + chr(64 + two), b[2:])
    backtrack('', s)
    print(result)
    return len(result)
run(input())

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
