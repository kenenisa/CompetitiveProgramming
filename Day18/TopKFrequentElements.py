# from collections import defaultdict
# import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        df = defaultdict(int)
        for i in nums:
            df[i] += 1
        heap = []
        for key, val in df.items():
            heapq.heappush(heap, (-val, key))

        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result