# class Node:
#     def __init__(self,val,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    parents = list(map(int,input().split()))
    df = {}
    leafs = [True] * (n+1)
    for i in range(n):
        if i+1 == parents[i]:
            df[i+1] = 0
        else:
            df[i+1] = parents[i]
        leafs[parents[i]] = False
    result = []
    l = n  - len(set(parents))
    if l > 0:
        print(l)
        visited = defaultdict(bool)
        for i in range(1,n+1):
            if leafs[i]:
                path = []
                p = i
                while p and (not visited[p]):
                    visited[p] = True
                    path.append(p)
                    p = df[p]
                path.reverse()
                print(len(path))
                print(*path)
    else:
        print(1)
        print(1)
        print(*parents)
    print()