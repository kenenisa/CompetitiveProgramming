class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        b = [a for a in b]
        for i in range(len(b)):
            if b[i] == "0":
                b[i] = "1"
            else:
                b[i] = "0"
        return int("".join(b),2)
