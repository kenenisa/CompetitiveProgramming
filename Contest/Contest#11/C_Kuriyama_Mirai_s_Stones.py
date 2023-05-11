n = int(input())
v = list(map(int,input().split()))
u = sorted(v)
v.insert(0,0)
u.insert(0,0)
for i in range(1,n+1):
    v[i] += v[i-1]
    u[i] += u[i-1]
m = int(input())
for _ in range(m):
    t,l,r = list(map(int,input().split()))
    if t == 1:
        print(v[r] - v[l-1])
    else:
        print(u[r] - u[l-1])