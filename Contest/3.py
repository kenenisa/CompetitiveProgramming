cases = int(input())

for _ in range(cases):
    n = int(input())
    arr = list(map(int,input().split()))
    # look for same parity
    evenIndex = arr[0] % 2 == 0
    oddIndex = arr[1] % 2 == 0
    evenTray = True
    oddTray = True
    for i in range(0,n,2):
        if (arr[i] % 2 == 0) == evenIndex:
            continue
        evenTray = False
        break
    for i in range(1,n,2):
        if (arr[i] % 2 == 0) == oddIndex:
            continue
        oddTray = False
        break
    print(evenTray,oddTray)
    print("yes" if evenTray and oddTray else "no")