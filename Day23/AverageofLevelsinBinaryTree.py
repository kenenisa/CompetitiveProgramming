# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root: return result
        q = Queue()
        q.put(root)
        
        while not q.empty():
            sumAvg = 0
            
            length = q.qsize()
            for i in range(length):
                node = q.get()
                sumAvg += node.val
                
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            
            result.append(sumAvg/length)
        return result

        
        
