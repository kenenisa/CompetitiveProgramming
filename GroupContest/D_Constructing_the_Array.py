from heapq import *
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0] * n
    h = []
    heappush(h,(n-1,(0,n-1)))

    for i in range(n): 
        l,seg = heappop(h)
        left,right = seg
        value = right - left + 1

        if value % 2 == 0:
            index = (left + right - 1) // 2
        else:
            index = (left + right) // 2
        
        nums[index] = i+1

        if left != index:
            heappush(h,(-(index-left),(left,index-1)))
        if right != index:
            heappush(h,(-(right-index),(index+1,right)))

    print(*nums)