class Node:
    def __init__(self,val: int,node=None):
        self.val = val
        self.next = node
class MyLinkedList:
    def __init__(self):
        self.start = self.end = None
        self.size = 0
    # def firstElement(self,val:int):
    #     node = Node(val)
    #     self.start = self.end = node
    
    def get(self, index: int) -> int:
        i=0
        temp = self.start
        while temp:
            if i == index:
                return temp.val
            i += 1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.start:
            self.start = self.end = node
        else:
            node.next = self.start
            self.start = node
        self.size += 1
    def addAtTail(self, val: int) -> None:
        
        node = Node(val)
        if not self.start:
            self.start = self.end = node
        else:
            self.end.next = node
            self.end = node
        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            if index == 0:
                self.addAtHead(val)
            elif index == self.size:
                self.addAtTail(val)
            else:
                temp = self.start
                # prev = self.start
                for i in range(1,index):
                    # prev = temp
                    temp = temp.next
                temp.next = Node(val, temp.next)
                self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if index == 0:
                self.start = self.end = self.start.next
            else:
                i = 1
                temp = self.start
                tempHead = tempTail = Node(temp.val)
                temp = temp.next
                while temp:
                    if i != index:
                        n = Node(temp.val)
                        tempTail.next = n
                        tempTail = n
                    i += 1
                    if not temp.next:
                        self.end = tempTail
                    temp = temp.next
                self.start = tempHead
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)