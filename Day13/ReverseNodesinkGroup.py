# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = end = ListNode('')
        while head:
            temp = head
            s = e = ListNode(head.val)
            head = head.next
            x = k
            while x > 1  and head:
                n = ListNode(head.val)
                n.next = s
                s = n
                head = head.next
                x-=1
            if x > 1:
                end.next = temp
            else:
                end.next = s
                end =e
        return start.next