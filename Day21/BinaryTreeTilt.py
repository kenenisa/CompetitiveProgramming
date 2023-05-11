# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        global total
        total = 0
        
        def dfs(node):
            global total
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                
                sub = left[0] + right[0] + node.val
                tilt = left[1] + right[1] + abs(left[0] - right[0])
                return [sub,tilt]
            return [0,0] 
        return dfs(root)[1]
                
