n = int(input())
arr = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

prefixSum = [[0 for _ in range(n)] for _ in range(n)]
for j in range(n):
    prefixSum[0][j] = arr[0][j]
    if j > 0:
        prefixSum[0][j] += prefixSum[0][j - 1]
for i in range(n):
    prefixSum[i][0] = arr[i][0]
    if i > 0:
        prefixSum[i][0] += prefixSum[i - 1][0]
for i in range(1,n):
    for j in range(1,n):
        prefixSum[i][j] = arr[i][j] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]
q = int(input())

s = 0
for _ in range(q):
    x1,y1,x2,y2=list(map(int,input().split()))
    if x2 < x1:
        x1,x2=x2,x1
    if y2 < y1:
        y1,y2 = y2,y1

    s += prefixSum[x2][y2]

    if x1 > 0:
        s -= prefixSum[x1 - 1][y2]

    if y1 > 0:
        s -= prefixSum[x2][y1 - 1]

    if x1 > 0 and y1 > 0:
        s += prefixSum[x1 - 1][y1 - 1]
bluma = int(input())
if s*2 > bluma:
    print("YES")
else:
    print("NO")