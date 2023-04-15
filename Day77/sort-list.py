# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        ary = []
        if node:
            while node.next:
                ary.append(node.val)
                node = node.next
            ary.append(node.val)
            node = head
            ary.sort()
            for i in ary:
                node.val = i
                node = node.next
        return head
#         node = head
#         def srted():
#             nd = head
#             if  not nd:
#                 return True
#             while nd.next:
#                 if nd.val > nd.next.val:
#                     return False
#                 nd = nd.next
#             return True

#         while not srted():
#             while node.next:
#                 if(node.val > node.next.val):
#                     temp = node.val
#                     node.val = node.next.val
#                     node.next.val = temp
#                 node = node.next
#             node = head
#         return head
        # while node.next:
        #     count += 1
        #     node = node.next
        # for i in range(count):
            