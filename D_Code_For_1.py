n,l,r=list(map(int,input().split()))
result = 0
left = 0
for i in range(51):
    if n & (1<<i):
        left = i
for i in range(l,r+1):
    right = 0
    while not (i & (1<<right)):
        right += 1
    if n & (1<<(left - right)):
        result += 1
print(result)