# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur(node, left, right):
            if not node: return True
            if  left >=  node.val or node.val  >= right:
                return False
            return recur(node.left, left, node.val) and recur(node.right, node.val, right)

        return recur(root, float("-inf"), float("inf"))

        