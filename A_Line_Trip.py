t = int(input())
for _ in range(t):
    n,x=list(map(int,input().split()))
    a = list(map(int,input().split()))

    tank = max(a[0],(x- a[-1])*2)
    for i in range(1,len(a)):
        tank = max(tank,a[i] - a[i-1])
    print(tank)
    
