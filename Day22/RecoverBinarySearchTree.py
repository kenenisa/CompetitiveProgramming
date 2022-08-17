# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversed=[]
        def traversal(node):
            if node:
                traversal(node.left)
                traversed.append(node.val)
                traversal(node.right)
        traversal(root)
        n = len(traversed)
        for i in range(n):
            for j in range(n-1,i,-1):
                if traversed[i] > traversed[j]:
                    x = traversed[j]
                    y = traversed[i]
                    traversed[i] = x
                    traversed[j] = y
        def dfs(node):
            if node:
                dfs(node.left)
                if node.val==x:
                    node.val=y
                elif node.val==y:
                    node.val=x
                dfs(node.right)
        dfs(root)
