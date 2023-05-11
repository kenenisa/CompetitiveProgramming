t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    strip = [a for a in input()]
    blacks = 0
    whites = 0
    for i in range(k):
        if strip[i] == "W":
            whites+=1
        else: 
            blacks+=1
    i = 0
    j = k
    max_blacks = blacks
    while  j < n:
        if strip[j] == 'B':
            blacks += 1
        else:
            whites+=1
        if strip[i] == "B":
            blacks -= 1
        else: 
            whites-=1
        j+=1
        i+=1
        max_blacks = max(max_blacks,blacks)

    print(k-max_blacks)