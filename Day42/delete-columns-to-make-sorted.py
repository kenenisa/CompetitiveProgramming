class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cols = []
        for j in range(m):
            col = []
            for i in range(n):
                col.append(strs[i][j])
            cols.append(col)
        result = 0
        for c in cols:
            if c != sorted(c):
                result += 1
        return result