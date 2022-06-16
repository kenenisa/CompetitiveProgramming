class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.el = nums
        self.k = k
        heapq.heapify(self.el)
        while len(self.el) > self.k:
            heapq.heappop(self.el) 

    def add(self, val: int) -> int:
        n = len(self.el)
        if n < self.k:
            heapq.heappush(self.el, val)
        elif val > self.el[0]:
            heapq.heapreplace(self.el, val)
        return self.el[0]