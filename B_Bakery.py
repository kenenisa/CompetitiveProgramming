from collections import *

def run():
    n,m,k=list(map(int,input().split()))
    if k == 0 or k == n: return -1
    df = defaultdict(list)

    for _ in range(m):
        u,v,l=list(map(int,input().split()))
        df[u].append((v,l))
        df[v].append((u,l))
    storage = list(map(int,input().split()))
    q = deque(list(zip(storage,[0]*len(storage))))
    st = set(storage)
    result = float('inf')
    visited = set()
    while q:
        node,path = q.popleft()
        if node not in st:
            result = min(result,path)
        else:
            for n,p in df[node]:
                if (n,p) not in visited:
                    q.append((n,path+p))
                    visited.add((n,p))
    return -1 if result == float('inf') else result
    

print(run())

    


