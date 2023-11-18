n,k=list(map(int,input().split()))
e  = n//2
o = n - e
if k > o:
    k -= o
    print(2*k)
else:
    print((2*k)-1)