# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = end = ListNode(-1)
        while list1 or list2:
            if not list1:
                node = ListNode(list2.val)
                end.next = node
                end = node
                list2 = list2.next
            elif not list2:
                node = ListNode(list1.val)
                end.next = node
                end = node
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    node = ListNode(list2.val)
                    end.next = node
                    end = node
                    list2 = list2.next
                else:
                    node = ListNode(list1.val)
                    end.next = node
                    end = node
                    list1 = list1.next

        return start.next