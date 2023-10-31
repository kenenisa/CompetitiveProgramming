k,n,w=list(map(int,input().split()))

m = 0
for i in range(1,w+1):
    m += i*k
if m > n:
    print(m-n)
else: print(0)