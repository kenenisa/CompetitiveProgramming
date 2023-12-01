t = int(input())
for _ in range(t):
    x,y=list(map(int,input().split()))
    a = y//x
    b = y%x
    print(int(sum(map(int,list(str(a)))))+b)

