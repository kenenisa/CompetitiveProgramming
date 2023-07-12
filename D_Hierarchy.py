n=int(input())
# n = int(input())
qul = list(map(int,input().split()))
lookup = [float('inf')]*n
for i in range(int(input())):
    a,b,c = list(map(int,input().split()))
    lookup[b-1] = min(lookup[b-1],c)
for i in range(len(lookup)):
    if lookup[i] == float('inf'):
        lookup[i] = 0
        break

s = sum(lookup)
if s == float('inf'):
    print(-1)
else:
    print(s)