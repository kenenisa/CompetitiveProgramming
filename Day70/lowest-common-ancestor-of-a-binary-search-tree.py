# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ps = []
        qs = []
        def treverse(node,val,s):
            if not node: return 
            if node.val == val:
                s.append(node)
                return 
            if node.val > val:
                s.append(node)
                treverse(node.left,val,s)
            else:
                s.append(node)
                treverse(node.right,val,s)
        treverse(root,p.val,ps)
        treverse(root,q.val,qs)
        ps = list(reversed(ps))
        qs = list(reversed(qs))
        v = -1
        for i in range(min(len(ps),len(qs))):
            if qs[i] in ps:
                return qs[i]
            elif ps[i] in qs:
                return ps[i]