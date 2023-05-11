# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        startOdd = endOdd = None
        startEven = endEven = None
        if not head or not head.next:
            return head
        if head.next and not head.next.next:
            return head 
        odd = head
        while odd and odd.next:
            if startOdd:
                n = ListNode(odd.val)
                endOdd.next = n
                endOdd = n
            else:
                startOdd = endOdd = ListNode(odd.val)
            odd = odd.next.next
        if odd:
            n = ListNode(odd.val)
            endOdd.next = n
            endOdd = n
        even = head.next
        while even and even.next:
            if startEven:
                n = ListNode(even.val)
                endEven.next = n
                endEven = n
            else:
                startEven = endEven = ListNode(even.val)
            even = even.next.next
        if even:
            n = ListNode(even.val)
            endEven.next = n
            endEven = n
        endOdd.next = startEven
        return startOdd
