class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        # print(stones)
        def abs(val):
            if(val < 0):
                val = val * -1
            return val
        while len(stones) > 1:
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            if x - y == 0:
                continue
            stones.append(abs(x-y))              
            heapq._heapify_max(stones)

        return stones[0] if len(stones) > 0 else 0