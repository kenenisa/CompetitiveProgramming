n,m=list(map(int,input().split()))
e = [0]*n
for _ in range(m):
    u,v=list(map(int,input().split()))
    e[u-1] += 1
    e[v-1] += 1
def check():
    for a in e:
        if a != e[0]:
            return "NO"
    return "YES"
print(check())