# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        forward = temp.next

        while forward:
            tmp = forward.val
            forward.val = temp.val
            temp.val = tmp

            if forward.next is None:
                break
            forward = forward.next.next
            temp = temp.next.next
        return head
            