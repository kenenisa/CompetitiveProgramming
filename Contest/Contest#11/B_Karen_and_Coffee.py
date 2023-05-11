n,k,q=list(map(int,input().split()))
c = [0]*200002
for _ in range(n):
    l,r=list(map(int,input().split()))
    c[l] += 1
    c[r+1] -= 1
for i in range(1,200002):
    c[i] += c[i-1]

for i in range(1,200002):
    if c[i] >= k:
        c[i] = c[i-1] + 1
    else:
        c[i] = c[i-1]
# for i in range(1,200002):
#     c[i] += c[i-1]

result = []
for _ in range(q):
    a,b=list(map(int,input().split()))
    print(c[b] - c[a-1])
    