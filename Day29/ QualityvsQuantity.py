tests = int(input())

for _ in range(tests):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()

    l = 1
    found = False
    leftSum  = a[0]
    rightSum = 0
    # 
    while(l<=n):
        leftSum += a[l]
        rightSum += a[n-1]
        if(leftSum < rightSum):
            found = True
            break;
        l += 1
        n -= 1
    if(found):
        print("YES")
    else:
        print("No")

