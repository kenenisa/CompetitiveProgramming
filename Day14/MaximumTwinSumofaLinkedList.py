# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        mx = 0
        half = []
        for i in range(n):
            if i <= (n/2) -1:
                half.append(head.val)
            else:
                mx = max(mx,head.val + half[n-(i+1)])
            head = head.next
        return mx