class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        df = defaultdict(int)
        for i in words:
            df[i] += 1
        heap = []
        for key, val in df.items():
            heapq.heappush(heap, (-val, key))

        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result