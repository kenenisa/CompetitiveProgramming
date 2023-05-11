# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode('')
        start.next = head

        while head.next:
            node = head.next
            temp = start
            while temp.next != node and temp.next.val <= node.val:
                temp = temp.next

            if temp.next == node:
                head = head.next
            else:
                head.next = node.next
                node.next = temp.next
                temp.next = node

        return start.next