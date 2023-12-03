t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    prefix = [(a[0],0)]
    for i in range(1,n):
        prefix.append(min(prefix[-1],(a[i],i)))
    suffix = [(a[-1],n-1)]
    for i in range(n-2,-1,-1):
        suffix.append(min(suffix[-1],(a[i],i)))
    suffix.reverse()
    valid = False
    for i in range(1,n-1):
        if prefix[i-1][0] < a[i] and a[i] > suffix[i+1][0]:
            print("YES")
            print(prefix[i-1][1]+1,i+1,suffix[i+1][1]+1) 
            valid = True
            break
    if not valid: print('NO')