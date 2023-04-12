# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        df = defaultdict(list)
        def recur(node,row,col):
            if not node: return 
            df[col].append((node.val,row))
            recur(node.left,row+1,col-1)
            recur(node.right,row+1,col+1)
        recur(root,0,0)
        result = []
        for key,val in sorted(df.items(),key=lambda item:item[0]):
            val.sort()
            val.sort(key=lambda item: item[1])
            result.append(list(map(lambda item:item[0],val)))
        return result
            