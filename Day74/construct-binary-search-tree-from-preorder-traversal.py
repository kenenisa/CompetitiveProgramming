# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insert(self,root,node):
            if not root: return node
            if root.val > node.val:
                root.left = self.insert(root.left,node)
            else:
                root.right = self.insert(root.right,node)
            return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            root = self.insert(root,TreeNode(preorder[i]))
        return root