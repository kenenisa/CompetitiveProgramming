n = int(input())
a = list(map(int,input().split()))

result = (float('inf'),0)

for i in range(1,n+1):
    c = (a[i-1] - i)//n
    b = (c*n)+i
    if result[0] > b:
        result = (b,i)
print(result[1])
