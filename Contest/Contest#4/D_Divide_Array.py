n = int(input())
arr = list(map(int, input().split()))

ng = []
p = []
z = []

for i in arr:
    if i < 0:
        ng.append(i)
    elif i > 0:
        p.append(i)
    else:
        z.append(i)

if not p:
    if len(ng)>1:
        p.append(ng.pop())
        p.append(ng.pop())
if len(ng) % 2 == 0:
    z.append(ng.pop())

print(len(ng), *ng)
print(len(p), *p)
print(len(z), *z)
