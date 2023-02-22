# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start = end = None
        great = []
        while head:
            if head.val < x:
                if not start:
                    start = end = ListNode(head.val)
                else:
                    n = ListNode(head.val)
                    end.next = n
                    end = n
            else:
                great.append(head.val)
            head = head.next
        for g in great:
            if not start:
                start = end = ListNode(g)
            else:
                n = ListNode(g)
                end.next = n
                end = n
        return start