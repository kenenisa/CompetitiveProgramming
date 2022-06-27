# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         al = []
#         start = end = ListNode(-1)
#         for i in lists:
#             while i:
#                 al.append(i.val)
#                 i = i.next
#         for j in sorted(al):
#             n = ListNode(j)
#             end.next = n 
#             end = n
#         return start.next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        start = end = ListNode(-1)
        for i in lists:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next
        while heap:
            n = ListNode(heapq.heappop(heap))
            end.next = n
            end = n
        return start.next