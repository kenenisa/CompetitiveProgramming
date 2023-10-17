t = int(input())
for _ in range(t):
    n,m,k=list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if k%2==0:
        ma = max(a)
        mb = max(b)
        mia = min(a)
        if ma < mb or mia < mb:
            print(sum(a) - min(a) + mb)
        else:
            print(sum(a))
    else:
        if min(b) < max(a):
            print(sum(a) - max(a) + min(b))
        else:
            print(sum(a))