# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recur(node):
            nonlocal result
            if not node: return [0,0]
            left = recur(node.left)
            right = recur(node.right)
            count = 1+right[1]+left[1]
            total = node.val + left[0] + right[0]
            if node.val == total//count:
                result += 1
            return [total,count]
        recur(root)
        return result