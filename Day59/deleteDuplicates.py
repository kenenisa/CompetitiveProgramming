# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = end = ListNode('start')
        removing = ''
        while head:
            # print(start)
            if head.val != end.val and head.val != removing:
                n = ListNode(head.val)
                end.next = n
                end = n
            else:
                removing = head.val
                # print(head.val)
                if end.val != 'start' and end.val == head.val:
                    if start == None or start.next == None:
                        start = None
                    else:
                        prev = start
                        while(prev.next.next):
                            prev = prev.next
                        prev.next = None
                        end = prev
                
            head = head.next
        return start.next
