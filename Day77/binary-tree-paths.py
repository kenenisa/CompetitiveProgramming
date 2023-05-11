# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        def path(node,parents):
            if not node: return 
            parents.append(str(node.val))
            if not node.left and not node.right:
                results.append("->".join(parents))
                return
            path(node.left,parents[::])
            path(node.right,parents[::])
        path(root,[])
        return results

            