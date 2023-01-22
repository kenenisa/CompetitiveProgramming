class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        corners = [[0,0],[0,n-1],[n-1,n-1],[n-1,0]]
        for i in range(n//2):
            rot = [c[:] for c in corners]
            for j in range(n-1-(i*2)):
                # prepare corners
                first = matrix[rot[0][0]][rot[0][1]]
                second = matrix[rot[1][0]][rot[1][1]]
                third = matrix[rot[2][0]][rot[2][1]]
                fourth = matrix[rot[3][0]][rot[3][1]]
                # rotate
                matrix[rot[1][0]][rot[1][1]] = first
                matrix[rot[2][0]][rot[2][1]] = second
                matrix[rot[3][0]][rot[3][1]] = third
                matrix[rot[0][0]][rot[0][1]] = fourth
                # next to be rotated
                rot[0][1] += 1
                rot[1][0] += 1
                rot[2][1] -= 1
                rot[3][0] -= 1
            # move the corners inside
            corners[0][0] += 1
            corners[0][1] += 1
            corners[1][0] += 1
            corners[1][1] -= 1
            corners[2][0] -= 1
            corners[2][1] -= 1
            corners[3][0] -= 1
            corners[3][1] += 1