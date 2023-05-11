t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    mx = (n + m) //4
    print(min(min(n,m),int(mx)))
