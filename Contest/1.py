#q4
cases = input()
def kill(k,h,n,prefix):
    for i in range(n):
        if h < 0:
            return h
        if i+1 == n:
            return h-k
        if prefix[i]  >= k:
            h -= k 
        else:
            h -= prefix[i]
def binarySearch(start,end,h,n,prefix):
    if start == end:
        return start
    mid = (start+end)//2
    if kill(mid,h,n,prefix) > 0:
        return binarySearch(mid+1,end,h,n,prefix)
    return binarySearch(start,mid,h,n,prefix)
for line in range(int(cases)):
    first = input()
    n,h = map(int,first.split())
    attacks = list(map(int,input().split()))
    prefix = []
    for i in range(n-1):
        prefix.append(attacks[i+1] - attacks[i])
    print(binarySearch(1,h,h,n,prefix))

#q3
# from heapq import heappush, heappop

# h  = []
# cases = input()
# results = []
# for line in range(int(cases)):
#     inp = input()
#     inps = inp.split()
#     if inps[0] == 'insert':
#         heappush(h, int(inps[1]))
#         results.append(inp)
#     if inps[0] == 'removeMin':
#         if h:
#             heappop(h)
#             results.append(inp)
#         else:
#             results.append('insert ' + str(99999))
#             results.append('removeMin')
#     if inps[0] == 'getMin':
#         while h and int(inps[1]) > h[0]:
#             heappop(h)
#             results.append('removeMin')
#         if h and int(inps[1]) == h[0]:
#             results.append('getMin ' + str(h[0]))
#         else:
#             heappush(h, int(inps[1]))
#             results.append('insert ' + str(inps[1]))
#             results.append('getMin ' + str(h[0]))
# print(len(results))
# for r in results:
#     print(r)



#q2
# cases = input()
# for line in range(int(cases)):
#     snum = input()
#     num = int(snum)
#     if num % 2  == 0:
#         print(0)
#         continue
#     if int(snum[0]) % 2 == 0:
#         print(1)
#         continue
#     by2 = False
#     for i in snum:
#         if i in ('0','2','4','6','8'):
#             print(2)
#             by2 = True
#             break
#     if not by2:
#         print(-1)
#q1
# import sys
# for line in sys.stdin:
#     numbers = [int(x) for x in line.strip().split()]
#     minutes = 4 * 60
#     n = numbers[0]
#     k = numbers[1]
#     minutes = minutes - k
#     mx = 0
#     for i in range(1,n+1):
#         if mx + 5*i > minutes:
#             print(i-1) 
#             break
#         elif mx + 5*i == minutes:
#             print(i)
#             break
#         if i == n:
#             print(n)
#         mx += 5*i