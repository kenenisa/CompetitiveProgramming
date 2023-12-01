t = int(input())
for _ in range(t):
    a,b,c=list(map(int,input().split()))
    if a > b:
        print("First")
        continue
    if b > a:
        print("Second")
        continue
    if c%2==0:
        print("Second")
    else:
        print("First")
    