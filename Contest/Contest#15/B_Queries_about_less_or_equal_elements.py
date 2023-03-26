import bisect
n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
result = []
for j in b:
    result.append(bisect.bisect_right(a,j))
print(*result)