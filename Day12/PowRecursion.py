class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(b, e):
            if(e == 0):
                    return 1
            if(e < 0):
                return pow(1/b,n*-1)
            half = pow(b, int(e/2))
            if(e % 2):
                return half * half * b
            return half * half
        return pow(x,n)