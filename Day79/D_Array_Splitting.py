n,m=list(map(int,input().split()))
a = list(map(int,input().split()))


suffixSum = [a[-1]]
for i in range(n-2,0,-1):
    suffixSum.append(suffixSum[-1] + a[i])

suffixSum.sort(reverse=True)
result = sum(a)
for i in range(m-1):
    result += suffixSum[i]    
print(result)
