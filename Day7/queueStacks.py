class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = self.stack[0]
        self.stack = self.stack[1:]
        return temp
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return False if len(self.stack) > 0 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()