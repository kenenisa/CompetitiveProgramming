t = int(input())
for _ in range(t):
    n= int(input())
    a = list(map(int,input().split()))
    
    count = 1
    result = []
    result.append(a[0])
    for i in range(1,n):
        if a[i] != a[i-1]:
            result.append(a[i])
    valley = 0
    c = len(result)
    if c < 3:
        print("YES")
        continue
    if result[0]< result[1]:
        valley += 1
   
    for i in range(1,c-1):
        if result[i] < result[i-1] and result[i] < result[i+1]:
            valley += 1
    if result[c-1] < result[c-2]:
        valley += 1
    if valley > 1:
        print("NO")
    else:
        print("YES")

