# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        global total
        total = 0
        def dfs(node,p):
            global total
            if node:
                if p[0]: total += node.val if p[0] % 2 == 0 else 0
                dfs(node.left,[p[1],node.val])
                dfs(node.right,[p[1],node.val])
        dfs(root,[None,None])
        return total
