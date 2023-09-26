n,t=list(map(int,input().split()))
a = list(map(int,input().split()))
i,j = 0,0
running = 0
mx = float('-inf')
while i < n:
    while j < n and running + a[j] <= t:
        running += a[j]
        j += 1
    running -= a[i]
    mx = max(mx,j-i)
    i += 1
print(mx)
