class MyCircularDeque:

    def __init__(self, k: int):
        self.stack = []
        self.k = k
        self.sl = len(self.stack)

    def insertFront(self, value: int) -> bool:
        if(self.sl < self.k):
            self.stack.append(value)
            self.sl += 1
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if(self.sl < self.k):
            self.stack = [value] + self.stack
            self.sl += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if(self.sl > 0):
            self.stack.pop()
            self.sl -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if(self.sl > 0):
            self.stack = self.stack[1:]
            self.sl -= 1
            return True
        return False

    def getFront(self) -> int:
        last = self.sl
        if(last > 0):
            return self.stack[last - 1]
        return -1

    def getRear(self) -> int:
        if(self.sl > 0):
            return self.stack[0]
        return -1

    def isEmpty(self) -> bool:
        return self.sl == 0

    def isFull(self) -> bool:
        return self.sl == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()