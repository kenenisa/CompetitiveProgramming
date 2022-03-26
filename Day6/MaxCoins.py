class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        pl = len(piles)
        result = 0
        for i in range(int(pl/3),pl,2):
            result += piles[i]
        return result
