class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        def isMagic(r,c):
            cols = [0] * 3
            d1 = 0
            d2 = 0
            row = 0
            dist = set()
            # rows
            for i in range(r,r+3):
                s = 0
                for j in range(c,c+3):
                    g = grid[i][j]
                    if not (g in range(1,10)):
                        return False
                    dist.add(g)
                    s += g
                    cols[j-c] += g
                    if (i - r) == (j - c):
                        d1 += g
                    if (i - r) + (j - c) == 2:
                        d2 += g
                if i == r:
                    row = s
                else:
                    if row != s:
                        return False
            if len(dist) != 9:
                return False
            # cols
            if not (cols[0] == cols[1] == cols[2] == row):
                return False
            # diagonals
            if not (d1 == d2 == row):
                return False
            return True
        result = 0
        for i in range(n-2):
            for j in range(n-2):
                result += 1 if isMagic(i,j) else 0
        return result