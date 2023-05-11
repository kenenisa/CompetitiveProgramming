class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        big = []
        for i in matrix:
            big.extend(i)
        heapq.heapify(big)
        return heapq.nsmallest(k,big)[-1]