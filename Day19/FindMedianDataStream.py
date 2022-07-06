class MedianFinder:

    def __init__(self):
        self.mx = []
        self.mi = []

    def addNum(self, num: int) -> None:
        if len(self.mx) == 0 or num <= -1*self.mx[0]:
            heapq.heappush(self.mx,-1*num)
        else:
            heapq.heappush(self.mi,num)
        if len(self.mx) - len(self.mi) > 1:
            heapq.heappush(self.mi,-1*heapq.heappop(self.mx))
        elif len(self.mi) - len(self.mx) > 0:
            heapq.heappush(self.mx,-1*heapq.heappop(self.mi))

    def findMedian(self) -> float:
        if len(self.mx) > len(self.mi):
            return -1*self.mx[0]
        else:
            return (-1*self.mx[0] + self.mi[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
