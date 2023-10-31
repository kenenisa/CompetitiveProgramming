n = int(input())
count = 0

for _ in range(n):
    p,q=list(map(int,input().split()))
    if abs(q-p)>=2:
        count+=1
print(count)