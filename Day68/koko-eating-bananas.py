class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = 0
        while left <= right:
            mid = (right + left) // 2
            s = 0
            for p in piles:
                s += ceil(p/mid)
            if s > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result