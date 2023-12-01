t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    a = list(map(int,input().split()))
    if a  == sorted(a):
        print("YES")
        continue
    if k == 1:
        print("NO")
    else:
        print("YES")
    