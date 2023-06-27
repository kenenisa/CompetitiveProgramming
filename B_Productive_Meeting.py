# from heapq import *;import sys;input=sys.stdin.readline
# for i in range(int(input())):
#     n=int(input())
#     a=[]
#     for x,i in enumerate([*map(int,input().split())]):
#         heappush(a,[-i,x])
#     l=[]
#     while 1:
#         s=heappop(a)
#         b=heappop(a)
#         if s[0]==0 or b[0]==0:break
#         l.append([s[1]+1,b[1]+1])
#         s[0]+=1
#         b[0]+=1
#         heappush(a,s)
#         heappush(a,b)
#     print(len(l))
#     for i in l:print(*i)

import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    h = []
    for i in range(n):
        heapq.heappush(h,[-a[i],i])
    result = []
    x1 = 1
    y1 = 1
    while True:
        x1,x2 = heapq.heappop(h)
        y1,y2 = heapq.heappop(h)
        if x1 == 0 or y1 == 0: break
        result.append(str(x2+1)+ " " +str(y2+1))
        heapq.heappush(h,[x1+1,x2])
        heapq.heappush(h,[y1+1,y2])
    print(len(result))
    for val in result:
        print(val)