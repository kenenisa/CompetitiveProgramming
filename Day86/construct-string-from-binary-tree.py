# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:


        def dfs(node):
            s = []
            s.append(str(node.val))
            if node.left:
                s.append("(")
                s.append(dfs(node.left))
                s.append(")")
            if node.right:
                if not node.left: s.append("()")
                s.append("(")
                s.append(dfs(node.right))
                s.append(")")

            return "".join(s)
        return dfs(root)