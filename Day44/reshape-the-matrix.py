class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n * m != r * c:
            return mat
        flatten = []
        for row in mat:
            flatten += row
        result = []
        for col in range(0,len(flatten)-(c-1),c):
            result.append(flatten[col:col+c])
        return result