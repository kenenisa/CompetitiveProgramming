from collections import *

t = int(input())
for _ in range(t):
    def run():
        n = int(input())
        df = defaultdict(list)
        preReq = []
        q = deque()
        for i in range(n):
            a = list(map(int,input().split()))
            k = a[0]
            for el in a[1:]:
                df[el-1].append(i) 
            preReq.append(k)    
            if k == 0:
                q.append(i)
        result = [1]*n
        while q:
            u = q.popleft()
            for v in df[u]:
                preReq[v] -= 1
                result[v] = max(result[v],result[u]+1 if v<u else result[u])
                if preReq[v] == 0:
                    q.append(v)
        for p in preReq:
            if p > 0:
                return -1
        return max(result)
    print(run())

