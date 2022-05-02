# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        x = length
        temp = head
        newHead = newTail = ListNode(-1)
        
        while x > 0:
            x -= 1
            if x + 1 != n:
                nh = ListNode(temp.val)
                newTail.next = nh
                newTail = nh
            temp = temp.next
        return newHead.next