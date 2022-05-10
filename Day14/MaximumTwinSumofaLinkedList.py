class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.access = 0
        self.data = {}
    def get(self, key: int) -> int:
        if self.data.get(key):
            self.data[key][1] = self.access
            self.access += 1
            return self.data[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.data.get(key):
            self.data[key][0] = value 
            self.data[key][1] = self.access
        else:
            if self.capacity <= 0:
                mi = self.access
                remove = ''
                for x in self.data:
                    if mi > self.data[x][1]:
                        remove = x
                        mi = self.data[x][1]
                del self.data[remove]
            self.data[key] = [value,self.access]
            self.capacity -= 1
        self.access += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)