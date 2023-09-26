n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = 0
for i in range(n-1):
    a[i+1] = max(a[i+1] + b[i],a[i])
    b[i+1] = max(b[i+1] + a[i],b[i])
    result = max(a[i+1],b[i+1])
print(max(result,max(a[n-1],b[n-1])))

