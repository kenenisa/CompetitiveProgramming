def count(k,d,n,a):
    con = 0
    for i in range(d):
        #should cycle
        j = i%k
        con += a[j] if j < n else 0
    return con
def run():
    n,c,d=list(map(int,input().split()))
    a = list(map(int,input().split()))
    a.sort(reverse=True)

    if a[0]*d < c:
        return "Impossible"
    
    left = 0
    right = d+1
    while left < right:
        mid = (left+right)//2
        if count(mid,d,n,a)<c:
            right = mid
        else:
            left = mid+1
    if left == d+1: return "Infinity"
    return left-2

t = int(input())
for _ in range(t):
    print(run())
    
