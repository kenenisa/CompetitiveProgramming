from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n-2,-1,-1):
        # WTTT
        if a[i] > a[i+1]:
            if a[i+1] > a[i]//2:
                count += 1
                a[i] = a[i]//2
            else:
                x = ceil(a[i]/a[i+1])-1
                count += x
                a[i] = a[i]//(x+1)
        # print(a)
    print(count)