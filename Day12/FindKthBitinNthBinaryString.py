class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bits):
            keys = {"0":"1","1":"0"}
            def inv(u):
                return keys[u]
            return "".join(list(map(inv,bits)))
        def s(bits,n):
            if n == 1 or len(bits) >= k:
                return bits
            n -= 1;
            return s(bits + "1" + (invert(bits)[::-1]),n)
        return s("0",n)[k-1]