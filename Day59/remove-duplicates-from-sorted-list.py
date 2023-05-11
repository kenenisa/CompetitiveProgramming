# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = end = ListNode('')
        while head:
            if end.val != head.val:
                node = ListNode(head.val)
                end.next = node
                end = node
            head = head.next
        
        return start.next
