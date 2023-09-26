from collections import Counter
from heapq import *
n,m=list(map(int,input().split()))
a = list(map(int,input().split()))

c = Counter(a)
h = []
for k,v in c.items():
    for div in range(v):
        if len(h) == m:
            heappushpop(h,((v//(div+1)),k,v))
        else:
            heappush(h,((v//(div+1)),k,v))

print(h)
print(*[x[1] for x in h])