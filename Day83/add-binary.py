class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        a = list(map(int,a))
        b = list(map(int,b))
        n = len(a)
        m = len(b)
        k = min(n,m)
        if n > m:
            b = ([0] * (n-m)) + b
            m = n
        else:
            a = ([0] * (m-n)) + a
            n = m
        def binaryTable(x,y,c):
            tree = [
                [
                    [(0,0),(1,0)],#0
                    [(1,0),(0,1)]#1
                ],#0
                [
                    [(1,0),(0,1)],#0
                    [(0,1),(1,1)]#1
                ]#1
            ]
            return tree[x][y][c]
    
        for i in range(n):
            s,carry = binaryTable(a[n-i-1],b[m-i-1],carry)
            result = str(s) + result
        if carry == 1:
            result = str(carry) + result
        return result

