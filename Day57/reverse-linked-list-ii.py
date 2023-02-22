# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left:
            return head
       
        first = firstEnd= None
        middle = middleEnd = None
        last = lastEnd = None
        i = 1

        while head:
            n =ListNode(head.val)
            if i < left:
                if not first:
                    first = firstEnd = n
                else:
                    firstEnd.next = n
                    firstEnd = n
            elif i > right:
                if not last:
                    last = lastEnd = n
                else:
                    lastEnd.next = n
                    lastEnd = n
            elif i >= left or i <= right:
                if not middle:
                    middle = middleEnd = n
                else:
                    temp = n
                    temp.next = middle
                    middle = temp
            i += 1
            head = head.next
            
        middleEnd.next = last
        if first:
            firstEnd.next = middle
            return first
        return middle
        