# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = end = ListNode(head.val)
        head = head.next
        switch = True
        while head:
            tl = ListNode(head.val)
            tl.next = start
            start = tl
            head = head.next
        return start