class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result =1
        k -= 1
        while k > 0:
            s = 0
            j = result
            x = j + 1
            while j <= n:
                s += min(n-j+1,x - j)
                j *= 10
                x *= 10
            if k >= s:
                result += 1
                k -= s
            else:
                result *= 10
                k-=1
        return result
