from collections import defaultdict
import sys
sys.setrecursionlimit(2500)

n = int(input())
# class Node:
#     def __init__(self,val,c=None):
#         self.val = val
#         self.c = c

tree = defaultdict(list)
for i in range(n):
    p = int(input())
    tree[p].append(i+1)


depth = 0
def traverse(vals,i):
    global depth
    if len(vals) > 0:
        depth = max(depth,i)
        for v in vals: 
            traverse(tree[v],i+1)
traverse(tree[-1],1)
print(depth)