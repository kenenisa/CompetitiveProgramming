n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()

result = 1e9

right = n-1
for i in range(m-n+1):
    result = min(result,a[i+n-1] - a[i])
print(result)
