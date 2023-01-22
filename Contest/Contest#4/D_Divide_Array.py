n = int(input())
arr = list(map(int, input().split()))

neg = []
pos = []
zero = []

for i in arr:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
    else:
        zero.append(i)

if not pos:
    if len(neg)>1:
        pos.append(neg.pop())
        pos.append(neg.pop())
if len(neg) % 2 == 0:
    zero.append(neg.pop())

print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
