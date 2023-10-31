n,m,k=list(map(int,input().split()))
left = 1
right = n*m
while left < right:
    mid = (left+right)//2
    s = 0
    for i in range(1,n+1):
        s += min(mid//i,m) 
    if s < k:
        left = mid+1
    else:
        right = mid
print(left)