class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.myPow(x, int(n/2))
        if n % 2:
            if n > 0:
                return x * half * half
            return (half * half)/x
        return half * half