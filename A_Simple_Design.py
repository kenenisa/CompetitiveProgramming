t = int(input())
for _ in range(t):
    x,k=list(map(int,input().split()))
    if x%k == 0:
        print(x+k)
    