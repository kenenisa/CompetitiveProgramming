n = int(input())
a = list(map(int,input().split()))
a.sort()
s = 1
for x in a:
    if x > s:
        break
    s += x
print(s)