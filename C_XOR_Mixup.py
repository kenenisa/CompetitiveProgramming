n,m,k=list(map(int,input().split()))
a = list(map(int,input().split()))
op = []
for _ in range(m):
    op.append(list(map(int,input().split())))
op_prefix = [0]*(m+1)
for _ in range(k):
    x,y=list(map(int,input().split()))
    op_prefix[x-1] += 1
    op_prefix[y] -= 1

for i in range(1,m):
    op_prefix[i] += op_prefix[i-1]

a_prefix = [0]*n

for i in range(m):
    l,r,d = op[i]
    incur =  d * op_prefix[i]
    a_prefix[l-1] += incur
    if r < n:
        a_prefix[r] -= incur
for i in range(1,n):
    a_prefix[i] += a_prefix[i-1]
for i in range(n):
    if i<n-1:
        print(a[i] + a_prefix[i],end=' ')
    else:
        print(a[i] + a_prefix[i])
