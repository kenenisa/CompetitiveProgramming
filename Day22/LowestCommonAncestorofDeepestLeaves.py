# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ancestor = root
        mx = -1
        def dfs(node, d):
            nonlocal ancestor, mx
            if node:
                left, ld = dfs(node.left, d + 1)
                right, rd = dfs(node.right, d + 1)
                if left and right and ld == rd:
                    if  mx <= ld:
                        mx = ld
                        ancestor = node
                    return True, max(ld, rd)
                return left or right, max(ld, rd)
            return True, d
        dfs(ancestor, 0)
        return ancestor
#         global mx
#         mx = [root,0]
#         def dfs(node,pd):
#             global mx
#             if node:
#                 if pd[1] > mx[1]:
#                     mx = pd
#                 pd = [node,pd[1]+1]
                
#                 dfs(node.left,pd)
#                 dfs(node.right,pd)
#         print(root)
#         dfs(root,mx)
#         if mx[0].left and not mx[0].right:
#             mx[0] = mx[0].left
#         if mx[0].right and not mx[0].left:
#             mx[0] = mx[0].right
#         return mx[0]
        
        
