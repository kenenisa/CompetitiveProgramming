class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations)
        n = len(citations)

        x= 0
        for i in range(n-1,-1,-1):
            if c[i] >= x + 1:
                x += 1
            else:
                break
        return x