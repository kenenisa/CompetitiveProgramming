n = int(input())
a = list(map(int,input().split()))
r = input()

mx = 0
valid = True
for i in range(n-1):
    mx = max(mx,a[i])
    if r[i] == "0" and mx > i + 1:
        valid = False
        break
if valid:
    print("YES")
else:
    print("NO")
