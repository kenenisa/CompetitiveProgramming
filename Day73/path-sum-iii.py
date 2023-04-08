# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        df = defaultdict(int)
        df[0] = 1

        def recur(node, acc):
            nonlocal result
            if not node: return
            s = node.val + acc
            if df[s - targetSum]:
                result += df[s - targetSum]
            df[s] += 1
            recur(node.left, s)
            recur(node.right, s)
            df[s] -= 1
         
        recur(root, 0)

        return result