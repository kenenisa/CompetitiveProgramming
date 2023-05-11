class MinStack:

    def __init__(self):
        self.stack = []       
        self.min = 0

    def push(self, val: int) -> None:
        if(len(self.stack) == 0):
            self.min = val
        elif(val < self.min):
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if(x == self.min and len(self.stack)):
            self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min