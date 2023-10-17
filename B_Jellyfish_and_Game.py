t = int(input())
for _ in range(t):
    n,m,k=list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c,d,e,f=min(a),max([min(a)]+b),min(a+b),max(a+b)
    if k%2:
        print(sum(a)-c+d)
    else:
        print(sum(a)-c+d+e-f)