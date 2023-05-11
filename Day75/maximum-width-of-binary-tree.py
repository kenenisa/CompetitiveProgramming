# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        df = {}
        def recur(node, idx,lvl):
            if not node: return 
            if lvl in df:
                df[lvl] = [min(df[lvl][0],idx),max(df[lvl][1],idx)]
            else:
                df[lvl] = [idx,idx]
            lvl += 1
            recur(node.left,  idx*2,lvl)
            recur(node.right,  (idx * 2) + 1, lvl)
        recur(root, 0 , 0)
        result = 0
        for val in df.values():
            result = max(result, val[1] - val[0] + 1)
        return result