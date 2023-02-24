# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = 0
        temp = head
        while temp:
            x += 1
            temp = temp.next
        newHead = newTail = ListNode(-1)
        while x > 0:
            x -= 1
            if x + 1 != n:
                node = ListNode(head.val)
                newTail.next = node
                newTail = node
            head = head.next
        return newHead.next