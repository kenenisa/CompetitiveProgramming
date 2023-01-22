t = int(input())
for _ in range(t):
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    if a[1] != b[1]:
        print("No")
    else:
        if a[0] + b[0] == a[1]:
            print("Yes")
        else:
            print("No")
