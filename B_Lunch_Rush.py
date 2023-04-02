n,k=list(map(int,input().split()))

result = float("-inf")
for _ in range(n):
    f,t=list(map(int,input().split()))
    if t > k:
        result = max(result,f-(t-k))
    else:
        result = max(result,f)
print(result)