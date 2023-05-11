
t = int(input())
for _ in range(t):
    n = int(input())
    if(n&(n-1)):
        print("YES")
    else:
        print("NO")