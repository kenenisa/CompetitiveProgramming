# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        result = []
        while q:
            result.append([])
            for i in range(len(q)):
                elem = q.popleft()
                if elem:
                    result[-1].append(elem.val)
                    if elem.left:
                        q.append(elem.left)
                    if elem.right:
                        q.append(elem.right)
                
        return result