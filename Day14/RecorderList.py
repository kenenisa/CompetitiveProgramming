# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp1 = head
        temp2 = head.next
        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
        nxt=temp1.next
        prv = temp1.next = None

        while nxt:
            temp = nxt.next
            nxt.next = prv
            prv = nxt
            nxt = temp

        first = head
        nxt = prv
        while nxt:
            temp1 = first.next
            temp2 = nxt.next
            first.next = nxt
            nxt.next = temp1
            first = temp1
            nxt = temp2