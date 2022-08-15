"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        global deepest
        deepest = 0

        def dfs(node,depth):
            global deepest
            if node:
                depth += 1
                deepest = max(deepest,depth)
                for n in node.children:
                    dfs(n,depth)
                    
        dfs(root,0)
        return deepest
