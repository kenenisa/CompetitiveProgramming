# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #get length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        x = length
        temp = head
        while x > -(length//-2):
            x -= 1
            temp = temp.next
        return temp