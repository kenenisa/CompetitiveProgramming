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
# a
# 1 2 3
# 3 4 3
# 9 10 9
# 9 18 17

# 1 2 3
# 3 2 1
# 9 2 1
# 9 10 1
# 9 19
# op
# 1 2 1
# 1 3 2
# 2 3 4

# [2,3,2]
# xy
# 1 2
# 1 3
# 2 3