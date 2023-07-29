from math import * 
t = int(input())
for tt in range(t):
    n,k=list(map(int,input().split()))
    a = list(map(int,input().split()))
    # if len(a) == 1:
    #     print(a[0]-k)
    #     continue
    # elif sum(a) <= k:
    #     print(0)
    #     continue
    a.sort()
    smallest = a[0]

    prefixSum = [0]
    for i in range(1,n):
        prefixSum.append(prefixSum[-1] + a[i])
    result = float('inf')
    for i in range(n):
        dec = (k - prefixSum[i])//(n-i)
        result = min(result,n-i-1 if dec >= smallest else smallest-dec+n-i-1)
    print(result)
