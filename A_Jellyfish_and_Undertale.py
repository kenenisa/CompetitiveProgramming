t = int(input())
for _ in range(t):
    a,b,n=list(map(int,input().split()))
    st = list(map(int,input().split()))
    s = b
    for i in range(n):
        s += min(a-1,st[i])
    print(s)
# anor