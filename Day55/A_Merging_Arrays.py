n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i = 0
j = 0
result = []
while i < n and j < m:
    if a[i] < b[j]:
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1
result += a[i:]
result += b[j:]
print(*result)