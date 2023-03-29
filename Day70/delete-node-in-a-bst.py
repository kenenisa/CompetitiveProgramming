# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def insertNode(tree,node):
            if not tree: return node
            if tree.val < node.val:
                tree.right =insertNode(tree.right,node)
                return tree
            tree.left = insertNode(tree.left,node)
            return tree
            
        def deleteTree(node):
            if not node: return node
            if node.val == key:
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                temp = node.left
                node = node.right
                return insertNode(node,temp)
            if node.val < key:
                node.right = deleteTree(node.right)
                return node
            node.left = deleteTree(node.left)
            return node
        return deleteTree(root)