# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        df = defaultdict(list)

        def dfs(node):
            if not node: return 
            if node.left:
                df[node.left.val].append(node.val)
                df[node.val].append(node.left.val)
            if node.right:
                df[node.right.val].append(node.val)
                df[node.val].append(node.right.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        result = []

        q = deque([(target.val,0)])
        visited = set([target.val])

        while q:
            v,d = q.popleft()
            if d == k:
                result.append(v)
            else:
                for e in df[v]:
                    if e not in visited:
                        q.append((e,d+1))
                        visited.add(e)
        return result
        
            
